---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-aipp-param-8h
title: hiai_aipp_param.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > hiai_aipp_param.h
category: harmonyos-references
scraped_at: 2026-06-01T16:40:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95f861edea0bec68d9ee6ab48d160796815cd59f8223852051c5b20b2760ed28
---
## 概述

PhonePC/2in1TabletTV

模型推理时动态AIPP对象创建，参数设置和查询的接口。

**引用文件：** <CANNKit/hiai\_aipp\_param.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：** [CANN](../../../模块/CANN/cannkit.md)

## 汇总

PhonePC/2in1TabletTV

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) [HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) | AIPP参数对象。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) {  HIAI\_YUV420SP\_U8 = 0,  HIAI\_XRGB8888\_U8 = 1,  HIAI\_YUV400\_U8 = 2,  HIAI\_ARGB8888\_U8 = 3,  HIAI\_YUYV\_U8 = 4,  HIAI\_YUV422SP\_U8 = 5,  HIAI\_AYUV444\_U8 = 6,  HIAI\_RGB888\_U8 = 7,  HIAI\_BGR888\_U8 = 8,  HIAI\_YUV444SP\_U8 = 9,  HIAI\_YVU444SP\_U8 = 10,  HIAI\_IMAGE\_FORMAT\_INVALID = 255  } | CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。 |
| [HiAI\_ImageColorSpace](../../../模块/CANN/cannkit.md#hiai_imagecolorspace) {  HIAI\_JPEG = 0,  HIAI\_BT\_601\_NARROW = 1,  HIAI\_BT\_601\_FULL = 2,  HIAI\_BT\_709\_NARROW = 3,  HIAI\_IMAGE\_COLOR\_SPACE\_INVALID = 4  } | 图像色域空间类型。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \* [HMS\_HiAIAippParam\_Create](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_create) (uint32\_t batchNum) | 根据batchNum创建动态AippParam对象。 |
| void \* [HMS\_HiAIAippParam\_GetData](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getdata) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 获取AippParam申请的内存地址。 |
| uint32\_t [HMS\_HiAIAippParam\_GetDataSize](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getdatasize) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 获取AippParam申请的内存大小。 |
| int [HMS\_HiAIAippParam\_GetInputIndex](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getinputindex) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象所在输入的索引。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputIndex](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setinputindex) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t inputIndex) | 设置AippParam在输入上的索引。 |
| int [HMS\_HiAIAippParam\_GetInputAippIndex](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getinputaippindex) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象在该输入的多个输出分支上的索引。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputAippIndex](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setinputaippindex) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t inputAippIndex) | 设置AippParam对象作用于该输入的多个输出分支上的索引。 |
| void [HMS\_HiAIAippParam\_Destroy](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_destroy) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*\*aippParam) | 释放AippParam对象。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputFormat](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setinputformat) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) inputFormat) | 设置AippParam对象的输入图像格式。 |
| [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) [HMS\_HiAIAippParam\_GetInputFormat](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getinputformat) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象的输入图像格式。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputShape](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setinputshape) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t srcImageW, uint32\_t srcImageH) | 设置AippParam对象的输入图像宽高。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetInputShape](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getinputshape) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t \*srcImageW, uint32\_t \*srcImageH) | 查询AippParam对象的输入图像宽高。 |
| uint32\_t [HMS\_HiAIAippParam\_GetBatchCount](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getbatchcount) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象的图像数量。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCscConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setcscconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) inputFormat, [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) outputFormat, [HiAI\_ImageColorSpace](../../../模块/CANN/cannkit.md#hiai_imagecolorspace) space) | 设置AippParam对象的CSC色域转换参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCscConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getcscconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) \*inputFormat, [HiAI\_ImageFormat](../../../模块/CANN/cannkit.md#hiai_imageformat) \*outputFormat, [HiAI\_ImageColorSpace](../../../模块/CANN/cannkit.md#hiai_imagecolorspace) \*space) | 查询AippParam对象的CSC色域转换相关参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelSwapConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setchannelswapconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, bool rbuvSwapSwitch, bool axSwapSwitch) | 设置AippParam对象的ChannelSwap通道交换参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelSwapConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getchannelswapconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, bool \*rbuvSwapSwitch, bool \*axSwapSwitch) | 查询AippParam对象的ChannelSwap通道交换参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetSingleBatchMultiCrop](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setsinglebatchmulticrop) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, bool singleBatchMultiCrop) | 设置AippParam对象的SingleBatchMultiCrop标识。 |
| bool [HMS\_HiAIAippParam\_GetSingleBatchMultiCrop](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getsinglebatchmulticrop) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam) | 查询AippParam对象的SingleBatchMultiCrop标识。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCropConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setcropconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH) | 设置AippParam对象的裁剪参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCropConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getcropconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*startPosW, uint32\_t \*startPosH, uint32\_t \*croppedW, uint32\_t \*croppedH) | 查询AippParam对象的裁剪参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetResizeConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setresizeconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH) | 设置AippParam对象的图像缩放参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetResizeConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getresizeconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*resizedW, uint32\_t \*resizedH) | 查询AippParam对象的图像缩放参数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetPadConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setpadconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize) | 设置AippParam对象的输入图像的填充像素数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetPadConfig](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getpadconfig) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*leftPadSize, uint32\_t \*rightPadSize, uint32\_t \*topPadSize, uint32\_t \*bottomPadSize) | 查询AippParam对象的输入图像的填充像素数。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelPadding](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setchannelpadding) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues[], uint32\_t channelCount) | 设置AippParam对象的通道padding填充值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelPadding](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getchannelpadding) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues[], uint32\_t channelCount) | 查询AippParam对象的通道padding填充值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetRotationAngle](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setrotationangle) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float rotationAngle) | 设置AippParam对象的旋转角度。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetRotationAngle](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getrotationangle) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float \*rotationAngle) | 查询AippParam对象的图像旋转角度。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMeanPixel](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setdtcmeanpixel) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel[], uint32\_t channelCount) | 设置AippParam对象的数据类型转换通道像素平均值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMeanPixel](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getdtcmeanpixel) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel[], uint32\_t channelCount) | 查询AippParam对象的数据类型转换通道像素平均值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMinPixel](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setdtcminpixel) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel[], uint32\_t channelCount) | 设置AippParam对象的数据类型转换通道像素最小值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMinPixel](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getdtcminpixel) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel[], uint32\_t channelCount) | 查询AippParam对象的数据类型转换通道像素最小值。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcVarReciPixel](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_setdtcvarrecipixel) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel[], uint32\_t channelCount) | 设置AippParam对象的数据类型转换通道像素方差。 |
| OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcVarReciPixel](../../../模块/CANN/cannkit.md#hms_hiaiaippparam_getdtcvarrecipixel) ([HiAI\_AippParam](../../../模块/CANN/cannkit.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel[], uint32\_t channelCount) | 查询AippParam对象的数据类型转换通道像素方差。 |
