from CipherTools import gcd,inv
class MultiplicativeCipher():
    base = 26

    def getInfo(self):
        print('This is a multiplicative cipher.')

    def changeBase(self, newbase):
        self.base = newbase

    def Encrypt(self, messages, key):
        if key <= 0 or gcd(key, self.base) != 1:
            print('A wrong key!')
            return 'ERROR'
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

    def Decrypt(self, messages, key):
        if key <= 0 or gcd(key, self.base) != 1:
            print('A wrong key!')
            return 'ERROR'
        key = inv(key, self.base)
        return self.Encrypt(messages, key)


if __name__ == "__main__":
    a = MultiplicativeCipher()
    messages = 'This is a message.'
    key = 9
    t1 = a.Encrypt(messages, key)
    t2 = a.Decrypt(t1, key)
    print(t1+'\n'+t2)
