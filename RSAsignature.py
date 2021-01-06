from BlockCipher.ublockcipher import uBlockCipher
a=uBlockCipher('sm4')
s = b'zzzzzzzzzzzzzzzz'
    # 可以拆成filepath，filename
a.encryptFile('C:\\Users\\wwwwww931121\\Desktop\\123.txt', s,s, mode='cfb', padding='pkcs7', coding='base64')
a.decryptFile('C:\\Users\\wwwwww931121\\Desktop\\123.txt.encrypt',s, s, mode='cfb', padding='pkcs7', coding='base64')
#from PublickeyCipher.RSA import RSA
#from PublickeyCipher.cipherbase import CipherBase
'''
class RSASignature():
    def __init__(self,mode='private'):
        self.a = RSA()
        if mode.lower() != 'private' and mode.lower()!='public':
            raise('签名模式错误。')
        self.mode=mode
        '''