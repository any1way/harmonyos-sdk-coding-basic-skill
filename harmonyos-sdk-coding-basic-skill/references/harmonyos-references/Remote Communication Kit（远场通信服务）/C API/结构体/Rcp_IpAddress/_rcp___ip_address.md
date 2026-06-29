---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address
title: Rcp_IpAddress
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_IpAddress
category: harmonyos-references
scraped_at: 2026-06-01T16:08:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60b29a58d8a259cd5e108d5cbcb569615d47299589c4d393c1f881bb4a1ff9ef
---
## 概述

PhonePC/2in1TabletTVWearable

指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](../Rcp_StaticDnsRuleItem/_rcp___static_dns_rule_item.md)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char [ipAddress](_rcp___ip_address.md#ipaddress) [[RCP\_IP\_MAX\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_ip_max_len)] | IP地址。 |
| struct [Rcp\_IpAddress](_rcp___ip_address.md) \* [next](_rcp___ip_address.md#next) | 链式存储。指向下一个[Rcp\_IpAddress](_rcp___ip_address.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### ipAddress

PhonePC/2in1TabletTVWearable

```
1. char Rcp_IpAddress::ipAddress[RCP_IP_MAX_LEN]
```

**描述**

ip地址。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_IpAddress* Rcp_IpAddress::next
```

**描述**

链式存储。指向下一个[Rcp\_IpAddress](_rcp___ip_address.md)。
