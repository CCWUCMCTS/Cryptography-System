from cipherbase import CipherBase
class RC4(CipherBase):
    def getInfo():  
        '''
            打印LSFR的信息。
        '''
        print('这是一个RC4密码。')

    def init(self,key):
        self.S = [self.i2b(i,1) for i in range(256)]
        self.T = [self.i2b(key[i % len(key)], 1) for i in range(256)]
        j = 0
        for i in range(256):
            j = (j+self.S[i][0]+self.T[i][0]) % 256
            self.S[i],self.S[j] = self.S[j],self.S[i]
        print(self.S)

if __name__ == "__main__":
    a=RC4()
    a.init(b'\x01\x02')