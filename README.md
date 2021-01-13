# Cryptography-System

> mi码学ke设，构建了一个简易的密码学库，可以进行调用。

## 特性

能够生成PEM格式的RSA密钥，于[这个网站](http://ctf.ssleye.com/)可以解析以测试。

仅适合练习或理解密码使用，加密解密效率极低。

## 程序结构

- Cryptography-System
  - CipherTools.py
  - RSAsignature.py
  - show.py
  - BlockCipher
    - CipherTools.py
    - des.py
    - sm4.py
    - ublockcipher.py
  - ClassicalCipher
    - affinecipher.py
    - caesarcipher.py
    - CipherTools.py
    - multiplicativecipher.py
    - vigenerecipher.py
    - 仿射.cpp
  - Hash
    - CipherTools.py
    - md5.py
  - KeyExchange
    - diffiehellman.py
  - PublickeyCipher
    - 51Nod 1106.py
    - CipherTools.py
    - RSA.py
    - uRSA.py
  - StreamCipher
    - CipherTools.py
    - lfsr.py
    - rc4.py



## 特别说明

我为什么改了名，希望大家ke设自己做，如果做得好是可以当作项目经历的，同时能锻炼自己的能力，复习所学。用这个项目里的程序来对拍，尽量别抄。

**别卷了别卷了。**

> ## 版权说明
> Cryptography-System is an [GPL](https://github.com/CCWUCMCTS/Cryptography-System/blob/main/LICENSE) Free Program.
> **注意：基于本项目源码从事科研、论文、系统开发，请在文中或系统中表明来自于本项目的内容和创意。**
> PS: GPL保证你可以合法忽略以上注意事项但不能保证你不受鄙视，呵呵。