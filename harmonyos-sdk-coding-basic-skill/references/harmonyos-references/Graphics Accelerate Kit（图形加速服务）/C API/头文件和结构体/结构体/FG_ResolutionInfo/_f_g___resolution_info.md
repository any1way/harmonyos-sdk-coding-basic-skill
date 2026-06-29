---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___resolution_info
title: FG_ResolutionInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_ResolutionInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:30:59+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:091344fb730468b8ecd5e0e373dca92d276b041a2cb9336f51ca47678a04451c
---
## 概述

PhoneTabletTV

此结构体描述超帧输入输出图像的分辨率。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](../../../模块/GraphicsAccelerate/_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_base.h](../../头文件/frame_generation_base.h/frame__generation__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_Dimension2D](../FG_Dimension2D/_f_g___dimension2_d.md) [inputColorResolution](_f_g___resolution_info.md#inputcolorresolution) | 真实渲染帧颜色缓冲区分辨率。 |
| [FG\_Dimension2D](../FG_Dimension2D/_f_g___dimension2_d.md) [inputDepthStencilResolution](_f_g___resolution_info.md#inputdepthstencilresolution) | 真实渲染帧深度模板缓冲区分辨率。当设置成0时，系统中会默认使用[inputColorResolution](_f_g___resolution_info.md#inputcolorresolution)作为真实帧深度模板缓冲区分辨率。 |
| [FG\_Dimension2D](../FG_Dimension2D/_f_g___dimension2_d.md) [outputColorResolution](_f_g___resolution_info.md#outputcolorresolution) | 预测帧缓冲区分辨率。当设置成0时，系统中会默认使用[inputColorResolution](_f_g___resolution_info.md#inputcolorresolution)作为预测帧缓冲区分辨率。 |

## 结构体成员变量说明

PhoneTabletTV

### inputColorResolution

PhoneTabletTV

```
1. FG_Dimension2D FG_ResolutionInfo::inputColorResolution
```

**描述**

真实渲染帧颜色缓冲区分辨率。

### inputDepthStencilResolution

PhoneTabletTV

```
1. FG_Dimension2D FG_ResolutionInfo::inputDepthStencilResolution
```

**描述**

真实渲染帧深度模板缓冲区分辨率。当设置成0时，系统中会默认使用[inputColorResolution](_f_g___resolution_info.md#inputcolorresolution)作为真实帧深度模板缓冲区分辨率。

### outputColorResolution

PhoneTabletTV

```
1. FG_Dimension2D FG_ResolutionInfo::outputColorResolution
```

**描述**

预测帧缓冲区分辨率。当设置成0时，系统中会默认使用[inputColorResolution](_f_g___resolution_info.md#inputcolorresolution)作为预测帧缓冲区分辨率。
