class CipherBase:
    def getInfo(self):
        print('This is a base class for cipher.')

    def Encrypt(self):
        pass

    def Decrypt(self):
        pass


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = exgcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def inv(a, b):
    x, _, z = exgcd(a, b)
    if z != 1:
        return -1
    return x % b


if __name__ == "__main__":
    a = CipherBase()
    print(exgcd(5, 26))
