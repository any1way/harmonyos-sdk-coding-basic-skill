---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action
title: NetworkBoost_DataSpeedAction
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_DataSpeedAction
category: harmonyos-references
scraped_at: 2026-06-11T16:15:20+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:a9e36c610bc3b0e271b6c4b7539406462755e20c0f2813d6650fd38fd4c0742f
---
## 概述

PhonePC/2in1Tablet

发包速率建议。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](../../头文件/network_boost_handover.h/network-boost-c-files-handover.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_DataSpeedSimpleAction](../../模块/NetworkBoost/network-boost-c-overview.md#networkboost_dataspeedsimpleaction-1) [dataSpeedSimpleAction](network-boost-c-struct-data_speed_action.md#dataspeedsimpleaction) | 应用发包策略的简单建议。 |
| uint64\_t [linkUpBandwidth](network-boost-c-struct-data_speed_action.md#linkupbandwidth) | 上行带宽。 |
| uint64\_t [linkDownBandwidth](network-boost-c-struct-data_speed_action.md#linkdownbandwidth) | 下行带宽。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### dataSpeedSimpleAction

PhonePC/2in1Tablet

```
1. NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedAction::dataSpeedSimpleAction
```

**描述**

应用发包策略的简单建议。

### linkDownBandwidth

PhonePC/2in1Tablet

```
1. uint64_t NetworkBoost_DataSpeedAction::linkDownBandwidth
```

**描述**

下行带宽。

### linkUpBandwidth

PhonePC/2in1Tablet

```
1. uint64_t NetworkBoost_DataSpeedAction::linkUpBandwidth
```

**描述**

上行带宽。
