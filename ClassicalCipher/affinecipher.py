'''
文件名: affinecipher.py
介绍: 
时间: 2021/01/11 16:20:32
作者: CCWUCMCTS
版本: 1.0
'''


if __name__ == "__main__":
    from caesarcipher import CaesarCipher
    from multiplicativecipher import MultiplicativeCipher
else:
    from .caesarcipher import CaesarCipher
    from .multiplicativecipher import MultiplicativeCipher


class AffineCipher():
    c = CaesarCipher()
    m = MultiplicativeCipher()

    # 仿射密码加密
    def Encrypt(self, messages, key1, key2):
        return self.c.Encrypt(self.m.Encrypt(messages, key1), key2)

    # 仿射密码解密
    def Decrypt(self, messages, key1, key2):
        return self.m.Decrypt(self.c.Decrypt(messages, key2), key1)

    # 仿射密码测试
    def test(self):
        messages = 'Hello, Cryptography!'
        key1 = 25
        key2 = 17
        t1 = a.Encrypt(messages, key1, key2)
        t2 = a.Decrypt(t1, key1, key2)
        print(t1+'\n'+t2)

    # 仿射密码攻击
    def attack(self, messages):
        print('attack:', messages)
        for i in range(26):
            for j in range(26):
                try:
                    print(self.Decrypt(messages, i, j),
                          'key1 =', i, 'key2 =', j)
                except:
                    pass


if __name__ == "__main__":
    a = AffineCipher()
    a.test()
    a.attack('Knggd, Patcydlarckt!')
