from cipherbase import CipherBase
class RC4(CipherBase):
    n = 8
    p = 256
    def getInfo(self):  
        '''
            打印LSFR的信息。
        '''
        print('这是一个RC4密码。')
    def setN(self,n):
        self.n = n
        self.p = 2**n
    def init(self,key):
        self.S = [self.i2b(i,1) for i in range(self.p)]
        self.T = [self.i2b(key[i % len(key)], 1) for i in range(self.p)]
        j = 0
        for i in range(self.p):
            j = (j+self.S[i][0]+self.T[i][0]) % self.p
            self.S[i],self.S[j] = self.S[j],self.S[i]
        print(self.S)
        
    def generateSeq(self,key,length):
        self.init(key)
        i = 0
        j = 0
        self.seq = []
        for _ in range(length):
            i = (i+1)%self.p
            j = (j+self.S[i][0])%self.p
            self.S[i],self.S[j] = self.S[j],self.S[i]
            t = (self.S[i][0]+self.S[j][0])%self.p
            k = self.S[t]
            self.seq.append(k)


if __name__ == "__main__":
    a=RC4()
    a.setN(3)
    a.generateSeq(b'\x05\x06\x07',5)
    print(a.seq)