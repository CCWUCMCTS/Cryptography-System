from cipherbase import *
class Caesar(CipherBase):
    def getInfo(self):
        print('This is a Caesar cipher.')
    def Encrypt(self,message,key):
        pass
a = Caesar()
a.getInfo()
