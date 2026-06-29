---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-fontsizeanimation
title: Class (FontSizeAnimation)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (FontSizeAnimation)
category: harmonyos-references
scraped_at: 2026-06-01T16:35:54+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:064ba7e4ad9f88b2942ce782f399e3bb498b59e6cfb1f66107fc2daa91618e5e
---
## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## FontSizeAnimation

PhonePC/2in1TabletWearable

控制字体大小的动画类，继承[Animation](<../Class (Animation)/map-map-animation.md>)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

PhonePC/2in1TabletWearable

constructor(fromSize: number, toSize: number)

创建一个控制字体大小的动画实例，通过指定起始字体大小和目标字体大小来初始化该动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromSize | number | 是 | 起始的字体大小。取值范围：[0，100]，单位：px，异常值不处理。 |
| toSize | number | 是 | 目标的字体大小。取值范围：[0，100]，单位：px，异常值不处理。 |

**示例：**

```
1. let animation: map.FontSizeAnimation = new map.FontSizeAnimation(5, 25);
```
