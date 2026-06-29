---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-2
title: rcp请求是否有数据大小限制
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp请求是否有数据大小限制
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:06+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:c6f3f8b3140b57d82d9180f332ce3b7e3bbd68d60672c464c33b12a4131e92a0
---
rcp请求默认情况下，[response](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#response>)响应中最大数据量为50MB，超过此限制建议通过[HttpEventsHandler](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#httpeventshandler>)的[onDataReceive](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#ondatareceive>)实现流式数据接收。

**参考链接**

[response](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#response>)

[HttpEventsHandler](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#httpeventshandler>)

[onDataReceive](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#ondatareceive>)
