'''
文件名: uRSA.py
介绍: 
时间: 2021/01/12 23:31:58
作者: CCWUCMCTS
版本: 1.0
'''


from CipherTools import *
if __name__ == "__main__":
    from RSA import RSA
else:
    from .RSA import RSA
import os


class usefulRSA():

    # 初始化，若未输入密钥路径，则随机生成密钥
    def __init__(self, nbits=512, outpath=None, keypath=None):
        self.a = RSA()
        if keypath != None:
            self.a.inputKey(keypath)
            self.mode = self.a.mode
            return
        if outpath == None:
            outpath = 'PublickeyCipher\\'
        self.a.generateKey(nbits)
        self.a.outputPublicKey(outpath)
        self.a.outputPrivateKey(outpath)

    # 手动设置密钥
    def setKey(self, outpath):
        self.a.inputKey(outpath)
        self.mode = self.a.mode

    # 文件加密
    def fileEncrypt(self, filepath, suffix='.encrypt'):
        f1 = open(filepath, 'rb')
        c = self.a.Encrypt(f1.read())
        f1.close()
        f2 = open(filepath+suffix, 'wb')
        f2.write(c)
        f2.close()

    # 文件解密
    def fileDecrypt(self, filepath, suffix='.decrypt'):
        f1 = open(filepath, 'rb')
        m = self.a.Decrypt(f1.read())
        f1.close()
        f2 = open(filepath+suffix, 'wb')
        f2.write(m)
        f2.close()

    # 字节加密
    def byteEncrypt(self, messageByte):
        return self.a.Encrypt(messageByte)

    # 字节解密
    def byteDecrypt(self, messageBytes):
        return self.a.Decrypt(messageBytes)

    # 效果展示
    def show(self):
        file = 'PublickeyCipher\\message'
        self.fileEncrypt(file)
        self.fileDecrypt(file+'.encrypt')


if __name__ == "__main__":
    a = usefulRSA()
    a.show()
