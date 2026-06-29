---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyinfo
title: OH_Huks_KeyInfo
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:13:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c1d6bd3235e785a70885a85663c8208ccb213c596cd68f7369e1e2591525f362
---
```
1. struct OH_Huks_KeyInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义密钥信息的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](../../模块/HuksTypeApi/capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](../../头文件/native_huks_type.h/capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [OH\_Huks\_Blob](../OH_Huks_Blob/capi-hukstypeapi-oh-huks-blob.md) alias | 密钥的别名。 |
| struct [OH\_Huks\_ParamSet](../OH_Huks_ParamSet/capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向密钥参数集的指针。 |
