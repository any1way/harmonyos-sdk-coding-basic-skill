---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout
title: 弹性布局 (Flex)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 弹性布局 (Flex)
category: harmonyos-guides
scraped_at: 2026-06-11T14:30:20+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:cb4b0a592065f0bfaab2ed5f1f3310d4a5bd2788fc2f96ea052a34d9fe0deef0
---
## 概述

弹性布局（[Flex](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/0tC0JNGrSUyK7f-aAd6TMw/zh-cn_image_0000002592218106.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=587DB2FE541422FBC951D3C2A59C892BFD1FE4B3164EA3049F05CC5D78689668)

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/TyOqz4sBRHmacN-QLEDb4A/zh-cn_image_0000002592378040.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=A75D98CADDE553A7B96BAE806123D8BB14D96F0EBD69E35B85203F448FDACF3C)

* FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.Row }) {
  2. Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionRow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionRow.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/X7zff3vITWmLdvgLOOHazA/zh-cn_image_0000002622857547.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=450A8206266100854F67F88EB0A1B214C7D0BEA3E2C30B20E693FD1266BDB5D1)
* FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.RowReverse }) {
  2. Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionRowReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionRowReverse.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/PE6qXsJJT6edRf977ftOJQ/zh-cn_image_0000002622697669.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=4EEDE2511401DC25292DFD00665A37207DE9E5E69B83578C27FCD51896655904)
* FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.Column }) {
  2. Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('100%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionColumn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionColumn.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/8Lsd5J3NQZOVcccfJOgbyQ/zh-cn_image_0000002592218108.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=7C3A81D2FC4C51D554692CB6E9BC0811E009CFE79A3E9B10AC7EC533DA3A0E5F)
* FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.ColumnReverse }) {
  2. Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('100%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionColumnReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionColumnReverse.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/rX8K21_-S6yHBikp3-gvRw/zh-cn_image_0000002592378042.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=AB2D25E7AAB599DCE1A90B595902B33999B4A64FF40259A3F7911FC6781D0E9D)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

* FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。

  ```
  1. Flex({ wrap: FlexWrap.NoWrap }) {
  2. Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('50%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexWrapNoWrap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapNoWrap.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/gCHUW-tXSM6k642tuhIjmw/zh-cn_image_0000002622857549.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=F5738654AA1C07A0454B45B4214FEEBB6D3ED890056801332222F9E11052C51C)
* FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。

  ```
  1. Flex({ wrap: FlexWrap.Wrap }) {
  2. Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('50%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('50%').height(50).backgroundColor('#D2B48C')
  5. }
  6. .width('90%')
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexWrapWrap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapWrap.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Y_160RNNQ16VBhbe4VUppw/zh-cn_image_0000002622697671.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=DD750A62B1DFA49693D7898D85E721F99A271D8CD7FA94B29ABB905E2B45FC2C)
* FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。

  ```
  1. Flex({ wrap: FlexWrap.WrapReverse}) {
  2. Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('50%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexWrapWrapReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapWrapReverse.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/mgyZhO9VSiqbJioBcAkqjw/zh-cn_image_0000002592218110.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=38CC1B89AB11BFCAD980B2DE1137F67D5A9E60166C3B646A947F0AD858B11161)

## 主轴对齐方式

通过[justifyContent](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md#flexoptions对象说明)参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/h5xeZNE5Rv-h6voPKsDhGQ/zh-cn_image_0000002592378044.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=427A50299823D5E7BDEB1AC1E5303FE09803AB3714770EBA373700ADCFF6F6D5)

* FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.Start }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignStart.ets#L20-L122)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/dAoS9wyoQCOS7r96bny5wA/zh-cn_image_0000002622857551.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=319782B95D3CF651300C2C8A709407C84EB8065B849C5C7A311CC46B36FBD35D)
* FlexAlign.Center：子元素在主轴方向居中对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.Center }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenter.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/oSj4iqf4Tm6Mr1LvpYSEIw/zh-cn_image_0000002622697673.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=804886AB866CE404F20085905BD1927944FE37F7058DCDCBE5BDBF3DECB30AA3)
* FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.End }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignEnd.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/mRyKdGcvTBeyPYPtFIJTsg/zh-cn_image_0000002592218112.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=B7450D8C2BC2814E9308E9D80F7F00D8E4F484587F28630C88DBE622DA5231A6)
* FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceBetween.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/bQLBI5ZjQ5a3x8aOig_VZw/zh-cn_image_0000002592378046.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=83EF20320700BF47B2CF0620DF43D275DDF3F50343468CB3F05D2B15EA428B0B)
* FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceAround }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceAround.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/DPpwFFu6SAeWTb5tSSi2_A/zh-cn_image_0000002622857553.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=FE0450C67E0C38DF7442738D2B87F8B32D32912D1488FC2BB51047E288E24CD8)
* FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceEvenly.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/UmsAR-UiQvS32Ku7Kg95YA/zh-cn_image_0000002622697675.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=C52CE1942EEE161D195147C2550175C79F1F02A5E50250BB01B62074BAE13756)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

* ItemAlign.Auto：使用Flex容器中默认配置。

  ```
  1. Flex({ alignItems: ItemAlign.Auto }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignAuto.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignAuto.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/72JJe7gQTrmIHeKivLxSQA/zh-cn_image_0000002592218114.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=421598074B6FDA81CB4F8E7ADB6802364DF3B70F63EF99841526319320ECF73A)
* ItemAlign.Start：交叉轴方向首部对齐。

  ```
  1. Flex({ alignItems: ItemAlign.Start }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStart.ets#L20-L103)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/qdrK2iLJRZi-oXn9ifj8lg/zh-cn_image_0000002592378048.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=E9428927479DC83BCAB40CF25CA616F3EE91C174A527BB1104CA89381B18497E)
* ItemAlign.Center：交叉轴方向居中对齐。

  ```
  1. Flex({ alignItems: ItemAlign.Center }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignCenter.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/GslOhwmTSRiKKk12mTPr-g/zh-cn_image_0000002622857555.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=5F9FEFCA6B3AE23A08FB55AC07B18F513656080354D9561E29E118C2C8A9E656)
* ItemAlign.End：交叉轴方向底部对齐。

  ```
  1. Flex({ alignItems: ItemAlign.End }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignEnd.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/h4WiCfr5RI6L_7yrY4rZ9A/zh-cn_image_0000002622697677.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=895C81873FB41383767D696CDE6F4BE9B7F62A51793C15D5C6205FCED1F0F412)
* ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。

  ```
  1. Flex({ alignItems: ItemAlign.Stretch }) {
  2. Text('1').width('33%').backgroundColor('#F5DEB3')
  3. Text('2').width('33%').backgroundColor('#D2B48C')
  4. Text('3').width('33%').backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignStretch.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStretch.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/fuEI41oAQlK4MTRx1XTfOg/zh-cn_image_0000002592218116.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=9866B994023D84EAAD3AD3EF573B3A00DB1D528CE83A71A135B0492B7B617E1D)
* ItemAlign.Baseline：交叉轴方向文本基线对齐。

  ```
  1. Flex({ alignItems: ItemAlign.Baseline }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignBaseline.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignBaseline.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/VmKWB90fT0SMXnYhFPVWBQ/zh-cn_image_0000002592378050.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=56EC69DA1823AAD975073FA6E477A0FF0ABB4110EBF7C0F4BAAD449195F1E820)

### 子元素设置交叉轴对齐

子元素的[alignSelf](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/Flex布局/ts-universal-attributes-flex-layout.md#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

```
1. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) { // 容器组件设置子元素居中
2. Text('alignSelf Start').width('25%').height(80)
3. .alignSelf(ItemAlign.Start)
4. .backgroundColor('#F5DEB3')
5. Text('alignSelf Baseline')
6. .alignSelf(ItemAlign.Baseline)
7. .width('25%')
8. .height(80)
9. .backgroundColor('#D2B48C')
10. Text('alignSelf Baseline').width('25%').height(100)
11. .backgroundColor('#F5DEB3')
12. .alignSelf(ItemAlign.Baseline)
13. Text('no alignSelf').width('25%').height(100)
14. .backgroundColor('#D2B48C')
15. Text('no alignSelf').width('25%').height(100)
16. .backgroundColor('#F5DEB3')

18. }.width('90%').height(220).backgroundColor('#AFEEEE')
```

[FlexAlignSelf.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSelf.ets#L20-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/656yudPHS5KuMJscwv-qLw/zh-cn_image_0000002622857557.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=9B7C27F6559769DF1ECAE22CB987D876FA25874A5382C5E90754005B386161C3)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

* FlexAlign.Start：子元素各行与交叉轴起点对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignStart.ets#L20-L60)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/g6mCCPWZQ2W09syQ7lo-RA/zh-cn_image_0000002622697679.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=B60AAD1342A0918E19FA62B037AABCC99F800D48A0352C575BB4E492956F08E0)
* FlexAlign.Center：子元素各行在交叉轴方向居中对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/6TS0ASf4S-uWAp4tTkUJlw/zh-cn_image_0000002592218118.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=9B03CAFDA345C257444891736E3DCAB55C60832A7DA0BBC4F2E3D5B48D8053BC)
* FlexAlign.End：子元素各行与交叉轴终点对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/QIwZm6pIQQCDna4tsfDB_w/zh-cn_image_0000002592378052.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=DEBF442BC07FA99E45B62922E05A384DA431FB26520DE90017EDE5709B019A40)
* FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceBetween.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/ZwYPrSzYRTODKlCzBQPGzw/zh-cn_image_0000002622857559.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=58391B1BFA005B3590D2C3C2F77444913C44BBA8A4FB12415C48AC0B237B7186)
* FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceAround.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/PoAFIRXGSfSa40JriOCImg/zh-cn_image_0000002622697681.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=EFD95A107BB52FCBCCCD5E22CB5B663DF48978BFBF62F83C1E24836D3F5DB29F)
* FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceEvenly.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/jIvzGJS2R8uvxrikVSRDMw/zh-cn_image_0000002592218120.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=704D07BFA7DDD875C58CC1FA59F80620C5D90C083763AC754BD4C5DC9F500723)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

* [flexBasis](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/Flex布局/ts-universal-attributes-flex-layout.md#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。

  ```
  1. Flex() {
  2. Text('flexBasis("auto")')
  3. .flexBasis('auto')// 未设置width以及flexBasis值为auto，内容自身宽度
  4. .height(100)
  5. .backgroundColor('#F5DEB3')
  6. Text('flexBasis("auto")'+' width("40%")')
  7. .width('40%')
  8. .flexBasis('auto')// 设置width以及flexBasis值auto，使用width的值
  9. .height(100)
  10. .backgroundColor('#D2B48C')

  12. Text('flexBasis(100)') // 未设置width以及flexBasis值为100，宽度为100vp
  13. .flexBasis(100)
  14. .height(100)
  15. .backgroundColor('#F5DEB3')

  17. Text('flexBasis(100)')
  18. .flexBasis(100)
  19. .width(200)// flexBasis值为100，覆盖width的设置值，宽度为100vp
  20. .height(100)
  21. .backgroundColor('#D2B48C')
  22. }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  [FlexBasis.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexBasis.ets#L20-L43)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/s1wo4-RqTQK_QJp0HmQb_w/zh-cn_image_0000002592378054.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=0DBC88FEAC3A8A9E3F1E63A4223A62CD6F37728987C3809E7EF56B9F406A5A8A)
* [flexGrow](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/Flex布局/ts-universal-attributes-flex-layout.md#flexgrow)：设置父容器的剩余空间分配给此属性所在组件的比例，用于分配父组件的剩余空间。

  ```
  1. Flex() {
  2. Text('flexGrow(1)')
  3. .flexGrow(1)
  4. .width(100)
  5. .height(100)
  6. .backgroundColor('#F5DEB3')
  7. Text('flexGrow(4)')
  8. .flexGrow(4)
  9. .width(100)
  10. .height(100)
  11. .backgroundColor('#D2B48C')

  13. Text('no flexGrow')
  14. .width(100)
  15. .height(100)
  16. .backgroundColor('#F5DEB3')
  17. }.width(360).height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  [FlexGrow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexGrow.ets#L20-L38)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/nZ4etoJuQi-rTDFwXKw6xw/zh-cn_image_0000002622857561.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=7692FF13166C58313BF7FE1716A0E3711F8A684F1B219C3E1F09F860A2AF17A0)

  父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

  第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp \* 1/5=108vp，第二个元素为100vp+40vp \* 4/5=132vp。
* [flexShrink](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/Flex布局/ts-universal-attributes-flex-layout.md#flexshrink): 当父容器空间不足时，子元素的压缩比例。

  ```
  1. Flex({ direction: FlexDirection.Row }) {
  2. Text('flexShrink(3)')
  3. .flexShrink(3)
  4. .width(200)
  5. .height(100)
  6. .backgroundColor('#F5DEB3')

  8. Text('no flexShrink')
  9. .width(200)
  10. .height(100)
  11. .backgroundColor('#D2B48C')

  13. Text('flexShrink(2)')
  14. .flexShrink(2)
  15. .width(200)
  16. .height(100)
  17. .backgroundColor('#F5DEB3')
  18. }.width(400).height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  [FlexShrink.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexShrink.ets#L20-L39)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/9IhmZnfCQ7WCSoR-xNSUSw/zh-cn_image_0000002622697683.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=1A2ECB145D2DD7306E7E992DB0990925F0A6C3C0681A377238ADA5BB23058812)

  父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。

  将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) \* 3=68vp，第三个元素为200vp - (220vp / 5) \* 2=112vp。

## 场景示例

使用弹性布局，可以实现子元素沿水平方向排列，两端对齐，子元素间距平分，垂直方向上子元素居中的效果。

```
1. @Entry
2. @Component
3. struct FlexExample {
4. build() {
5. Column() {
6. Column({ space: 5 }) {
7. Flex({
8. direction: FlexDirection.Row,
9. wrap: FlexWrap.NoWrap,
10. justifyContent: FlexAlign.SpaceBetween,
11. alignItems: ItemAlign.Center
12. }) {
13. Text('1').width('30%').height(50).backgroundColor('#F5DEB3')
14. Text('2').width('30%').height(50).backgroundColor('#D2B48C')
15. Text('3').width('30%').height(50).backgroundColor('#F5DEB3')
16. }
17. .height(70)
18. .width('90%')
19. .backgroundColor('#AFEEEE')
20. }.width('100%').margin({ top: 5 })
21. }.width('100%')
22. }
23. }
```

[FlexExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexExample.ets#L15-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PDtkcK7sSs-UGQ6A5HbIMg/zh-cn_image_0000002592218122.png?HW-CC-KV=V1&HW-CC-Date=20260611T063018Z&HW-CC-Expire=86400&HW-CC-Sign=27D1AA57BD60444EDB681C08AD7B9FE599738CB46F744414D4BD173532D2A9FB)
