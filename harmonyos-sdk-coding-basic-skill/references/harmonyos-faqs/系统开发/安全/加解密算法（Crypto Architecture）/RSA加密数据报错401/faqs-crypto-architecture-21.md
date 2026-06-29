---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-21
title: RSA加密数据报错401
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > RSA加密数据报错401
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0625e5689a64e363e057f2b15a3104c731cf610180fc7df25d0f5fe22aa38995
---
生成RSA密钥长度与生成密钥时传入参数有关，例如生成2048位RSA密钥参数可以传'RSA2048|PRIMES\_2'或者'RSA2048|PRIMES\_3'。

**参考链接**

[RSA](<../../../../../harmonyos-guides/系统/安全/Crypto Architecture Kit（加解密算法框架服务）/加解密/加解密算法规格/非对称密钥加解密算法规格/crypto-asym-encrypt-decrypt-spec.md#rsa>)
