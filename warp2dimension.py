def asInt(hex_):
    return hex_[0] & 0xFF | (hex_[1] & 0xFF) << 8 | (hex_[2] & 0xFF) << 16 | (hex_[3] & 0xFF) << 24


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

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        print(warp2Dimension(' '.join(sys.argv[1:])))
    else:
        print('Used for Minecraft 20w14infinite command /warp to dimension data')
        print('Usage:' + sys.argv[0] + ' <str>')
