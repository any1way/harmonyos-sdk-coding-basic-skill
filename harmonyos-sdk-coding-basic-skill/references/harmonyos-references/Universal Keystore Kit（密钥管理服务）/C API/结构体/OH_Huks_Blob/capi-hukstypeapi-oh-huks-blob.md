---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob
title: OH_Huks_Blob
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Blob
category: harmonyos-references
scraped_at: 2026-06-11T16:13:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2a24f6b4e482716906cb52ae73f707424c0ec5ea83a35862a974cbf7e32deb09
---
```
1. struct OH_Huks_Blob {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义存放数据的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](../../模块/HuksTypeApi/capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](../../头文件/native_huks_type.h/capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 数据大小。 |
| uint8\_t \*data | 指向数据内存的指针。 |
