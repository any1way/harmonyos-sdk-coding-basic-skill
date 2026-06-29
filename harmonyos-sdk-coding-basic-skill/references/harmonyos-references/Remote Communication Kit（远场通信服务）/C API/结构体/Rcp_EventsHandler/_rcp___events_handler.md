---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler
title: Rcp_EventsHandler
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_EventsHandler
category: harmonyos-references
scraped_at: 2026-06-01T16:08:37+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:dab56526e4a3cbe3e9cf917e344ec40d3d4e4ea53a8af89c6ac770f4dabbfbd0
---
## 概述

PhonePC/2in1TabletTVWearable

监听不同HTTP事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnDataReceiveCallback](../Rcp_OnDataReceiveCallback/_rcp___on_data_receive_callback.md) [onDataReceive](_rcp___events_handler.md#ondatareceive) | 收到响应体时的回调函数。 |
| [Rcp\_OnProgressCallback](../Rcp_OnProgressCallback/_rcp___on_progress_callback.md) [onUploadProgress](_rcp___events_handler.md#onuploadprogress) | 上传时调用的回调函数。 |
| [Rcp\_OnProgressCallback](../Rcp_OnProgressCallback/_rcp___on_progress_callback.md) [onDownloadProgress](_rcp___events_handler.md#ondownloadprogress) | 下载时调用的回调函数。 |
| [Rcp\_OnHeaderReceiveCallback](../Rcp_OnHeaderReceiveCallback/_rcp___on_header_receive_callback.md) [onHeaderReceive](_rcp___events_handler.md#onheaderreceive) | 收到header时的回调函数。 |
| [Rcp\_OnVoidCallback](../Rcp_OnVoidCallback/_rcp___on_void_callback.md) [onDataEnd](_rcp___events_handler.md#ondataend) | 传输结束时的回调函数。 |
| [Rcp\_OnVoidCallback](../Rcp_OnVoidCallback/_rcp___on_void_callback.md) [onCanceled](_rcp___events_handler.md#oncanceled) | 请求或会话被取消时的回调函数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### onCanceled

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnVoidCallback Rcp_EventsHandler::onCanceled
```

**描述**

请求或会话被取消时的回调函数。

### onDataEnd

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnVoidCallback Rcp_EventsHandler::onDataEnd
```

**描述**

传输结束时的回调函数。

### onDataReceive

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnDataReceiveCallback Rcp_EventsHandler::onDataReceive
```

**描述**

收到响应体时的回调函数。

### onDownloadProgress

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnProgressCallback Rcp_EventsHandler::onDownloadProgress
```

**描述**

下载时调用的回调函数。

### onHeaderReceive

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnHeaderReceiveCallback Rcp_EventsHandler::onHeaderReceive
```

**描述**

收到header时的回调函数。

### onUploadProgress

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnProgressCallback Rcp_EventsHandler::onUploadProgress
```

**描述**

上传时调用的回调函数。
