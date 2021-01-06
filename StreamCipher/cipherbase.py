class CipherBase:
    def getInfo(self):
        print('This is a base class for cipher.')

    def Encrypt(self):
        pass

    def Decrypt(self):
        pass

    def getNextKey(self):
        pass

    def b2i(self, x):
        return int.from_bytes(x, 'big')

    def i2b(self, x, num):
        return int.to_bytes(x, num, 'big')

    def byte2bit(self, bytek):
        ret = []
        for i in bytek:
            # print(i)
            t = 0x80
            for j in range(8):
                ret.append((i & t) >> (7-j))
                t >>= 1
        return ret

    def bit2byte(self, bits):
        ret = []
        for i in range(0, len(bits), 8):
            ret.append(self.bit2int(bits[i:i+8]))
        return bytes(ret)

    def bit2int(self, bits):
        ret = 0
        for bit in bits:
            ret <<= 1
            ret |= bit
        return ret


def showbytes(b):
    return [hex(i) for i in list(b)]


def showbytesbin(b):
    return [bin(i) for i in list(b)]


if __name__ == "__main__":
    a = CipherBase()
    print(a.i2b(666, 3))
