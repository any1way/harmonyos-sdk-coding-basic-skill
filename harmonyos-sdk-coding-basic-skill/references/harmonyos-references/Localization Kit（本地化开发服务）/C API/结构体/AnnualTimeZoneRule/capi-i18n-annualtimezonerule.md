---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule
title: AnnualTimeZoneRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > AnnualTimeZoneRule
category: harmonyos-references
scraped_at: 2026-06-01T16:00:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9e8eea38765dc1b76ae8c28f6cecaa37c328137768a8db6e10ae166e8d450bed
---
```
1. typedef struct AnnualTimeZoneRule {...} AnnualTimeZoneRule
```

## 概述

PhonePC/2in1TabletTVWearable

每年生效的时区规则。

**起始版本：** 22

**相关模块：** [i18n](../../模块/i18n/capi-i18n.md)

**所在头文件：** [timezone.h](../../头文件/timezone.h/capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* name | 时区规则的名称。 |
| int32\_t startYear | 时区规则生效的起始年份。 |
| int32\_t endYear | 时区规则生效的终止年份。 |
| int32\_t rawOffset | 时区的原始偏移量。 |
| int32\_t dstSavings | 夏令时的偏移量。 |
| [DateTimeRule](../DateTimeRule/capi-i18n-datetimerule.md) dateTimeRule | 时间日期规则。 |
