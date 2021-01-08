import base64
import os
import zipfile
from random import randint
from shutil import copyfile

from RSAsignature import RSASignature
from BlockCipher.ublockcipher import uBlockCipher
from PublickeyCipher.uRSA import usefulRSA
from PublickeyCipher.RSA import RSA
from Hash.md5 import MD5
from CipherTools import i2b
pathA = './test/Alice'  # 发送目录
pathB = './test/Bob'  # 接收目录
filename = 'impotant'  # 发送文件名
sfile = os.path.join(pathA, filename)  # 发送文件路径
rfile = os.path.join(pathB, filename)  # 接收文件路径
szipfile1 = os.path.join(pathA, 'zip1.zip')  # 发送内层zip路径
szipfile2 = os.path.join(pathA, 'zip2.zip')  # 发送外层zip路径
rzipfile1 = os.path.join(pathB, 'zip1.zip')  # 接收内层zip路径
rzipfile2 = os.path.join(pathB, 'zip2.zip')  # 接收外层zip路径
skeyfile = os.path.join(pathA,'sm4.key')
rkeyfile = os.path.join(pathB,'sm4.key')
rang = 4294967296**4-1


def createFile():
    output = b''
    for i in range(1024*1024//16//16):
        output += i2b(randint(0, rang), 16)
    with open(sfile, 'wb') as f:
        f.write(output)
    print('文件创建成功。')


def generateKey():
    global AlicePrivateKey, AlicePublicKey, BobPrivateKey, BobPublicKey, sm4key, IV
    a = RSA()
    a.generateKey(nbits=512)
    AlicePrivateKey = a.outputPrivateKey(pathA)
    AlicePublicKey = a.outputPublicKey(pathB)
    print('Alice私钥生成成功，公钥已传输给Bob。')
    a.generateKey()
    BobPrivateKey = a.outputPrivateKey(pathB)
    BobPublicKey = a.outputPublicKey(pathA)
    print('Bob私钥生成成功，公钥已传输给Alice。')
    sm4key = IV = b''
    for i in range(16):
        sm4key += i2b(randint(0, 255), 1)
        IV += i2b(randint(0, 255), 1)
    print('对称加密密钥与初始向量生成成功。')


def Alice():
    print('Alice正在准备：')
    a = RSASignature(AlicePrivateKey)
    signpath = a.sign(sfile, 'CCWUCMCTS')
    print('RSA签名成功。')
    z = zipfile.ZipFile(szipfile1, 'w')
    z.write(sfile, os.path.basename(sfile))
    z.write(signpath, os.path.basename(signpath))
    z.close()
    print('文件与签名压缩完成。')
    a = uBlockCipher('sm4')
    a.encryptFile(szipfile1, sm4key, IV, mode='cbc',
                  padding='pkcs7', coding='base64')
    print('文件加密完成。')
    b = usefulRSA(keypath=BobPublicKey)
    _key = base64.b64encode(b.byteEncrypt(sm4key))
    _IV = base64.b64encode(b.byteEncrypt(IV))
    with open(skeyfile,'wb') as f:
        f.write(_key + b'\x00' + _IV)
    print('密钥加密完成。')
    z = zipfile.ZipFile(szipfile2, 'w')
    z.write(szipfile1+'.encrypt', os.path.basename(szipfile1+'.encrypt'))
    z.write(skeyfile, os.path.basename(skeyfile))
    z.close()
    print('所有文件打包完成。')
    copyfile(szipfile2,rzipfile2)
    print('文件传输完成。')
    
def Bob():
    print('Bob已收到文件。')
    z=zipfile.ZipFile(rzipfile2,'r')
    z.extractall(pathB)
    z.close()
    print('文件解压成功，得到密钥与文件。')
    with open(rkeyfile,'rb') as f:
        _key,_IV = f.read().split(b'\x00')
    a = usefulRSA(keypath=BobPrivateKey)
    key = a.byteDecrypt(base64.b64decode(_key))
    IV = a.byteDecrypt(base64.b64decode(_IV))
    b = uBlockCipher('sm4')
    b.decryptFile(rzipfile1+'.encrypt',key,IV,mode='cbc',padding='pkcs7',coding='base64')
    print('文件解密成功。')
    z=zipfile.ZipFile(rzipfile1+'.encrypt.decrypt','r')
    z.extractall(pathB)
    z.close()
    print('文件解压成功，得到原始文件和签名。')
    a = RSASignature(AlicePublicKey)
    a.check(rfile+'.sign',rfile)


generateKey()
print()
createFile()
print()
Alice()
print()
Bob()