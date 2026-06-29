---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules
title: TimeZoneRules
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > TimeZoneRules
category: harmonyos-references
scraped_at: 2026-06-01T16:00:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f8af7ea8d31a9acc2c0ee60c112111e6ee89af2b8c99e6ef2572ebbad2addbe1
---
```
1. typedef struct TimeZoneRules {...} TimeZoneRules
```

## 概述

PhonePC/2in1TabletTVWearable

完整的时区规则。

**起始版本：** 22

**相关模块：** [i18n](../../模块/i18n/capi-i18n.md)

**所在头文件：** [timezone.h](../../头文件/timezone.h/capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InitialTimeZoneRule](../InitialTimeZoneRule/capi-i18n-initialtimezonerule.md) initial | 起始时区规则。 |
| [TimeArrayTimeZoneRule\*](../TimeArrayTimeZoneRule/capi-i18n-timearraytimezonerule.md) timeArrayRules | 起始时间戳数组定义的时区规则数组。 |
| [AnnualTimeZoneRule\*](../AnnualTimeZoneRule/capi-i18n-annualtimezonerule.md) annualRules | 每年生效的时区规则数组。 |
| size\_t numTimeArrayRules | 起始时间戳数组定义的时区规则数组的大小。 |
| size\_t numAnnualRules | 每年生效的时区规则数组的大小。 |
