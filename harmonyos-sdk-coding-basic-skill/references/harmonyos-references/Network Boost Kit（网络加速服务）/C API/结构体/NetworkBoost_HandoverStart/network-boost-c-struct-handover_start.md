---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_start
title: NetworkBoost_HandoverStart
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_HandoverStart
category: harmonyos-references
scraped_at: 2026-06-11T16:15:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5da0a018ed9d419645eb7249dc5fb86c66a38cadf0d7406956e51ab34ccbd9be
---
## 概述

PhonePC/2in1Tablet

连接迁移开始信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](../../头文件/network_boost_handover.h/network-boost-c-files-handover.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t [expires](network-boost-c-struct-handover_start.md#expires) | 连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。 |
| [NetworkBoost\_DataSpeedAction](../NetworkBoost_DataSpeedAction/network-boost-c-struct-data_speed_action.md) [dataSpeedAction](network-boost-c-struct-handover_start.md#dataspeedaction) | 老链路的发包建议。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### dataSpeedAction

PhonePC/2in1Tablet

```
1. NetworkBoost_DataSpeedAction NetworkBoost_HandoverStart::dataSpeedAction
```

**描述**

老链路的发包建议。

### expires

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_HandoverStart::expires
```

**描述**

连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。
