---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule
title: TimeArrayTimeZoneRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > TimeArrayTimeZoneRule
category: harmonyos-references
scraped_at: 2026-06-01T16:00:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c2f56eeacc6bfc932b3951ea5284ee76dea3ba800a380f1916bd15c1dac9b074
---
```
1. typedef struct TimeArrayTimeZoneRule {...} TimeArrayTimeZoneRule
```

## 概述

PhonePC/2in1TabletTVWearable

起始时间戳数组定义的时区规则。

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
| int32\_t rawOffset | 时区的原始偏移量。 |
| int32\_t dstSavings | 夏令时的偏移量。 |
| double\* startTimes | 规则生效的起始时间戳数组。 |
| int32\_t numStartTimes | 规则生效的起始时间戳数组的大小。 |
| [TimeRuleType](../../头文件/timezone.h/capi-timezone-h.md#timeruletype) timeRuleType | 时间规则类型。 |
