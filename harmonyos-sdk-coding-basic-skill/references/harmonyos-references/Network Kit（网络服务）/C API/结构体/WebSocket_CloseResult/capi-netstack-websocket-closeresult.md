---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeresult
title: WebSocket_CloseResult
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_CloseResult
category: harmonyos-references
scraped_at: 2026-06-01T16:07:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4833e16789b99a7ffe11f341284a98463a94f90ffeae4965439838e3967e9ba7
---
```
1. struct WebSocket_CloseResult {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端接收到服务端关闭的参数。

**起始版本：** 11

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](../../头文件/net_websocket_type.h/capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t code | 错误值。 |
| const char \*reason | 错误原因。 |
