---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-scaleanimation
title: Class (ScaleAnimation)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (ScaleAnimation)
category: harmonyos-references
scraped_at: 2026-06-01T16:35:52+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:83985512f875452015369f54d5293a8bd40c1dca729f97f4d4db215f9f3dca54
---
## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## ScaleAnimation

PhonePC/2in1TabletWearable

控制缩放的动画类，继承[Animation](<../Class (Animation)/map-map-animation.md>)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

PhonePC/2in1TabletWearable

constructor(fromX: number, toX: number, fromY: number, toY: number)

构造器，构造控制缩放的动画实例。

说明

0表示动画缩小消失。

1表示动画不缩放。

小于1的值表示动画缩小。

大于1的值表示动画放大。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromX | number | 是 | 指动画开始时应用的水平缩放倍数，负数按0处理，异常值不处理。 |
| toX | number | 是 | 指动画结束时应用的水平缩放倍数，负数按0处理，异常值不处理。 |
| fromY | number | 是 | 指动画开始时应用的垂直缩放倍数，负数按0处理，异常值不处理。 |
| toY | number | 是 | 指动画结束时应用的垂直缩放倍数，负数按0处理，异常值不处理。 |

**示例：**

```
1. let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
```
