import random
from math import sqrt
import cv2
import numpy as np
import threading
import time
import argparse
import re


def _de_channel_Multiplier(inp, AllChannelMultiplier, forcenet=False):
    inp += random.randint(-1, 1) * 256 + random.uniform(-0.5, 0.5)
    if forcenet:
        inp /= 0.74
    else:
        inp /= AllChannelMultiplier
        inp /= random.uniform(0.8, 1)
    return round((inp / 256) - random.uniform(0.0017, 0.0042), 9)


def _channel_Multiplier(inp, AllChannelMultiplier, forcenet=None):
    # ## Multiply (so that we step towards the range of a Byte)
    # I think it has a little bit offset?
    inp += random.uniform(0.0017, 0.0042)
    #  Multiply channel by 256
    inp *= 256
    #  ## Randomize (note that this causes a triangular distribution
    #  ## such that 0.74 is the mean net multiplier)
    if forcenet:
        inp *= forcenet
    #  Multiply channel by RandomBetween(0.8, 1.0)
    #  Multiply channel by AllChannelMultiplier
    else:
        inp *= random.uniform(0.8, 1)
        inp *= AllChannelMultiplier
    #  ## Convert (to an actual Byte value)
    #  Round channel toward zero, to the nearest integer
    inp = round(inp)
    #  Set channel = channel Mod 256
    return divmod(inp, 256)[1]


def calculate_d2rgb(xd, yd, zd, forcenet=None):
    # Set Red = xd, Green = yd, Blue = zd
    r = xd
    g = yd
    b = zd
    # Multiply each (Red, Green, Blue) by speed
    # r *= speed;g *= speed;b *= speed
    # If Red = 0 then set Red = 1
    if r == 0: r = 1
    # Set AllChannelMultiplier = RandomBetween(0.6, 1.0)
    AllChannelMultiplier = random.uniform(0.6, 1)
    # For each channel (Red, Green, Blue):
    r = _channel_Multiplier(r, AllChannelMultiplier, forcenet)
    g = _channel_Multiplier(g, AllChannelMultiplier, forcenet)
    b = _channel_Multiplier(b, AllChannelMultiplier, forcenet)

    # Return color of this particle as (Red, Green, Blue)
    return (r, g, b)


def calculate_rgb2d(r, g, b, speed=1):
    AllChannelMultiplier = random.uniform(0.6, 1)
    r = _de_channel_Multiplier(r, AllChannelMultiplier)
    g = _de_channel_Multiplier(g, AllChannelMultiplier)
    b = _de_channel_Multiplier(b, AllChannelMultiplier)

    return r, g, b


# 补全
def fillchar(inp, len_):
    inp = str(inp)
    if len(inp) < len_:
        return '0' * (len_ - len(inp)) + inp
    return inp


def rgb2hex(r, g, b):
    try:
        return '#' + fillchar(hex(r)[2:], 2) + fillchar(hex(g)[2:], 2) + fillchar(hex(b)[2:], 2)
    except:
        return '#FFFFFF'


def hex2rgb(hex_):
    try:
        hex_ = hex_[1:]
        r = int('0x' + hex_[0:2], 16)
        g = int('0x' + hex_[2:4], 16)
        b = int('0x' + hex_[4:6], 16)
        return r, g, b
    except:
        return 0, 0, 0


def map_r_g_b_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return (255 - abs(r1 - r2) * 0.297 - abs(g1 - g2) * 0.593 - abs(b1 - b2) * 0.11) / 255


# method 2
def map_r_g_b_distance_2(rgb_1, rgb_2):
    R_1, G_1, B_1 = rgb_1
    R_2, G_2, B_2 = rgb_2
    rmean = (R_1 + R_2) / 2
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    return sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2))


def mapcolordistance(targethex, dx, dy, dz):
    loss = 0
    # print(targethex,dx,dy,dz)
    for i in range(64):
        u = map_r_g_b_distance(calculate_d2rgb(dx, dy, dz), hex2rgb(targethex))
        # print(u)
        loss += u
    return loss / 64


