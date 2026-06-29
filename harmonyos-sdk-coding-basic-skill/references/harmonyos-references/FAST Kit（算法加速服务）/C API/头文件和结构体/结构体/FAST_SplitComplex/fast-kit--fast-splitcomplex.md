---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplex
title: FAST_SplitComplex
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_SplitComplex
category: harmonyos-references
scraped_at: 2026-06-01T16:12:04+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:0ac33af0c315211e5b5cde1c5d15e735e2e39cfd7ea677b3ea3df20ecf814f3b
---
## 概述

PhonePC/2in1Tablet

定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。

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
| float\* [real](fast-kit--fast-splitcomplex.md#real) | 实部数组指针。 |
| float\* [imag](fast-kit--fast-splitcomplex.md#imag) | 虚部数组指针。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### imag

PhonePC/2in1Tablet

```
1. float* FAST_SplitComplex::imag
```

**描述**

指向虚部数组的指针。数组长度应与实部数组相同，存储复数信号的虚部数据。

### real

PhonePC/2in1Tablet

```
1. float* FAST_SplitComplex::real
```

**描述**

指向实部数组的指针。数组长度应与虚部数组相同，存储复数信号的实部数据。
