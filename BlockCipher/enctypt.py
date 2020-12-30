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
    def CBC_E(self,key,IV):
        self.cdata = b''
        a = DES()
        a.generateKey(key)
        for i in range(0,len(self.data),8):
            tmp = b''
            for j in range(8):
                tmp += self.i2b(IV[j]^self.data[i+j],1)
            IV = a.aBlockEncode(tmp)
            self.cdata += IV
    def ECB_E(self,key):
        self.cdata = b''
        a = DES()
        a.generateKey(key)
        for i in range(0,len(self.data),8):
            self.cdata = a.aBlockEncode(self.data[i:i+8])
    def CFB_E(self,key,IV,cfb_s):
        if cfb_s % 8 != 0 or cfb_s > 64:
            raise('明文分组长度超限。')
        self.cdata = b''
        a = DES()
        a.generateKey(key)
        for i in range(0,len(self.data),cfb_s//8):
            tmp = b''
            eIV = a.aBlockEncode(IV)
            try:
                for j in range(cfb_s//8):
                    tmp += self.i2b(eIV[j]^self.data[i+j],1)
            except:
                print('没有整除，问题不大。')
            IV = IV[cfb_s//8:] + tmp
            self.cdata += tmp
    def encryptFile(self,filename,key,IV,mode='cbc',padding='zero',coding='base64',cfb_s=8):
        self.readFile(filename)
        self.aPadding(padding)
        if mode.lower() == 'ecb':
            print('请注意，ECB模式可能不安全！')
            self.ECB_E(key)
        elif mode.lower() == 'cbc':
            self.CBC_E(key,IV)
        elif mode.lower() == 'cfb':
            self.CFB_E(key,IV,cfb_s)
        else:
            pass
            
        if coding.lower() == 'base64':
            self.cdata = base64.b64encode(self.cdata)
            
        elif coding.lower() == 'hex':
            self.cdata = ''.join([hex(i)[2:] for i in self.cdata]).encode('utf-8')
        else:
            raise('没有这种加密模式！')
        self.writeFile(filename)

if __name__ == '__main__':
    a = Encrypt()
    s = b'zzzzzzzz'
    a.encryptFile('C:\\Users\\wwwwww931121\\Desktop\\123.txt',s,s,mode='cfb',padding='zero',coding='base64',cfb_s=8)