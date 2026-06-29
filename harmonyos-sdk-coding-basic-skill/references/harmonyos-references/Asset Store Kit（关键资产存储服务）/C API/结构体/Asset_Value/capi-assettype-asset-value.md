---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-value
title: Asset_Value
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Value
category: harmonyos-references
scraped_at: 2026-06-11T16:07:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:446534bcb5f36f5b10233aada169402bc0063d8e2f52b3ede6aff0354f715362
---
```
1. typedef union {...} Asset_Value
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产属性内容。

**起始版本：** 11

**相关模块：** [AssetType](../../模块/AssetType/capi-assettype.md)

**所在头文件：** [asset\_type.h](../../头文件/asset_type.h/capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool boolean | 该字段用于传入bool类型的关键资产。 |
| uint32\_t u32 | 该字段用于传入uint32类型的关键资产。 |
| [Asset\_Blob](../Asset_Blob/capi-assettype-asset-blob.md) blob | 该字段用于传入bytes类型的关键资产。 |