def mapcolordistance_and_wave(targethex, dx, dy, dz, wave=True, times=64):
    loss = 0
    # print(targethex,dx,dy,dz)
    li = []
    force_ = calculate_d2rgb(dx, dy, dz, forcenet=0.74)
    for i in range(times):
        now_ = calculate_d2rgb(dx, dy, dz)
        u = map_r_g_b_distance(now_, hex2rgb(targethex))
        # li.append(map_r_g_b_distance(force_,now_))
        li.append(now_)
        # print(u)
        loss += u
    # 求方差
    if wave:
        return loss / times, force_, mapcolor_wave(force_, li)
    else:
        return loss / times, force_


def mapcolor_wave_with_d(dx, dy, dz, times=64):
    li = []
    force_ = calculate_d2rgb(dx, dy, dz, forcenet=0.74)
    for i in range(times):
        li.append(calculate_d2rgb(dx, dy, dz))
    return force_, mapcolor_wave(force_, li)


def mapcolor_wave(forcergb_, randrgbli):
    li = []
    for i in randrgbli:
        li.append(map_r_g_b_distance(forcergb_, i))
    # narray = np.array(li)
    # sum1 = narray.sum()
    # narray2 = narray * narray
    # sum2 = narray2.sum()
    # mean = sum1 / 64
    # var = sum2 / 64 - mean ** 2

    return round(np.var(np.array(li)) * 10000)
    # return np.var(np.array(li))


def mapcolordistance_r_r(targr, targg, targb, dx, dy, dz, times=64):
    loss = 0
    # print(targethex,dx,dy,dz)
    for i in range(times):
        u = map_r_g_b_distance(calculate_d2rgb(dx, dy, dz), (targr, targg, targb))
        # print(u)
        loss += u
    return loss / times


def float2str(float_, n=5):
    str_ = ('%' + '.%sf' % n) % float_
    while True:
        if str_[-1] == '0':
            str_ = str_[:-1]
        elif str_[-1] == '.':
            return str_[:-1]
        else:
            return str_


def getImage(path):
    try:
        return [True, cv2.imread(path)]
    except cv2.error:
        return [False, None]


class Thread_Logger():
    def __init__(self):
        self._log = []
        self.all2process = 0
        self.now2process = 0
        self.data = []
        self.nowthr = 0

    def append(self, str_):
        self._log.append(str_)

    def setsimuall(self, all):
        self.all2process = all
        self.now2process = 0

    def setsimunow(self, now):
        self.now2process = now

    def addsimunow(self):
        self.now2process += 1

    def getnow(self):
        return self.now2process

    def appenddata(self, data):
        self.data.append(data)


thr_log = Thread_Logger()


def forcergb2data(r, g, b, forceseq=0.95, trytime=10000, _main=None):
    max_similar = -1
    d = 0
    # 黑白检查
    if r >= 250 and g >= 250 and b >= 250:
        return True, -0.01, -0.01, -0.01, 0.98
    elif r <= 6 and g <= 6 and b <= 6:
        return True, (0.01, 0.01, 0.01), 0.98
    while trytime:
        trytime -= 1
        # if _main:
        #     _main.setsimunum(trytime)
        dx, dy, dz = calculate_rgb2d(r, g, b)
        u = mapcolordistance_r_r(r, g, b, dx, dy, dz)
        if u > max_similar:
            max_similar = u
            d = (dx, dy, dz)
            if max_similar >= forceseq:
                return True, dx, dy, dz, u
    return False, d[0],d[1],d[2], max_similar


def ProcessImage2dust_singleThread(path, _main, forceseq=0.95):
    img = getImage(path)
    if img[0]:
        img = img[1]
        ylen, xlen, gp = img.shape
        if gp != 3:
            return False, '非标准rgb文件(通道数量%s)' % gp
        else:
            data = []
            _main.setsimuall(ylen * xlen)
            # all_ = ylen * xlen
            start_ = time.time()
            now = 0
            for y in range(ylen):
                for x in range(xlen):
                    now += 1
                    _main.setsimunow(now)
                    # print('%s/%s' % (now, all_))
                    b, g, r = img[y][x]
                    if not time.time() - start_ <= 0.1:
                        _main.simu_color_now.setStyleSheet("background-color:%s" % rgb2hex(r, g, b))
                    start_ = time.time()
                    data.append([[x, y], list(forcergb2data(r, g, b, forceseq, _main))])
            return True, data
    else:
        return False, '图像文件读取错误'


