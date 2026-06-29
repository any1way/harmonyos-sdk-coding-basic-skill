---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-pubkeyinfo
title: OH_Huks_PubKeyInfo
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_PubKeyInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:13:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1b309cf079f6bcc63727f2fa1c9f9be5a2f3423ef097b608ff0bd48645c3f2ea
---
```
1. struct OH_Huks_PubKeyInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义公钥信息的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](../../模块/HuksTypeApi/capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](../../头文件/native_huks_type.h/capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](../../头文件/native_huks_type.h/capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 公钥的算法类型。 |
| uint32\_t keySize | 公钥的长度。 |
| uint32\_t nOrXSize | n或X值的长度。 |
| uint32\_t eOrYSize | e或Y值的长度。 |
| uint32\_t placeHolder | 占位符大小。 |
