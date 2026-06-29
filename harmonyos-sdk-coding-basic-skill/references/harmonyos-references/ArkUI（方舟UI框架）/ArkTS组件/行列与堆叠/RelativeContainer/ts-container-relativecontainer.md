---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer
title: RelativeContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 行列与堆叠 > RelativeContainer
category: harmonyos-references
scraped_at: 2026-06-11T15:45:51+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:3e92f15a584cf5de066938ec9e53e95e3629fb64caad4b7724ca0174a4519739
---
相对布局组件，用于复杂场景中元素对齐的布局。

子组件可以通过设置[alignRules](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#alignrules9)来设置自身在相对容器中的对齐规则。

说明

* 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 在RelativeContainer组件中，不设置[width](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#width)、[height](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#height)时，对应属性布局表现与设置为100%相同。
* 从API version 11开始，在RelativeContainer组件中，[width](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#width)、[height](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#height)设置"auto"表示自适应子组件。当width设置"auto"时，如果水平方向上子组件以容器作为锚点，则"auto"不生效（即视为不设置width），垂直方向上同理。
* 从API version 20开始，在RelativeContainer组件中，[width](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#width15)、[height](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#height15)设置LayoutPolicy.wrapContent表示自适应子组件且被祖先节点尺寸约束，设置LayoutPolicy.fixAtIdealSize表示自适应子组件且不被祖先节点尺寸约束。当width设置wrapContent或fixAtIdealSize时，如果水平方向上子组件直接或间接以容器作为锚点，则容器在该方向上的尺寸不自适应该组件，垂直方向上同理。
* 相对布局容器内的子组件的[margin](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#margin)含义不同于通用属性的margin，其含义为到该方向上的锚点的距离。若该方向上没有锚点，则该方向的margin不生效。

## 子组件

PhonePC/2in1TabletTVWearable

支持多个子组件。

## 接口

PhonePC/2in1TabletTVWearable

RelativeContainer()

相对布局组件，用于复杂场景中元素对齐的布局。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](../../通用属性/ts-component-general-attributes.md)外，还支持如下属性：

### guideLine12+

PhonePC/2in1TabletTVWearable

guideLine(value: Array<GuideLineStyle>)

设置RelativeContainer容器内的[辅助线](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/组件布局/构建布局/相对布局 (RelativeContainer)/arkts-layout-development-relative-layout.md#使用辅助线辅助定位子组件>)，Array中每个项目即为一条guideLine。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[GuideLineStyle](ts-container-relativecontainer.md#guidelinestyle12对象说明)> | 是 | RelativeContainer容器内的辅助线。 |

### barrier12+

PhonePC/2in1TabletTVWearable

barrier(value: Array<BarrierStyle>)

设置RelativeContainer容器内的[屏障](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/组件布局/构建布局/相对布局 (RelativeContainer)/arkts-layout-development-relative-layout.md#多个组件的屏障>)，Array中每个项目即为一条barrier。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[BarrierStyle](ts-container-relativecontainer.md#barrierstyle12对象说明)> | 是 | RelativeContainer容器内的屏障。 |

### barrier12+

PhonePC/2in1TabletTVWearable

barrier(barrierStyle: Array<LocalizedBarrierStyle>)

设置RelativeContainer容器内的屏障，Array中每个项目即为一条barrier，支持定义镜像模式的屏障线。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| barrierStyle | Array<[LocalizedBarrierStyle](ts-container-relativecontainer.md#localizedbarrierstyle12对象说明)> | 是 | RelativeContainer容器内的屏障。 |

## GuideLineStyle12+对象说明

PhonePC/2in1TabletTVWearable

guideLine参数，用于定义一条guideLine的id、方向和位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | guideLine的id，必须是唯一的并且不可与容器内组件重名。 |
| direction | [Axis](../../公共定义/枚举说明/ts-appendix-enums.md#axis) | 否 | 否 | 指定guideLine的方向。  垂直方向的guideLine仅能作为组件水平方向的锚点，作为垂直方向的锚点时值为0；水平方向的guideLine仅能作为组件垂直方向的锚点，作为水平方向的锚点时值为0。  默认值：Axis.Vertical  非法值：按默认值处理。 |
| position | [GuideLinePosition](ts-container-relativecontainer.md#guidelineposition12对象说明) | 否 | 否 | 指定guideLine的位置。  当未声明或声明异常值（如undefined）时，guideLine的位置默认为start: 0。start和end两种声明方式选择一种即可。若同时声明，仅start生效。若容器在某个方向的size被声明为"auto"，则该方向上guideLine的位置只能使用start方式声明（不允许使用百分比）。  默认值：  {  start: 0  }  非法值：按默认值处理。 |

## GuideLinePosition12+对象说明

PhonePC/2in1TabletTVWearable

guideLine位置参数，用于定义guideLine的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [Dimension](../../公共定义/基础类型定义/ts-types.md#dimension10) | 否 | 是 | guideLine距离容器左侧或者顶部的距离。 |
| end | [Dimension](../../公共定义/基础类型定义/ts-types.md#dimension10) | 否 | 是 | guideLine距离容器右侧或者底部的距离。 |

## BarrierStyle12+对象说明

PhonePC/2in1TabletTVWearable

barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | barrier的id，必须是唯一的并且不可与容器内组件重名。 |
| direction | [BarrierDirection](ts-container-relativecontainer.md#barrierdirection12枚举说明) | 否 | 否 | 指定barrier的方向。  垂直方向（TOP，BOTTOM）的barrier仅能作为组件的水平方向锚点，用作垂直方向锚点时值为0；水平方向（LEFT，RIGHT）的barrier仅能作为组件的垂直方向锚点，用作水平方向锚点时值为0。  默认值：BarrierDirection.LEFT  非法值：按默认值处理。 |
| referencedId | Array<string> | 否 | 否 | 指定生成barrier所依赖的组件。 |

## BarrierDirection12+枚举说明

PhonePC/2in1TabletTVWearable

定义屏障线的方向。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#barrierstyle12对象说明)的最左侧。 |
| RIGHT | 1 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#barrierstyle12对象说明)的最右侧。 |
| TOP | 2 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#barrierstyle12对象说明)的最上方。 |
| BOTTOM | 3 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#barrierstyle12对象说明)的最下方。 |

## LocalizedBarrierStyle12+对象说明

PhonePC/2in1TabletTVWearable

barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | barrier的id，必须是唯一的并且不可与容器内组件重名。 |
| localizedDirection | [LocalizedBarrierDirection](ts-container-relativecontainer.md#localizedbarrierdirection12枚举说明) | 否 | 否 | 指定barrier的方向。  垂直方向（TOP，BOTTOM）的barrier仅能作为组件的水平方向锚点，作为垂直方向锚点时值为0。水平方向（START，END）的barrier仅能作为组件的垂直方向锚点，作为水平方向锚点时值为0。 |
| referencedId | Array<string> | 否 | 否 | 指定生成barrier所依赖的组件。 |

## LocalizedBarrierDirection12+枚举说明

PhonePC/2in1TabletTVWearable

定义支持镜像模式的屏障线的方向。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#localizedbarrierstyle12对象说明)的最左/右侧，LTR模式时为最左侧，RTL模式时为最右侧。 |
| END | 1 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#localizedbarrierstyle12对象说明)的最左/右侧, LTR模式时为最右侧，RTL模式时为最左侧。 |
| TOP | 2 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#localizedbarrierstyle12对象说明)的最上方。 |
| BOTTOM | 3 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#localizedbarrierstyle12对象说明)的最下方。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](../../通用事件/ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（以容器和容器内组件作为锚点进行布局）

本示例通过alignRules接口实现了以容器和容器内组件作为锚点进行布局的功能。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. top: { anchor: "__container__", align: VerticalAlign.Top },
16. left: { anchor: "__container__", align: HorizontalAlign.Start }
17. })
18. .id("row1")

20. Row() {
21. Text('row2')
22. }
23. .justifyContent(FlexAlign.Center)
24. .width(100)
25. .height(100)
26. .backgroundColor('#00ae9d')
27. .alignRules({
28. top: { anchor: "__container__", align: VerticalAlign.Top },
29. right: { anchor: "__container__", align: HorizontalAlign.End }
30. })
31. .id("row2")

33. Row() {
34. Text('row3')
35. }
36. .justifyContent(FlexAlign.Center)
37. .height(100)
38. .backgroundColor('#0a59f7')
39. .alignRules({
40. top: { anchor: "row1", align: VerticalAlign.Bottom },
41. left: { anchor: "row1", align: HorizontalAlign.End },
42. right: { anchor: "row2", align: HorizontalAlign.Start }
43. })
44. .id("row3")

46. Row() {
47. Text('row4')
48. }.justifyContent(FlexAlign.Center)
49. .backgroundColor('#2ca9e0')
50. .alignRules({
51. top: { anchor: "row3", align: VerticalAlign.Bottom },
52. bottom: { anchor: "__container__", align: VerticalAlign.Bottom },
53. left: { anchor: "__container__", align: HorizontalAlign.Start },
54. right: { anchor: "row1", align: HorizontalAlign.End }
55. })
56. .id("row4")

58. Row() {
59. Text('row5')
60. }.justifyContent(FlexAlign.Center)
61. .backgroundColor('#30c9f7')
62. .alignRules({
63. top: { anchor: "row3", align: VerticalAlign.Bottom },
64. bottom: { anchor: "__container__", align: VerticalAlign.Bottom },
65. left: { anchor: "row2", align: HorizontalAlign.Start },
66. right: { anchor: "__container__", align: HorizontalAlign.End }
67. })
68. .id("row5")
69. }
70. .width(300).height(300)
71. .margin({ left: 50 })
72. .border({ width: 2, color: "#6699FF" })
73. }
74. .height('100%')
75. }
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/O3Ba-PRMTTe2bAUqyVPM7A/zh-cn_image_0000002592379994.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=9F7742073344C92D651DBA3109EEF5BC5B568B8C6C30D60EC68F8BED7912BE55)

### 示例2（子组件设置外边距）

本示例展示容器内子组件设置外边距的方法。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. top: { anchor: "__container__", align: VerticalAlign.Top },
16. left: { anchor: "__container__", align: HorizontalAlign.Start }
17. })
18. .id("row1")
19. .margin(10)

21. Row() {
22. Text('row2')
23. }
24. .justifyContent(FlexAlign.Center)
25. .width(100)
26. .height(100)
27. .backgroundColor('#00ae9d')
28. .alignRules({
29. left: { anchor: "row1", align: HorizontalAlign.End },
30. top: { anchor: "row1", align: VerticalAlign.Top }
31. })
32. .id("row2")

34. Row() {
35. Text('row3')
36. }
37. .justifyContent(FlexAlign.Center)
38. .width(100)
39. .height(100)
40. .backgroundColor('#0a59f7')
41. .alignRules({
42. left: { anchor: "row1", align: HorizontalAlign.Start },
43. top: { anchor: "row1", align: VerticalAlign.Bottom }
44. })
45. .id("row3")

47. Row() {
48. Text('row4')
49. }
50. .justifyContent(FlexAlign.Center)
51. .width(100)
52. .height(100)
53. .backgroundColor('#2ca9e0')
54. .alignRules({
55. left: { anchor: "row3", align: HorizontalAlign.End },
56. top: { anchor: "row2", align: VerticalAlign.Bottom }
57. })
58. .id("row4")
59. .margin(10)
60. }
61. .width(300).height(300)
62. .margin({ left: 50 })
63. .border({ width: 2, color: "#6699FF" })
64. }
65. .height('100%')
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/yGoz_heUQHC72GZqKWzEcQ/zh-cn_image_0000002622859503.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=838119B6980F3E13FC940ABE6F4CBFB6224DCA34923A53AD4F65DAFC9FB378EB)

### 示例3（设置容器大小自适应内容）

本示例展示了容器大小适应内容（声明width或height为"auto"）的用法。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .id("row1")

16. Row() {
17. Text('row2')
18. }
19. .justifyContent(FlexAlign.Center)
20. .width(100)
21. .height(100)
22. .backgroundColor('#00ae9d')
23. .alignRules({
24. left: { anchor: "row1", align: HorizontalAlign.End },
25. top: { anchor: "row1", align: VerticalAlign.Top }
26. })
27. .id("row2")

29. Row() {
30. Text('row3')
31. }
32. .justifyContent(FlexAlign.Center)
33. .width(100)
34. .height(100)
35. .backgroundColor('#0a59f7')
36. .alignRules({
37. left: { anchor: "row1", align: HorizontalAlign.Start },
38. top: { anchor: "row1", align: VerticalAlign.Bottom }
39. })
40. .id("row3")

42. Row() {
43. Text('row4')
44. }
45. .justifyContent(FlexAlign.Center)
46. .width(100)
47. .height(100)
48. .backgroundColor('#2ca9e0')
49. .alignRules({
50. left: { anchor: "row3", align: HorizontalAlign.End },
51. top: { anchor: "row2", align: VerticalAlign.Bottom }
52. })
53. .id("row4")
54. }
55. .width("auto").height("auto")
56. .margin({ left: 50 })
57. .border({ width: 2, color: "#6699FF" })
58. }
59. .height('100%')
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/AiZV0B5FRy6J02-961m7kA/zh-cn_image_0000002622699623.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=2E88B0D5511CA7AA2544629DAF6521305ADBD855DFD3088E78C337D2FF247C57)

