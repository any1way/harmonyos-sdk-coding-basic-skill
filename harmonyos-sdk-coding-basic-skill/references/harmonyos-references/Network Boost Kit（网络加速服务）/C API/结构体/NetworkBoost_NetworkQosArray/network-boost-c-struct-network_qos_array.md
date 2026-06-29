---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos_array
title: NetworkBoost_NetworkQosArray
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_NetworkQosArray
category: harmonyos-references
scraped_at: 2026-06-11T16:15:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca1dd043e5f0a89d0391cd00429313211f51d72d3460faf21648eced455286e8
---
## 概述

PhonePC/2in1Tablet

网络质量变化的详细信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](../../头文件/network_boost_quality.h/network-boost-c-files-quality.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t [pathNum](network-boost-c-struct-network_qos_array.md#pathnum) | 网络质量信息中的路径数量，取值范围 [1, 4]。 |
| [NetworkBoost\_NetworkQos](../NetworkBoost_NetworkQos/network-boost-c-struct-network_qos.md) [networkQos](network-boost-c-struct-network_qos_array.md#networkqos) [[NETBOOST\_MAX\_PATH\_NUM](../../模块/NetworkBoost/network-boost-c-overview.md#netboost_max_path_num)] | 多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### networkQos

PhonePC/2in1Tablet

```
1. NetworkBoost_NetworkQos NetworkBoost_NetworkQosArray::networkQos[NETBOOST_MAX_PATH_NUM]
```

**描述**

多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。

### pathNum

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_NetworkQosArray::pathNum
```

**描述**

网络质量信息中的路径数量，取值范围 [1, 4]。
