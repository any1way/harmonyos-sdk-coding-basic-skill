---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-extension-8h
title: xeg_gles_extension.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_gles_extension.h
category: harmonyos-references
scraped_at: 2026-06-01T16:31:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2bd5524589d01e3dd8ffe5725d0418dd4e7ab88aebda3ee49465c8f421d73112
---
## 概述

PhonePC/2in1TabletTV

XEngine扩展特性查询接口（OpenGL ES）。

**引用文件**：<xengine/xeg\_gles\_extension.h>

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
| [XEG\_EXTENSIONS](../../../模块/XEngine/xengine-kit-xengine.md#xeg_extensions) 0x01U | 作为[HMS\_XEG\_GetString](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_getstring)接口的入参，以获取XEngine支持的OpenGL ES扩展特性。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef const GLubyte \*(GL\_APIENTRYP [PFN\_HMS\_XEG\_GETSTRING](../../../模块/XEngine/xengine-kit-xengine.md#pfn_hms_xeg_getstring)) (GLenum name) | XEngine OpenGL ES扩展特性查询接口函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| const GLubyte \* [HMS\_XEG\_GetString](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_getstring) (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
