---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstate
title: FAST_BiquadState
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadState
category: harmonyos-references
scraped_at: 2026-06-01T16:12:02+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:21fcbaa3ff596f8b2e94c48ed85b3a696de21eb6deb32e0fb98a089901814009
---
## 概述

PhonePC/2in1Tablet

定义单精度二阶IIR滤波器节的状态变量。

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
| float [d1](fast-kit--fast-biquadstate.md#d1) | 第一个延迟单元（y[n-1]）。 |
| float [d2](fast-kit--fast-biquadstate.md#d2) | 第二个延迟单元（y[n-2]）。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### d1

PhonePC/2in1Tablet

```
1. float FAST_BiquadState::d1
```

**描述**

第一个延迟单元，存储上一时刻的输出值y[n-1]。

### d2

PhonePC/2in1Tablet

```
1. float FAST_BiquadState::d2
```

**描述**

第二个延迟单元，存储上上时刻的输出值y[n-2]。
