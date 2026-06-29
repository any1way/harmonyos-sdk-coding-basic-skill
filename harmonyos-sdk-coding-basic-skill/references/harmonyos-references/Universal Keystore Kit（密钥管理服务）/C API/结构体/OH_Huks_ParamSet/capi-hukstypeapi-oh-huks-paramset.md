---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-paramset
title: OH_Huks_ParamSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_ParamSet
category: harmonyos-references
scraped_at: 2026-06-11T16:13:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dfcbf138bcc96e273ba8019f13f61f42ddd1a1c19ade204754219baea51a82f8
---
```
1. struct OH_Huks_ParamSet {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义参数集的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](../../模块/HuksTypeApi/capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](../../头文件/native_huks_type.h/capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t paramSetSize | 参数集的内存大小。 |
| uint32\_t paramsCnt | 参数的个数。 |
| struct [OH\_Huks\_Param](../OH_Huks_Param/capi-hukstypeapi-oh-huks-param.md) params[] | 参数数组。 |
