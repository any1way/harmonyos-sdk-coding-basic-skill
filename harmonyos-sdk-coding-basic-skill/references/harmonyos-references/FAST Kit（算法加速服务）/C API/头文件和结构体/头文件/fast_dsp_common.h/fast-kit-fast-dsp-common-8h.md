---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h
title: fast_dsp_common.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_dsp_common.h
category: harmonyos-references
scraped_at: 2026-06-01T16:11:57+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:15967dc8b3230a6c5b8d03120bb18808b2c935dcbc760f19e592bd4bcc1276d8
---
## 概述

PhonePC/2in1Tablet

数字信号处理（DSP）通用数据结构和工具函数定义，包括向量运算、复数处理以及二阶IIR滤波器管理。支持单精度（float）和双精度（double）算术运算。

**引用文件：** <FASTKit/fast\_dsp\_common.h>

**库：** libfast\_dsp.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](../../../模块/FAST/fast-kit-fast.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [FAST\_SplitComplex](../../结构体/FAST_SplitComplex/fast-kit--fast-splitcomplex.md) | 定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。 |
| struct [FAST\_SplitComplexD](../../结构体/FAST_SplitComplexD/fast-kit--fast-splitcomplexd.md) | 定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。 |
| struct [FAST\_BiquadCoefficients](../../结构体/FAST_BiquadCoefficients/fast-kit--fast-biquadcoefficients.md) | 定义单精度二阶（biquad）IIR滤波器节的系数。 |
| struct [FAST\_BiquadCoefficientsD](../../结构体/FAST_BiquadCoefficientsD/fast-kit--fast-biquadcoefficientsd.md) | 定义双精度二阶（biquad）IIR滤波器节的系数。 |
| struct [FAST\_BiquadState](../../结构体/FAST_BiquadState/fast-kit--fast-biquadstate.md) | 定义单精度二阶IIR滤波器节的状态变量。 |
| struct [FAST\_BiquadStateD](../../结构体/FAST_BiquadStateD/fast-kit--fast-biquadstated.md) | 定义双精度二阶IIR滤波器节的状态变量。 |
| struct [FAST\_Biquadm](../../结构体/FAST_Biquadm/fast-kit--fast-biquadm.md) | 定义单精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct [FAST\_BiquadmD](../../结构体/FAST_BiquadmD/fast-kit--fast-biquadmd.md) | 定义双精度多通道、多节二阶IIR滤波器组的数据结构。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef struct [FAST\_SplitComplex](../../结构体/FAST_SplitComplex/fast-kit--fast-splitcomplex.md) [FAST\_SplitComplex](../../结构体/FAST_SplitComplex/fast-kit--fast-splitcomplex.md) | 单精度浮点复数信号结构体。 |
| typedef struct [FAST\_SplitComplexD](../../结构体/FAST_SplitComplexD/fast-kit--fast-splitcomplexd.md) [FAST\_SplitComplexD](../../结构体/FAST_SplitComplexD/fast-kit--fast-splitcomplexd.md) | 双精度浮点复数信号结构体。 |
| typedef struct [FAST\_BiquadCoefficients](../../结构体/FAST_BiquadCoefficients/fast-kit--fast-biquadcoefficients.md) [FAST\_BiquadCoefficients](../../结构体/FAST_BiquadCoefficients/fast-kit--fast-biquadcoefficients.md) | 单精度二阶IIR滤波器系数。 |
| typedef struct [FAST\_BiquadCoefficientsD](../../结构体/FAST_BiquadCoefficientsD/fast-kit--fast-biquadcoefficientsd.md) [FAST\_BiquadCoefficientsD](../../结构体/FAST_BiquadCoefficientsD/fast-kit--fast-biquadcoefficientsd.md) | 双精度二阶IIR滤波器系数。 |
| typedef struct [FAST\_BiquadState](../../结构体/FAST_BiquadState/fast-kit--fast-biquadstate.md) [FAST\_BiquadState](../../结构体/FAST_BiquadState/fast-kit--fast-biquadstate.md) | 单精度二阶IIR滤波器状态。 |
| typedef struct [FAST\_BiquadStateD](../../结构体/FAST_BiquadStateD/fast-kit--fast-biquadstated.md) [FAST\_BiquadStateD](../../结构体/FAST_BiquadStateD/fast-kit--fast-biquadstated.md) | 双精度二阶IIR滤波器状态。 |
| typedef struct [FAST\_Biquadm](../../结构体/FAST_Biquadm/fast-kit--fast-biquadm.md) [FAST\_Biquadm](../../结构体/FAST_Biquadm/fast-kit--fast-biquadm.md) | 单精度多通道多节IIR滤波器组。 |
| typedef struct [FAST\_BiquadmD](../../结构体/FAST_BiquadmD/fast-kit--fast-biquadmd.md) [FAST\_BiquadmD](../../结构体/FAST_BiquadmD/fast-kit--fast-biquadmd.md) | 双精度多通道多节IIR滤波器组。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| float [HMS\_FAST\_DSP\_Maxmgv](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxmgv) (const float\* input, size\_t stride, size\_t length) | 计算步长实值向量中的最大幅值（单精度）。 |
| double [HMS\_FAST\_DSP\_MaxmgvD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxmgvd) (const double\* input, size\_t stride, size\_t length) | 计算步长实值向量中的最大幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Maxvi](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxvi) (const float\* input, size\_t stride, size\_t length, float\* value, size\_t\* index) | 查找步长实值向量中的最大值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MaxviD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxvid) (const double\* input, size\_t stride, size\_t length, double\* value, size\_t\* index) | 查找步长实值向量中的最大值及其索引（双精度）。 |
| float [HMS\_FAST\_DSP\_Meamgv](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_meamgv) (const float\* input, size\_t stride, size\_t length) | 计算步长实值向量绝对值的均值（单精度）。 |
| double [HMS\_FAST\_DSP\_MeamgvD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_meamgvd) (const double\* input, size\_t stride, size\_t length) | 计算步长实值向量绝对值的均值（双精度）。 |
| float [HMS\_FAST\_DSP\_Sve](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_sve) (const float\* input, size\_t stride, size\_t length) | 计算步长实值向量的和（单精度）。 |
| double [HMS\_FAST\_DSP\_SveD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_sved) (const double\* input, size\_t stride, size\_t length) | 计算步长实值向量的和（双精度）。 |
| float [HMS\_FAST\_DSP\_Svemg](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_svemg) (const float\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double [HMS\_FAST\_DSP\_SvemgD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_svemgd) (const double\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float [HMS\_FAST\_DSP\_Dotpr](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_dotpr) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, size\_t length) | 计算两个步长实值向量的点积（单精度）。 |
| double [HMS\_FAST\_DSP\_DotprD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_dotprd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, size\_t length) | 计算两个步长实值向量的点积（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsbsm](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_vsbsm) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float scalar, float\* outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（单精度）。 |
| void [HMS\_FAST\_DSP\_VsbsmD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_vsbsmd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double scalar, double\* outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（双精度）。 |
| void [HMS\_FAST\_DSP\_Ctoz](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_ctoz) (const float\* input, size\_t strideInput, FAST\_SplitComplex\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void [HMS\_FAST\_DSP\_CtozD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_ctozd) (const double\* input, size\_t strideInput, FAST\_SplitComplexD\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void [HMS\_FAST\_DSP\_Ztoc](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_ztoc) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void [HMS\_FAST\_DSP\_ZtocD](../../../模块/FAST/fast-kit-fast.md#hms_fast_dsp_ztocd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（双精度）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFilters](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setactivefilters) (FAST\_Biquadm\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFiltersD](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setactivefiltersd) (FAST\_BiquadmD\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingle](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffsingle) (FAST\_Biquadm\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDouble](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffdouble) (FAST\_Biquadm\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingleD](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffsingled) (FAST\_BiquadmD\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDoubleD](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffdoubled) (FAST\_BiquadmD\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_Create](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_create) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_Biquadm\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_CreateD](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_created) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_BiquadmD\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void [HMS\_FAST\_Biquadm\_Destroy](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_destroy) (FAST\_Biquadm\* filter) | 销毁二阶滤波器实例（单精度）。 |
| void [HMS\_FAST\_Biquadm\_DestroyD](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm_destroyd) (FAST\_BiquadmD\* filter) | 销毁二阶滤波器实例（双精度）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadm) (FAST\_Biquadm\* filter, const float\*\* input, const size\_t strideInput, float\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_BiquadmD](../../../模块/FAST/fast-kit-fast.md#hms_fast_biquadmd) (FAST\_BiquadmD\* filter, const double\*\* input, const size\_t strideInput, double\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |
