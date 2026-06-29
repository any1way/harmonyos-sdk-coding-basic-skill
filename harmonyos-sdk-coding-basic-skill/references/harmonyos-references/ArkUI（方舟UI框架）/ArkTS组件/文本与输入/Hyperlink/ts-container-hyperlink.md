---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink
title: Hyperlink
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > Hyperlink
category: harmonyos-references
scraped_at: 2026-06-11T15:47:34+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:75aa0260672907a8c017070052f6782e16f556f1a69c8cc10016abe6509e1322
---
超链接组件，组件宽高范围内点击实现跳转。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅支持与系统浏览器配合使用。

## 需要权限

PhonePC/2in1TabletTVWearable

跳转的目标应用使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含[Image](../../图片与视频/Image/ts-basic-components-image.md)子组件。

## 接口

PhonePC/2in1TabletTVWearable

Hyperlink(address: string | Resource, content?: string | Resource)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 是 | Hyperlink组件跳转的网页。 |
| content | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | Hyperlink组件中超链接显示文本。  默认值：''。若不传该参数且组件内无子组件时，默认显示address参数值链接地址。  **说明：**  组件内有子组件时，不显示超链接文本。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](../../通用属性/ts-component-general-attributes.md)外，还支持以下属性：

### color

PhonePC/2in1TabletTVWearable

color(value: Color | number | string | Resource)

设置超链接文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Color](../../公共定义/枚举说明/ts-appendix-enums.md#color) | number | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 是 | 超链接文本的颜色。  phone默认值为'#ff007dff'，wearable设备默认值'#1F71FF'，tv设备默认值为'#266EFB'，均显示为蓝色。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例展示了超链接图片和文本跳转的效果。

```
1. @Entry
2. @Component
3. struct HyperlinkExample {
4. build() {
5. Column() {
6. Column() {
7. Hyperlink('https://example.com/') {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. .width(200)
11. .height(100)
12. }
13. }

15. Column() {
16. Hyperlink('https://example.com/', 'Go to the developer website') {
17. }
18. .color(Color.Blue)
19. }
20. }.width('100%').height('100%').justifyContent(FlexAlign.Center)
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ORRBQiHfTO-l2gdTkbvJXQ/zh-cn_image_0000002592380220.png?HW-CC-KV=V1&HW-CC-Date=20260611T074733Z&HW-CC-Expire=86400&HW-CC-Sign=01D94EF7788AD48B1EE07710A798945F28691D4B28DD1D61F65FE1FAACAAF233)
