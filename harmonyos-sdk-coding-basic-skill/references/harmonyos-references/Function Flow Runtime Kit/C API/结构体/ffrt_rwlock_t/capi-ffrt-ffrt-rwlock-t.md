---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-rwlock-t
title: ffrt_rwlock_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_rwlock_t
category: harmonyos-references
scraped_at: 2026-06-11T16:19:54+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d6d5679dad0eba3b485717ac2c20c8ddb4c42921b964696228af24b6a4cbcabb
---
```
1. typedef struct {...} ffrt_rwlock_t
```

## 概述

PhonePC/2in1TabletTVWearable

FFRT读写锁结构。

**起始版本：** 18

**相关模块：** [FFRT](../../模块/FFRT/capi-ffrt.md)

**所在头文件：** [type\_def.h](../../头文件/type_def.h/capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_rwlock\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | FFRT读写锁占用空间 |
