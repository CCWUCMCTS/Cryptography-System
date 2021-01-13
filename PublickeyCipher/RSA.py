'''
文件名: RSA.py
介绍: 
时间: 2021/01/12 23:00:02
作者: CCWUCMCTS
版本: 1.0
'''


from CipherTools import getPrime, speed, inv, gcd, derRSAPublicKey, derRSAPrivateKey, i2b, b2i
from random import randint
import os


class RSA():

    # 密钥生成
    def generateKey(self, nbits=512):
        self.p = getPrime(nbits)
        self.q = getPrime(nbits)
        self.n = self.p * self.q
        eulerN = (self.p - 1) * (self.q - 1)
        # 此处可改小e做优化
        self.e = randint(2, eulerN-1)
        while gcd(self.e, eulerN) != 1:
            self.e = randint(2, eulerN)
        self.d = inv(self.e, eulerN)
        self.mode = 'private'
        # print('密钥生成成功！')

    # 字节加密
    def Encrypt(self, messageBytes):
        if b2i(messageBytes) >= self.n:
            print('消息过长无法加密。')
        return i2b(speed(b2i(messageBytes), self.e, self.n))

    # 字节解密
    def Decrypt(self, messageBytes):
        if self.mode != 'private':
            raise('请载入一个私钥。')
        return i2b(speed(b2i(messageBytes), self.d, self.n))

    # 整数加密
    def testEncrypt(self, messageInt):
        if messageInt >= self.n:
            print('消息过长无法加密。')
        return speed(messageInt, self.e, self.n)

    # 整数解密
    def testDecrypt(self, messageInt):
        if self.mode != 'private':
            raise('请载入一个私钥。')
        return speed(messageInt, self.d, self.n)

    # 输出私钥
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
        return txtpath

    # 输出公钥
    def outputPublicKey(self, filepath, filename='public', sep='\n'):
        pempath = os.path.join(filepath, filename+'.pem')
        with open(pempath, 'w') as f:
            for i in derRSAPublicKey(self.n, self.e):
                f.write(i.decode('utf-8')+sep)
        txtpath = os.path.join(filepath, filename+'.txt')
        with open(txtpath, 'w') as f:
            f.write('n = '+str(self.n)+sep)
            f.write('e = '+str(self.e)+sep)
        return txtpath

    # 输入密钥
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

    # 展示
    def show(self):
        self.generateKey(512)
        self.outputPublicKey('PublickeyCipher')
        self.outputPrivateKey('PublickeyCipher')
        self.inputKey('PublickeyCipher\\private.txt')
        print(b2i('hello'.encode('utf-8')))
        x = self.Encrypt('hello'.encode('utf-8'))
        print(x)
        y = self.Decrypt(x)
        print(y)


if __name__ == "__main__":
    a = RSA()
    a.show()