# class ProcessImage_Thread(threading.Thread):
#     def __init__(self,thrlog,y,imgy,name=''):
#         super(ProcessImage_Thread,self).__init__()
#         self.thrlog = thrlog
#         self.name = '#Thr'+name
#         self.y = y
#         self.imgy = imgy
#
#     def run(self):
#         for i in range(len(self.imgy)):
#             self.thrlog.addnow()
#             b, g, r = self.imgy[i]
#             self.thrlog.appenddata([[i, self.y], list(forcergb2data(r, g, b))])
#             print(self.name + ' Finish ' + str(self.thrlog.getnow()))
#         self.thrlog.nowthr -= 1
#         return
# def ProcessImage2dust_multiThread(path, thread_log:Thread_Logger):
#     img = getImage(path)
#     pool = []
#     notfinish = True
#     if img[0]:
#         img = img[1]
#         ylen, xlen, gp = img.shape
#         if gp != 3:
#             return False, '非标准rgb文件(通道数量%s)' % gp
#         else:
#             thread_log.setall(ylen * xlen)
#             all_ = ylen * xlen
#             now = 0
#             for y in range(ylen):
#                 while notfinish:
#                     if thread_log.nowthr >= 32:
#                         time.sleep(1)
#                     else:
#                         u = ProcessImage_Thread(thr_log,y,img[y],str(thread_log.nowthr))
#                         u.start()
#                         pool.append(u)
#                         thread_log.nowthr += 1
#                         notfinish = False
#                 notfinish = True
#             while thread_log.nowthr != 0:
#                 time.sleep(1)
#                 print(thread_log.nowthr)
#             return thread_log.data
#     else:
#         return False, '图像文件读取错误'

def write2mcfunction(data_, path='./output.mcfunction',
                     format='particle minecraft:dust %.5f %.5f %.5f 1 ~%s ~%s ~%s 0 0 0 0 1', scale=0.15, yf=1):
    u = []
    for i in data_:
        # if i[1][0] == False:
        #     u.append(format % (
        #         i[1][1][0], i[1][1][1], i[1][1][2], round(i[0][0] * scale, 3), str(yf), round(i[0][1] * scale, 3)))
        # else:
        u.append(
            format % (i[1][1], i[1][2], i[1][3], round(i[0][0] * scale, 3), str(yf), round(i[0][1] * scale, 3)))
    with open(path, 'w+') as file_:
        for i in u:
            file_.write(i + '\n')


def calculate_channle2drange(inp):
    return (((inp - 256 - 0.5) / (0.6 * 0.8)) / 256) - 0.0042, (((inp + 0.5) / (0.6 * 0.8)) / 256) - 0.0017


def iandfrange(start, *args):
    try:
        args[2]
    except Exception as e:
        pass
    else:
        raise Exception(ValueError, "The function receive three args!")
    # 保证传入的3个参数能正确匹配到start,end和step三个变量上
    try:
        end, step = args[0], args[1]
    except IndexError:
        try:
            end = args[0]
        except IndexError:
            end = start
            start = 0
        finally:
            step = 1
            # 参数正确性校验，包括对step是否是int或float的校验，提示用户输出数据可能只有start的校验以及start>=end的情况
    try:
        try:
            a, b = str(step).split(".")
            roundstep = len(b)
        except Exception as e:
            if isinstance(step, int):
                roundstep = 0
            else:
                raise Exception(TypeError, "Sorry,the function not support the step type except integer or float!")
        if start + step >= end:
            print("The result list may include the 'start' value only!")
        if start >= end:
            raise Exception(ValueError,
                            "Please check you 'start' and 'end' value,may the 'start' greater or equle the 'end'!")
    except TypeError as e:
        roundstep = 0
        print(e)
    else:
        pass
    # 输出range序列
    lista = []
    while start < end:
        lista.append(start)

        start = round(start + step, roundstep)
    return lista


def tuple2str(t_, format_=''):
    if not format_:
        return str(t_)
    else:
        try:
            return format_ % t_
        except:
            return str(t_)


