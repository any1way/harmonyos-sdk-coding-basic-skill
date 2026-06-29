---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_sync___v_k
title: FG_ImageSync_VK
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_ImageSync_VK
category: harmonyos-references
scraped_at: 2026-06-01T16:30:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ba6789e5a69e39ce096a3d9fa857041af53953cc872bbfc961d3480a8de9fcd
---
## 概述

PhoneTabletTV

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](../../../模块/GraphicsAccelerate/_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_vk.h](../../头文件/frame_generation_vk.h/frame__generation__vk_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| VkAccessFlagBits [accessMask](_f_g___image_sync___v_k.md#accessmask) | 内存访问类型的位掩码。 |
| VkImageLayout [layout](_f_g___image_sync___v_k.md#layout) | 图像和图像子资源的内存布局。 |
| VkPipelineStageFlagBits [stages](_f_g___image_sync___v_k.md#stages) | 管线阶段的位掩码。 |

## 结构体成员变量说明

PhoneTabletTV

### accessMask

PhoneTabletTV

```
1. VkAccessFlagBits FG_ImageSync_VK::accessMask
```

**描述**

内存访问类型的位掩码。

### layout

PhoneTabletTV

```
1. VkImageLayout FG_ImageSync_VK::layout
```

**描述**

图像和图像子资源的内存布局。

### stages

PhoneTabletTV

```
1. VkPipelineStageFlagBits FG_ImageSync_VK::stages
```

**描述**

管线阶段的位掩码。
