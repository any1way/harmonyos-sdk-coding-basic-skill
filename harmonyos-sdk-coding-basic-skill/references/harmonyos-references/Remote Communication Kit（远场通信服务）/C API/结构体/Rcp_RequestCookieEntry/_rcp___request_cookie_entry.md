---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry
title: Rcp_RequestCookieEntry
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_RequestCookieEntry
category: harmonyos-references
scraped_at: 2026-06-01T16:08:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d199215b7760060c0c4e406fa0be025e1ff0835dd07089c6d1362b3bb7945c3
---
## 概述

PhonePC/2in1TabletTVWearable

描述请求的所有Cookie键值对。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \* [key](_rcp___request_cookie_entry.md#key) | 请求Cookie键值对的键。 |
| char \* [value](_rcp___request_cookie_entry.md#value) | 请求Cookie键值对的值。 |
| struct [Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md) \* [next](_rcp___request_cookie_entry.md#next) | 链式存储。指向下一个[Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### key

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_RequestCookieEntry::key
```

**描述**

请求Cookie键值对的键。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_RequestCookieEntry* Rcp_RequestCookieEntry::next
```

**描述**

链式存储。指向下一个[Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)的指针。

### value

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_RequestCookieEntry::value
```

**描述**

请求Cookie键值对的值。
