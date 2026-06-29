---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeoption
title: WebSocket_CloseOption
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_CloseOption
category: harmonyos-references
scraped_at: 2026-06-01T16:07:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2c95ba61715e02b9982ac71bee651d08b82135ae446b3a17bf0ce619a3312531
---
```
1. struct WebSocket_CloseOption {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端主动关闭的参数。

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
