---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-initialtimezonerule
title: InitialTimeZoneRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > InitialTimeZoneRule
category: harmonyos-references
scraped_at: 2026-06-01T16:00:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4bdd37a42d134f498554130a9879c4bf1e611c14851ea3eece293612da2a7759
---
```
1. typedef struct InitialTimeZoneRule {...} InitialTimeZoneRule
```

## 概述

PhonePC/2in1TabletTVWearable

起始时区规则。

**起始版本：** 22

**相关模块：** [i18n](../../模块/i18n/capi-i18n.md)

**所在头文件：** [timezone.h](../../头文件/timezone.h/capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t rawOffset | 时区的原始偏移量。 |
| int32\_t dstSavings | 夏令时的偏移量。 |
