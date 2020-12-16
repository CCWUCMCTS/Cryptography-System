class CipherBase:
    def getInfo(self):
        print('This is a base class for cipher.')
    def Encrypt(self):
        pass
    def Decrypt(self):
        pass
    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b,a%b)
    def exgcd(self,a,b):     
        if b == 0:         
            return 1, 0, a     
        else:         
            x, y, q = self.exgcd(b, a % b)        
            x, y = y, (x - (a // b) * y)         
            return x, y, q
def main():
    a=CipherBase()
    print(a.exgcd(5,26))
if __name__ == "__main__":
    main()