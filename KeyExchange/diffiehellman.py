from Crypto.Util import number
from Crypto.Random import random
from time import sleep
import time
class DiffieHellman:
    '''
        (25,64,100000)可以在100次运行中取得较高的准确率和成功率
    '''
    MAXROUND = 25 # 生成素数及原根的最大轮数
    GENBIT = 64 # 生成素数的二进制位数
    FAILEDFACTOR = 100000 # p-1有大于此的因子即失败，限制时间

    def getPrimitiveRoot(self,p):
        '''
            输入一个质数p，返回它的最小原根。
            源自OpenJudge-51Nod-1135原根，效率最高的python代码。
            出于时间考虑，FAILEDFACTOR限制了p-1的最大因子，导致生成的质数很弱，同时素数P也不能太大，最好小于等于64。
        '''
        q = p - 1
        i = 2
        h = []
        while i * i <= q:
            if q % i == 0:
                h.append(i)
                while q % i == 0:
                    q //= i
            i += 1
            if(i%self.FAILEDFACTOR==0):
                return 0
        if q != 1:
            h.append(q)
        i = 2
        while 1:
            for j in h:
                if pow(i, (p - 1) // j, p) == 1:
                    break
            else:
                return i
            i += 1

    def generatePG(self):
        '''
            采用素数库生成一个GENBIT位的素数，尝试寻找原根。
            最大生成MAXROUND次，超过即失败。
        '''
        i = 0
        print('Start to generate P and G...')
        while(i<self.MAXROUND):
            print('Round:',i)
            p=number.getPrime(self.GENBIT)
            rt=self.getPrimitiveRoot(p)
            if rt:
                print('Success!',p,rt)
                self.P = p
                self.G = rt
                return True
            else:
                print('Time out!',p)
                i+=1
        print('Failed...')
        return False

    def generateRandomA(self):
        '''
            Alice生成私有的随机数A，并把Ya=g^A (mod P)发送给B。
        '''
        self.A = random.randint(1,self.P-1)
        self.Ya = pow(self.G,self.A,self.P)
        print('Alice\tgenerate:','A =',self.A,'\tsend:','Ya =',self.Ya)

    def generateRandomB(self):
        '''
            Bob生成私有的随机数B，并把Yb=g^B (mod P)发送给A。
        '''
        self.B = random.randint(1,self.P-1)
        self.Yb = pow(self.G,self.B,self.P)
        print('Bob\tgenerate:','B =',self.B,'\tsend:','Yb =',self.Yb)

    def calculateKa(self):
        '''
            Alice接收到Yb，计算Ka=Yb^A (mod P)。
            等价于计算(g^B)^A (mod P)。
        '''
        print('Alice geted Yb.')
        self.Ka = pow(self.Yb,self.A,self.P)
        print('Ka =',self.Ka)

    def calculateKb(self):
        '''
            Bob接收到Ya，计算Kb=Ya^B (mod P)。
            等价于计算(g^A)^B (mod P)。
        '''
        print('Bob geted Ya.')
        self.Kb = pow(self.Ya,self.B,self.P)
        print('Kb =',self.Kb)

    def verifyKey(self):
        '''
            验证(g^B)^A equal (g^A)^B (mod P)。
        '''
        if self.Ka == self.Kb:
            print('Verification successful!')
        else:
            print('Verification failed...')

    def exchangeKey(self):
        '''
            模拟整个密钥交换过程，返回运行状态与计算时间
        '''
        time_start=time.time()
        runstate = self.generatePG()
        if runstate == False:
            print('Run failed...')
            time_end=time.time()
            print('Totally cost:',time_end-time_start)
            return False, time_end-time_start
        #sleep(1.5)
        self.generateRandomA()
        #sleep(1.5)
        self.generateRandomB()
        #sleep(1.5)
        self.calculateKa()
        #sleep(1.5)
        self.calculateKb()
        #sleep(1.5)
        self.verifyKey()
        time_end=time.time()
        print('Totally cost:',time_end-time_start)
        return True, time_end-time_start

# 1轮交换测试：
d = DiffieHellman()
d.exchangeKey()
# 100轮交换测试
print('100 rounds test:')
cnt = 0
totTime = 0
def print(*args):
    '''
        覆盖print函数屏蔽输出
    '''
    pass
for i in range(100):
    d = DiffieHellman()
    x,y = d.exchangeKey()
    if x:
        cnt += 1
    totTime += y
del print
print('Success:',cnt)
print('Totally cost:',totTime)