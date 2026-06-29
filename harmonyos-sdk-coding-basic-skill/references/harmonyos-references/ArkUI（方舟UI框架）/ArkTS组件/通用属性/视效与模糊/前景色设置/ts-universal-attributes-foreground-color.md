---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color
title: 前景色设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 前景色设置
category: harmonyos-references
scraped_at: 2026-06-11T15:44:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8c5420b244e58680a210f625f0bbb2d19506471ffb37115607033969c9669e13
---
设置组件的前景色。与背景色相对应，前景色会影响绘制组件内容的颜色。主要影响文字的颜色、形状绘制组件的填充色。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## foregroundColor

PhonePC/2in1TabletTVWearable

foregroundColor(value: ResourceColor | ColoringStrategy): T

设置组件的前景色。当组件未设置前景色，默认继承父组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../../公共定义/基础类型定义/ts-types.md#resourcecolor) | [ColoringStrategy](../../../公共定义/枚举说明/ts-appendix-enums.md#coloringstrategy10) | 是 | 设置组件的前景颜色或者根据智能取色策略设置前景颜色。不支持[属性动画](<../../../动画/属性动画 (animation)/ts-animatorproperty.md>)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## foregroundColor18+

PhonePC/2in1TabletTVWearable

foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T

设置组件的前景色。当组件未设置前景色，默认继承父组件。与[foregroundColor](ts-universal-attributes-foreground-color.md#foregroundcolor)相比，color参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](../../动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](../../../公共定义/基础类型定义/ts-types.md#resourcecolor) | [ColoringStrategy](../../../公共定义/枚举说明/ts-appendix-enums.md#coloringstrategy10)> | 是 | 设置组件的前景颜色或者根据智能取色策略设置前景颜色。不支持属性动画。  当color的值为undefined时，维持之前取值或组件默认取值，具体行为不同组件可能会有差异，建议开发者使用确定颜色或[ColoringStrategy](../../../公共定义/枚举说明/ts-appendix-enums.md#coloringstrategy10)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用前景色设置）

该示例主要演示通过foregroundColor设置前景色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ForegroundColorExample {
5. build() {
6. Column({ space: 100 }) {
7. // 绘制一个直径为150的圆，默认填充色为黑色
8. Circle({ width: 150, height: 200 }).margin(20)
9. // 绘制一个直径为150的圆，设置前景色为橙色
10. Circle({ width: 150, height: 200 }).foregroundColor(Color.Orange)
11. }.width('100%').backgroundColor(Color.Gray)
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/fx9ME0A3SOCASbmJgjHZWA/zh-cn_image_0000002622699545.png?HW-CC-KV=V1&HW-CC-Date=20260611T074433Z&HW-CC-Expire=86400&HW-CC-Sign=08E42406ECB17CCD22EDD1FB234CA55409F56F2C269E8B554B62C01BC5B4B329)

### 示例2（设置前景色为组件背景色反色）

该示例通过[ColoringStrategy](../../../公共定义/枚举说明/ts-appendix-enums.md#coloringstrategy10).INVERT将前景色设置为背景色反色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ColoringStrategyExample {
5. build() {
6. Column({ space: 100 }) {
7. // 绘制一个直径为150的圆,默认填充色为黑色
8. Circle({ width: 150, height: 200 })
9. // 绘制一个直径为150的圆，设置前景色为组件背景色的反色
10. Circle({ width: 150, height: 200 })
11. .backgroundColor(Color.Black)
12. .foregroundColor(ColoringStrategy.INVERT)
13. }.width('100%')
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/fga5hjCrRai2gxmG7KThaw/zh-cn_image_0000002592219984.png?HW-CC-KV=V1&HW-CC-Date=20260611T074433Z&HW-CC-Expire=86400&HW-CC-Sign=EF55741A83203B884B131A44E1C1EC8F3B4F605159780F3474DC925A03B7F973)

### 示例3（前景色未继承父组件）

该示例主要演示组件同时设置前景色和背景色与只设置背景色的效果对比。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ForegroundColorInherit {
5. build() {
6. Column() {
7. Button('设置前景色为橘色').fontSize(20).foregroundColor(Color.Orange).backgroundColor(Color.Gray)
8. Divider()
9. Button('未设置前景色继承自父组件').fontSize(20).backgroundColor(Color.Gray)
10. }.foregroundColor(Color.Pink)
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/lz8umDNHSe-kfA4LCrmHDA/zh-cn_image_0000002592379918.png?HW-CC-KV=V1&HW-CC-Date=20260611T074433Z&HW-CC-Expire=86400&HW-CC-Sign=7E49DDEB799EAD457B4914F0255EFFB16215962DA32AFC6DC4DE6458F685B543)
