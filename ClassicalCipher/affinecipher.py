from cipherbase import CipherBase
from caesarcipher import CaesarCipher
from multiplicativecipher import MultiplicativeCipher
class AffineCipher(CipherBase):
    c=CaesarCipher()
    m=MultiplicativeCipher()
    def getInfo(self):
        print('This is a affine cipher.')
    def Encrypt(self,messages,key1,key2):
        return self.c.Encrypt(self.m.Encrypt(messages,key1),key2)
    def Decrypt(self,messages,key1,key2):
        return self.m.Decrypt(self.c.Decrypt(messages,key2),key1)

if __name__ == "__main__":
    a=AffineCipher()
    messages='This is a message.'
    key1=25;key2=17
    t1=a.Encrypt(messages,key1,key2)
    t2=a.Decrypt(t1,key1,key2)
    print(t1+'\n'+t2)