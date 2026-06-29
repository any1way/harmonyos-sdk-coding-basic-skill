---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls
title: Rcp_Urls
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Urls
category: harmonyos-references
scraped_at: 2026-06-01T16:09:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:39fd25a5e4cedcdd83b67f5a63122973e9c7eed81f5653e93ac5a6bc787c6524
---
## 概述

PhonePC/2in1TabletTVWearable

URLs，用于确定主机是否正在使用代理。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* [url](_rcp___urls.md#url) | 匹配的URL。 |
| struct [Rcp\_Urls](_rcp___urls.md) \* [next](_rcp___urls.md#next) | 链式存储。指向下一个[Rcp\_Urls](_rcp___urls.md)的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_Urls* Rcp_Urls::next
```

**描述**

链式存储。指向下一个[Rcp\_Urls](_rcp___urls.md)的指针。

### url

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_Urls::url
```

**描述**

匹配的URL。
