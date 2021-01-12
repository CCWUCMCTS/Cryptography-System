'''
文件名: vigenerecipher.py
介绍: 
时间: 2021/01/12 17:44:17
作者: CCWUCMCTS
版本: 1.0
'''


class VigenereCipher():

    # 维吉尼亚密码加密
    def Encrypt(self, messages, akey):
        if akey.isalpha() == False:
            raise('A wrong key!')
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

    # 维吉尼亚密码解密
    def Decrypt(self, messages, akey):
        if akey.isalpha() == False:
            raise('A wrong key!')
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

    # 维吉尼亚密码测试
    def test(self):
        messages = 'RFMRHNS{Tlsw_Xctc_Tn!!}'
        key = 'playfun'
        print(a.Decrypt(messages, key))
        messages = 'Hello, Cryptography!'
        key = 'ohhhhh'
        t1 = a.Encrypt(messages, key)
        t2 = a.Decrypt(t1, key)
        print(t1+'\n'+t2)


if __name__ == "__main__":
    a = VigenereCipher()
    a.test()
