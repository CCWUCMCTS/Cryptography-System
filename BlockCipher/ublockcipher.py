'''
文件名: ublockcipher.py
介绍: 
时间: 2021/01/12 22:15:55
作者: CCWUCMCTS
版本: 1.0
'''


from CipherTools import i2b
if __name__ == "__main__":
    from des import DES
    from sm4 import SM4
else:
    from .des import DES
    from .sm4 import SM4
import base64


class uBlockCipher():

    # 初始化选择密码算法
    def __init__(self, mode='des'):
        if mode.lower() == 'des':
            self.a = DES()
            self.blocksize = 8
        elif mode.lower() == 'sm4':
            self.a = SM4()
            self.blocksize = 16

    # 读取文件
    def readFile(self, filename):
        f = open(filename, 'rb')
        self.data = f.read()
        f.close()

    # 写加密后文件
    def writeFile(self, filename, ed):
        f = open(filename+ed, 'wb')
        f.write(self.cdata)
        f.close()

    # 填充，支持零填充、pkcs7
    def aPadding(self, s):
        if s.lower() == 'zero':
            t = self.blocksize - len(self.data) % self.blocksize
            for _ in range(t):
                self.data += b'\x00'
        elif s.lower() == 'pkcs7':
            t = self.blocksize - len(self.data) % self.blocksize
            pad = i2b(t, 1)
            for _ in range(t):
                self.data += pad
        else:
            raise('没有这种填充方式。')

    # 反填充
    def rePadding(self, s):
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

    # ECB模式加密
    def ECB_E(self, key):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0, len(self.data), self.blocksize):
            self.cdata += self.a.aBlockEncode(self.data[i:i+self.blocksize])

    # ECB模式解密
    def ECB_D(self, key):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0, len(self.data), self.blocksize):
            self.cdata += self.a.aBlockDecode(self.data[i:i+self.blocksize])

    # CBC模式加密
    def CBC_E(self, key, IV):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0, len(self.data), self.blocksize):
            tmp = b''
            # print(len(self.data))
            for j in range(self.blocksize):
                # print(j,i+j)
                tmp += i2b(IV[j] ^ self.data[i+j], 1)
            IV = self.a.aBlockEncode(tmp)
            self.cdata += IV

    # CBC模式解密
    def CBC_D(self, key, IV):
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0, len(self.data), self.blocksize):
            tmp = self.a.aBlockDecode(self.data[i:i+self.blocksize])
            for j in range(self.blocksize):
                self.cdata += i2b(IV[j] ^ tmp[j], 1)
            IV = self.data[i:i+self.blocksize]

    # CFB模式加密
    def CFB_E(self, key, IV, cfb_s=8):
        if cfb_s % 8 != 0 or cfb_s > self.blocksize * 8:
            raise('明文分组长度出错。')
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0, len(self.data), cfb_s//8):
            tmp = b''
            eIV = self.a.aBlockEncode(IV)
            for j in range(cfb_s//8):
                tmp += i2b(eIV[j] ^ self.data[i+j], 1)
            IV = IV[cfb_s // 8:] + tmp
            self.cdata += tmp

    # CFB模式解密
    def CFB_D(self, key, IV, cfb_s=8):
        if cfb_s % 8 != 0 or cfb_s > self.blocksize * 8:
            raise('明文分组长度出错。')
        self.cdata = b''
        self.a.generateKey(key)
        for i in range(0, len(self.data), cfb_s//8):
            tmp = b''
            eIV = self.a.aBlockEncode(IV)
            for j in range(cfb_s//8):
                tmp += i2b(eIV[j] ^ self.data[i+j], 1)
            IV = IV[cfb_s // 8:] + self.data[i:i + cfb_s // 8]
            self.cdata += tmp

    # 文件加密
    def encryptFile(self, filename, key, IV, mode='cbc', padding='pkcs7', coding='base64', cfb_s=8):
        self.readFile(filename)
        self.aPadding(padding)
        if mode.lower() == 'ecb':
            print('请注意，ECB模式可能不安全！')
            self.ECB_E(key)
        elif mode.lower() == 'cbc':
            self.CBC_E(key, IV)
        elif mode.lower() == 'cfb':
            self.CFB_E(key, IV, cfb_s)
        else:
            raise('没有这种工作模式。')

        if coding.lower() == 'base64':
            self.cdata = base64.b64encode(self.cdata)

        elif coding.lower() == 'hex':
            self.cdata = ''.join([hex(i)[2:]
                                  for i in self.cdata]).encode('utf-8')
        else:
            raise('没有这种编码方案')
        self.writeFile(filename, '.encrypt')

    # 文件解密
    def decryptFile(self, filename, key, IV, mode='cbc', padding='pkcs7', coding='base64', cfb_s=8):
        self.readFile(filename)
        if coding.lower() == 'base64':
            self.data = base64.b64decode(self.data)
        elif coding.lower() == 'hex':
            tmp = b''
            for i in range(0, len(self.data), 2):
                tmp += i2b(int(self.data[i:i+2].decode('utf-8'), 16), 1)
            self.data = tmp
        else:
            raise('没有这种编码方案')

        if mode.lower() == 'ecb':
            self.ECB_D(key)
        elif mode.lower() == 'cbc':
            self.CBC_D(key, IV)
        elif mode.lower() == 'cfb':
            self.CFB_D(key, IV, cfb_s)
        else:
            raise('没有这种工作模式。')
        self.rePadding(padding)
        self.writeFile(filename, '.decrypt')

    # 测试模式
    def show(self):
        s = b'zzzzzzzz'
        self.encryptFile('BlockCipher\\123.txt', s, s, mode='cfb',
                         padding='pkcs7', coding='base64')
        self.decryptFile('BlockCipher\\123.txt.encrypt', s, s, mode='cfb',
                         padding='pkcs7', coding='base64')


if __name__ == '__main__':
    a = uBlockCipher('des')
    a.show()
