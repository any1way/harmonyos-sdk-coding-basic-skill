---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___timeout
title: Rcp_Timeout
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Timeout
category: harmonyos-references
scraped_at: 2026-06-01T16:09:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:789105152e3f293e4c23448cdf9877b6a0005f4107e491255c3d2b55dd3bc2b2
---
## 概述

PhonePC/2in1TabletTVWearable

请求的超时配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t [connectMs](_rcp___timeout.md#connectms) | 连接超时时间。默认值为60000毫秒。 |
| uint32\_t [transferMs](_rcp___timeout.md#transferms) | 传输超时时间。默认值为60000毫秒。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### connectMs

PhonePC/2in1TabletTVWearable

```
1. uint32_t Rcp_Timeout::connectMs
```

**描述**

连接超时时间。默认值为60000毫秒。

### transferMs

PhonePC/2in1TabletTVWearable

```
1. uint32_t Rcp_Timeout::transferMs
```

**描述**

传输超时时间。默认值为60000毫秒。
