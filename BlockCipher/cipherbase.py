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

def showbytes(b):
    return [hex(i) for i in list(b)]

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def exgcd(a,b):     
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = exgcd(b, a % b)        
        x, y = y, (x - (a // b) * y)         
        return x, y, q

def inv(a,b):
    x,_,z=exgcd(a,b)
    if z != 1:
        return -1
    return x%b


if __name__ == "__main__":
    a=CipherBase()
    print(exgcd(5,26))