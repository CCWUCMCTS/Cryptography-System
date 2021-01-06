from PublickeyCipher.uRSA import usefulRSA
from Hash.md5 import MD5
import base64
class RSASignature():
    def __init__(self,path):
        self.a = usefulRSA(keypath=path)
        self.mode=self.a.mode
    def sign(self,path,data):
        if self.mode == 'public':
            raise('公钥无法签名！')
        m5 = MD5()
        md5 = m5.fileHash(path)
        data = md5.encode('utf-8') + b'\x00' + data.encode('utf-8')
        s = self.a.byteDecrypt(data)
        s = base64.b64encode(s)
        with open(path+'.sign','wb') as f:
            f.write(s)
    def check(self,signpath,filepath,data0=None):
        with open(signpath,'rb') as f:
            data = f.read()
        s = self.a.byteEncrypt(base64.b64decode(data)).decode('utf-8')
        m5 = MD5()
        md5 = m5.fileHash(filepath)
        s=s.split('\x00')
        data1 = s[1]
        print('消息:',data1)
        recv = s[0]
        print(recv,md5)
        if recv == md5 and (data0 == None or data0 == data1):
            print('验证成功！')
            return True
        else:
            print('验证失败！')
            return False
if __name__ == "__main__":
    a = RSASignature('C:\\Users\\wwwwww931121\\Desktop\\private.txt')
    a.sign('C:\\Users\\wwwwww931121\\Desktop\\网络安全A.rar','from CCWUCMCTS')
    a.check('C:\\Users\\wwwwww931121\\Desktop\\网络安全A.rar.sign','C:\\Users\\wwwwww931121\\Desktop\\网络安全A.rar','from CCWUCMCTS')