def match_seq_rgb2d(r, g, b, _main=None, force_=None):
    rmin, rmax = calculate_channle2drange(r)
    print('[rCol-dx]from<%.3f>to<%.3f>' % (rmin, rmax))
    gmin, gmax = calculate_channle2drange(g)
    print('[gCol-dy]from<%.3f>to<%.3f>' % (gmin, gmax))
    bmin, bmax = calculate_channle2drange(b)
    print('[bCol-dz]from<%.3f>to<%.3f>' % (bmin, bmax))
    d = 0
    max_simur = -1
    lent = len(iandfrange(rmin, rmax, 0.01))
    if force_:
        print('[Controller]Force Accurate set to:%f' % force_)
    simwave = 99
    for dx in iandfrange(rmin, rmax, 0.01):
        for dy in iandfrange(gmin, gmax, 0.01):
            for dz in iandfrange(bmin, bmax, 0.01):
                # 有了rgb 也就是目标rgb 也有了dxdydz的全部范围
                # 那么就将dxdydz随机
                # (255 - abs(r1 - r2) * 0.297 - abs(g1 - g2) * 0.593 - abs(b1 - b2) * 0.11) / 255
                # u = map_r_g_b_distance((r, g, b), (divmod(round(dx*256*0.74),256)[1], divmod(round(dy*256*0.74),256)[1], divmod(round(dz*256*0.74),256)[1]))
                simwave = mapcolor_wave_with_d(dx, dy, dz, 2)[1]
                if simwave <= 5:
                    # print('gota: <%.3f %.3f %.3f>'%(dx,dy,dz))
                    u = mapcolordistance_r_r(r, g, b, dx, dy, dz, 32)
                else:
                    u = 0
                if u >= max_simur:
                    max_simur = u
                    d = (dx, dy, dz)
                    if max_simur >= 0.986:
                        print('[Processing]similar[%.5f]with<%s>' % (max_simur, tuple2str(d, '%.3f %.3f %.3f')))
                        # return d,max_simur
                    if force_:
                        if max_simur >= force_:
                            return d, max_simur
            print('[dy]%.3f/%.3f maxnow=%.5f<%s> wave%s \r' % (
                dy, gmax, max_simur, tuple2str(d, '%.3f %.3f %.3f'), simwave), end='')
        print('[dx]%.3f/%.3f maxnow=%.5f<%s> wave%s  ' % (dx, rmax, max_simur, tuple2str(d, '%.3f %.3f %.3f'), simwave))

        if _main:
            pass

    return d, max_simur


def float_(inp):
    try:
        return float(inp)
    except:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')


def parse(help=False):
    parse = argparse.ArgumentParser(description='Minecraft dust Particle tools')
    parse.add_argument('-a', '--action', choices=['rgb2d', 'd2rgb', 'genimg', 'match'], metavar='',
                       help='模式选择{rgb2d,d2rgb,genimg,matchv}')
    # parse.add_argument('-rgb2d','--rgb2d',default=False,action='store_true')
    # parse.add_argument('-d2rgb','--d2rgb',default=False,action='store_true')
    # parse.add_argument('-genimg','--genimg',default=False,action='store_true')
    # parse.add_argument('-match','--match',default=False,action='store_true',help='')

    parse.add_argument('-r', '--red', default=None, type=int, metavar='', help='Red')
    parse.add_argument('-g', '--green', default=None, type=int, metavar='', help='Green')
    parse.add_argument('-b', '--blue', default=None, type=int, metavar='', help='Blue')

    parse.add_argument('-dx', default=None, type=float_)
    parse.add_argument('-dy', default=None, type=float_)
    parse.add_argument('-dz', default=None, type=float_)

    parse.add_argument('-fa', '--forceaccurate', default=0.97, type=float_, metavar='<0.01~0.99>', help='强制精确度[默认0.97]')
    parse.add_argument('-sa', '--searchall', default=False, action='store_true', help='全部搜索[默认关闭]')
    parse.add_argument('-t', '--trytimes', default=-1, metavar='', type=int, help='尝试次数[还原默认10000/转换默认64]')
    parse.add_argument('-s', '--scale', default=0.15, metavar='', type=float_, help='输出粒子图像缩放倍数[默认0.15]')
    parse.add_argument('-yf', '--y_offset', default=1.0, metavar='', type=float_, help='输出图像Y偏移[默认1.0]')

    parse.add_argument('-i', '--input_image', default='', metavar='', help='输入图像文件路径')
    parse.add_argument('-o', '--output_mcf', default='', metavar='', help='输出MCFUNCTION文件路径')
    if help:
        parse.print_help()
        return
    return parse.parse_args(), parse.print_help


