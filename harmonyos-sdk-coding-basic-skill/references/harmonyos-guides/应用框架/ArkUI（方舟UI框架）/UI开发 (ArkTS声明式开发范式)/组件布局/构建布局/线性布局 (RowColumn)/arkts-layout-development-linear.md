---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-06-11T14:30:16+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:3f357a8c62f19b244dc89c4db2a7753f08e014fc37a837424c44688ebffb907a
---
## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md)和[Column](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

说明

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](../../../../../../../best-practices/布局与弹窗/布局优化指导/bpta-improve-layout-performance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/hxmNNBxmS7iukbL6nvIBGg/zh-cn_image_0000002622857525.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=89FD9C8905E2109B88328D38B809BDD1E1C26273F74B54A8D5FC991EBAD0E16B)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/5El7OIfiQm-c6YCKLzmSwQ/zh-cn_image_0000002622697647.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=E376487DA7721D900316F597081B066302EC19E3B8451AC7F20E86440F59C444)

## 基本概念

* 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
* 布局子元素：布局容器内部的元素。
* 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](<../弹性布局 (Flex)/arkts-layout-development-flex-layout.md#基本概念>)中的主轴）。
* 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](<../弹性布局 (Flex)/arkts-layout-development-flex-layout.md#基本概念>)中的交叉轴）。
* 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过[Row](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md)组件的[space](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md#rowoptions18对象说明)属性或[Column](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md)组件的[space](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md#columnoptions18对象说明)属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Pd6FugKxQEW4j-AaLM-5jg/zh-cn_image_0000002592218086.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=367AC61B1A4B67317FB794A97D1C1BF023AA636F645F09590857FFAE4D33668B)

```
1. Column({ space: 20 }) {
2. Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
3. Row().width('90%').height(50).backgroundColor(0xF5DEB3)
4. Row().width('90%').height(50).backgroundColor(0xD2B48C)
5. Row().width('90%').height(50).backgroundColor(0xF5DEB3)
6. }.width('100%')
```

[ColumnLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutExample.ets#L20-L27)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/_PBXdwl7QhCOM7fbHSfzIw/zh-cn_image_0000002592378020.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=2DF00A8234A11D85E3614DBB41B5093A37EB061A5498F8D42EEB847F01CD6CEA)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/teMjpJWJQMedVQq6PQ2Quw/zh-cn_image_0000002622857527.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=5C3DF1E2966FF163B09E4021D44E0E872624BE9B97CD9589C3A364FDC410F21F)

```
1. Row({ space: 35 }) {
2. Text('space: 35').fontSize(15).fontColor(Color.Gray)
3. Row().width('10%').height(150).backgroundColor(0xF5DEB3)
4. Row().width('10%').height(150).backgroundColor(0xD2B48C)
5. Row().width('10%').height(150).backgroundColor(0xF5DEB3)
6. }.width('90%')
```

[RowLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutExample.ets#L20-L27)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/NlJoRPF4RK2YF0yGBK7WOw/zh-cn_image_0000002622697649.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=59FF4D95522C840D2BF241BBFA8ACE4659D56A253F2F735578491AA0C6B661CB)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Zq0yy2zQRFOtDNc5mqwQdA/zh-cn_image_0000002592218088.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=48D7F58EB9767DEDC7D03506B465EF56A66D4E9FF6BDBD70DE10EBD7ABAF9991)

* justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
  ```

  [ColumnLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentStart.ets#L20-L66)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/F3xOkAEgQ76CgmQ5Jd93eQ/zh-cn_image_0000002592378022.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=5D1B73B63030733A9F87EC0FF8643BF615F5A7769CCB4B6AA74CC0DED6686B51)
* justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
  ```

  [ColumnLayoutJustifyContentCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/xSB6qA6hSe-pxWszMNoUxg/zh-cn_image_0000002622857529.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=168F6A8B600381F52547703FBDEBD95E434CF0E85F844A75895EE17ECAAC193C)
* justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
  ```

  [ColumnLayoutJustifyContentEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/_00V3Bz-R2uvFJ-iBhuv2g/zh-cn_image_0000002622697651.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=3139FC1ABA13AAD2E7B4976194155C08E8C9CAA0EBF99C8980BDE8D386452B7B)
* justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
  ```

  [ColumnLayoutJustifyContentSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceBetween.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/H0voP7-1R6S9Vh2TgSMNRA/zh-cn_image_0000002592218090.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=6FA5F16BCC547F503C9B3EE6477678C8574F61D3D25D720495AFAE74A02B20F9)
* justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
  ```

  [ColumnLayoutJustifyContentSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceAround.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qKIP-DtxTfysv9oonplBZQ/zh-cn_image_0000002592378024.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=271B91767B5549DDC5B6F5A27C49887D76A21047D6D94905F87855E26400DB4A)
* justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
  ```

  [ColumnLayoutJustifyContentSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceEvenly.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3wo8jXoXSG6xQGP_6N01VQ/zh-cn_image_0000002622857531.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=E8F52A7CB5306F5143B91D52170CABCC1A36191CF02B65F3E42FC94892172314)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/LTrBbe9zQh6kgyu6MHtYmg/zh-cn_image_0000002622697653.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=3CDE2B2C89560EC6967A2427A7B0A5F15DE9AC064B7035E183272C37ECA06628)

* justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
  ```

  [RowLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentStart.ets#L20-L22)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/828uC8asTpGBsU9NJWPneQ/zh-cn_image_0000002592218092.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=371B0822992066756F2CC4553B3C007A96F8E337F6F43BFC6035DEB927EDD1F5)
* justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
  ```

  [RowLayoutJustifyContentCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/z73WZGoQRYmgyktB8tsF2w/zh-cn_image_0000002592378026.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=DA08E5AE23CC35D9AB54703089FEF4025876D1BCF5598EDB77D47C25DF71DE18)
* justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
  ```

  [RowLayoutJustifyContentEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/vwREcTQIRtClgFDhSaVLcA/zh-cn_image_0000002622857533.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=936BDCE8CE0E31B6A4C254A5A63DABD2A3053B0EA94064FB93A377C093A9C46D)
* justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
  ```

  [RowLayoutJustifyContentSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceBetween.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/MArjlxP5TeShed1KhYJoBA/zh-cn_image_0000002622697655.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=5F86C98FDE158B2505EF1F6019284C6817BAD5C1469F41ADA4F7982C8717232A)
* justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
  ```

  [RowLayoutJustifyContentSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceAround.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/pSHcItPjQziZKbTm8Be6yA/zh-cn_image_0000002592218094.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=BB6B92C47763F8A9BDDA5605BC8C02C3BB903FC20DDD234BED2C883303ADEC3E)
* justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
  ```

  [RowLayoutJustifyContentSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceEvenly.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/PLRZht_JQ16KQLKf4KQS8A/zh-cn_image_0000002592378028.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=D69E94613C09B2262B3D2CCBA7C142FC84B2853D9480B284FA77131A8FB1E7EE)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/Flex布局/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/fDFf_EX3QSmOLMIsMvB_LA/zh-cn_image_0000002622857535.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=4DF6479DBAC5B3907B72960C9CF7D05A78CE3B66F0BFCC075AA537CC69B9812E)

* HorizontalAlign.Start：子元素在水平方向左对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutHorizontalAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignStart.ets#L20-L120)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/mPHpudDCRfG0zeNHH70sxg/zh-cn_image_0000002622697657.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=638B0A0D9D8635C5FB855899C495471616F5A051C5D765DEEA523532F8F5F8EB)
* HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutHorizontalAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/JGDee2wpRVqFElgZRL-Z1w/zh-cn_image_0000002592218096.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=2A882927B133CDDCBD2EE690657AFB50EF49FD57B3C5F3A3496134F2BE0FC9BC)
* HorizontalAlign.End：子元素在水平方向右对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutHorizontalAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/de6sUuETREuhtc-atkRlVg/zh-cn_image_0000002592378030.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=2CFB25F0D6A74D47C29EC034BBFC957749DE03536F899DA32D481E6BCDE9EAE8)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/vrnXzg0rQKGKO8YEcZNaJA/zh-cn_image_0000002622857537.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=07000C07B73B5F195CADFB9E58C63121A702AAEAFA19C1F39C1AD12F4F7C4F01)