### 示例4（设置偏移）

本示例通过[bias](../../公共定义/基础类型定义/ts-types.md#bias对象说明)实现了子组件的位置在垂直方向的两个锚点间偏移的效果。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row()
8. .width(100)
9. .height(100)
10. .backgroundColor('#a3cf62')
11. .alignRules({
12. top: { anchor: "__container__", align: VerticalAlign.Top },
13. bottom: { anchor: "__container__", align: VerticalAlign.Bottom },
14. left: { anchor: "__container__", align: HorizontalAlign.Start },
15. right: { anchor: "__container__", align: HorizontalAlign.End },
16. bias: { vertical: 0.3 }
17. })
18. .id("row1")
19. }
20. .width(300).height(300)
21. .margin({ left: 50 })
22. .border({ width: 2, color: "#6699FF" })
23. }
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/55HBtnhmS2KZgdFzqXvIYg/zh-cn_image_0000002592220062.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=540075E2B101B9679E1785D6D6F45DBC89C260B7AD54972123F90DF72963FD38)

### 示例5（设置辅助线）

本示例展示了相对布局组件通过[guideLine](ts-container-relativecontainer.md#guideline12)接口设置辅助线，子组件以辅助线为锚点的功能。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row()
8. .width(100)
9. .height(100)
10. .backgroundColor('#a3cf62')
11. .alignRules({
12. left: { anchor: "guideline1", align: HorizontalAlign.End },
13. top: { anchor: "guideline2", align: VerticalAlign.Top }
14. })
15. .id("row1")
16. }
17. .width(300)
18. .height(300)
19. .margin({ left: 50 })
20. .border({ width: 2, color: "#6699FF" })
21. .guideLine([{ id: "guideline1", direction: Axis.Vertical, position: { start: 50 } },
22. { id: "guideline2", direction: Axis.Horizontal, position: { start: 50 } }])
23. }
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/8MSOisKtQreeR2LlfkCSIA/zh-cn_image_0000002592379996.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=4D09CBA4C94C69860407700E84F99AAFE8F63D4304491D0CA2827F20664FB009)

