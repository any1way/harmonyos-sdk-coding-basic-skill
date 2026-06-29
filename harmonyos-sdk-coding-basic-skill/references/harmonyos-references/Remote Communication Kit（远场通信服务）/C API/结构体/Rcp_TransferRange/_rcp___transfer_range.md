---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range
title: Rcp_TransferRange
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TransferRange
category: harmonyos-references
scraped_at: 2026-06-01T16:09:08+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:320beda6492d68d224771fd55b50ba2fd5bc594a2c7ed6d78dd545422d459136
---
## 概述

PhonePC/2in1TabletTVWearable

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t [from](_rcp___transfer_range.md#from) | 传输起始位置。 |
| bool [hasZeroFrom](_rcp___transfer_range.md#haszerofrom) | 是否从零开始。true表示从零开始，false表示不从零开始。默认值为false。 |
| int64\_t [to](_rcp___transfer_range.md#to) | 传输结束位置。 |
| bool [hasZeroTo](_rcp___transfer_range.md#haszeroto) | 是否以零结束。true表示以零结束，false表示不以零结束。默认值为false。 |
| struct [Rcp\_TransferRange](_rcp___transfer_range.md) \* [next](_rcp___transfer_range.md#next) | 链式存储。指向下一个[Rcp\_TransferRange](_rcp___transfer_range.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### from

PhonePC/2in1TabletTVWearable

```
1. int64_t Rcp_TransferRange::from
```

**描述**

传输起始位置。

### hasZeroFrom

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TransferRange::hasZeroFrom
```

**描述**

请求范围是否从零开始。true表示从零开始，false表示不从零开始。默认值为false。

### hasZeroTo

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TransferRange::hasZeroTo
```

**描述**

是否以零结束。true表示以零结束，false表示不以零结束。默认值为false。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_TransferRange* Rcp_TransferRange::next
```

**描述**

链式存储。指向下一个[Rcp\_TransferRange](_rcp___transfer_range.md)。

### to

PhonePC/2in1TabletTVWearable

```
1. int64_t Rcp_TransferRange::to
```

**描述**

传输结束位置。
