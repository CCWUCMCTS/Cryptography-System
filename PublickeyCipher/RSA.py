from cipherbase import CipherBase
from cipherbase import getPrime, speed, inv, gcd, derRSAPublicKey, derRSAPrivateKey
from random import randint
import os


class RSA(CipherBase):
    # 使用PKCS #1存储密钥
    def getInfo(self):
        print('这是一个RSA密码。')

    def generateKey(self, nbits=512):
        self.p = getPrime(nbits)
        self.q = getPrime(nbits)
        self.n = self.p * self.q
        eulerN = (self.p - 1) * (self.q - 1)
        self.e = randint(2, eulerN-1)
        while gcd(self.e, eulerN) != 1:
            self.e = randint(2, eulerN)
        self.d = inv(self.e, eulerN)
        self.mode = 'private'
        print('密钥生成成功！')

    def Encrypt(self, messageBytes):
        if self.b2i(messageBytes) >= self.n:
            print('消息过长无法加密。')
        return self.i2b(speed(self.b2i(messageBytes), self.e, self.n))

    def Decrypt(self, messageBytes):
        if self.mode != 'private':
            raise('请载入一个私钥。')
        return self.i2b(speed(self.b2i(messageBytes), self.d, self.n))

    def testEncrypt(self, messageInt):
        if messageInt >= self.n:
            print('消息过长无法加密。')
        return speed(messageInt, self.e, self.n)

    def testDecrypt(self, messageInt):
        if self.mode != 'private':
            raise('请载入一个私钥。')
        return speed(messageInt, self.d, self.n)

    def outputPrivateKey(self, filepath, filename='private', sep='\n'):
        pempath = os.path.join(filepath, filename+'.pem')
        with open(pempath, 'w') as f:
            for i in derRSAPrivateKey(self.n, self.e, self.d, self.p, self.q):
                f.write(i.decode('utf-8')+sep)
        txtpath = os.path.join(filepath, filename+'.txt')
        with open(txtpath, 'w') as f:
            f.write('n = '+str(self.n)+sep)
            f.write('e = '+str(self.e)+sep)
            f.write('d = '+str(self.d)+sep)
            f.write('p = '+str(self.p)+sep)
            f.write('q = '+str(self.q)+sep)

    def outputPublicKey(self, filepath, filename='public', sep='\n'):
        pempath = os.path.join(filepath, filename+'.pem')
        with open(pempath, 'w') as f:
            for i in derRSAPublicKey(self.n, self.e):
                f.write(i.decode('utf-8')+sep)
        txtpath = os.path.join(filepath, filename+'.txt')
        with open(txtpath, 'w') as f:
            f.write('n = '+str(self.n)+sep)
            f.write('e = '+str(self.e)+sep)

    def inputKey(self, keypath):
        self.n = self.e = self.d = self.p = self.q = 1
        with open(keypath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(' ')
                if line[0].lower() == 'n':
                    self.n = int(line[2])
                elif line[0].lower() == 'e':
                    self.e = int(line[2])
                elif line[0].lower() == 'd':
                    self.d = int(line[2])
                elif line[0].lower() == 'p':
                    self.p = int(line[2])
                elif line[0].lower() == 'q':
                    self.q = int(line[2])
        if self.n == 1 or self.e == 1:
            raise('请检查n和e。')
        self.mode = 'public'
        if self.d == 1 or self.p == 1 or self.q == 1:
            print('公钥加载成功，当前运行模式为：仅加密。')
            return
        self.mode = 'private'
        print('私钥加载成功，当前运行模式为：加密解密。')


if __name__ == "__main__":
    a = RSA()
    a.generateKey(512)
    a.outputPublicKey('C:\\Users\\wwwwww931121\\Desktop')
    a.outputPrivateKey('C:\\Users\\wwwwww931121\\Desktop')
    a.inputKey('C:\\Users\\wwwwww931121\\Desktop\\private.txt')

    print(a.b2i('hello'.encode('utf-8')))
    x = a.Encrypt('hello'.encode('utf-8'))
    print(x)
    y = a.Decrypt(x)
    print(y)
