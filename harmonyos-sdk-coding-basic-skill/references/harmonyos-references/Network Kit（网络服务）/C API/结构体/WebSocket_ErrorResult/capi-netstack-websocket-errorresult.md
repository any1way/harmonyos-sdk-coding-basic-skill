---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-errorresult
title: WebSocket_ErrorResult
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_ErrorResult
category: harmonyos-references
scraped_at: 2026-06-01T16:07:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1db37d597e9462cef430d7f98c40fec8c0784181616c9726e21f72847ae94e5f
---
```
1. struct WebSocket_ErrorResult {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端来自服务端连接错误的参数。

**起始版本：** 11

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](../../头文件/net_websocket_type.h/capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t errorCode | 错误码。 |
| const char \*errorMessage | 错误的消息。 |
