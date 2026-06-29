---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration
title: Rcp_ProxyConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ProxyConfiguration
category: harmonyos-references
scraped_at: 2026-06-01T16:08:51+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1df73c9e68449a7b3f4e03b1c045155c088274247c123f39e88b2f0bd9e1201c
---
## 概述

PhonePC/2in1TabletTVWearable

代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ProxyType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytype) [proxyType](_rcp___proxy_configuration.md#proxytype) | 区分请求使用的代理类型。 |
| [Rcp\_WebProxy](../Rcp_WebProxy/_rcp___web_proxy.md) [customProxy](_rcp___proxy_configuration.md#customproxy) | 自定义代理配置，参见[Rcp\_WebProxy](../Rcp_WebProxy/_rcp___web_proxy.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### customProxy

PhonePC/2in1TabletTVWearable

```
1. Rcp_WebProxy Rcp_ProxyConfiguration::customProxy
```

**描述**

自定义代理配置，参见[Rcp\_WebProxy](../Rcp_WebProxy/_rcp___web_proxy.md)。

### proxyType

PhonePC/2in1TabletTVWearable

```
1. Rcp_ProxyType Rcp_ProxyConfiguration::proxyType
```

**描述**

区分请求使用的代理类型。
