'''
文件名: RSAsignature.py
介绍: 
时间: 2021/01/13 13:33:54
作者: CCWUCMCTS
版本: 1.0
'''


from PublickeyCipher.uRSA import usefulRSA
from Hash.md5 import MD5
import base64


class RSASignature():

    # 密钥和模式导入
    def __init__(self, path):
        self.a = usefulRSA(keypath=path)
        self.mode = self.a.mode

    # 文件签名
    def sign(self, path, data='签名作者：CCWUCMCTS'):
        if self.mode == 'public':
            raise('公钥无法签名！')
        m5 = MD5()
        md5 = m5.fileHash(path, output=False)
        data = md5.encode('utf-8') + b'\x00' + data.encode('utf-8')
        s = self.a.byteDecrypt(data)
        s = base64.b64encode(s)
        with open(path+'.sign', 'wb') as f:
            f.write(s)
        return path+'.sign'

    # 签名检验
    def check(self, signpath, filepath, data0=None):
        with open(signpath, 'rb') as f:
            data = f.read()
        s = self.a.byteEncrypt(base64.b64decode(data)).decode('utf-8')
        m5 = MD5()
        md5 = m5.fileHash(filepath, output=False)
        s = s.split('\x00')
        data1 = s[1]
        print('消息:', data1)
        recv = s[0]
        print(recv, md5)
        if recv == md5 and (data0 == None or data0 == data1):
            print('验证成功！')
            return True
        else:
            print('验证失败！')
            return False

    # 效果展示
    def show(self):
        self.sign('RSAsignature_sample', 'from CCWUCMCTS')
        self.check('RSAsignature_sample.sign', 'RSAsignature_sample')  # 不检验消息
        self.check('RSAsignature_sample.sign', 'RSAsignature_sample',
                   'from CCWUCMCTS')  # 检验消息，消息正确
        self.check('RSAsignature_sample.sign', 'RSAsignature_sample',
                   'wrong signature')  # 检验消息，消息错误


if __name__ == "__main__":
    a = RSASignature('PublickeyCipher\\private.txt')
    a.show()
