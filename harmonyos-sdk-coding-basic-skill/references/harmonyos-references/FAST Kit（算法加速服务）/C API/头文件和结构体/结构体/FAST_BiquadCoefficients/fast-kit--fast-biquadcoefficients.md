---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficients
title: FAST_BiquadCoefficients
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadCoefficients
category: harmonyos-references
scraped_at: 2026-06-01T16:11:59+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:48ce9db3e5e8aa1959aa194ebcf872b59de03e326f29e3c32ed82e8da695336a
---
## 概述

PhonePC/2in1Tablet

定义单精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。

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
| float [a1](fast-kit--fast-biquadcoefficients.md#a1) | z⁻¹ 分母系数。 |
| float [a2](fast-kit--fast-biquadcoefficients.md#a2) | z⁻² 分母系数。 |
| float [b0](fast-kit--fast-biquadcoefficients.md#b0) | z⁰ 分子系数。 |
| float [b1](fast-kit--fast-biquadcoefficients.md#b1) | z⁻¹ 分子系数。 |
| float [b2](fast-kit--fast-biquadcoefficients.md#b2) | z⁻² 分子系数。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### a1

PhonePC/2in1Tablet

```
1. float FAST_BiquadCoefficients::a1
```

**描述**

z⁻¹ 分母系数。

### a2

PhonePC/2in1Tablet

```
1. float FAST_BiquadCoefficients::a2
```

**描述**

z⁻² 分母系数。

### b0

PhonePC/2in1Tablet

```
1. float FAST_BiquadCoefficients::b0
```

**描述**

z⁰ 分子系数。

### b1

PhonePC/2in1Tablet

```
1. float FAST_BiquadCoefficients::b1
```

**描述**

z⁻¹ 分子系数。

### b2

PhonePC/2in1Tablet

```
1. float FAST_BiquadCoefficients::b2
```

**描述**

z⁻² 分子系数。
