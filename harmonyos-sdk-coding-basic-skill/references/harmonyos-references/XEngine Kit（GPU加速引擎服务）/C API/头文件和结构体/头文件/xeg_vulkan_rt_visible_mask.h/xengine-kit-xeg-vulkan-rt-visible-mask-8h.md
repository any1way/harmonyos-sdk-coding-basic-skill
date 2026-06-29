---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-visible-mask-8h
title: xeg_vulkan_rt_visible_mask.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_rt_visible_mask.h
category: harmonyos-references
scraped_at: 2026-06-01T16:31:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b5ee73686739bfea0be45d9e7096c130989e64570df93aeb77640104aa93bd79
---
## 概述

PhonePC/2in1TabletTV

XEngine RT VisibleMask特性接口。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rt_shadow_ao_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_rt\_visible\_mask.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](../../../模块/XEngine/xengine-kit-xengine.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [XEG\_RTShadowAOCreateInfo](../../结构体/XEG_RTShadowAOCreateInfo/xengine-kit-xeg-rtshadowaocreateinfo.md) | 此结构体描述创建支持光线追踪阴影和环境光遮蔽效果[XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)实例的初始化信息。当结构体中的信息变化时，需要创建新的[XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| struct [XEG\_RTShadowParameters](../../结构体/XEG_RTShadowParameters/xengine-kit-xeg-rtshadowparameters.md) | 光线追踪阴影（Shadow）算法参数。 |
| struct [XEG\_RTAOParameters](../../结构体/XEG_RTAOParameters/xengine-kit-xeg-rtaoparameters.md) | 光线追踪环境光遮蔽（AO）算法参数。 |
| struct [XEG\_RTShadowAODenoiserParameters](../../结构体/XEG_RTShadowAODenoiserParameters/xengine-kit-xeg-rtshadowaodenoiserparameters.md) | 光线追踪阴影和环境光遮蔽算法去噪参数。 |
| struct [XEG\_RTShadowAODescription](../../结构体/XEG_RTShadowAODescription/xengine-kit-xeg-rtshadowaodescription.md) | 此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)) | [XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)的句柄。表示光线追踪VisibleMask特性实例，支持阴影和环境光遮蔽效果。 |
| typedef enum [XEG\_DenoiseQualityMode](../../../模块/XEngine/xengine-kit-xengine.md#xeg_denoisequalitymode) XEG\_DenoiseQualityMode | 去噪质量模式枚举。 |
| typedef enum [XEG\_TraversalMode](../../../模块/XEngine/xengine-kit-xengine.md#xeg_traversalmode) XEG\_TraversalMode | 遍历模式枚举。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#pfn_hms_xeg_creatertvisiblemask)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask) \*pRTVisibleMask) | 创建[XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderrtvisiblemask)) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription) | 录制光线追踪VisibleMask渲染命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#pfn_hms_xeg_destroyrtvisiblemask)) ([XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask) | 销毁[XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)对象的函数指针定义。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_DenoiseQualityMode](../../../模块/XEngine/xengine-kit-xengine.md#xeg_denoisequalitymode) { XEG\_DENOISE\_QUALITY\_MODE\_NONE = 0, XEG\_DENOISE\_QUALITY\_MODE\_QUALITY = 1, XEG\_DENOISE\_QUALITY\_MODE\_BALANCED = 2, XEG\_DENOISE\_QUALITY\_MODE\_PERFORMANCES = 3 } | 去噪质量模式枚举。 |
| [XEG\_TraversalMode](../../../模块/XEngine/xengine-kit-xengine.md#xeg_traversalmode) { XEG\_TRAVERSAL\_MODE\_DEFAULT = 0, XEG\_TRAVERSAL\_MODE\_PERFORMANCES = 1 } | 遍历模式枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_creatertvisiblemask) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask) \*pRTVisibleMask) | 创建[XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_cmdrenderrtvisiblemask) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription) | 录制光线追踪VisibleMask渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#hms_xeg_destroyrtvisiblemask) ([XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask) rtVisibleMask) | 销毁[XEG\_RTVisibleMask](../../../模块/XEngine/xengine-kit-xengine.md#xeg_rtvisiblemask)对象。 |
