'''
文件名: NTLM-Hash.py
介绍: 
时间: 2021/01/29 19:52:43
作者: CCWUCMCTS
版本: 1.0
'''


from BlockCipher.des import DES
from CipherTools import b2i,i2b
from Hash.md5 import MD5
import hashlib

def Zero_padding(str):
    b = []
    l = len(str)
    for i in range(0,l,7):
        b.append(str[i:i + 7] + '0')
    return ''.join(b)

magic = b'KGS!@#$%'
def lm_hash(passwd):
    # 用户的密码转换为大写,并转换为16进制字符串
    passwd = passwd.upper().encode('utf-8')
    pswd = ''
    for i in passwd:
        pswd += hex(i)[2:].rjust(2, '0')
    passwd = pswd
    str_len = len(passwd)

    # 密码不足14字节将会用0来补全
    if str_len < 28:
        passwd = passwd.ljust(28, '0')

    # 固定长度的密码被分成两个7byte部分
    t_1 = passwd[0:14]
    t_2 = passwd[14:]

    # 每部分转换成比特流，并且长度位56bit，长度不足使用0在左边补齐长度
    t_1 = bin(int(t_1, 16)).lstrip('0b').rjust(56, '0')
    t_2 = bin(int(t_2, 16)).lstrip('0b').rjust(56, '0')

    # 再分7bit为一组末尾加0，组成新的编码
    t_1 = Zero_padding(t_1)
    t_2 = Zero_padding(t_2)
    t_1 = hex(int(t_1, 2))
    t_2 = hex(int(t_2, 2))
    t_1 = t_1[2:].rjust(16,'0')
    t_2 = t_2[2:].rjust(16,'0')
    t_1 = i2b(int(t_1,16),8)
    t_2 = i2b(int(t_2,16),8)
    

    a = DES()
    a.generateKey(t_1)
    LM_1 = a.aBlockEncode(magic)
    a.generateKey(t_2)
    LM_2 = a.aBlockEncode(magic)
    LM = hex(b2i(LM_1+LM_2))[2:].rjust(32,'0').upper()
    return LM

dic = []
for i in range(32,97):
    dic.append(chr(i))
for i in range(123,127):
    dic.append(chr(i))
s='1999FLAG1'
'''
for i in dic:
    print(i)
    for j in dic:
            sr = s+i+j+'7er'
            if lm_hash(sr)[27:] == "DEE73":
                print(i,j,sr)
'''
passwd = '1999flag1227er'
sta = [4,5,6,7,12,13]
for i in range(2**6):
    cur = list(passwd)
    for j in range(6):
        if i & (1 << j) == 1:
            cur[sta[j]]=cur[sta[j]].upper()
        else:
            cur[sta[j]]=cur[sta[j]].lower()
    upass = ''.join(cur).encode('utf-16')[2:]
    curs = hashlib.new('md4',upass).hexdigest()
    if curs[0:4] == 'f54a':
        print(curs)
        print(''.join(cur))
    

m = MD5()
print('CUMTCTF{'+m.hash(passwd.encode('utf-8')).lower()+'}')
