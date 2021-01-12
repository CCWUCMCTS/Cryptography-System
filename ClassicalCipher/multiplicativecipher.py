'''
文件名: multiplicativecipher.py
介绍: 
时间: 2021/01/11 16:14:09
作者: CCWUCMCTS
版本: 1.0
'''


from CipherTools import gcd, inv


class MultiplicativeCipher():
    base = 26

    # 修改模数
    def changeBase(self, newbase):
        self.base = newbase

    # 乘法密码加密
    def Encrypt(self, messages, key):
        if key <= 0 or gcd(key, self.base) != 1:
            raise('A wrong key!')
        ret = ''
        for message in messages:
            cur = ord(message)
            if cur >= ord('a') and cur <= ord('z'):
                cur -= ord('a')
                cur = cur*key % self.base
                cur += ord('a')
            elif cur >= ord('A') and cur <= ord('Z'):
                cur -= ord('A')
                cur = cur*key % self.base
                cur += ord('A')
            ret += chr(cur)
        return ret

    # 乘法密码解密
    def Decrypt(self, messages, key):
        if key <= 0 or gcd(key, self.base) != 1:
            raise('A wrong key!')
        key = inv(key, self.base)
        return self.Encrypt(messages, key)

    # 乘法密码测试
    def test(self):
        messages = 'Hello, Cryptography!'
        key = 9
        t1 = self.Encrypt(messages, key)
        t2 = self.Decrypt(t1, key)
        print(t1+'\n'+t2)

    # 乘法密码攻击
    def attack(self, messages):
        print('attack:', messages)
        for i in range(1, self.base):
            try:
                s = self.Decrypt(messages, i)
                print(s, 'key =', i)
            except:
                pass


if __name__ == "__main__":
    a = MultiplicativeCipher()
    # a.test()
    a.attack('Lkvvw, Sxifpwcxafli!')
