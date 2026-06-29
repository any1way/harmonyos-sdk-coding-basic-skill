---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-credentialdetaillist
title: OH_CM_CredentialDetailList
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > C API > 结构体 > OH_CM_CredentialDetailList
category: harmonyos-references
scraped_at: 2026-06-11T16:12:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:abcf5ccd5937355286acd5511e84822300f2c227303ed2c1da7e6c637aaede0f
---
```
1. typedef struct {...} OH_CM_CredentialDetailList
```

## 概述

PhonePC/2in1TabletTVWearable

定义证书凭据详情列表的结构体类型。

**起始版本：** 22

**相关模块：** [CertManagerType](../../模块/CertManagerType/capi-certmanagertype.md)

**所在头文件：** [cm\_native\_type.h](../../头文件/cm_native_type.h/capi-cm-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t credentialCount | 表示证书凭据详情的个数。 |
| [OH\_CM\_Credential](../OH_CM_Credential/capi-certmanagertype-oh-cm-credential.md) \*credential | 表示证书凭据详情列表。 |
