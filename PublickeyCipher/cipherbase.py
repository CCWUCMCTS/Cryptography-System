from random import randint
pri=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,233,239,
    241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,
    421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,
    607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,
    809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997
    ]
class CipherBase:
    def getInfo(self):
        print('This is a base class for cipher.')

    def Encrypt(self):
        pass

    def Decrypt(self):
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

def speed(a,b,p):
    ans = 1
    cur = a
    while b != 0:
        if b & 1:
            ans = ans * cur % p
        cur = cur * cur % p
        b >>= 1
    return ans

def Miller_Rabin(n,k=5):
    if n <= 1000:
        return n in pri
    t = n - 1
    s = 0
    while(t % 2 == 0):
        s += 1
        t = t // 2
    for _ in range(k):
        b = randint(2,n-2)
        r = speed(b,t,n)
        if r == 1 or r == n-1:
            continue
        else:
            for _ in range(1,s):
                r = r * r % n
                if r == n-1:
                    break
            else:
                return False
    return True

def getPrime(n):
    while(True):
        num = int('1'+''.join([str(randint(0,1)) for i in range(n-2)])+'1',2)
        if Miller_Rabin(num):
            return num
if __name__ == "__main__":
    a=CipherBase()
    print(speed(2,133424343434,3557),pow(2,133424343434,3557))
    print(getPrime(512))
    s=[0]*10
    