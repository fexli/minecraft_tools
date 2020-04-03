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


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        print(warp2Dimension(' '.join(sys.argv[1:])))
    else:
        print('Used for Minecraft 20w14infinite command /warp to dimension data')
        print('Usage:' + sys.argv[0] + ' <str>')
