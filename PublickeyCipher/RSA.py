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
if __name__ == "__main__":
    a = RSA()
    a.generateKey()
    print(a.__dict__.items())