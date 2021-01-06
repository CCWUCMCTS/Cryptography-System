from RSA import RSA
from cipherbase import CipherBase
import os
class usefulRSA(CipherBase):
    def __init__(self,nbits=512,outpath=None,keypath=None):
        self.a = RSA()
        if keypath != None:
            self.a.inputKey(keypath)
            return
        if outpath == None:
            outpath = './'
        self.a.generateKey(nbits)
        self.a.outputPublicKey(outpath)
        self.a.outputPrivateKey(outpath)
    def setKey(self,outpath):
        self.a.inputKey(outpath)
    def fileEncrypt(self,filepath):
        f1 = open(filepath,'rb')
        c = self.a.Encrypt(f1.read())
        f1.close()
        f2 = open(filepath+'.encrypt','wb')
        f2.write(c)
        f2.close()
    def fileDecrypt(self,filepath):
        f1 = open(filepath,'rb')
        m = self.a.Decrypt(f1.read())
        f1.close()
        f2 = open(filepath+'.decrypt','wb')
        f2.write(m)
        f2.close()
    def strEncrypt(self,messageStr):
        return self.a.Encrypt(messageStr.encode('utf-8'))
    def strDecrypt(self,messageBytes):
        return self.a.Decrypt(messageBytes).decode('utf-8')
if __name__ == "__main__":
    a = usefulRSA()
    file='message'
    a.fileEncrypt(file)
    a.fileDecrypt(file+'.encrypt')
