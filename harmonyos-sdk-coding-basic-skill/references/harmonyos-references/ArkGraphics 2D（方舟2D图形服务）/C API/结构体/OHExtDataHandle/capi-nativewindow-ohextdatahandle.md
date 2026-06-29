---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-ohextdatahandle
title: OHExtDataHandle
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OHExtDataHandle
category: harmonyos-references
scraped_at: 2026-06-01T16:29:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a253405bf7839c18ec643df392a3ce566cb0ff5790dc3ab0f82ce0f23076c667
---
```
1. typedef struct OHExtDataHandle {...} OHExtDataHandle
```

## 概述

PhonePC/2in1TabletTVWearable

扩展数据句柄结构体定义。

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**相关模块：** [NativeWindow](../../模块/NativeWindow/capi-nativewindow.md)

**所在头文件：** [external\_window.h](../../头文件/external_window.h/capi-external-window-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t fd | 句柄 Fd，-1代表不支持。 |
| uint32\_t reserveInts | Reserve数组的个数。 |
| int32\_t reserve[0] | Reserve数组。 |