### 示例6（设置屏障）

本示例展示了相对布局组件通过[barrier](ts-container-relativecontainer.md#barrier12)接口设置屏障，子组件以屏障为锚点的用法。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .id("row1")

16. Row() {
17. Text('row2')
18. }
19. .justifyContent(FlexAlign.Center)
20. .width(100)
21. .height(100)
22. .backgroundColor('#00ae9d')
23. .alignRules({
24. middle: { anchor: "row1", align: HorizontalAlign.End },
25. top: { anchor: "row1", align: VerticalAlign.Bottom }
26. })
27. .id("row2")

29. Row() {
30. Text('row3')
31. }
32. .justifyContent(FlexAlign.Center)
33. .width(100)
34. .height(100)
35. .backgroundColor('#0a59f7')
36. .alignRules({
37. left: { anchor: "barrier1", align: HorizontalAlign.End },
38. top: { anchor: "row1", align: VerticalAlign.Top }
39. })
40. .id("row3")

42. Row() {
43. Text('row4')
44. }
45. .justifyContent(FlexAlign.Center)
46. .width(50)
47. .height(50)
48. .backgroundColor('#2ca9e0')
49. .alignRules({
50. left: { anchor: "row1", align: HorizontalAlign.Start },
51. top: { anchor: "barrier2", align: VerticalAlign.Bottom }
52. })
53. .id("row4")
54. }
55. .width(300)
56. .height(300)
57. .margin({ left: 50 })
58. .border({ width: 2, color: "#6699FF" })
59. .barrier([{ id: "barrier1", direction: BarrierDirection.RIGHT, referencedId: ["row1", "row2"] },
60. { id: "barrier2", direction: BarrierDirection.BOTTOM, referencedId: ["row1", "row2"] }])
61. }
62. .height('100%')
63. }
64. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/SFIEAHmMSk2XoUo76QL6ZA/zh-cn_image_0000002622859505.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=8F53590F9494C0F2A8C651F05A55D92D032F68F5887A5D45206861D9FC11751B)

