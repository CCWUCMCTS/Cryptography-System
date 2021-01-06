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


    def Encrypt(self,messageBytes):
        return speed(self.b2i(messageBytes),self.e,self.n)

    def Decrypt(self,messageInt):
        return speed(messageInt,self.d,self.n)

    def outputPrivateKey(self,filepath,filename='private',sep='\n'):
        pempath = os.path.join(filepath,filename+'.pem')
        with open(pempath,'w') as f:
            for i in derRSAPrivateKey(self.n,self.e,self.d,self.p,self.q):
                f.write(i.decode('utf-8')+sep)
        txtpath = os.path.join(filepath,filename+'.txt')
        with open(txtpath,'w') as f:
            f.write('n = '+str(self.n)+sep)
            f.write('e = '+str(self.e)+sep)
            f.write('d = '+str(self.d)+sep)
            f.write('p = '+str(self.p)+sep)
            f.write('q = '+str(self.q)+sep)

    def outputPublicKey(self,filepath,filename='public',sep='\n'):
        pempath = os.path.join(filepath,filename+'.pem')
        with open(pempath,'w') as f:
            for i in derRSAPublicKey(self.n,self.e):
                f.write(i.decode('utf-8')+sep)
        txtpath = os.path.join(filepath,filename+'.txt')
        with open(txtpath,'w') as f:
            f.write('n = '+str(self.n)+sep)
            f.write('e = '+str(self.e)+sep)

    def inputPrivateKey(self,filepath,sep='\n'):
        with open(filepath,'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(' ')
                if line[0].lower == 'n':
                    self.n = int(line[2])
                elif line[0].lower == 'e':
                    self.e = int(line[2])
                elif line[0].lower == 'd':
                    self.d = int(line[2])
                elif line[0].lower == 'p':
                    self.p = int(line[2])
                elif line[0].lower == 'q':
                    self.q = int(line[2])
        print(self.n)
        print(self.e)
        print(self.d)
        print(self.p)
        print(self.q)
    
if __name__ == "__main__":
    a = RSA()
    a.generateKey(512)
    a.outputPublicKey('C:\\Users\\wwwwww931121\\Desktop')
    a.outputPrivateKey('C:\\Users\\wwwwww931121\\Desktop')
    a.inputPrivateKey('C:\\Users\\wwwwww931121\\Desktop\\private.txt')
    '''
    print(a.b2i('hello'.encode('utf-8')))
    x=a.Encrypt('hello'.encode('utf-8'))
    print(x)
    y=a.Decrypt(x)
    print(y)
    '''