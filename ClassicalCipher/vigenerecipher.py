from cipherbase import CipherBase


class VigenereCipher(CipherBase):
    def getInfo(self):
        print('This is a vigenere cipher.')

    def Encrypt(self, messages, akey):
        if akey.isalpha() == False:
            print('A wrong key!')
            return 'ERROR'
        ret = ''
        key = []
        length = len(akey)
        for k in akey:
            if ord(k) >= ord('a') and ord(k) <= ord('z'):
                key.append(ord(k)-ord('a'))
            else:
                key.append(ord(k)-ord('A'))
        i = 0
        for message in messages:
            cur = ord(message)
            if cur >= ord('a') and cur <= ord('z'):
                cur -= ord('a')
                cur = (cur+key[i % length]) % 26
                cur += ord('a')
                i += 1
            elif cur >= ord('A') and cur <= ord('Z'):
                cur -= ord('A')
                cur = (cur+key[i % length]) % 26
                cur += ord('A')
                i += 1
            ret += chr(cur)
        return ret

    def Decrypt(self, messages, akey):
        if akey.isalpha() == False:
            print('A wrong key!')
            return 'ERROR'
        ret = ''
        key = []
        length = len(akey)
        for k in akey:
            if ord(k) >= ord('a') and ord(k) <= ord('z'):
                key.append(ord(k)-ord('a'))
            else:
                key.append(ord(k)-ord('A'))
        i = 0
        for message in messages:
            cur = ord(message)
            if cur >= ord('a') and cur <= ord('z'):
                cur -= ord('a')
                cur = (cur-key[i % length]) % 26
                cur += ord('a')
                i += 1
            elif cur >= ord('A') and cur <= ord('Z'):
                cur -= ord('A')
                cur = (cur-key[i % length]) % 26
                cur += ord('A')
                i += 1
            ret += chr(cur)
        return ret


if __name__ == "__main__":
    a = VigenereCipher()
    messages = 'RFMRHNS{Tlsw_Xctc_Tn!!}'
    key = 'playfun'
    print(a.Decrypt(messages, key))
    t1 = a.Encrypt(messages, key)
    t2 = a.Decrypt(t1, key)
    print(t1+'\n'+t2)
