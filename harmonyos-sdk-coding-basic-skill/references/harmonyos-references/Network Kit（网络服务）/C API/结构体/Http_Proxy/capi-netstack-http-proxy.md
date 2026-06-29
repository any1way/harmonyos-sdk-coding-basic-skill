---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-proxy
title: Http_Proxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Proxy
category: harmonyos-references
scraped_at: 2026-06-01T16:07:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dd89e3ee5f833ca7284192795c1411e620e205614671f142d345f6a29b424ba4
---
```
1. typedef struct Http_Proxy {...} Http_Proxy
```

## 概述

PhonePC/2in1TabletTVWearable

代理配置结构体。

**起始版本：** 20

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_http\_type.h](../../头文件/net_http_type.h/capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Http\_ProxyType](../../头文件/net_http_type.h/capi-net-http-type-h.md#http_proxytype) proxyType | 代理配置类型，参考[Http\_ProxyType](../../头文件/net_http_type.h/capi-net-http-type-h.md#http_proxytype)。 |
| [Http\_CustomProxy](../Http_CustomProxy/capi-netstack-http-customproxy.md) customProxy | 自定义代理配置信息，参考[Http\_CustomProxy](../Http_CustomProxy/capi-netstack-http-customproxy.md)。 |