### 示例7（设置链）

本示例通过[chainMode](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainmode12)接口从上至下分别实现了水平方向的[SPREAD](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainstyle12)链、[SPREAD\_INSIDE](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainstyle12)链和[PACKED](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainstyle12)链。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(80)
12. .height(80)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. left: { anchor: "__container__", align: HorizontalAlign.Start },
16. right: { anchor: "row2", align: HorizontalAlign.Start },
17. top: { anchor: "__container__", align: VerticalAlign.Top }
18. })
19. .id("row1")
20. .chainMode(Axis.Horizontal, ChainStyle.SPREAD)

22. Row() {
23. Text('row2')
24. }
25. .justifyContent(FlexAlign.Center)
26. .width(80)
27. .height(80)
28. .backgroundColor('#00ae9d')
29. .alignRules({
30. left: { anchor: "row1", align: HorizontalAlign.End },
31. right: { anchor: "row3", align: HorizontalAlign.Start },
32. top: { anchor: "row1", align: VerticalAlign.Top }
33. })
34. .id("row2")

36. Row() {
37. Text('row3')
38. }
39. .justifyContent(FlexAlign.Center)
40. .width(80)
41. .height(80)
42. .backgroundColor('#0a59f7')
43. .alignRules({
44. left: { anchor: "row2", align: HorizontalAlign.End },
45. right: { anchor: "__container__", align: HorizontalAlign.End },
46. top: { anchor: "row1", align: VerticalAlign.Top }
47. })
48. .id("row3")

