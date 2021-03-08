# Cryptography-System

> mi码学ke设，构建了一个简易的密码学库，可以进行调用。

## 特性

能够生成PEM格式的RSA密钥，[这个网站](http://ctf.ssleye.com/)可以解析。

仅适合练习或理解密码使用，加密解密效率极低，如因错误的商业使用造成损失概不负责。

## 程序结构

- Cryptography-System
  - CipherTools.py
  - RSAsignature.py
  - show.py
  - NTLM-Hash.py
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

在github上很容易就搜到16、17级两位学长的项目，他们的程序在我对拍时起到了极大的作用，在此表示感谢。

而我在上传项目时，特意改了名，我不希望我的项目被拿去随便运行一下，就交上去水成绩。学弟学妹们，如果你们找到了这个项目，我希望你们可以认真做一下这个ke设，仅把此项目作为对拍程序，培养设计程序、将程序抽象的能力。把现成的项目拿去改，是很难有这种能力的。

从零开始设计编写这个课设项目，对你们的考研、保研、工作都有极大的帮助。

如果执意要直接使用本项目作为你的ke设，**请遵循避免过度内卷的原则，不传播或大范围传播**，并尊重著作权。

以下说明源自某OJ，我曾经见到有人把这个OJ改得面目全非，仅在html里才找到没删干净的只言片语。把这段话放在这里，提醒我们每个人都有责任建设这个尊重、包容、开放的开源环境。

> ## 版权说明
> Cryptography-System is an [GPL](https://github.com/CCWUCMCTS/Cryptography-System/blob/main/LICENSE) Free Program.
> 
> **注意：基于本项目源码从事科研、论文、系统开发，请在文中或系统中表明来自于本项目的内容和创意。**
> 
> PS: GPL保证你可以合法忽略以上注意事项但不能保证你不受鄙视，呵呵。
