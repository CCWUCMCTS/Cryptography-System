from CipherTools import *
if __name__ == "__main__":
    from RSA import RSA
else:
    from .RSA import RSA
import os


class usefulRSA():
    def __init__(self, nbits=512, outpath=None, keypath=None):
        self.a = RSA()
        if keypath != None:
            self.a.inputKey(keypath)
            self.mode=self.a.mode
            return
        if outpath == None:
            outpath = './'
        self.a.generateKey(nbits)
        self.a.outputPublicKey(outpath)
        self.a.outputPrivateKey(outpath)

    def setKey(self, outpath):
        self.a.inputKey(outpath)
        self.mode=self.a.mode

    def fileEncrypt(self, filepath,suffix='.encrypt'):
        f1 = open(filepath, 'rb')
        c = self.a.Encrypt(f1.read())
        f1.close()
        f2 = open(filepath+suffix, 'wb')
        f2.write(c)
        f2.close()

    def fileDecrypt(self, filepath,suffix='.decrypt'):
        f1 = open(filepath, 'rb')
        m = self.a.Decrypt(f1.read())
        f1.close()
        f2 = open(filepath+suffix, 'wb')
        f2.write(m)
        f2.close()

    def byteEncrypt(self, messageByte):
        return self.a.Encrypt(messageByte)

    def byteDecrypt(self, messageBytes):
        return self.a.Decrypt(messageBytes)


if __name__ == "__main__":
    a = usefulRSA()
    file = 'message'
    a.fileEncrypt(file)
    a.fileDecrypt(file+'.encrypt')
