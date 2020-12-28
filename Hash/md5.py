from cipherbase import CipherBase
import math
class MD5(CipherBase):

    IV_A, IV_B, IV_C, IV_D = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

    lshift = [
        [7,12,17,22],
        [5,9,14,20],
        [4,11,16,23],
        [6,10,15,21]
    ]

    mindex = []

    T = []

    def getInfo(self):
        print("这是一个MD5哈希算法。")

    def generateSinTable(self,i):
        return math.floor(abs(math.sin(i)) * 2 ** 32)

    def __init__(self):
        self.mindex.append([i for i in range(16)])
        self.mindex.append([(1+5*i)%16 for i in range(16)])
        self.mindex.append([(5+3*i)%16 for i in range(16)])
        self.mindex.append([7*i%16 for i in range(16)])
        self.T.extend([self.generateSinTable(i+1) for i in range(64)])
        
    @staticmethod
    def F(X,Y,Z):
        return (X & Y) | (~X & Z)

    @staticmethod
    def G(X,Y,Z):
        return (X & Z) | (Y & ~Z)

    @staticmethod
    def H(X,Y,Z):
        return X ^ Y ^ Z

    @staticmethod
    def I(X,Y,Z):
        return Y ^ (X | ~Z)

    fun = [F.__func__,G.__func__,H.__func__,I.__func__]

    def getPadding(self,message):
        fir = b'\x80'
        other = b'\x00'
        length = len(message)
        if length % 64 == 56:
            message += fir + other * 63
        elif length % 64 < 56:
            message += fir + other * (56 - length % 64 - 1)
        else:
            message += fir + other * (120 - length % 64 - 1)
        length *= 8
        length %= 2**64
        message += self.i2b(length,8)[::-1]
        return message

    def aBlockHash(self,a,b,c,d,m):
        A,B,C,D = a,b,c,d
        groups = [self.b2i(m[i:i+4][::-1]) for i in range(0,len(m),4)]
        for i in range(4):
            for j in range(16):
                AA,BB = A,B
                fout = self.fun[i](B,C,D)
                A,C,D = D,B,C
                B = self.addm(AA,fout)
                B = self.addm(B,groups[self.mindex[i][j]])
                B = self.addm(B,self.T[i*16+j])
                B = self.a32CycleLeftMove(B,self.lshift[i][j%4])
                B = self.addm(B,BB)
        A = self.addm(A,a)
        B = self.addm(B,b)
        C = self.addm(C,c)
        D = self.addm(D,d)
        return A,B,C,D

    

    def hash(self,message):
        message = self.getPadding(message)
        blocks = [message[i:i+64] for i in range(0,len(message),64)]
        A,B,C,D = self.IV_A,self.IV_B,self.IV_C,self.IV_D
        for block in blocks:
            A,B,C,D = self.aBlockHash(A,B,C,D,block)
        A = self.i2LittleStr(A,4)
        B = self.i2LittleStr(B,4)
        C = self.i2LittleStr(C,4)
        D = self.i2LittleStr(D,4)
        return A+B+C+D


if __name__ == "__main__":
    a=MD5()
    print(a.hash(b'asjkfskdfsdjnjfl243435knknknkjkdsdda22424244242ksdlsskkmfkdfkdmkgm242323493894587487asjkfskdfsdjnjfl243435knknknkjkdsdda22424244242ksdlsskkmfkdfkdmkgm242323493894587487asjkfskdfsdjnjfl243435knknknkjkdsdda22424244242ksdlsskkmfkdfkdmkgm242323493894587487asjkfskdfsdjnjfl243435knknknkjkdsdda22424244242ksdlsskkmfkdfkdmkgm242323493894587487'))
