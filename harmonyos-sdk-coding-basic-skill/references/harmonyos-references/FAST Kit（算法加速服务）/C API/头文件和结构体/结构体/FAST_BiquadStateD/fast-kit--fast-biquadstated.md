---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstated
title: FAST_BiquadStateD
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadStateD
category: harmonyos-references
scraped_at: 2026-06-01T16:12:03+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:b5f5a0ba67703be5c4bccf6e770e5d974134586cb1b4b6f3304b829fd8847ce8
---
## 概述

PhonePC/2in1Tablet

定义双精度二阶IIR滤波器节的状态变量。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](../../../模块/FAST/fast-kit-fast.md)

**所在头文件：** [fast\_dsp\_common.h](../../头文件/fast_dsp_common.h/fast-kit-fast-dsp-common-8h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| double [d1](fast-kit--fast-biquadstated.md#d1) | 第一个延迟单元（y[n-1]）。 |
| double [d2](fast-kit--fast-biquadstated.md#d2) | 第二个延迟单元（y[n-2]）。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### d1

PhonePC/2in1Tablet

```
1. double FAST_BiquadStateD::d1
```

**描述**

第一个延迟单元，存储上一时刻的输出值y[n-1]。

### d2

PhonePC/2in1Tablet

```
1. double FAST_BiquadStateD::d2
```

**描述**

第二个延迟单元，存储上上时刻的输出值y[n-2]。
