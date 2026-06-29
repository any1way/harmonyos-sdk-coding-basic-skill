---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication
title: Rcp_ServerAuthentication
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ServerAuthentication
category: harmonyos-references
scraped_at: 2026-06-01T16:08:58+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e191fd97f539e3e6a61524d575466421db22f280f728bbf67537da0b534e98b0
---
## 概述

PhonePC/2in1TabletTVWearable

服务器身份验证。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Credential](../Rcp_Credential/_rcp___credential.md) [credential](_rcp___server_authentication.md#credential) | 服务器的凭据。 |
| [Rcp\_AuthenticationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_authenticationtype) [authenticationType](_rcp___server_authentication.md#authenticationtype) | 服务器的身份验证类型。如果未设置，请与服务器协商。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### authenticationType

PhonePC/2in1TabletTVWearable

```
1. Rcp_AuthenticationType Rcp_ServerAuthentication::authenticationType
```

**描述**

服务器的身份验证类型。如果未设置，请与服务器协商。

### credential

PhonePC/2in1TabletTVWearable

```
1. Rcp_Credential Rcp_ServerAuthentication::credential
```

**描述**

服务器的凭据。