def checkd(dx, dy, dz):
    if dx and dy and dz:
        return (float(dx), float(dy), float(dz))
    else:
        print('[ERROR]dx dy dz数据有缺失！')
        exit(0)


def checkrgb(r, g, b):
    if r and g and b:
        return (r, g, b)
    else:
        print('[Error]RGB数据有缺失！')
        exit(0)


def checkpath(inp_, opt_):
    if inp_ == '':
        print('[ERROR]输入图像文件缺失 请使用 -i <Path>导入')
        quit(0)
    if opt_ == '':
        print('[NOTICE]输出文件路径缺省,输出至原始文件目录')
        opt_ = os.path.splitext(inp_)[0] + '.mcfunction'
    if not os.path.exists(inp_):
        print('[ERROR]输入文件不存在！')
        exit(0)
    if os.path.exists(opt_):
        print('[WARN]输出文件已存在，完成计算时将覆盖源文件！')
    try:
        return cv2.imread(inp_), opt_, os.path.splitext(inp_)[0] + '.log'
    except cv2.error:
        print('[ERROR]输入文件非可读取图像文件')
        exit(0)


def matchSingleLog(str_):
    try:
        li = str_.split(' ')
        if len(li) != 8:
            return None
        return [int(li[2]), int(li[3])], [True, float(li[5]), float(li[6]), float(li[7]), float(li[4])]
    except:
        return None

def matchLogFile(path):
    if os.path.exists(path):
        pixlist = []
        data = []
        file =  open(path, 'r')
        while True:
            s_ = file.readline().strip()
            if s_ != '':
                try:
                    p_, d_ = matchSingleLog(s_)
                    pixlist.append(p_)
                    # print(str(p_),str(d_))
                    data.append([p_, d_])
                except:
                    pass
            else:
                file.close()
                print('[Controller]从记录中完成读取%s条数据'%len(pixlist))
                return pixlist, data

    else:
        return [], []


