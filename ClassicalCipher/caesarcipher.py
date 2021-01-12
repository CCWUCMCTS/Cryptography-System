'''
文件名: caesarcipher.py
介绍: 
时间: 2021/01/11 15:26:04
作者: CCWUCMCTS
版本: 1.0
'''


class CaesarCipher():

    # 凯撒密码移位加密
    def Encrypt(self, messages, key):
        ret = ''
        for message in messages:
            cur = ord(message)
            if cur >= ord('a') and cur <= ord('z'):
                cur -= ord('a')
                cur = (cur+key) % 26
                cur += ord('a')
            elif cur >= ord('A') and cur <= ord('Z'):
                cur -= ord('A')
                cur = (cur+key) % 26
                cur += ord('A')
            ret += chr(cur)
        return ret

    # 凯撒密码反移位解密
    def Decrypt(self, messages, key):
        ret = ''
        for message in messages:
            cur = ord(message)
            if cur >= ord('a') and cur <= ord('z'):
                cur -= ord('a')
                cur = (cur-key) % 26
                cur += ord('a')
            elif cur >= ord('A') and cur <= ord('Z'):
                cur -= ord('A')
                cur = (cur-key) % 26
                cur += ord('A')
            ret += chr(cur)
        return ret

    # 凯撒密码测试
    def test(self):
        messages = 'Hello, Cryptography!'
        key = 17
        t1 = self.Encrypt(messages, key)
        t2 = self.Decrypt(t1, key)
        print(t1)
        print(t2)

    # 凯撒密码攻击
    def attack(self, messages):
        print('attack:', messages)
        for i in range(26):
            print(self.Decrypt(messages, i), 'key =', i)


if __name__ == "__main__":
    a = CaesarCipher()
    # a.test()
    a.attack('Yvccf, Tipgkfxirgyp!')
