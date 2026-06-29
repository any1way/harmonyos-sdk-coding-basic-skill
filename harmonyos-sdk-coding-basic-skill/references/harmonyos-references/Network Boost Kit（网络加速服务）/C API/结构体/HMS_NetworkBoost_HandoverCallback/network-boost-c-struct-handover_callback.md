---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_callback
title: HMS_NetworkBoost_HandoverCallback
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > HMS_NetworkBoost_HandoverCallback
category: harmonyos-references
scraped_at: 2026-06-11T16:15:20+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:127f3ed9835cf56f668013f0a7db9cbd4eca80536fedeb691780dc7a9672492e
---
## 概述

PhonePC/2in1Tablet

回调函数，返回连接迁移开始和完成的详细信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](../../头文件/network_boost_handover.h/network-boost-c-files-handover.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [HMS\_NetworkBoost\_OnHandoverStart](../../模块/NetworkBoost/network-boost-c-overview.md#hms_networkboost_onhandoverstart) [onNetworkHandoverStart](network-boost-c-struct-handover_callback.md#onnetworkhandoverstart) | 连接迁移开始的回调。 |
| [HMS\_NetworkBoost\_OnHandoverComplete](../../模块/NetworkBoost/network-boost-c-overview.md#hms_networkboost_onhandovercomplete) [onNetworkHandoverComplete](network-boost-c-struct-handover_callback.md#onnetworkhandovercomplete) | 连接迁移结束的回调。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### onNetworkHandoverStart

PhonePC/2in1Tablet

```
1. HMS_NetworkBoost_OnHandoverStart HMS_NetworkBoost_HandoverCallback::onNetworkHandoverStart
```

**描述**

连接迁移开始的回调。

### onNetworkHandoverComplete

PhonePC/2in1Tablet

```
1. HMS_NetworkBoost_OnHandoverComplete HMS_NetworkBoost_HandoverCallback::onNetworkHandoverComplete
```

**描述**

连接迁移结束的回调。
