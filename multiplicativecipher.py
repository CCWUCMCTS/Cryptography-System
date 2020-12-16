from cipherbase import *
class MultiplicativeCipher(CipherBase):
    self.base = 26
    def getInfo(self):
        print('This is a multiplicative cipher.')
    def changeBase(newbase):
        self.base = newbase
    def Encrypt(self,messages,key):
        pass
    def Decrypt(self,messages,key):
        pass
def main():
    a = MultiplicativeCipher()
    a.getInfo()
    messages='This is a message.'
    key=17
    t1=a.Encrypt(messages,key)
    t2=a.Decrypt(t1,key)
    print(t1)
    print(t2)
if __name__ == "__main__":
    main()