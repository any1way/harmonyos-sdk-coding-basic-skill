---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-fiber-t
title: ffrt_fiber_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_fiber_t
category: harmonyos-references
scraped_at: 2026-06-11T16:19:58+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:84a338c4bcfdeb501522da1d6f2bceea202a66dd800a35494a84aff80bfa138b
---
```
1. typedef struct {...} ffrt_fiber_t
```

## 概述

PhonePC/2in1TabletTVWearable

纤程结构。

**起始版本：** 20

**相关模块：** [FFRT](../../模块/FFRT/capi-ffrt.md)

**所在头文件：** [type\_def.h](../../头文件/type_def.h/capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uintptr\_t storage[ffrt\_fiber\_storage\_size] | 纤程上下文占用空间。 |
