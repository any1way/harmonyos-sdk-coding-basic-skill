---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyaliasset
title: OH_Huks_KeyAliasSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyAliasSet
category: harmonyos-references
scraped_at: 2026-06-11T16:13:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ed912208f060932e32d846743da6257e22ca12f143bc7c5944108704efa21a82
---
```
1. struct OH_Huks_KeyAliasSet {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义密钥别名集的结构体类型。

**起始版本：** 20

**相关模块：** [HuksTypeApi](../../模块/HuksTypeApi/capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](../../头文件/native_huks_type.h/capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t aliasesCnt | 密钥别名集个数。 |
| struct [OH\_Huks\_Blob](../OH_Huks_Blob/capi-hukstypeapi-oh-huks-blob.md) \*aliases | 指向密钥别名集数据的指针。 |
