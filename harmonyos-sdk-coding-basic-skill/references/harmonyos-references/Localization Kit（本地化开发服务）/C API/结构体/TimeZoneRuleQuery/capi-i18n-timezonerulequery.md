---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery
title: TimeZoneRuleQuery
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > TimeZoneRuleQuery
category: harmonyos-references
scraped_at: 2026-06-01T16:00:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4195747a2b8000123ceaa0611077610bb0f35eec8dcb991087ed631f0ab78913
---
```
1. typedef struct TimeZoneRuleQuery {...} TimeZoneRuleQuery
```

## 概述

PhonePC/2in1TabletTVWearable

用于传入查询的信息，并接收查询的结果。

**起始版本：** 22

**相关模块：** [i18n](../../模块/i18n/capi-i18n.md)

**所在头文件：** [timezone.h](../../头文件/timezone.h/capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| double base | 查询的基准时间。 |
| int32\_t prevRawOffset | 上一次的时区原始偏移量。 |
| int32\_t prevDSTSavings | 上一次的夏令时偏移量。 |
| bool inclusive | 查询结果是否包含基准时间。true：查询结果包含基准时间；false：查询结果不包含基准时间。 |
| double result | 查询结果。 |
