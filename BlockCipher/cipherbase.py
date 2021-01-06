'''
文件名: cipherbase.py
介绍: 分组密码的父类和工具库。
时间: 2021/01/06 16:15:09
作者: CCWUCMCTS
版本: 1.0
'''


class CipherBase:
    def getInfo(self):
        print('This is a base class for cipher.')

    def Encrypt(self):
        pass

    def Decrypt(self):
        pass

    def generateKey(self):
        pass

    def aBlockEncode(self):
        pass

    def aBlockDecode(self):
        pass

    def a32CycleLeftMove(self, num, i):
        """
        函数描述:
        32位循环左移。

        参数:
        @num: 需要循环左移的数字。
        @i: 循环左移的位数。

        返回值:
        32位循环左移结果。
        """
        i = i % 32
        return (((num >> (32-i)) | (num << i))) & 0xffffffff

    def aCycleLeftMove(self, num, bas, i):
        """
        函数描述:
        任意位循环左移。

        参数:
        @num: 需要循环左移的数字。
        @bas: 循环的位数。
        @i: 循环左移的位数。

        返回值:
        任意位循环左移结果。
        """
        i = i % bas
        return (((num >> (bas-i)) | (num << i))) & ((1 << bas)-1)

    def cutNumber2List(self, num, total, piece):
        """
        函数描述:
        将一个数字按二进制位的固定长度分组，返回分组后的数字列表。

        参数:
        @num: 待分组的数字。
        @total: 数字的二进制位数。
        @piece: 每组的大小。

        返回值:
        返回数字的二进制分组后的列表。

        示例:
        十进制421，即0b110100101，分组后返回[110,100,101]。
        """

        if total % piece != 0:
            raise Exception
        ret = []
        for _ in range(total//piece):
            ret.append(num & ((1 << piece)-1))
            num >>= piece
        return ret[::-1]

    def mergeList2Number(self, inputs, piece):
        ret = 0
        for input in inputs:
            ret <<= piece
            ret |= input
        return ret

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


def nhex(n):
    ret = hex(n)[2:]
    if len(ret) % 2 == 1:
        return '0' + ret
    else:
        return ret


def showbytes(b):
    return ''.join([nhex(i) for i in list(b)])


def showbytesbin(b):
    return [bin(i) for i in list(b)]


if __name__ == "__main__":
    a = CipherBase()
    print(a.bit2byte([0, 0, 0, 1, 1, 0, 0, 0]))
    print(a.i2b(2**64, 8))
