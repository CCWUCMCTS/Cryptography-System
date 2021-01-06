
import random

class LSFR():
    def getInfo(self):
        '''
            打印LSFR的信息。
        '''
        print('这是一个线性反馈移位寄存器。')

    def showPolynomial(self):
        '''
            打印对象当前的多项式。
        '''
        print('当前的多项式为：1', end='')
        for i in self.pol:
            print('+x^'+str(i), end='')
        print('')

    def setPolynomial(self, s, n=None):
        '''
            设置对象的多项式。
            s: 表示系数为1的项的次数列表，有没有0均不影响。
            n: 表示LSFR的级数，当最高次项次数为n时不需要。
            self.pol: 存储了系数为1的项的次数列表，不包含0次。
        '''
        self.pol = sorted(s)
        if n == None:
            self.n = self.pol[-1]
        else:
            self.n = n
        if self.pol[0] == 0:
            self.pol = self.pol[1:]
        self.showPolynomial()

    def inputPolynomial(self, n=None):
        '''
            提示输入一个多项式，并加载到对象中。
            需要在一行中输入多项式系数为1的项的次数，以空格隔开。
            n: 表示LSFR的级数，当最高次项次数为n时不需要。
        '''
        while True:
            print('请输入多项式系数为1的项的次数，用空格隔开：')
            inputs = input()
            try:
                inputs = [int(i) for i in inputs.split(' ')]
            except:
                print('错误')
                continue
            self.setPolynomial(inputs, n)
            break

    def randomInitSeq(self):
        '''
            随机LSFR中n个寄存器的初始值。
            self.initseq: n个寄存器的初始值。
        '''
        try:
            self.pol
        except:
            print('请先设置多项式。')
        self.initseq = [random.randint(0, 1) for _ in range(self.n)]

    def setInitSeq(self, f):
        '''
            设定LSFR中n个寄存器的初始值。
            self.initseq: n个寄存器的初始值。
        '''
        try:
            self.pol
        except:
            print('请先设置多项式。')
        self.initseq = f

    def generateSeq(self, end=-1):
        '''
            生成序列至指定的长度，若当前多项式为本源多项式，则生成的是m序列。
            end: 序列将被生成至end长度，在不启用周期检测时，默认生成至最大可能周期。
            若删去下面的注释，则启用状态检测，检测到一个周期完成时退出，但速度极慢，慎用。
            self.seq: 生成的序列。
        '''
        if end == -1:
            end = 2**self.n-1
        try:
            self.seq
        except:
            self.seq = self.initseq
        # status = []
        for i in range(len(self.seq), end):
            t = 0
            '''
            # 与上面的status一起记录状态，保证只有一个循环节，输入为本原多项式时不需要
            cur = self.seq[i-self.n:i]
            if cur in status:
                #return len(self.seq)
            status.append(cur)
            '''
            for j in self.pol:
                t ^= self.seq[i-j]
            self.seq.append(t)
        return len(self.seq)

    def countSeqm(self):
        '''
            对当前已经生成的序列中，长度为1-n的0、1游程进行统计，输出游程统计字典。
            self.mdict: 游程统计字典，键为长度，值为元组，两个位置分别为该长度的0游程个数、1游程个数。
        '''
        num = [[], []]
        sta = 1
        while(sta < len(self.seq) and self.seq[sta-1] == self.seq[sta]):
            sta += 1
        cur = self.seq[sta]
        cnt = 1
        i = (sta+1) % len(self.seq)
        while(i != sta):
            if self.seq[i-1] == self.seq[i]:
                cnt += 1
            else:
                num[cur].append(cnt)
                cur = self.seq[i]
                cnt = 1
            i = (i+1) % len(self.seq)
        num[cur].append(cnt)
        num[0].sort()
        num[1].sort()
        self.mdict = {}
        for i in range(self.n):
            self.mdict[i+1] = (num[0].count(i+1), num[1].count(i+1))
        # print(self.mdict)

    def show(self):
        '''
            效果展示函数。
        '''
        a = LSFR()
        a.inputPolynomial()
        a.randomInitSeq()
        # a.setInitSeq([1,0,0,1,1])
        t = a.generateSeq()
        # print(''.join([str(i) for i in a.seq]))
        print('生成序列长度为：'+str(t))
        a.countSeqm()
        print('游程字典为：\n'+str(a.mdict))


if __name__ == "__main__":
    b = LSFR()
    b.show()
