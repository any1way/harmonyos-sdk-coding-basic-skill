---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-key
title: @security/no-unsafe-rsa-key
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-rsa-key
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c3fa357c506f8bebd1c575bf6fca5b73f9aa4480c66fb952204fc81d7ebdd460
---
该规则禁止使用不安全的RSA密钥，如RSA模数长度小于2048bit。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见：[RSA密钥](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/ohaeggeneratersakeypairbase64-0000001864601898)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-rsa-key": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('RSA3072|PRIMES_2');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('RSA512|PRIMES_2');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
