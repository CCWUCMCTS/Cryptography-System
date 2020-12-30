class CipherBase:
    def getInfo(self):
        print('This is a base class for cipher.')

    def Encrypt(self):
        pass

    def Decrypt(self):
        pass

    def generateKey(self,key):
        pass

    def aBlockEncode(self,messages):
        pass

    def aBlockDecode(self,messages):
        pass

    def a32CycleLeftMove(self,num,i):
        i = i%32
        return (((num>>(32-i))|(num<<i)))&0xffffffff
    def aCycleLeftMove(self,num,bas,i):
        i = i%bas
        return (((num>>(bas-i))|(num<<i)))&((1<<bas)-1)
    def cutNumber2List(self,num,total,piece):
        if total % piece != 0:
            raise Exception
        ret = []
        for _ in range(total//piece):
            ret.append(num&((1<<piece)-1))
            num >>= piece
        return ret[::-1]

    def mergeList2Number(self,inputs,piece):
        ret = 0
        for input in inputs:
            ret <<= piece
            ret |= input
        return ret

    def b2i(self,x):
        return int.from_bytes(x,'big')

    def i2b(self,x,num):
        return int.to_bytes(x,num,'big')
    def byte2bit(self,bytek):
        ret = []
        for i in bytek:
            #print(i)
            t = 0x80
            for j in range(8):
                ret.append((i&t)>>(7-j))
                t >>= 1
        return ret
    def bit2byte(self,bits):
        ret = []
        for i in range(0,len(bits),8):
            ret.append(self.bit2int(bits[i:i+8]))
        return bytes(ret)
    def bit2int(self,bits):
        ret = 0
        for bit in bits:
            ret <<= 1
            ret |= bit
        return ret
def showbytes(b):
    return [hex(i) for i in list(b)]
def showbytesbin(b):
    return [bin(i) for i in list(b)]
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def exgcd(a,b):
    x0 = 1; y0 = 0
    x1 = 0; y1 = 1
    x = 0; y = 1  
    r = a % b
    q = (a - r) // b
    while r != 0:
        x = x0 - q * x1
        y = y0 - q * y1
        x0 = x1; y0 = y1
        x1 = x; y1 = y
        a = b; b = r; r = a % b
        q = (a - r) // b
    return x, y, b  

def inv(a,b):
    x,_,z=exgcd(a,b)
    if z != 1:
        return -1
    return x%b


if __name__ == "__main__":
    a=CipherBase()
    print(a.bit2byte([0,0,0,1,1,0,0,0]))
    print(a.i2b(2**64,8))