---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficientsd
title: FAST_BiquadCoefficientsD
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadCoefficientsD
category: harmonyos-references
scraped_at: 2026-06-01T16:12:00+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9c39664acf37f6823dcb60e56913e00a15dfa4b8db9297fe7d32e97885d64981
---
## 概述

PhonePC/2in1Tablet

定义双精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。

传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)

注意

分母中的1实际上为系数a0归一化后的结果。

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
| double [a1](fast-kit--fast-biquadcoefficientsd.md#a1) | z⁻¹ 分母系数。 |
| double [a2](fast-kit--fast-biquadcoefficientsd.md#a2) | z⁻² 分母系数。 |
| double [b0](fast-kit--fast-biquadcoefficientsd.md#b0) | z⁰ 分子系数。 |
| double [b1](fast-kit--fast-biquadcoefficientsd.md#b1) | z⁻¹ 分子系数。 |
| double [b2](fast-kit--fast-biquadcoefficientsd.md#b2) | z⁻² 分子系数。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### a1

PhonePC/2in1Tablet

```
1. double FAST_BiquadCoefficientsD::a1
```

**描述**

z⁻¹ 分母系数。

### a2

PhonePC/2in1Tablet

```
1. double FAST_BiquadCoefficientsD::a2
```

**描述**

z⁻² 分母系数。

### b0

PhonePC/2in1Tablet

```
1. double FAST_BiquadCoefficientsD::b0
```

**描述**

z⁰ 分子系数。

### b1

PhonePC/2in1Tablet

```
1. double FAST_BiquadCoefficientsD::b1
```

**描述**

z⁻¹ 分子系数。

### b2

PhonePC/2in1Tablet

```
1. double FAST_BiquadCoefficientsD::b2
```

**描述**

z⁻² 分子系数。
