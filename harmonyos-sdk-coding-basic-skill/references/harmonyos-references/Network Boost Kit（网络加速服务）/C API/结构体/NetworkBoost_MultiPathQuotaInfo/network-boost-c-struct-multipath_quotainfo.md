---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quotainfo
title: NetworkBoost_MultiPathQuotaInfo
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_MultiPathQuotaInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:15:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24629d975ee9306b26797f46041d0ea20814f5812add2dd40628f20f2ab62d77
---
## 概述

PhonePC/2in1Tablet

多网配额信息，包含配额次数信息和时长信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](../../头文件/network_boost_handover.h/network-boost-c-files-handover.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint16\_t [count](network-boost-c-struct-multipath_quotainfo.md#count) | 配额次数信息。 |
| uint16\_t [duration](network-boost-c-struct-multipath_quotainfo.md#duration) | 配额时长信息，单位为s。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

## count

PhonePC/2in1Tablet

```
1. uint16_t NetworkBoost_MultiPathQuotaInfo::count
```

**描述**

配额次数信息。

## duration

PhonePC/2in1Tablet

```
1. uint16_t NetworkBoost_MultiPathQuotaInfo::duration
```

**描述**

配额时长信息，单位为s。