50. Row() {
51. Text('row4')
52. }
53. .justifyContent(FlexAlign.Center)
54. .width(80)
55. .height(80)
56. .backgroundColor('#a3cf62')
57. .alignRules({
58. left: { anchor: "__container__", align: HorizontalAlign.Start },
59. right: { anchor: "row5", align: HorizontalAlign.Start },
60. center: { anchor: "__container__", align: VerticalAlign.Center }
61. })
62. .id("row4")
63. .chainMode(Axis.Horizontal, ChainStyle.SPREAD_INSIDE)

65. Row() {
66. Text('row5')
67. }
68. .justifyContent(FlexAlign.Center)
69. .width(80)
70. .height(80)
71. .backgroundColor('#00ae9d')
72. .alignRules({
73. left: { anchor: "row4", align: HorizontalAlign.End },
74. right: { anchor: "row6", align: HorizontalAlign.Start },
75. top: { anchor: "row4", align: VerticalAlign.Top }
76. })
77. .id("row5")

79. Row() {
80. Text('row6')
81. }
82. .justifyContent(FlexAlign.Center)
83. .width(80)
84. .height(80)
85. .backgroundColor('#0a59f7')
86. .alignRules({
87. left: { anchor: "row5", align: HorizontalAlign.End },
88. right: { anchor: "__container__", align: HorizontalAlign.End },
89. top: { anchor: "row4", align: VerticalAlign.Top }
90. })
91. .id("row6")

