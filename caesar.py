from cipherbase import *
class Caesar(CipherBase):
    def getInfo(self):
        print('This is a Caesar cipher.')
    def Encrypt(self,message,key):
        pass

def main():
    a = Caesar()
    a.getInfo()
if __name__ == "__main__":
    main()
