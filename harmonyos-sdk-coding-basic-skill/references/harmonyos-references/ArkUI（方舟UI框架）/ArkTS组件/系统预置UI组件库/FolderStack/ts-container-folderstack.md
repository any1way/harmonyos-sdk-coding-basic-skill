---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-folderstack
title: FolderStack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FolderStack
category: harmonyos-references
scraped_at: 2026-06-11T15:50:08+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:4549fcd573d3a5e978564def8b40b74bc232eeef2619a2ee6a1a535ff8a3cfae
---
FolderStack继承于[Stack](../../行列与堆叠/Stack/ts-container-stack.md)(层叠布局)控件，新增了[折叠屏悬停](../../../../../best-practices/一次开发，多端部署/多设备界面开发/特殊界面布局场景/折叠屏悬停态/bpta-folded-hover.md)能力，通过在FolderStack的配置项[FolderStackOptions](ts-container-folderstack.md#folderstackoptions18对象说明)的upperItems数组上设置子组件id，使相应子组件自动避让折叠屏折痕区后移到上半屏。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件的悬停态能力针对[双折叠](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141)设计，只在双折叠设备生效。

当该组件的父组件为[if/else：条件渲染](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式渲染控制/ifelse：条件渲染/arkts-rendering-control-ifelse.md>)节点时，折叠屏悬停能力将会失效。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含多个子组件。

## 接口

PhonePC/2in1TabletTVWearable

FolderStack(options?: FolderStackOptions)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FolderStackOptions](ts-container-folderstack.md#folderstackoptions18对象说明) | 否 | FolderStack的配置项。 |

## FolderStackOptions18+对象说明

PhonePC/2in1TabletTVWearable

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| upperItems11+ | Array<string> | 否 | 是 | 定义悬停态会被移到上半屏的子组件的id数组。  当悬停触发时，upperItems数组中的子组件自动避让折叠屏折痕区后移到上半屏，其它组件堆叠在下半屏区域。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

说明

设置offset和margin属性，可能会导致上下半屏遮挡折痕区，不建议开发者使用。

除支持[通用属性](../../通用属性/ts-component-general-attributes.md)外，还支持以下属性：

### alignContent

PhonePC/2in1TabletTVWearable

alignContent(value: Alignment)

设置子组件在容器内的对齐方式。该属性与[align](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#align)同时设置时，后设置的属性生效。

说明

从API version 12开始，该接口支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Alignment](../../公共定义/枚举说明/ts-appendix-enums.md#alignment) | 是 | 子组件在容器内的对齐方式。  默认值：Alignment.Center  非法值：按默认值处理。 |

### enableAnimation

PhonePC/2in1TabletTVWearable

enableAnimation(value: boolean)

设置是否使用默认动效。

说明

从API version 12开始，该接口支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否使用默认动效。  默认值：true，设置true表示使用默认动效，设置false表示不使用默认动效。  非法值：按默认值处理。 |

### autoHalfFold

PhonePC/2in1TabletTVWearable

autoHalfFold(value: boolean)

设置是否开启自动旋转，仅在系统自动旋转关闭时该属性生效。

说明

从API version 12开始，该接口支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启自动旋转。  默认值：true，设置true表示FolderStack在半折叠状态（见[FoldStatus](../../公共定义/枚举说明/ts-appendix-enums.md#foldstatus11)）进行布局时开启自动旋转，设置false表示关闭自动旋转。该属性不区分设备类型。  非法值：按默认值处理。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](../../通用事件/ts-component-general-events.md)外，还支持以下事件：

### onFolderStateChange

PhonePC/2in1TabletTVWearable

onFolderStateChange(callback: OnFoldStatusChangeCallback)

当前设备的折叠状态改变时触发回调，仅在横屏状态下生效。

说明

从API version 20开始，该接口支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFoldStatusChangeCallback](ts-container-folderstack.md#onfoldstatuschangecallback18) | 是 | 当前设备的折叠状态改变时触发的回调。 |

### onHoverStatusChange12+

PhonePC/2in1TabletTVWearable

onHoverStatusChange(handler: OnHoverStatusChangeCallback)

当前设备的悬停状态改变时触发回调。

说明

从API version 20开始，该接口支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnHoverStatusChangeCallback](ts-container-folderstack.md#onhoverstatuschangecallback18) | 是 | 当前设备的悬停状态改变时触发的回调。 |

## OnHoverStatusChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnHoverStatusChangeCallback = (param: HoverEventParam) => void

当前设备的悬停状态改变时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [HoverEventParam](ts-container-folderstack.md#hovereventparam12对象说明) | 是 | 当前设备与悬停状态相关的参数，包括设备的折叠状态、悬停状态、应用方向以及窗口模式枚举。 |

## OnFoldStatusChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnFoldStatusChangeCallback = (event: OnFoldStatusChangeInfo) => void

当前设备的折叠状态。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnFoldStatusChangeInfo](ts-container-folderstack.md#onfoldstatuschangeinfo18) | 是 | 当前设备的折叠状态。 |

## OnFoldStatusChangeInfo18+

PhonePC/2in1TabletTVWearable

当折叠状态改变的时候回调，仅在横屏状态下生效。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foldStatus11+ | [FoldStatus](../../公共定义/枚举说明/ts-appendix-enums.md#foldstatus11) | 否 | 否 | 当前设备的折叠状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## HoverEventParam12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foldStatus | [FoldStatus](../../公共定义/枚举说明/ts-appendix-enums.md#foldstatus11) | 否 | 否 | 当前设备的折叠状态。 |
| isHoverMode | boolean | 否 | 否 | 当前是否为悬停态。设置为true时表示当前为悬停态，设置为false时表示当前为非悬停态。 |
| appRotation | [AppRotation](../../公共定义/枚举说明/ts-appendix-enums.md#approtation12) | 否 | 否 | 当前应用方向。 |
| windowStatusType | [WindowStatusType](ts-container-folderstack.md#windowstatustype12) | 否 | 否 | 窗口模式枚举。 |

## WindowStatusType12+

PhonePC/2in1TabletTVWearable

type WindowStatusType = WindowStatusType

窗口模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [WindowStatusType](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Enums/arkts-apis-window-e.md#windowstatustype11>) | 窗口模式枚举。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（FolderStack折叠屏悬停能力）

该示例实现了折叠屏悬停能力。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. // upperItems将所需要的悬停到上半屏的id放入upperItems传入，其余组件会堆叠在下半屏区域
7. FolderStack({ upperItems: ["upperitemsId"] }) {
8. // 此Column会自动上移到上半屏
9. Column() {
10. Text("video zone").height("100%").width("100%").textAlign(TextAlign.Center).fontSize(25)
11. }.backgroundColor('rgb(0, 74, 175)').width("100%").height("100%").id("upperitemsId")

13. // 下列两个Column堆叠在下半屏区域
14. Column() {
15. Text("video title")
16. .width("100%")
17. .height(50)
18. .textAlign(TextAlign.Center)
19. .backgroundColor('rgb(213, 213, 213)')
20. .fontSize(25)
21. }.width("100%").height("100%").justifyContent(FlexAlign.Start)

23. Column() {
24. Text("video bar ")
25. .width("100%")
26. .height(50)
27. .textAlign(TextAlign.Center)
28. .backgroundColor('rgb(213, 213, 213)')
29. .fontSize(25)
30. }.width("100%").height("100%").justifyContent(FlexAlign.End)
31. }
32. .backgroundColor('rgb(39, 135, 217)')
33. // 是否启动动效
34. .enableAnimation(true)
35. // 是否自动旋转
36. .autoHalfFold(true)
37. // folderStack回调 当折叠状态改变时回调
38. .onFolderStateChange((msg) => {
39. if (msg.foldStatus === FoldStatus.FOLD_STATUS_EXPANDED) {
40. console.info("The device is currently in the expanded state")
41. } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_HALF_FOLDED) {
42. console.info("The device is currently in the half folded state")
43. } else {
44. // .............
45. }
46. })
47. // hoverStatusChange回调 当悬停状态改变时回调
48. .onHoverStatusChange((msg) => {
49. console.info('this foldStatus:' + msg.foldStatus);
50. console.info('this isHoverMode:' + msg.isHoverMode);
51. console.info('this appRotation:' + msg.appRotation);
52. console.info('this windowStatusType:' + msg.windowStatusType);
53. })
54. // folderStack如果不撑满页面全屏，作为普通Stack使用
55. .alignContent(Alignment.Bottom)
56. .height("100%")
57. .width("100%")
58. .backgroundColor('rgb(39, 135, 217)')

60. }
61. .height("100%")
62. .width("100%")
63. .borderWidth(1)
64. .borderColor('rgb(213, 213, 213)')
65. .backgroundColor('rgb(0, 74, 175)')
66. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
67. }
68. }
```

**图1** 横屏展开

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/0m5T90iOTPOskylE1PksGg/zh-cn_image_0000002592220580.png?HW-CC-KV=V1&HW-CC-Date=20260611T075007Z&HW-CC-Expire=86400&HW-CC-Sign=7A43D1F3DD793885C92D4E585A046E693631E7A1536FD5CAA7667C0B43944EF1)

**图2** 横屏半折叠

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/c40zNg10Rymp2F4nY-FWAw/zh-cn_image_0000002592380512.png?HW-CC-KV=V1&HW-CC-Date=20260611T075007Z&HW-CC-Expire=86400&HW-CC-Sign=9651FB1A600D363C48E7B4DBADADB326FF95F1146FE70B97C999F1CB032EB3C1)

### 示例2（使用attributeModifier动态设置FolderStack组件的属性及方法）

该示例展示了如何使用attributeModifier动态设置FolderStack组件的onFolderStateChange和onHoverStatusChange方法。

```
1. // xxx.ets
2. class MyFolderStackModifier implements AttributeModifier<FolderStackAttribute> {
3. applyNormalAttribute(instance: FolderStackAttribute): void {
4. // folderStack回调 当折叠状态改变时回调
5. instance.onFolderStateChange((msg) => {
6. if (msg.foldStatus === FoldStatus.FOLD_STATUS_EXPANDED) {
7. console.info("The device is currently in the expanded state")
8. } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_HALF_FOLDED) {
9. console.info("The device is currently in the half folded state")
10. } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_FOLDED) {
11. console.info("The device is currently in the folded state")
12. } else {
13. // .............
14. }
15. })
16. // hoverStatusChange回调 当悬停状态改变时回调
17. instance.onHoverStatusChange((msg) => {
18. console.info('this foldStatus:' + msg.foldStatus);
19. console.info('this isHoverMode:' + msg.isHoverMode);
20. console.info('this appRotation:' + msg.appRotation);
21. console.info('this windowStatusType:' + msg.windowStatusType);
22. })
23. }
24. }

26. @Entry
27. @Component
28. struct attributeDemo {
29. @State modifier: MyFolderStackModifier = new MyFolderStackModifier()

31. build() {
32. Column() {
33. // upperItems将所需要的悬停到上半屏的id放入upperItems传入，其余组件会堆叠在下半屏区域
34. FolderStack({ upperItems: ["upperitemsId"] }) {
35. // 此Column会自动上移到上半屏
36. Column() {
37. Text("video zone").height("100%").width("100%").textAlign(TextAlign.Center).fontSize(25)
38. }.backgroundColor('rgb(0, 74, 175)').width("100%").height("100%").id("upperitemsId")

40. // 下列两个Column堆叠在下半屏区域
41. Column() {
42. Text("video title")
43. .width("100%")
44. .height(50)
45. .textAlign(TextAlign.Center)
46. .backgroundColor('rgb(213, 213, 213)')
47. .fontSize(25)
48. }.width("100%").height("100%").justifyContent(FlexAlign.Start)

50. Column() {
51. Text("video bar ")
52. .width("100%")
53. .height(50)
54. .textAlign(TextAlign.Center)
55. .backgroundColor('rgb(213, 213, 213)')
56. .fontSize(25)
57. }.width("100%").height("100%").justifyContent(FlexAlign.End)
58. }
59. .backgroundColor('rgb(39, 135, 217)')
60. // 是否启动动效
61. .enableAnimation(true)
62. // 是否自动旋转
63. .autoHalfFold(true)
64. .attributeModifier(this.modifier)
65. // folderStack如果不撑满页面全屏，作为普通Stack使用
66. .alignContent(Alignment.Bottom)
67. .height("100%")
68. .width("100%")
69. .backgroundColor('rgb(39, 135, 217)')
70. }
71. .height("100%")
72. .width("100%")
73. .borderWidth(1)
74. .borderColor('rgb(213, 213, 213)')
75. .backgroundColor('rgb(0, 74, 175)')
76. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
77. }
78. }
```

**图1** 横屏展开

预期日志：

The device is currently in the expanded state

this foldStatus:1

this isHoverMode:0

this appRotation:3

this windowStatusType:1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/X6qX2QvfQA6ypFla3SjHng/zh-cn_image_0000002622860023.png?HW-CC-KV=V1&HW-CC-Date=20260611T075007Z&HW-CC-Expire=86400&HW-CC-Sign=825F665ACE85044D3C4081A68C39D4A3B35F75F88F829EA9D8380D92D893A4E6)

**图2** 横屏半折叠

预期日志：

The device is currently in the half folded state

this foldStatus:3

this isHoverMode:1

this appRotation:3

this windowStatusType:1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/mtasdZ54SIamrACmSMVULw/zh-cn_image_0000002622700141.png?HW-CC-KV=V1&HW-CC-Date=20260611T075007Z&HW-CC-Expire=86400&HW-CC-Sign=925FE4DE840A87622E7B97BF3BF87A630C980E996D73DA0D3FE50FE3CEED42A9)
