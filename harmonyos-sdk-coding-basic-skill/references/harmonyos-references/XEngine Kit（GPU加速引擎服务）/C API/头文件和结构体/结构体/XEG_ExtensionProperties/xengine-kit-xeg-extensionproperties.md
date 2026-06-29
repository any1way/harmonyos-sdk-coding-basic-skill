---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties
title: XEG_ExtensionProperties
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_ExtensionProperties
category: harmonyos-references
scraped_at: 2026-06-01T16:31:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d5d0017c48530ac3f56594d15e9098e97e7bf3f8365c2f1b768f3eb3762e62f4
---
## 概述

PhonePC/2in1TabletTV

此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](../../../模块/XEngine/xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_extension.h](../../头文件/xeg_vulkan_extension.h/xengine-kit-xeg-vulkan-extension-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| char [extensionName](xengine-kit-xeg-extensionproperties.md#extensionname) [[XEG\_MAX\_EXTENSION\_NAME\_SIZE](../../../模块/XEngine/xengine-kit-xengine.md#xeg_max_extension_name_size)] | XEngine支持的扩展特性名称。 |
| uint32\_t [version](xengine-kit-xeg-extensionproperties.md#version) | XEngine支持的扩展特性版本号。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### extensionName

PhonePC/2in1TabletTV

```
1. char XEG_ExtensionProperties::extensionName[XEG_MAX_EXTENSION_NAME_SIZE]
```

**描述**

XEngine支持的扩展特性名称。

### version

PhonePC/2in1TabletTV

```
1. uint32_t XEG_ExtensionProperties::version
```

**描述**

XEngine支持的扩展特性版本号。
