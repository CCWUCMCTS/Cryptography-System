'''
文件名: rc4.py
介绍: 
时间: 2021/01/12 18:46:56
作者: CCWUCMCTS
版本: 1.0
'''


from CipherTools import i2b


class RC4():
    n = 8
    p = 256

    # 设置参数n
    def setN(self, n):
        self.n = n
        self.p = 2**n

    # 数据表S的初始变换
    def init(self, key):
        self.S = [i2b(i, 1) for i in range(self.p)]
        self.T = [i2b(key[i % len(key)], 1) for i in range(self.p)]
        j = 0
        for i in range(self.p):
            j = (j+self.S[i][0]+self.T[i][0]) % self.p
            self.S[i], self.S[j] = self.S[j], self.S[i]
        print(self.S)

    # 密钥流的生成
    def generateSeq(self, key, length):
        self.init(key)
        i = 0
        j = 0
        self.seq = []
        for _ in range(length):
            i = (i+1) % self.p
            j = (j+self.S[i][0]) % self.p
            self.S[i], self.S[j] = self.S[j], self.S[i]
            t = (self.S[i][0]+self.S[j][0]) % self.p
            k = self.S[t]
            self.seq.append(k)

    # 按PPT进行展示
    def show(self):
        self.setN(3)
        self.generateSeq(b'\x05\x06\x07', 5)
        print(self.seq)


if __name__ == "__main__":
    a = RC4()
    a.show()
