---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi-oh-huks-externalcryptoparamset
title: OH_Huks_ExternalCryptoParamSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_ExternalCryptoParamSet
category: harmonyos-references
scraped_at: 2026-06-11T16:13:11+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:101e7b9d53660f54a87eb3da404e3f73c5cccf59ff690bca1876b33c79aea17b
---
```
1. typedef struct OH_Huks_ExternalCryptoParamSet {...} OH_Huks_ExternalCryptoParamSet
```

## 概述

PC/2in1Tablet

定义外部加密参数集合的结构。

**起始版本：** 22

**相关模块：** [HuksExternalCryptoTypeApi](../../模块/HuksExternalCryptoTypeApi/capi-huksexternalcryptotypeapi.md)

**所在头文件：** [native\_huks\_external\_crypto\_type.h](../../头文件/native_huks_external_crypto_type.h/capi-native-huks-external-crypto-type-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t paramSetSize | 参数集合所占内存大小，单位：Byte。  **起始版本：** 22 |
| uint32\_t paramsCnt | 参数集合中的参数数量。  **起始版本：** 22 |
| [OH\_Huks\_ExternalCryptoParam](../OH_Huks_ExternalCryptoParam/capi-huks-oh-huks-externalcryptoparam.md) params[] | 参数数组，大小由paramSetSize与paramsCnt决定。  **起始版本：** 22 |
