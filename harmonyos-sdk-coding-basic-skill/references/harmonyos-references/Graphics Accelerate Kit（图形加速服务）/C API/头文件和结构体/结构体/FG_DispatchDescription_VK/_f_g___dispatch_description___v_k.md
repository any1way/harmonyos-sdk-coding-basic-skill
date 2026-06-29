---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dispatch_description___v_k
title: FG_DispatchDescription_VK
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_DispatchDescription_VK
category: harmonyos-references
scraped_at: 2026-06-01T16:30:55+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:7d3f9f10326c4127320f96f4979cf830a36f894754ecb011b979bb9e9963f324
---
## 概述

PhoneTabletTV

此结构体描述下发帧生成命令[HMS\_FG\_Dispatch\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_dispatch_vk)需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](../../../模块/GraphicsAccelerate/_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_vk.h](../../头文件/frame_generation_vk.h/frame__generation__vk_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_ImageInfo\_VK](../FG_ImageInfo_VK/_f_g___image_info___v_k.md) [inputColorInfo](_f_g___dispatch_description___v_k.md#inputcolorinfo) | 真实渲染帧颜色缓冲区图像实例，该图像实例由[HMS\_FG\_CreateImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_createimage_vk)创建，由[HMS\_FG\_DestroyImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_destroyimage_vk)销毁。 |
| [FG\_ImageInfo\_VK](../FG_ImageInfo_VK/_f_g___image_info___v_k.md) [inputDepthStencilInfo](_f_g___dispatch_description___v_k.md#inputdepthstencilinfo) | 真实渲染帧深度模板缓冲区图像实例，该图像实例由[HMS\_FG\_CreateImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_createimage_vk)创建，由[HMS\_FG\_DestroyImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_destroyimage_vk)销毁。 |
| [FG\_ImageInfo\_VK](../FG_ImageInfo_VK/_f_g___image_info___v_k.md) [outputColorInfo](_f_g___dispatch_description___v_k.md#outputcolorinfo) | 预测帧缓冲区图像实例 ，该图像实例由[HMS\_FG\_CreateImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_createimage_vk)创建，由[HMS\_FG\_DestroyImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_destroyimage_vk)销毁。 |
| [FG\_Mat4x4](../FG_Mat4x4/_f_g___mat4x4.md) [viewProj](_f_g___dispatch_description___v_k.md#viewproj) | 真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| [FG\_Mat4x4](../FG_Mat4x4/_f_g___mat4x4.md) [invViewProj](_f_g___dispatch_description___v_k.md#invviewproj) | 真实渲染帧视图投影逆矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| VkCommandBuffer [vkCommandBuffer](_f_g___dispatch_description___v_k.md#vkcommandbuffer) | 用于录入超帧绘制指令的命令缓冲区。 |
| uint8\_t [frameIdx](_f_g___dispatch_description___v_k.md#frameidx) | 当前帧序号，序号计数从0开始。该值必须小于[FG\_ContextDescription\_VK](../FG_ContextDescription_VK/_f_g___context_description___v_k.md)中的framesInFlight，否则会返回错误码FG\_INVALID\_PARAMETER。 |

## 结构体成员变量说明

PhoneTabletTV

### frameIdx

PhoneTabletTV

```
1. uint8_t FG_DispatchDescription_VK::frameIdx
```

**描述**

当前帧序号，序号计数从0开始。该值必须小于[FG\_ContextDescription\_VK](../FG_ContextDescription_VK/_f_g___context_description___v_k.md)中的framesInFlight，否则会返回错误码FG\_INVALID\_PARAMETER。

### inputColorInfo

PhoneTabletTV

```
1. FG_ImageInfo_VK FG_DispatchDescription_VK::inputColorInfo
```

**描述**

真实渲染帧颜色缓冲图像实例，该图像实例由[HMS\_FG\_CreateImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_createimage_vk)创建，由[HMS\_FG\_DestroyImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_destroyimage_vk)销毁。

### inputDepthStencilInfo

PhoneTabletTV

```
1. FG_ImageInfo_VK FG_DispatchDescription_VK::inputDepthStencilInfo
```

**描述**

真实渲染帧深度模板缓冲区图像实例，该图像实例由[HMS\_FG\_CreateImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_createimage_vk)创建，由[HMS\_FG\_DestroyImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_destroyimage_vk)销毁。

### invViewProj

PhoneTabletTV

```
1. FG_Mat4x4 FG_DispatchDescription_VK::invViewProj
```

**描述**

真实渲染帧视图投影逆矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

### outputColorInfo

PhoneTabletTV

```
1. FG_ImageInfo_VK FG_DispatchDescription_VK::outputColorInfo
```

**描述**

预测帧缓冲区图像实例，该图像实例由[HMS\_FG\_CreateImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_createimage_vk)创建，由[HMS\_FG\_DestroyImage\_VK](../../../模块/GraphicsAccelerate/_graphics_accelerate.md#hms_fg_destroyimage_vk)销毁。

### viewProj

PhoneTabletTV

```
1. FG_Mat4x4 FG_DispatchDescription_VK::viewProj
```

**描述**

真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

### vkCommandBuffer

PhoneTabletTV

```
1. VkCommandBuffer FG_DispatchDescription_VK::vkCommandBuffer
```

**描述**

用于录入超帧绘制指令的命令缓冲区。
