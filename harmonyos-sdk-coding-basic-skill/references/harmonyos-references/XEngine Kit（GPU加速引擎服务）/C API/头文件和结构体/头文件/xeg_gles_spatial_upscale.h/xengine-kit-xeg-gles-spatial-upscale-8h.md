---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-spatial-upscale-8h
title: xeg_gles_spatial_upscale.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_gles_spatial_upscale.h
category: harmonyos-references
scraped_at: 2026-06-01T16:31:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b88e66b7bba910b3a7d515cd8ea556c861de1eaecdbfd7a5e0ee6a863017c10
---
## 概述

PhonePC/2in1TabletTV

XEngine空域GPU超分特性OpenGL ES接口。使用此头文件的接口前需要通过[HMS\_XEG\_GetString](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](../../../模块/XEngine/xengine-kit-xengine.md#xeg_spatial_upscale_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_gles\_spatial\_upscale.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](../../../模块/XEngine/xengine-kit-xengine.md)

## 汇总

PhonePC/2in1TabletTV

### 宏定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_SPATIAL\_UPSCALE\_SCISSOR](../../../模块/XEngine/xengine-kit-xengine.md#xeg_spatial_upscale_scissor) 0x1U | 用于设置[HMS\_XEG\_SpatialUpscaleParameter](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口的SCISSOR参数。 |
| [XEG\_SPATIAL\_UPSCALE\_SHARPNESS](../../../模块/XEngine/xengine-kit-xengine.md#xeg_spatial_upscale_sharpness) 0x2U | 用于设置[HMS\_XEG\_SpatialUpscaleParameter](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter)接口的SHARPNESS参数。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER](../../../模块/XEngine/xengine-kit-xengine.md#pfn_hms_xeg_spatialupscaleparameter)) (GLenum pname, GLvoid \*param) | 设置空域GPU超分输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE](../../../模块/XEngine/xengine-kit-xengine.md#pfn_hms_xeg_renderspatialupscale)) (GLuint inputTexture) | 执行空域GPU超分渲染命令的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_SpatialUpscaleParameter](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_spatialupscaleparameter) (GLenum pname, GLvoid \*param) | 设置空域GPU超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderSpatialUpscale](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_renderspatialupscale) (GLuint inputTexture) | 执行空域GPU超分渲染命令。 |
