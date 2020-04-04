def getCHARACTERS(int_) -> str:
    return [' ', ',', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][floorMod(int_, 29)]


def floorDiv(x: int, y: int) -> int:
    r = int(x / y)
    if (x ^ y) < 0 and r * y != x:
        r -= 1
    return r


def floorMod(x: int, y: int) -> int:
    return int(x - floorDiv(x, y) * y)


def asInt(hex_):
    return hex_[0] & 0xFF | (hex_[1] & 0xFF) << 8 | (hex_[2] & 0xFF) << 16 | (hex_[3] & 0xFF) << 24


# 仅用于实验目的，未进一步优化，有建议希望可以提给我！
# 仿java int溢出取低32位进行处理
def JavaInt2PythonInt(int_: int) -> int:
    if int_ >= 2 ** 48:
        raise ValueError('Invalid Integer')
    if int_ < 2 ** 31 and int_ >= -2 ** 31:
        return int_
    # fix
    if int_ < -2 ** 31:
        source = bin(2 ** 48 + int_)[-32:]
        return int(['0', '-0'][int(source[0])] + source[1:], 2)
    source = bin(int_)[-32:]
    if source[0] == '0':
        return int('0b' + source[1:], 2)
    else:
        bm = source[1:]
        fm = abs(int('0b' + bm, 2) - 1)

        return fm - (2 ** 31 - 1)


def javaIntSum(*Intlist):
    if len(Intlist) == 1:
        return Intlist[0]
    else:
        sum_ = 0
        for int_ in Intlist:
            sum_ = JavaInt2PythonInt(sum_ + int_)
        return sum_


# 字符串转换为维度数据
def warp2Dimension(str_):
    if isinstance(str_,str):
        import hashlib
        sha256_ = hashlib.sha256(str_.encode() + ':why_so_salty#LazyCrypto'.encode()).hexdigest()
        bytes_ = bytes.fromhex(sha256_)
        hex_ = []
        for i in range(4):
            hex_.append(bytes_[i])
        return (asInt(hex_) & 0x7FFFFFFF) - 1
    else:
        print('Unsupported value encountered.')
        return None


# warp2Dimension_fromBook(第一页内容字符串,第二页内容字符串...)
# 每页中换行符用\n(而非\\n)表示
# 单页、非换行的自写成书效果与/warp <str>指令效果相同
# 可以通过NBTExplorer等软件查看非自己编写成书的内容
def warp2Dimension_fromBook(*eachPage):
    return warp2Dimension('\n'.join(eachPage))


def warp2Dimension_frombookBox(x, y, z, facing='default'):
    p = getBook_fromBookbox(x, y, z, facing)
    return warp2Dimension_fromBook(*p['pages'])


def getBook_fromBookbox(x, y, z, facing='default'):
    import math
    from java_util_random import JavaRandom
    n3 = y
    if facing == 'NORTH':
        n = 15 - x & 0xF
        n2 = 0
    elif facing == 'SOUTH':
        n = x & 0xF
        n2 = 2
    elif facing == 'EAST':
        n = 15 - z & 0xF
        n2 = 1
    else:  # Default WEST
        n = z & 0xF
        n2 = 3
    if n > 0 and n < 15:
        cp_x = math.floor(x / 16)
        cp_z = math.floor(z / 16)
        str_ = str(cp_x) + '/' + str(cp_z) + '/' + str(n2) + '/' + str(n) + '/' + str(n3)
        r = JavaRandom(cp_x)
        r2 = JavaRandom(cp_z)
        r3 = JavaRandom((n << 8) + (n3 << 4) + n2)
        list_ = []
        for i in range(1, 17):
            sPage_ = ''
            for j in range(1, 129):
                # n4 = r.nextInt() + r2.nextInt() - r3.nextInt()
                n4 = javaIntSum(r.nextInt(), r2.nextInt(), -r3.nextInt())
                sPage_ += getCHARACTERS(n4)
            list_.append(sPage_)
        return {'title': str_, 'pages': list_, 'author': '§kUniverse itself'}
    else:
        return None


# /warp hex(list)[2:]
# 一个用于计算dimension的例子
def calculate(startint=0, times=10000):
    import struct
    structbyte_ = b''
    l = []
    for i in range(startint,startint+times):
        dim = warp2Dimension(hex(i)[2:])
        l.append(dim)
        structbyte_ += struct.pack('>I', dim)
    return structbyte_,l


def countrepeat(list_):
    import numpy as np
    li = np.array(list_)
    for item in li:
        whr = np.where(li==item)[0]
        s_count = len(whr)
        if s_count > 1:
            print("Dim %d repeat at %s" % (item, whr))
# Dim 618932306 repeat at [   1427 1777432]
# Dim 1878747668 repeat at [   1673 1805088]
# Dim 78823299 repeat at [   2281 1217584]
# Dim 708874572 repeat at [   6325 1461290]
# Dim 335680645 repeat at [ 6435 34590]
# Dim 1678524152 repeat at [   6557 1841129]...
# hex(6557)[2:] -> '199d'
# hex(1841129)[2:] -> '1c17e9'
# 带入20w14infinite可以发现/warp 199d和/warp 1c17e9效果是一样的


# 计算示例
def example():
    dim_list = []
#     if os.path.exists('./calculate.dim'):
#         os.remove('./calculate.dim')
    for i in range(20):
        s,l = calculate(i*100000,100000)
        dim_list += l
#         with open('./calculate.dim', 'ab') as f:
#             f.write(s)
        print('[C]已完成%d次计算' % ((i + 1) * 100000))
    return dim_list


def read_dimlist(path='./calculate.dim'):
    import struct
    dimlist = []
    if os.path.exists(path):
        file_ = open(path, 'rb')
        while True:
            try:
                dimlist.append(struct.unpack('>I', file_.read(4)))
            except struct.error:
                return dimlist
    return None


if __name__ == '__main__':
    import sys
    import os
    import struct
    import math
#     import numpy as np
    if len(sys.argv) >= 2:
        print(warp2Dimension(' '.join(sys.argv[1:])))
    else:
        print('Used for Minecraft 20w14infinite command /warp to dimension data')
        print('Usage:' + sys.argv[0] + ' <str>')
    # 你可以通过字符串查询可以去到的维度，例如：
    # print(warp2Dimension('cool'))
    # 你可以通过/warp cool指令前往，或者通过书与笔在第一页写下cool署名并丢入传送门进行传送
    # 你可以通过批量处理查找能去到的维度，例如：
    # dimlist = example()
    # import numpy as np
    # np.min(dimlist)
    # dimlist = np.array(dimlist) #numpy操作速度更高效
    # print('/warp' + hex(np.where(dimlist==dimlist.min())[0][0])[2:])
    # 经过500万次计算(~3-4分钟)后暂时发现最小维度值为538,指向该维度的字符串为hex(3166586)[2:]->'30517a'
    # 既/warp 30517a
    # 你也可以通过countrepeat(dimlist)来执行重复维度检查
    # 通过计算可以发现/warp 199d和/warp 1c17e9效果是一样的
    # 你可以用bookBox位置与朝向查询维度,例如：
    # print(warp2Dimension_frombookBox(260,64,-210,'WEST'))
