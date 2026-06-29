---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rotationoptions
title: ArkUI_RotationOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_RotationOptions
category: harmonyos-references
scraped_at: 2026-06-01T15:51:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7de18379f0d5bdfb7a19636b16c739d4b94c313f37df5ee69df0216d7a65afd7
---
```
1. typedef struct {...} ArkUI_RotationOptions
```

## 概述

PhonePC/2in1TabletTVWearable

定义组件转场时的旋转效果对象。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](../../头文件/native_type.h/capi-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| float x | 横向的旋转向量分量。 |
| float y | 纵向的旋转向量分量。 |
| float z | 竖向的旋转向量分量。 |
| float angle | 旋转角度。取值范围：(-∞, +∞)。取值为正时相对于旋转轴方向顺时针转动，取值为负时相对于旋转轴方向逆时针转动。 |
| float centerX | 变换中心点x轴坐标，单位为vp。 |
| float centerY | 变换中心点y轴坐标，单位为vp。 |
| float centerZ | z轴锚点，即3D旋转中心点的z轴分量，单位为px。 |
| float perspective | 视距，即视点到z=0平面的距离，单位为px。 |