93. Row() {
94. Text('row7')
95. }
96. .justifyContent(FlexAlign.Center)
97. .width(80)
98. .height(80)
99. .backgroundColor('#a3cf62')
100. .alignRules({
101. left: { anchor: "__container__", align: HorizontalAlign.Start },
102. right: { anchor: "row8", align: HorizontalAlign.Start },
103. bottom: { anchor: "__container__", align: VerticalAlign.Bottom }
104. })
105. .id("row7")
106. .chainMode(Axis.Horizontal, ChainStyle.PACKED)

108. Row() {
109. Text('row8')
110. }
111. .justifyContent(FlexAlign.Center)
112. .width(80)
113. .height(80)
114. .backgroundColor('#00ae9d')
115. .alignRules({
116. left: { anchor: "row7", align: HorizontalAlign.End },
117. right: { anchor: "row9", align: HorizontalAlign.Start },
118. top: { anchor: "row7", align: VerticalAlign.Top }
119. })
120. .id("row8")

122. Row() {
123. Text('row9')
124. }
125. .justifyContent(FlexAlign.Center)
126. .width(80)
127. .height(80)
128. .backgroundColor('#0a59f7')
129. .alignRules({
130. left: { anchor: "row8", align: HorizontalAlign.End },
131. right: { anchor: "__container__", align: HorizontalAlign.End },
132. top: { anchor: "row7", align: VerticalAlign.Top }
133. })
134. .id("row9")
135. }
136. .width(300).height(300)
137. .margin({ left: 50 })
138. .border({ width: 2, color: "#6699FF" })
139. }
140. .height('100%')
141. }
142. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gd8SB0PbTNmFO5YKxCPkpQ/zh-cn_image_0000002622699625.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=16F706051002D818920C384893C2CC8563AC6F3606AE37EF9431A9CE37819C24)

### 示例8（链中设置偏移）

本示例通过[chainMode](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainmode12)和[bias](../../公共定义/基础类型定义/ts-types.md#bias对象说明)接口实现了水平方向的带偏移的[PACKED](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainstyle12)链。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(80)
12. .height(80)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. left: { anchor: "__container__", align: HorizontalAlign.Start },
16. right: { anchor: "row2", align: HorizontalAlign.Start },
17. center: { anchor: "__container__", align: VerticalAlign.Center },
18. bias: { horizontal: 0 }
19. })
20. .id("row1")
21. .chainMode(Axis.Horizontal, ChainStyle.PACKED)

23. Row() {
24. Text('row2')
25. }
26. .justifyContent(FlexAlign.Center)
27. .width(80)
28. .height(80)
29. .backgroundColor('#00ae9d')
30. .alignRules({
31. left: { anchor: "row1", align: HorizontalAlign.End },
32. right: { anchor: "row3", align: HorizontalAlign.Start },
33. top: { anchor: "row1", align: VerticalAlign.Top }
34. })
35. .id("row2")

