---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-attr
title: Asset_Attr
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Attr
category: harmonyos-references
scraped_at: 2026-06-11T16:07:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:59f4ba268d54c3c2eea9ada1c8bc649f06b31094fcd447e36cd6d9d677703454
---
```
1. typedef struct {...} Asset_Attr
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产属性。

**起始版本：** 11

**相关模块：** [AssetType](../../模块/AssetType/capi-assettype.md)

**所在头文件：** [asset\_type.h](../../头文件/asset_type.h/capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t tag | 关键资产属性名称。 |
| [Asset\_Value](../Asset_Value/capi-assettype-asset-value.md) value | 关键资产属性内容。 |
