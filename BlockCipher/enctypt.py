from des import DES
from cipherbase import CipherBase
import base64
class Encrypt(CipherBase):
    def readFile(self,filename):
        f = open(filename,'rb')
        self.data = f.read()
        f.close()
    def writeFile(self,filename):
        f = open(filename+'.encrypt','wb')
        f.write(self.cdata)
        f.close()
    def aPadding(self,s):
        if s.lower() == 'zero':
            t = 8 - len(self.data) % 8
            for _ in range(t):
                self.data += b'\x00'
    def CBC(self,key,IV):
        self.cdata = b''
        a = DES()
        a.generateKey(key)
        for i in range(0,len(self.data),8):
            tmp = b''
            for j in range(8):
                tmp += self.i2b(IV[j]^self.data[i+j],1)
            IV = a.aBlockEncode(tmp)
            self.cdata += IV

    def encryptFile(self,filename,key,IV,mode='cbc',padding='zero',coding='base64'):
        self.readFile(filename)
        self.aPadding(padding)
        if mode.lower() == 'cbc':
            self.CBC(key,IV)
        else:
            pass
        if coding.lower() == 'base64':
            self.cdata = base64.b64encode(self.cdata)
        else:
            pass
        self.writeFile(filename)

if __name__ == '__main__':
    a = Encrypt()
    s = b'zzzzzzzz'
    a.encryptFile('C:\\Users\\wwwwww931121\\Desktop\\123.txt',s,s)