37. Row() {
38. Text('row3')
39. }
40. .justifyContent(FlexAlign.Center)
41. .width(80)
42. .height(80)
43. .backgroundColor('#0a59f7')
44. .alignRules({
45. left: { anchor: "row2", align: HorizontalAlign.End },
46. right: { anchor: "__container__", align: HorizontalAlign.End },
47. top: { anchor: "row1", align: VerticalAlign.Top }
48. })
49. .id("row3")
50. }
51. .width(300).height(300)
52. .margin({ left: 50 })
53. .border({ width: 2, color: "#6699FF" })
54. }
55. .height('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/pkslCJ8cSpSrqG687AaJpQ/zh-cn_image_0000002592220064.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=F6E3803881FF087D9D5258659F249B5FA89CC48086FF7ED66D94EE947B25E37C)

### 示例9（设置镜像模式）

本示例展示了在镜像模式（direction声明Direction.Rtl）下以屏障为锚点时使用[LocalizedAlignRuleOptions](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#localizedalignruleoptions12对象说明)和[LocalizedBarrierDirection](ts-container-relativecontainer.md#localizedbarrierdirection12枚举说明)设置对齐方式的用法。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .id("row1")

16. Row() {
17. Text('row2')
18. }
19. .justifyContent(FlexAlign.Center)
20. .width(100)
21. .height(100)
22. .backgroundColor('#00ae9d')
23. .alignRules({
24. middle: { anchor: "row1", align: HorizontalAlign.End },
25. top: { anchor: "row1", align: VerticalAlign.Bottom }
26. })
27. .id("row2")

29. Row() {
30. Text('row3')
31. }
32. .justifyContent(FlexAlign.Center)
33. .width(100)
34. .height(100)
35. .backgroundColor('#0a59f7')
36. .alignRules({
37. start: { anchor: "barrier1", align: HorizontalAlign.End },
38. top: { anchor: "row1", align: VerticalAlign.Top }
39. })
40. .id("row3")

42. Row() {
43. Text('row4')
44. }
45. .justifyContent(FlexAlign.Center)
46. .width(50)
47. .height(50)
48. .backgroundColor('#2ca9e0')
49. .alignRules({
50. start: { anchor: "row1", align: HorizontalAlign.Start },
51. top: { anchor: "barrier2", align: VerticalAlign.Bottom }
52. })
53. .id("row4")
54. }
55. .direction(Direction.Rtl)
56. .width(300)
57. .height(300)
58. .margin({ left: 50 })
59. .border({ width: 2, color: "#6699FF" })
60. .barrier([{ id: "barrier1", localizedDirection: LocalizedBarrierDirection.END, referencedId: ["row1", "row2"] },
61. { id: "barrier2", localizedDirection: LocalizedBarrierDirection.BOTTOM, referencedId: ["row1", "row2"] }])
62. }
63. .height('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/WrQmXPsGQ0qy3gnXPROZpw/zh-cn_image_0000002592379998.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=4C85D371CE484957B19E96ED31CB1C2A93628F12DC1D0FF68D78EB4B30DA1A22)

### 示例10（设置链中节点权重）

本示例展示了链中节点使用[chainWeight](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainweight14)设置尺寸权重的用法。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(80)
12. .height(80)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. left: { anchor: "__container__", align: HorizontalAlign.Start },
16. right: { anchor: "row2", align: HorizontalAlign.Start },
17. center: { anchor: "__container__", align: VerticalAlign.Center },
18. })
19. .id("row1")
20. .chainMode(Axis.Horizontal, ChainStyle.PACKED)

22. Row() {
23. Text('row2')
24. }
25. .justifyContent(FlexAlign.Center)
26. .width(80)
27. .height(80)
28. .backgroundColor('#00ae9d')
29. .alignRules({
30. left: { anchor: "row1", align: HorizontalAlign.End },
31. right: { anchor: "row3", align: HorizontalAlign.Start },
32. top: { anchor: "row1", align: VerticalAlign.Top }
33. })
34. .id("row2")
35. .chainWeight({ horizontal: 1 })

37. Row() {
38. Text('row3')
39. }
40. .justifyContent(FlexAlign.Center)
41. .width(80)
42. .height(80)
43. .backgroundColor('#0a59f7')
44. .alignRules({
45. left: { anchor: "row2", align: HorizontalAlign.End },
46. right: { anchor: "__container__", align: HorizontalAlign.End },
47. top: { anchor: "row1", align: VerticalAlign.Top }
48. })
49. .id("row3")
50. .chainWeight({ horizontal: 2 })
51. }
52. .width(300).height(300)
53. .margin({ left: 50 })
54. .border({ width: 2, color: "#6699FF" })
55. }
56. .height('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/yKznKjdvQt-mwptOPv8B0g/zh-cn_image_0000002622859507.png?HW-CC-KV=V1&HW-CC-Date=20260611T074549Z&HW-CC-Expire=86400&HW-CC-Sign=6E599EA6872248389C46AF67825C82ABD98AC5C4EF868E781DD41DDB0F9242B7)
