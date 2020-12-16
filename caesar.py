from cipherbase import *
class Caesar(CipherBase):
    def getInfo(self):
        print('This is a Caesar cipher.')
    def Encrypt(self,messages,key):
        ret=''
        for message in messages:
            cur=ord(message)
            if cur>=ord('a') and cur<=ord('z'):
                cur-=ord('a')
                cur=(cur+key)%26
                cur+=ord('a')
            elif cur>=ord('A') and cur<=ord('Z'):
                cur-=ord('A')
                cur=(cur+key)%26
                cur+=ord('A')
            ret+=chr(cur)
        return ret
    def Decrypt(self,messages,key):
        ret=''
        for message in messages:
            cur=ord(message)
            if cur>=ord('a') and cur<=ord('z'):
                cur-=ord('a')
                cur=(cur-key)%26
                cur+=ord('a')
            elif cur>=ord('A') and cur<=ord('Z'):
                cur-=ord('A')
                cur=(cur-key)%26
                cur+=ord('A')
            ret+=chr(cur)
        return ret

def main():
    a = Caesar()
    a.getInfo()
    messages='This is a message.'
    key=17
    t1=a.Encrypt(messages,key)
    t2=a.Decrypt(t1,key)
    print(t1)
    print(t2)
if __name__ == "__main__":
    main()