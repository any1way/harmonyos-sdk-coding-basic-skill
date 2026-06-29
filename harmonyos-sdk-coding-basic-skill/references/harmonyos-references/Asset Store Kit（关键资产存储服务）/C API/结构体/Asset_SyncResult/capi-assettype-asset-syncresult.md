---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-syncresult
title: Asset_SyncResult
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_SyncResult
category: harmonyos-references
scraped_at: 2026-06-11T16:07:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:79eb492da14249d102884d45c378510082cf7d7b4fd856d68b372736e9db886d
---
```
1. typedef struct {...} Asset_SyncResult
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产同步结果。

**起始版本：** 20

**相关模块：** [AssetType](../../模块/AssetType/capi-assettype.md)

**所在头文件：** [asset\_type.h](../../头文件/asset_type.h/capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t resultCode | 关键资产同步的结果码。 |
| uint32\_t totalCount | 触发同步的关键资产总数。 |
| uint32\_t failedCount | 关键资产同步失败的数量。 |
