---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule
title: Rcp_DnsRule
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DnsRule
category: harmonyos-references
scraped_at: 2026-06-01T16:08:36+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:a658bb1b728bff49ba8833334050de2af01a1555c4af6c632210a70e6484602c
---
## 概述

PhonePC/2in1TabletTVWearable

DNS规则配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_DnsRuleType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsruletype) [type](_rcp___dns_rule.md#type) | 表示union中使用的数据类型。 |
| union {  [Rcp\_DnsServers](../Rcp_DnsServers/_rcp___dns_servers.md) \* [dnsServers](_rcp___dns_rule.md#dnsservers);  [Rcp\_StaticDnsRule](../Rcp_StaticDnsRule/_rcp___static_dns_rule.md) \* [staticDnsRule](_rcp___dns_rule.md#staticdnsrule);  [Rcp\_DynamicDnsRuleFunction](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dynamicdnsrulefunction) [dynamicDnsRule](_rcp___dns_rule.md#dynamicdnsrule);  } data | dnsServers：DNS服务器。  staticDnsRule：静态DNS规则。  dynamicDnsRule：动态DNS规则。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### dnsServers

PhonePC/2in1TabletTVWearable

```
1. Rcp_DnsServers* Rcp_DnsRule::dnsServers
```

**描述**

DNS服务器。

### dynamicDnsRule

PhonePC/2in1TabletTVWearable

```
1. Rcp_DynamicDnsRuleFunction Rcp_DnsRule::dynamicDnsRule
```

**描述**

动态DNS规则。

### staticDnsRule

PhonePC/2in1TabletTVWearable

```
1. Rcp_StaticDnsRule* Rcp_DnsRule::staticDnsRule
```

**描述**

静态DNS规则。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_DnsRuleType Rcp_DnsRule::type
```

**描述**

表示union中使用的数据类型。