def dust_particle_main():
    args, help_ = parse()
    # print(args.action)
    if args.action == 'rgb2d':
        r, g, b = checkrgb(args.red, args.green, args.blue)
        if args.searchall:
            print('[FINAL]' + str(match_seq_rgb2d(r, g, b, force_=float(args.forceaccurate))))
        else:
            notfinish = True
            trytime = 0
            maxtrytime = int(args.trytimes)
            if maxtrytime <= 0:
                maxtrytime = 10000
            max_similar = -1
            d = 0
            hex_ = rgb2hex(r, g, b)
            print('[Controller][目标还原颜色%s][目标相似度%.4f]最大尝试次数%d次' % (hex_, args.forceaccurate, maxtrytime))
            while notfinish:
                trytime += 1
                if trytime >= maxtrytime:
                    notfinish = False
                    print('计算失败:请降低相似度并再次尝试[最高相似度%.4f<%s>]' % (max_similar, tuple2str(d, '%.4f %.4f %.4f')))
                dx, dy, dz = calculate_rgb2d(r, g, b)
                u = mapcolordistance_and_wave(hex_, dx, dy, dz, False)
                if u[0] >= float(args.forceaccurate):
                    centre_rgb, wave = mapcolor_wave_with_d(dx, dy, dz)
                    print('[FINAL]完成计算,相似度%.4f <dx:%.4f dy:%.4f dz:%.4f>' % (u[0], dx, dy, dz))
                    print('[FINAL][目标颜色%s]<尝试%s次>[与颜色中值%s差距%s]' % (hex_, trytime, rgb2hex(*centre_rgb), wave))
                    notfinish = False
                elif u[0] > max_similar:
                    max_similar = u[0]
                    d = (dx, dy, dz)
                    print('[Processing]similar[%.5f]with<%s>' % (max_similar, tuple2str(d, '%.3f %.3f %.3f')))
                # print('[Try]#%s/%s maxnow=%.5f<%s>'%(trytime,maxtrytime,max_similar,tuple2str(d,'%.3f %.3f %.3f')))
    elif args.action == 'd2rgb':
        li = []
        d = checkd(args.dx, args.dy, args.dz)
        force_ = calculate_d2rgb(*d, forcenet=0.74)
        maxtrytime = int(args.trytimes)
        if maxtrytime <= 0:
            maxtrytime = 64
        print('[Controller]设置%s 尝试次数:%s' % (tuple2str(d, 'dx:%.3f dy:%.3f dz:%.3f'), maxtrytime))
        for i in range(maxtrytime):
            now_ = calculate_d2rgb(*d)
            print('[Processing]#%s R%s G%s B%s' % (i, fillchar(now_[0], 3), fillchar(now_[1], 3), fillchar(now_[2], 3)))
            li.append(now_)
        print('[Processing]中心颜色%s(%s)' % (tuple2str(force_, 'R%sG%sB%s'), rgb2hex(*force_)))
        print('[FINAL]波动程度%s' % mapcolor_wave(force_, li))
    elif args.action == 'genimg':
        img, opt, logpath = checkpath(args.input_image, args.output_mcf)
        ylen, xlen, gp = img.shape
        if gp != 3:
            print('[ERROR]非标准RGB文件(通道数量%s)' % gp)
            exit(0)
        else:
            # data = []
            all_ = ylen * xlen
            start_total = time.time()
            force_ = args.forceaccurate
            maxtrytime = int(args.trytimes)
            if maxtrytime <= 0:
                maxtrytime = 10000
            now = 0
            print('[Controller]已选择输入路径:%s' % args.input_image)
            print('[Controller]完成图像读取:%sx%s 总像素数量%s' % (xlen, ylen, all_))
            print('[Controller]已选择输出路径:%s' % opt)
            print('[Controller]设置强制精确度为:%.3f' % force_)
            print('[Controller]设置最大尝试次数:%s' % maxtrytime)
            # TODO:两种模式计算！！
            # TODO:在这里插入一个检查已存在未生成完毕的临时文件
            if os.path.exists(logpath):
                print('[Controller]检测到存在未完成的记录文件，正在恢复')
            pix_, recovdata_ = matchLogFile(logpath)
            # time.sleep(0.1)
            # os.remove(logpath)
            for y in range(ylen):
                log_ = ''
                for x in range(xlen):
                    if [x, y] in pix_:
                        print('[SKIP]检测到像素[%s,%s]已被处理，跳过\r' % (x, y),end='')
                        # getdata_ = recovdata_[pix_.index([x, y])]
                        # data.append([[x, y], getdata_])
                        now += 1
                        # log_ += str(now) + ' 0.001 ' + str(x) + ' ' + str(y) + ' ' + str(getdata_[4]) + ' ' + str(
                        #     getdata_[1]) + ' ' + str(getdata_[2]) + ' ' + str(getdata_[3])+'\n'
                    else:
                        now += 1
                        start_ = time.time()
                        b, g, r = img[y][x]
                        print('[Processing]正在处理像素[%s/%s] %s\r' % (now, all_, rgb2hex(r, g, b)), end='')
                        ret_ = list(forcergb2data(r, g, b, force_, maxtrytime))
                        # data.append([[x, y], ret_])
                        log_ += str(now) + ' '+'%.3f'%(time.time() - start_)+' ' + str(x) + ' ' + str(y) + ' ' + str(
                            ret_[4]) + ' ' + str(ret_[1]) + ' ' + str(ret_[2]) + ' ' + str(ret_[3]) + '\n'
                        #                 return True, dx, dy, dz, u
                        #     return False, d, max_similar
                        # if ret_[0]:
                        print('[Processed]已完成处理像素#%s[耗时%.3fs][%s:%s]%.3f<%.4f %.4f %.4f>' % (
                            now, time.time() - start_, x, y, ret_[4], ret_[1], ret_[2], ret_[3]))
                        # else:
                        #     print('[Processed]已完成处理像素#%s[耗时%.3fs][%s:%s]%.3f<%.4f %.4f %.4f>' % (
                        #         now, time.time() - start_, x, y, ret_[2], ret_[1][0], ret_[1][1], ret_[1][2]))
                # TODO:添加存储log
                with open(logpath,'a') as fi_:
                    fi_.write(log_)
            # write2mcfunction(data, opt, args.scale, args.y_offset)
            print('[Processed]已完成全部像素处理，总耗时%.3fs 正在写入文件..' % (time.time() - start_total))
            data = matchLogFile(logpath)[1]
            write2mcfunction(data, opt, scale=args.scale, yf=args.y_offset)
            print('[FINAL]完成文件写入:%s' % opt)
    elif args.action == 'match':
        pass
    else:
        help_()


if __name__ == '__main__':
    import os
    dust_particle_main()
    #