from cipherbase import CipherBase
from cipherbase import getPrime,speed,inv,gcd,derRSAPublicKey,derRSAPrivateKey
from random import randint
import os
class RSA(CipherBase):
    # 使用PKCS #1存储密钥
    def getInfo(self):
        print('这是一个RSA密码。')
    def generateKey(self,nbits=512):
        self.p = getPrime(nbits)
        self.q = getPrime(nbits)
        self.n = self.p * self.q
        self.eulerN = (self.p - 1) * (self.q - 1)
        self.e = randint(2,self.eulerN-1)
        while gcd(self.e,self.eulerN) != 1:
            self.e = randint(2,self.eulerN)
        self.d = inv(self.e,self.eulerN)
        print('密钥生成成功！')
        #print('p =',hex(self.p))
        #print('q =',hex(self.q))
        #for i in derRSAPrivateKey(self.n,self.e,self.d,self.p,self.q):
            #print(i.decode('utf-8'))
        print('e =',hex(self.e))
        print('d =',hex(self.d))
        print('n =',hex(self.n))
    def Encrypt(self,messageBytes):
        return speed(self.b2i(messageBytes),self.e,self.n)
    def Decrypt(self,messageInt):
        return speed(messageInt,self.d,self.n)
    def outputPrivateKey(self,filepath,filename='private.pem'):
        path = os.path.join(filepath,filename)
        with open(path,'w') as f:
            for i in derRSAPrivateKey(self.n,self.e,self.d,self.p,self.q):
                f.write(i.decode('utf-8')+'\n')
    def outputPublicKey(self,filepath,filename='public.pem'):
        path = os.path.join(filepath,filename)
        with open(path,'w') as f:
            for i in derRSAPublicKey(self.n,self.e):
                f.write(i.decode('utf-8')+'\n')

    
if __name__ == "__main__":
    a = RSA()
    a.generateKey(512)
    a.outputPublicKey('C:\\Users\\wwwwww931121\\Desktop')
    a.outputPrivateKey('C:\\Users\\wwwwww931121\\Desktop')
    #print(a.__dict__.items())
    print(a.b2i('hello'.encode('utf-8')))
    x=a.Encrypt('hello'.encode('utf-8'))
    print(x)
    y=a.Decrypt(x)
    print(y)