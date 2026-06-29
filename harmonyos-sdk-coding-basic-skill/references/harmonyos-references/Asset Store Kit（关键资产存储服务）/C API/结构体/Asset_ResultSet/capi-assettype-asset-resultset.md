---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-resultset
title: Asset_ResultSet
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_ResultSet
category: harmonyos-references
scraped_at: 2026-06-11T16:07:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6effd1b26fc6428a7d6735f2ec5735c0bba3cb54c97f52d71bfabb6ce88766af
---
```
1. typedef struct {...} Asset_ResultSet
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产查询结果集合，用于定义多条关键资产。

**起始版本：** 11

**相关模块：** [AssetType](../../模块/AssetType/capi-assettype.md)

**所在头文件：** [asset\_type.h](../../头文件/asset_type.h/capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 关键资产的条数。 |
| [Asset\_Result](../Asset_Result/capi-assettype-asset-result.md) \*results | 指向关键资产数组的指针。 |