* VerticalAlign.Top：子元素在垂直方向顶部对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutVerticalAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignTop.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/1UjL9Q5UTUu0D6yJkm84sQ/zh-cn_image_0000002622697659.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=0596F03FCB83C9B082C28D2F808D076E62AF130EA6DFAB974703F68F56941514)
* VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutVerticalAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/UwUAyMsISbaOs9cjkRPG8Q/zh-cn_image_0000002592218098.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=85DF65277EA6507CEB29DC71C2511BCDD3244BACA5B9DF1C79E7EF375478C5CB)
* VerticalAlign.Bottom：子元素在垂直方向底部对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutVerticalAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignBottom.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/lr9lL0VUQO-foAf1unv6ow/zh-cn_image_0000002592378032.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=4C53A7C23496A50457145EF419639C430F74D1E971972924CBEDA7E8EF556A1A)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/空白与分隔/Blank/ts-basic-components-blank.md)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

```
1. @Entry
2. @Component
3. struct BlankExample {
4. build() {
5. Column() {
6. Row() {
7. Text('Bluetooth').fontSize(18)
8. Blank()
9. Toggle({ type: ToggleType.Switch, isOn: true })
10. }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
11. }.backgroundColor(0xEFEFEF).padding(20).width('100%')
12. }
13. }
```

[BlankExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/BlankExample.ets#L15-L29)

**图9** 竖屏（自适应屏幕窄边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/79aBDTAFQSq01KhLpv1D9g/zh-cn_image_0000002622857539.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=D33CB23D2D4F5DD5A9348AE568498D2C564C4561569C7A72E6226C7542011783)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/hZu1Gx6sR7qKRalKSVa-mg/zh-cn_image_0000002622697661.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=5F0E78B4432A23301FF83A4D2F95411BA01F6D0FC0214104EC33ED72EE668302)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

* 父容器尺寸确定时，使用[layoutWeight](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

  ```
  1. @Entry
  2. @Component
  3. struct LayoutWeightExample {
  4. build() {
  5. Column() {
  6. Text('1:2:3').width('100%')
  7. Row() {
  8. Column() {
  9. Text('layoutWeight(1)')
  10. .textAlign(TextAlign.Center)
  11. }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')

  13. Column() {
  14. Text('layoutWeight(2)')
  15. .textAlign(TextAlign.Center)
  16. }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')

  18. Column() {
  19. Text('layoutWeight(3)')
  20. .textAlign(TextAlign.Center)
  21. }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')

  23. }.backgroundColor(0xffd306).height('30%')

  25. Text('2:5:3').width('100%')
  26. Row() {
  27. Column() {
  28. Text('layoutWeight(2)')
  29. .textAlign(TextAlign.Center)
  30. }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')

  32. Column() {
  33. Text('layoutWeight(5)')
  34. .textAlign(TextAlign.Center)
  35. }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')

  37. Column() {
  38. Text('layoutWeight(3)')
  39. .textAlign(TextAlign.Center)
  40. }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
  41. }.backgroundColor(0xffd306).height('30%')
  42. }
  43. }
  44. }
  ```

  [LayoutWeightExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/LayoutWeightExample.ets#L15-L60)

  **图11** 横屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/iA0MO9mARtKIt5BZC8Uyng/zh-cn_image_0000002592218100.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=696891A5C8004F9A9D5CDF4F067E676CCBA3DDE23266068B748003BD224FE67F)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/gqZKkTBXSzu522qno1OYWQ/zh-cn_image_0000002592378034.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=9BD331A7D37538B883014DB71BA47579220A9D8403B212E469FE477935317F8D)
