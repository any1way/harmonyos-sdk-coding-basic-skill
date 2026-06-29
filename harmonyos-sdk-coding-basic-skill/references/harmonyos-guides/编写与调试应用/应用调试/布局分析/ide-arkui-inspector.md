---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:24+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:7f70bbb3972e03f0b1e747e310edf083c1e91442bb89af74a31104cbac73b6bd
---
开发者可以使用ArkUI Inspector，在DevEco Studio上查看应用在真机上的UI显示效果，并通过查看多次操作后的界面状态，快速分析定位UI界面存在的问题。

ArkUI Inspector支持的功能包括：

* [查看设备上应用的UI显示效果](ide-arkui-inspector.md#section1645813371383)。
* [导出及导入应用UI界面快照](ide-arkui-inspector.md#section0442629153111)，脱离设备查看UI显示效果。
* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* [UI组件源码跳转](ide-arkui-inspector.md#section1226015494335)，选中UI组件后点击源码跳转按钮即可跳转至源码位置。
* 在UI界面上选择Show Component Border，可[查看当前页面上所有组件显示区域](ide-arkui-inspector.md#section1137025915336)。
* 在组件树上选择自定义组件，属性列表显示当前组件配置的[状态变量信息以及影响组件](ide-arkui-inspector.md#section19923158103412)。
* [查看窗口交互事件](ide-arkui-inspector.md#section516993011576)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件。
* 按照组件粒度[3D展开应用](ide-arkui-inspector.md#section138812162416)，方便查看组件之间的嵌套、遮挡关系。

## 使用场景

针对界面较复杂的应用：

* 通过组件树查看组件的父子关系，检查是否存在冗余组件。
* 针对应用在真机或模拟器上运行出现UI界面显示异常，尤其经过多次界面复杂操作后产生的界面错误以及后台逻辑错误，进行问题分析定位。

## 使用约束

* 仅运行在前台的应用支持通过Inspector查看。
* 已通过USB或WLAN连接设备。
* 仅支持Stage工程。
* 仅支持全屏应用或者焦点在前台的窗口。
* 不支持应用市场上架的商用签名应用。

## 操作步骤

1. 在DevEco Studio下方点击**ArkUI Inspector**，打开ArkUI Inspector。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/c9nML23WSS24UIpTsWuW9w/zh-cn_image_0000002602065959.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=63BF8532A8BA4A6DD6316BA0D0C6FD7BDBE27F8340E235E5816A48B95B99ED07)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/B9rQ_SszScCGivHP-1Upyw/zh-cn_image_0000002602186039.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=531A9A34543DA9BCF82C654E1C6E911FF96AD4CC2E8CB2D9FC9E114B2D153046)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/XMP14t1UR5uh5N93VfOF5g/zh-cn_image_0000002602065999.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=192F1E89BB1E1F1914023C65FA55CCAF990068A23E2D323173539ECF9789ABCD)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/SX5h9c9sQZ6pmROAiYgwLw/zh-cn_image_0000002602065951.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=E001B0851432B2472A125D7CE2E4C2EC9C19F779951F0879A042BFB81284D1A1)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/rGwDrX1AQj-87BoFGNeRFw/zh-cn_image_0000002571386876.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=CB5F01C84FC2370E34692229642612B68CE576DCE1D85357A115745D17D8460A)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/wpp2Z-VoRAOAoNYiRIzDtA/zh-cn_image_0000002571386844.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=B0259E5618E54E980FEEB318B88DEFE4B2A98C3AA6007C9CD8DC0918E5FE3FB0)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/HEv-OZlySiG2AdI-rU44Cg/zh-cn_image_0000002602186025.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=C76B4F5968F6E9B01BDB6081E37CB7F0F25C9DAD5CC915D716A925AD78FB73C8)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/n0e58i6hRs6IPf6FP1IPuA/zh-cn_image_0000002602186019.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=B9A82BD652258161DDCD1783E8B30BD6C7BC75E3EEA7919CDFAF0587A793229E)，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/vVY5coxTQP-50fXKVz44EA/zh-cn_image_0000002602186037.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=0623817256BA753F64624FED8846387CC18366FB3FF1BBB03491AF5E4E0EEFED)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/dsWZ6dLrRTGjty1mouQr6w/zh-cn_image_0000002602186031.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=EA431156C0134E7D41DBBB731806C27A52B974F7CDB97C5F48746A7B6975F6F0)，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/vdXx7eXrRymvBKGJNbvAKw/zh-cn_image_0000002571386836.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=73E900F8B0DDDCBDFD64EFF93B6BB1248F7C64B4BBBB7111335CDA733E4FB16C)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/rI1gZo4US0qGzQ1EoajKEA/zh-cn_image_0000002602065947.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=9584C007645A6C47F0857C5BE0062F20FC9C0E437ED437EA1BAF40A53510F11C)，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/5CjjCaOSSninAw-0gFlklQ/zh-cn_image_0000002571546484.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=ADBF77D8BA9F3FB22D59885F59D82CDE211ED6E453FE7A79F71320A4ACB84DEF)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/FW0hY9-ZQ569Y5BVLWPhwA/zh-cn_image_0000002571386864.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=52BB0D455CC3D7D980848FC45C4CE7BBA8FEE19ED8586DC0E093B788A361F724)，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/OZEjyrHBRYu5L8AydFGOcw/zh-cn_image_0000002571546482.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=CDF06B340DDCFE6F96FBF2BA77D70A147038311BD4460D2E2B24F46A3E6F35F7)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/2io7I5V2RG2UekjmV26u1g/zh-cn_image_0000002602186001.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=5CAEFF3530BFCB5ADDA89A2B206EE84C803763D38CA553B9EF95C3E9BAD589EE)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/MWIGIkNmQb2U-E0vv0VwwQ/zh-cn_image_0000002602066001.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=98B49E233E764512944BB892A298A3A9FD726D050ED7A7078F4EEC03551BC45F)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/eHqVfeJ0TW2OB-bnvSaY-A/zh-cn_image_0000002602186043.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=273EE682D09A01AB2C7656DC6699A98DED82FA8D2F6E9E5856076F7DE5C31B93)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/8u0gI3lLSy2gxNPwln0nQg/zh-cn_image_0000002571546510.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=EBA7BBA51C4D8C484BA62413D915580AA3215B053CE81C4144C8AF20913A6291)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/LUTRxylxQfyDYiQQW9Ltiw/zh-cn_image_0000002571546496.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=29154064430AC150CD2A550A70FE4CB6592EEDD77E78DD5E041AE4F1A45F779E)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/VJDcmEs0Q2OU6iVxV4jlpA/zh-cn_image_0000002602186021.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=4E68968C8B9EED43034EE9CB4F5715322996F916A3B4A9275FC8143B27C32B29)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/vRQUlBXeSk2QCiwDbyTr4Q/zh-cn_image_0000002602065961.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=C28792F06E891A1AB66A956C727A1E0403DC7FEE6E45932C7BF57265DCC2B4DC)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](<../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/交互响应概述/arkts-interaction-capability-overview.md>)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/KiVtAUHbQ3-4BFdz3JAycA/zh-cn_image_0000002602186009.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=2AF94136A2E699599DAA83AC1096DC6C1A4231917B41EB777D84FC72E73D0A3D)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/6QyFiQXbRlyKwk2o1MCLzQ/zh-cn_image_0000002602065977.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=825743EE5CF6148045E0EFFF8ADEB99588F165AB83FA9DDAC457C35A0E5E34DD)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/bxPnvAOlSUCstHE-GcwYfQ/zh-cn_image_0000002602065971.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=08805964859557080A0704B9DFD718F8F76E676E786D2D3B30FE6981C4FD56EE)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/nFgPgVtDTxuf-x8l2fGfoQ/zh-cn_image_0000002571546498.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=2D5B4962BB5B4D8DA005742D492CF09D9FA4119090C910611E07DEAD6839FEB9)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/jtdbUKuxQPqY7omycVBNkg/zh-cn_image_0000002602065955.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=196DF08E6711639505BAF03184907387BFB1B79745EF348E522F2CE2FD2A59B2)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/xeghMRcASym3pRsLkBIvFQ/zh-cn_image_0000002571546470.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=B24B3DE6C48587228F2D5A7A0E782B2815A1016F41F40C666CCEFBC3E0CA75AA)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/3V4X5g6eSiGJG_9s_jWq9g/zh-cn_image_0000002571386854.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=F53D552F0978A2A50A6B7D20985375BCD29C5BDB934955DC773318A0EF94AD91)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Z5Dv0JCIQb-ZifsJUXSOzg/zh-cn_image_0000002602065983.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=B5B05886C78161283AEB55730396ACEC8AF7E5AFDB37AE3DD39C0C71A6BAAFB0)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/vj40CtIrTFOe_JRfaT11uQ/zh-cn_image_0000002602065965.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=998A432463893DC2E3C9998082D76C4E5DA5D9C488E544C36E0CB5669CC2C80A)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/CD1qUO-eTUagAZOLGRForg/zh-cn_image_0000002602066003.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=56B52CD821B405C551A5B3B8721B78627CBAF6E545D2BB058F4FFC576BD6DB32)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/wFJvNEV_SQerjLIf4TkFxA/zh-cn_image_0000002571546476.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=CA1458D4AF5D967A4228C454F9ACEAA35C8FC5095E7184D37437297D8D88DE24)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/DrnY01lGRGGYus7caNHtkw/zh-cn_image_0000002571546518.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=9041B36F7BFCCB283361D789B7BE997C307B0EA08FEB3C4980A1E035625D72FA)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/djhgtcIIQh-8KZDTnMByQQ/zh-cn_image_0000002571386842.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=618ADEE2587A86F5212D4501E9EE43DB36C3757336F31F8B54F8C1729452969B)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/j7Hq44R5RC66Y9nvKtEJpw/zh-cn_image_0000002602186029.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=3441E956E279D487CAB37920868A52738E15152F95AB955559897F3B8402E68C)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ZYG34S8MR8SH36ugE8BTcg/zh-cn_image_0000002602065953.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=E155C0EC15659293B53783549933D2271FF71AE862F20B2A30B642828EC6166A)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/4tLbLAmHT-GRpkN31bOmCg/zh-cn_image_0000002571386880.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=06AA67B9A0F9239DEA5531FAFDD212AF8FE3E5915F57866367FC14DF6A855E35)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/eKKFNVMjTOu4csdFBgKGpQ/zh-cn_image_0000002602186027.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=20AD5500F78CD6CA605AC6AAC0D4EF250F53A484683EBEE4DEE35F6F95F5C1AE)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Dakm0iqcTc-MB8e0MfFucA/zh-cn_image_0000002571546502.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=AFEA6526BC925B13A3E8657224A4B11F1E789EC8A65405CC02CDFBFBB8C8028F)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Kkt2_nikSuS_lVaTCtCHMA/zh-cn_image_0000002571546508.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=8B0B3D2B523F162B8B728DF8B7E09D6CDB56D1BFAA06AE61194646EDD7549750)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/7oejAYNfTTS3-f7nkmlBNQ/zh-cn_image_0000002571546488.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=F83F9A204E1FB886D1885343FBE4AFE654F4B855F466222C7589EBCC43104635)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/OegM90YDSk-jKpmAlI-D_g/zh-cn_image_0000002571386878.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=970BA5BBD8B9F04047B71A3FFC4EE0632CDF0A5C701FBE3855749BC1289573D5)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/eXdN-kOxTeW8Yy3-IkhDOQ/zh-cn_image_0000002602065957.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=D1295F068C1A1D3880FE1C55EE61D4F05A689EC3CE30A16F3FAC2136F992D6A2)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ckRhQSBqQaem7lZoP9SZxA/zh-cn_image_0000002571386870.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=B691CB9209406700CCE054B48847AF440765DB1556905D0BE5E7371C3DD46CA4)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/tqhBOqpOTpqJk_buZHEWjQ/zh-cn_image_0000002602186041.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=539476DACAF689B69AF91AF5455DCEF6BADA455A1F7B2C2CC360B858F7564327)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/74YrCA8bSD-p-_lGfluZZQ/zh-cn_image_0000002602065995.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=24E4D52BBB8A91C799EF090F71AD55C6960DDB06B6539680E24373834071B951)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xM8JP07xTDaoDMwTMCX8mw/zh-cn_image_0000002571386838.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=D96AF24ED2801E0832F9E0ABB790960D8539F795D4E6F49A0F3351613FB7A9C6)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/vjay-jgXSiSGh3V8meB_sw/zh-cn_image_0000002571546480.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=6B9DAC7FC9B97AD2BC2AC0A9869A567A96853B64F362F22428BF2AE0987AD9B5)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/nBHIEYKpS6aSxZAr_A-ytQ/zh-cn_image_0000002571546506.png?HW-CC-KV=V1&HW-CC-Date=20260611T072923Z&HW-CC-Expire=86400&HW-CC-Sign=FF24A707B524C6804222B81B10B523644CB564ABA695447A399FDB7224B6B88C)
