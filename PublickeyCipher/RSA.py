from cipherbase import CipherBase
from cipherbase import getPrime,speed,inv,gcd
from random import randint
class RSA(CipherBase):
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
        print('e =',hex(self.e))
        print('d =',hex(self.d))
        print('n =',hex(self.n))
    def Encrypt(self,messageBytes):
        return speed(self.b2i(messageBytes),self.e,self.n)
    def Decrypt(self,messageInt):
        return speed(messageInt,self.d,self.n)

if __name__ == "__main__":
    a = RSA()
    a.generateKey(1024)
    #print(a.__dict__.items())
    print(a.b2i('hello'.encode('utf-8')))
    x=a.Encrypt('hello'.encode('utf-8'))
    print(x)
    y=a.Decrypt(x)
    print(y)