* 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

  ```
  1. @Entry
  2. @Component
  3. struct WidthExample {
  4. build() {
  5. Column() {
  6. Row() {
  7. Column() {
  8. Text('left width 20%')
  9. .textAlign(TextAlign.Center)
  10. }.width('20%').backgroundColor(0xF5DEB3).height('100%')

  12. Column() {
  13. Text('center width 50%')
  14. .textAlign(TextAlign.Center)
  15. }.width('50%').backgroundColor(0xD2B48C).height('100%')

  17. Column() {
  18. Text('right width 30%')
  19. .textAlign(TextAlign.Center)
  20. }.width('30%').backgroundColor(0xF5DEB3).height('100%')
  21. }.backgroundColor(0xffd306).height('30%')
  22. }
  23. }
  24. }
  ```

  [WidthExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/WidthExample.ets#L15-L40)

  **图13** 横屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/UeJ21FOZR7aMX3IoeSEZDg/zh-cn_image_0000002622857541.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=0430859EFD282383A1458AB259629F02040D0735528B45641F70CAE816437AE9)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/DN1RTBsvSMyu_0WG-5yQJg/zh-cn_image_0000002622697663.png?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=9E49612451E59CABD7F5976962B7C7EBB7B233CA441531CC09C81E6307875EDC)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

* [在List中添加滚动条](<../../../列表与网格/创建列表 (List)/arkts-layout-development-create-list.md#添加滚动条>)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md#edgeeffect)属性设置拖动到内容最末端的回弹效果。
* 使用[Scroll](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。

  垂直方向布局中使用Scroll组件：

  ```
  1. @Entry
  2. @Component
  3. struct ScrollVerticalExample {
  4. scroller: Scroller = new Scroller();
  5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  7. build() {
  8. Scroll(this.scroller) {
  9. Column() {
  10. ForEach(this.arr, (item?:number|undefined) => {
  11. if(item != undefined){
  12. Text(item.toString())
  13. .width('90%')
  14. .height(150)
  15. .backgroundColor(0xFFFFFF)
  16. .borderRadius(15)
  17. .fontSize(16)
  18. .textAlign(TextAlign.Center)
  19. .margin({ top: 10 })
  20. }
  21. }, (item:number) => item.toString())
  22. }.width('100%')
  23. }
  24. .backgroundColor(0xDCDCDC)
  25. .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
  26. .scrollBar(BarState.On) // 滚动条常驻显示
  27. .scrollBarColor(Color.Gray) // 滚动条颜色
  28. .scrollBarWidth(10) // 滚动条宽度
  29. .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  30. }
  31. }
  ```

  [ScrollVerticalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ScrollVerticalExample.ets#L15-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/FsEM8oRVR8SjNo1sEtFS3g/zh-cn_image_0000002592218102.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=E71CECEB71258B276B0A043D3AFCA8CF74ECED74163DDE7149354FE7C965D768)

  水平方向布局中使用Scroll组件：

  ```
  1. @Entry
  2. @Component
  3. struct ScrollHorizontalExample {
  4. scroller: Scroller = new Scroller();
  5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  7. build() {
  8. Scroll(this.scroller) {
  9. Row() {
  10. ForEach(this.arr, (item?:number|undefined) => {
  11. if(item != undefined){
  12. Text(item.toString())
  13. .height('90%')
  14. .width(150)
  15. .backgroundColor(0xFFFFFF)
  16. .borderRadius(15)
  17. .fontSize(16)
  18. .textAlign(TextAlign.Center)
  19. .margin({ left: 10 })
  20. }
  21. })
  22. }.height('100%')
  23. }
  24. .backgroundColor(0xDCDCDC)
  25. .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
  26. .scrollBar(BarState.On) // 滚动条常驻显示
  27. .scrollBarColor(Color.Gray) // 滚动条颜色
  28. .scrollBarWidth(10) // 滚动条宽度
  29. .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  30. }
  31. }
  ```

  [ScrollHorizontalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ScrollHorizontalExample.ets#L15-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/G4098LYbQoqbunpvsexh1Q/zh-cn_image_0000002592378036.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063014Z&HW-CC-Expire=86400&HW-CC-Sign=5302E4A41BF9E14D087BA697AB531BEA31A00F5F7FE760EAA654D69267250725)
