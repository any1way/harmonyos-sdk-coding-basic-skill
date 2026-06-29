---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-encrypt
title: @security/no-unsafe-rsa-encrypt
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-rsa-encrypt
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0563bdb1ed0912c0f0bb52e6b6af8b1f7c70740248185615ee30e4425b63e9b8
---
该规则禁止使用不安全的RSA非对称加密算法，如RSA模数长度小于2048bit、填充模式为PKCS1、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法，推荐使用Petal Aegis SDK中的安全RSA加密和解密接口，详情参见：[RSA加解密](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-rsa-encrypt": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('RSA3072|PKCS1_OAEP|SHA256|MGF1_SHA256');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('RSA512|PKCS1');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
