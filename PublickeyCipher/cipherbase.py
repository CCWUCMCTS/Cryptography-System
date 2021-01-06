from random import randint
import base64
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
def i2b_ASN1(n):
    length = (len(bin(n)[2:]) + 7) // 8
    data = int.to_bytes(n,length,'big')
    return length,data
def derInteger(n):
    '''
        ASN.1标准中，INTEGER数据类型号为02。
        若数据长度小于128 Bytes，后接一个字节的数据长度，再接数据。
        否则，接一个0x8?，?代表数据长度为几个字节，之后为?字节的数据长度，再接数据。
        注意此处的数据为有符号的，即如果数据最高位为1，前面必须再接0x00，以避免产生负数。
        而根据观察，数据长度不需要带符号位。
        由此，这个函数不能处理负数的情况，如果数据长度非常非常大，也不能处理。

    '''
    length,data = i2b_ASN1(n)
    #print(data)
    if data[0] >= 128:
        data = b'\x00' + data
        length += 1
    if length < 128:
        return b'\x02' + int.to_bytes(length,1,'big') + data
    else:
        lengthlength,lengthdata = i2b_ASN1(length)
        return b'\x02' + int.to_bytes(128+lengthlength,1,'big') + lengthdata + data
def derTag(data):
    if len(data) < 128:
        return b'\x30' + int.to_bytes(len(data),1,'big') + data
    else:
        lengthlength,lengthdata = i2b_ASN1(len(data))
        return b'\x30' + int.to_bytes(128+lengthlength,1,'big') + lengthdata + data
def derBitString(data):
    data = b'\x00' + data
    if len(data) < 128:
        return b'\x03' + int.to_bytes(len(data),1,'big') + data
    else:
        lengthlength,lengthdata = i2b_ASN1(len(data))
        return b'\x03' + int.to_bytes(128+lengthlength,1,'big') + lengthdata + data
def derOctetString(data):
    if len(data) < 128:
        return b'\x04' + int.to_bytes(len(data),1,'big') + data
    else:
        lengthlength,lengthdata = i2b_ASN1(len(data))
        return b'\x04' + int.to_bytes(128+lengthlength,1,'big') + lengthdata + data
def derRSAPublicKey(n,e):
    
    data = derBitString(derTag(derInteger(n)+derInteger(e)))
    
    data = b'\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01\x01\x01\x05\x00' + data
    #print(showbytes(derTag(data)))
    rsapk = base64.b64encode(derTag(data))
    ret = []
    ret.append(b'-----BEGIN PUBLIC KEY-----')
    for i in range(0,len(rsapk),64):
        ret.append(rsapk[i:i+64])
    ret.append(b'-----END PUBLIC KEY-----')
    return ret
def derRSAPrivateKey(n,e,d,p,q):
    para1 = d % (p - 1)
    para2 = d % (q - 1)
    para3 = inv(q,p)
    data = derTag(derInteger(0)+derInteger(n)+derInteger(e)+derInteger(d)+derInteger(p)+derInteger(q)+derInteger(para1)+derInteger(para2)+derInteger(para3))
    
    data = derTag(derInteger(0)+b'\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01\x01\x01\x05\x00'+derOctetString(data))
    #print(showbytes(data))
    rsapk = base64.b64encode(data)
    ret = []
    ret.append(b'-----BEGIN PRIVATE KEY-----')
    for i in range(0,len(rsapk),64):
        ret.append(rsapk[i:i+64])
    ret.append(b'-----END PRIVATE KEY-----')
    return ret
'''
def exgcd(a,b):     
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = exgcd(b, a % b)        
        x, y = y, (x - (a // b) * y)         
        return x, y, q
        '''
        
def inv(a,b):
    x,_,z=exgcd(a,b)
    if z != 1:
        return -1
    return x%b

def speed(a,b,p):
    ans = 1
    cur = a % p
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
    '''
    a=CipherBase()
    print(speed(2,133424343434,3557),pow(2,133424343434,3557))
    print(getPrime(512))_
    s=[0]*10
    '''
    n=137015429574709912343865346940708311403051748153560874512698266923411251835816551968909371668151193640666768540429452379295325512807976338932581679767173077626808613537103155097678925760433414882731897852307263143791846318576784422533758581983294090370237306211012735981811220009739002094171150798990116063481
    e=65537
    d=52276894220297257399001373273912619232392525788177512965042955344612941577347038802242684873615218837982705149052267524364551542605908850801977583694373593853213399411401495810543246870663143926895824888055679882677865274245121492098101400555430614895884792809417275149086797396803208652152138651433334055553
    p=12095900113575032282912665577919892834500836240035429419972532290713062613645698757711921158386905204435634336047184481228965270011710698070057469234735657
    q=11327427333906281236874652509201762317492994571006699675106030231211264919537977441522403617158836694471602440337609739451512603688026500686788352058532433
    x=derRSAPrivateKey(n,e,d,p,q)
    #for i in x:
        #print(i.decode('utf-8'))
    
    