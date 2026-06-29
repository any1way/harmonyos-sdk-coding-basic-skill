---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule
title: Rcp_StaticDnsRule
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_StaticDnsRule
category: harmonyos-references
scraped_at: 2026-06-01T16:09:01+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:176ded04010d1fe768e19c67ad4c3ce2cde2f3115e3c112a49e81d8a0c445ba2
---
## 概述

PhonePC/2in1TabletTVWearable

静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_StaticDnsRuleItem](../Rcp_StaticDnsRuleItem/_rcp___static_dns_rule_item.md) [staticDnsRule](_rcp___static_dns_rule.md#staticdnsrule) | 单个静态DNS规则。 |
| struct [Rcp\_StaticDnsRule](_rcp___static_dns_rule.md) \* [next](_rcp___static_dns_rule.md#next) | 链式存储。指向下一个[Rcp\_StaticDnsRule](_rcp___static_dns_rule.md)的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_StaticDnsRule* Rcp_StaticDnsRule::next
```

**描述**

链式存储。指向下一个[Rcp\_StaticDnsRule](_rcp___static_dns_rule.md)的指针。

### staticDnsRule

PhonePC/2in1TabletTVWearable

```
1. Rcp_StaticDnsRuleItem Rcp_StaticDnsRule::staticDnsRule
```

**描述**

单个静态DNS规则。
