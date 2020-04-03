def asInt(hex_):
    return hex_[0] & 0xFF | (hex_[1] & 0xFF) << 8 | (hex_[2] & 0xFF) << 16 | (hex_[3] & 0xFF) << 24


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
    if os.path.exists('./calculate.dim'):
        os.remove('./calculate.dim')
    for i in range(20):
        s,l = calculate(i*100000,100000)
        dim_list += l
#         with open('./calculate.dim', 'ab') as f:
#             f.write(s)
        print('[C]已完成%d次计算' % ((i + 1) * 100000))
    return dim_list
# dimlist = example()
# countrepeat(dimlist)

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
    if len(sys.argv) >= 2:
        print(warp2Dimension(' '.join(sys.argv[1:])))
    else:
        print('Used for Minecraft 20w14infinite command /warp to dimension data')
        print('Usage:' + sys.argv[0] + ' <str>')
