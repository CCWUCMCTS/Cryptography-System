from des import DES
from sm4 import SM4
from cipherbase import CipherBase
import base64
class uBlockCipher(CipherBase):
    def __init__(self,mode='des'):
        if mode.lower() == 'des':
            self.a = DES()
            self.blocksize = 8
        elif mode.lower() == 'sm4':
            self.a = SM4()
            self.blocksize = 16
    def readFile(self,filename):
        f = open(filename,'rb')
        self.data = f.read()
        f.close()
    def writeFile(self,filename,ed):
        f = open(filename+ed,'wb')
        f.write(self.cdata)
        f.close()
    def aPadding(self,s):
        if s.lower() == 'zero':
            t = self.blocksize - len(self.data) % self.blocksize
            for _ in range(t):
                self.data += b'\x00'
        elif s.lower() == 'pkcs7':
            t = self.blocksize - len(self.data) % self.blocksize
            pad = self.i2b(t,1)
            for _ in range(t):
                self.data += pad
        else:
            raise('没有这种填充方式。')
    def rePadding(self,s):
        if s.lower() == 'zero':
            las = len(self.cdata) - 1
            while self.cdata[las] == 0:
                las -= 1
            self.cdata = self.cdata[0:las+1]
        elif s.lower() == 'pkcs7':
            num = self.cdata[-1]
            self.cdata = self.cdata[0:len(self.cdata)-num]
        else:
            raise('没有这种填充方式。')
    def ECB_E(self,key):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0,len(self.data),self.blocksize):
            self.cdata += self.a.aBlockEncode(self.data[i:i+self.blocksize])
    def ECB_D(self,key):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0,len(self.data),self.blocksize):
            self.cdata += self.a.aBlockDecode(self.data[i:i+self.blocksize])
    def CBC_E(self,key,IV):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0,len(self.data),self.blocksize):
            tmp = b''
            for j in range(self.blocksize):
                tmp += self.i2b(IV[j]^self.data[i+j],1)
            IV = self.a.aBlockEncode(tmp)
            self.cdata += IV
    def CBC_D(self,key,IV):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0,len(self.data),self.blocksize):
            tmp = b''
            for j in range(self.blocksize):
                tmp += self.i2b(IV[j]^self.data[i+j],1)
            IV = self.a.aBlockEncode(tmp)
            self.cdata += IV
    def CFB_E(self,key,IV,cfb_s=8):
        if cfb_s % 8 != 0 or cfb_s > self.blocksize * 8:
            raise('明文分组长度出错。')
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0,len(self.data),cfb_s//8):
            tmp = b''
            eIV = self.a.aBlockEncode(IV)
            for j in range(cfb_s//8):
                tmp += self.i2b(eIV[j]^self.data[i+j],1)
            IV = IV[cfb_s//8:] + tmp
            self.cdata += tmp
    def encryptFile(self,filename,key,IV,mode='cbc',padding='pkcs7',coding='base64',cfb_s=8):
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
            raise('没有这种工作模式。')
            
        if coding.lower() == 'base64':
            self.cdata = base64.b64encode(self.cdata)
            
        elif coding.lower() == 'hex':
            self.cdata = ''.join([hex(i)[2:] for i in self.cdata]).encode('utf-8')
        else:
            raise('没有这种编码方案')
        self.writeFile(filename,'.encrypt')
    def decryptFile(self,filename,key,IV,mode='cbc',padding='pkcs7',coding='base64',cfb_s=8):
        self.readFile(filename)
        if coding.lower() == 'base64':
            self.data = base64.b64decode(self.data)
        elif coding.lower() == 'hex':
            tmp = b''
            for i in range(0,len(self.data),2):
                tmp += self.i2b(int(self.data[i:i+2].decode('utf-8'),16),1)
            self.data = tmp
        else:
            raise('没有这种编码方案')
        
        if mode.lower() == 'ecb':
            self.ECB_D(key)
        elif mode.lower() == 'cbc':
            self.CBC_D(key,IV)
        elif mode.lower() == 'cfb':
            self.CFB_D(key,IV,cfb_s)
        else:
            raise('没有这种工作模式。')
        self.rePadding(padding)
        self.writeFile(filename,'.decrypt')

if __name__ == '__main__':
    a = uBlockCipher()
    s = b'zzzzzzzz'
    # 可以拆成filepath，filename
    a.encryptFile('C:\\Users\\wwwwww931121\\Desktop\\123.txt',s,s,mode='cbc',padding='pkcs7',coding='base64',cfb_s=8)