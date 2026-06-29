---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterial25519
title: OH_Huks_KeyMaterial25519
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterial25519
category: harmonyos-references
scraped_at: 2026-06-11T16:13:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:31b35c3a506f0a729ccf53d64a59db6d5c62ac914e2403af34f70fa3fb8942f0
---
```
1. struct OH_Huks_KeyMaterial25519 {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义25519类型密钥的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](../../模块/HuksTypeApi/capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](../../头文件/native_huks_type.h/capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](../../头文件/native_huks_type.h/capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 密钥的算法类型。 |
| uint32\_t keySize | 25519类型密钥的长度。 |
| uint32\_t pubKeySize | 公钥的长度。 |
| uint32\_t priKeySize | 私钥的长度。 |
| uint32\_t reserved | 预留字段。建议开发者赋值为0。 |
