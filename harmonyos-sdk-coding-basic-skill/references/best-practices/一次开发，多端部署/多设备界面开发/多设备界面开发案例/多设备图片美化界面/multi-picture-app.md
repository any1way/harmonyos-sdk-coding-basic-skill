---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-picture-app
title: 多设备图片美化界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备图片美化界面
category: best-practices
scraped_at: 2026-06-12T10:11:44+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:6fcbcfc0ede5b93b83ad8e86a694341fea8d928ea3fa084618b2b802e998d531
---
## 概述

本文从当前常见的多设备应用场景中，选取图片美化应用作为典型案例，详细介绍“一多”在实际开发中的应用。

图片美化应用的核心功能是用户交互，主要功能模块包含对话聊天、通讯录和社交圈等。开发者在开发“一多”应用时，常面临多端适配问题。本文针对图片美化应用的常见多端适配问题，提供解决方案。

应用当前已适配的设备包括：直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/arkui.md)和[一次开发，多端部署概览](../../../一次开发，多端部署概览/bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、页面开发三个角度，介绍图片美化应用在多设备开发中的最佳实践。

* [UX设计](multi-picture-app.md#section18771832172516)：介绍图片美化应用的交互逻辑和通用设计要点，对于类似的设计要点，开发者可以直接参考。
* [工程管理](multi-picture-app.md#section73711812196)：推荐“一多”项目采用分层架构，明确各层逻辑。同时，介绍图片美化应用适用的三层架构配置。
* [移动端页面](multi-picture-app.md#section202931220101020)和[电脑端页面](multi-picture-app.md#section5748352172710)：遵循实际应用开发流程，以页面为基本单元，逐项讲解各页面在窗口适配、页面开发的设计思路与实现方法。

## UX设计

图片美化应用的UX设计可参考社交通讯类多设备响应式设计指南的[拍摄美化类](https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples3-0000001746498074)章节，设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/kbZbSiAgRDSXfQFIOkiX1A/zh-cn_image_0000002610145561.png?HW-CC-KV=V1&HW-CC-Date=20260612T021131Z&HW-CC-Expire=86400&HW-CC-Sign=B42F088AFC3F9BE5863E0BC6D9D4EDD601D2B9A704A42EBBDB4D57A60D7CF445 "点击放大")

## 工程管理

为确保“一多”工程代码的可复用性与可维护性，推荐开发者采用分层架构组织代码工程。分层架构将项目划分为产品定制层（products）、基础特性层（features）和公共能力层（common）三个层级，各层级权责明确且功能独立，为开发者提供了清晰、高效且可扩展的设计架构。关于分层架构的具体设计细节，可参考[分层架构设计](../../../../应用架构/分层架构设计/bpta-layered-architecture-design.md)。

### 创建工程

建议开发者参考[多设备工程部署与发布](../../../多设备工程部署与发布/bpta-multi-device-ide.md)相关内容，在掌握分层架构工程的创建与配置方法后，创建模板项目工程，并根据图片美化应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

图片美化应用基于推荐的分层架构，按products、features、common三个层级组织代码工程。每个层级的设计如下：

* products层：图片美化应用需适配的设备包括直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。由于电脑设备的界面布局与其他设备差异较大，因此在products层单独创建名称为“pc”的HAP包作为电脑端的应用入口；直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备的界面布局整体相似，部分差异可通过“一多”[自适应布局](../../界面元素自适应变化/自适应布局/bpta-multi-device-adaptive-layout.md)和[响应式布局](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md)适配，因此在products层创建名称为“default”的HAP包作为这些设备的应用入口。
* features层：图片美化应用包含两个核心业务模块，分别为照片浏览（multipicturebrowsing）和照片编辑（multipictureediting）。在features层为两个业务模块分别创建对应的HAR包，供products层按需引用。两个业务模块相对独立，互不依赖，便于后续维护与迭代。
* common层：为提升代码复用性、减少冗余，在common层集中存放公共常量、路由跳转工具及窗口管理工具等需被多个模块共用的基础能力，供其他模块统一调用。

工程结构如下：

```
1. ├──features
2. │  ├──multipicturebrowsing                    // 照片浏览模块
3. │  │  └──src/main
4. │  │     ├──ets
5. │  │     │  ├──constants                      // 照片浏览常量类
6. │  │     │  ├──datasource                     // 照片数据源类
7. │  │     │  ├──model                          // 照片浏览模块数据模型
8. │  │     │  ├──view                           // 照片浏览模块视图
9. │  │     │  └──viewmodel                      // 照片浏览模块视图模型
10. │  │     └──resources                         // 照片浏览模块资源
11. │  └──multipictureediting                     // 照片编辑模块
12. │     └──src/main
13. │        ├──ets
14. │        │  ├──constants                      // 照片编辑常量类
15. │        │  ├──model                          // 照片编辑模块数据模型
16. │        │  ├──view                           // 照片编辑模块视图
17. │        │  └──viewmodel                      // 照片编辑模块视图模型
18. │        └──resources                         // 照片编辑模块资源
19. ├──multipicturecommon
20. │  └──src/main
21. │     ├──ets
22. │     │  ├──constants                         // 公共常量定义
23. │     │  └──utils                             // 工具类
24. │     └──resources                            // 公共资源
25. └──products
26. ├──multipicturedefaultsample                // 手机/平板设备
27. │  └──src/main
28. │     ├──ets
29. │     │  ├──constants                       // 常量类
30. │     │  ├──defaultability                  // 入口类
31. │     │  ├──defaultbackupability            // 应用数据备份恢复自定义拓展类
32. │     │  ├──model                           // 数据模型
33. │     │  ├──pages                           // 入口页面
34. │     │  ├──view                            // 视图
35. │     │  └──viewmodel                       // 视图模型
36. │     └──resources                          // 资源文件
37. └──multipicturepcsample                     // 电脑设备
38. └──src/main
39. ├──ets
40. │  ├──constants                        // 常量类
41. │  ├──model                            // 数据模型
42. │  ├──pages                            // 入口页面
43. │  ├──pcability                        // 入口类
44. │  └──pcbackupability                  // 应用数据备份恢复自定义拓展类
45. │  ├──view                             // 视图
46. │  └──viewmodel                        // 视图模型
47. └──resources                           // 资源文件
```

## 移动端页面

本章介绍如何针对直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备上的图片美化应用，使用“一多”布局能力，实现页面层级“一套代码、多端适配”的目标。同时，介绍这些设备上的窗口适配方案。

### 窗口适配

* 窗口模式

  适配设备支持全屏、分屏、悬浮窗和自由窗口模式，具体参见[窗口模式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode)。其中，分屏模式与悬浮窗无需特殊设计，可通过系统方式进入。应用内需监听窗口尺寸变化，[通过断点刷新UI](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section175001836203617)即可自动适配全屏、分屏、悬浮窗及自由窗口模式的布局。
* 窗口方向

  在类直板机型中推荐仅竖屏显示，在双折叠展开态、三折叠G态及平板等大屏幕场景下推荐支持四方向旋转，并受控于控制中心的旋转开关。图片美化类应用在module.json5配置文件中，建议设置orientation为FOLLOW\_DESKTOP，详细说明请参考[窗口方向](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction)。
* 窗口沉浸式

  根据UX设计要求，需实现不同窗口模式（全屏、分屏、悬浮窗、自由窗口）下的沉浸式效果，具体实现指南请参考[窗口沉浸式](../../多设备窗口形态/窗口沉浸式/bpta-multi-device-window-immersive.md)。推荐开发者采用组件级沉浸方案（通过组件设置页面沉浸）实现效果，同时需执行动态安全区避让，确保沉浸式显示效果。自由窗口模式下应使用window.[setWindowDecorVisible()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowdecorvisible11>)隐藏标题栏，仅保留右上角三键。此时，应用页面延伸至标题栏区域，实现沉浸式显示效果。

### 照片浏览页

图片美化应用的照片浏览页主要用于展示照片和提供分类导航，以满足用户查看不同相册照片的需求。根据功能设计，将照片浏览页的相关内容划分为4个区域，效果如下：

| 横向断点 | sm/md（横/纵断点） | sm | md | lg、xl |
| --- | --- | --- | --- | --- |
| 效果图 |  |  |  |  |

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 侧边导航栏 | 使用[HdsNavigation](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md>)组件实现，通过窗口宽度与高宽比，控制窗口变化时，修改mode单双栏显示。 |
| 2 | 顶部标题栏 | 使用[HdsNavDestination](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavDestination/ui-design-hdsnavdestination.md>)组件设置[titleBar](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#titlebar>)属性实现。在不同的设备宽度下组件自适应占满一屏。 |
| 3 | 底部导航栏 | 使用[HdsTabs](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md>)组件实现，通过[barFloatingStyle](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md#barfloatingstyle>)属性设置页签悬浮样式。 |
| 4 | 图片内容区 | 使用[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)组件实现，通过[@Env环境变量](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/响应式环境变量/@Env：环境变量/ts-env-system-property.md)修改不同断点下columnsTemplate，显示不同的列数，并设置图片的[aspectioRatio](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/布局约束/ts-universal-attributes-layout-constraints.md#aspectratio)属性固定宽高比。 |

### 照片编辑页

图片美化应用的照片编辑页主要用于一键套用预设滤镜，以满足用户的个性化表达需求。根据功能设计，将照片编辑页的相关内容划分为4个区域，效果如下：

| 横向断点 | sm/md（横/纵断点） | sm | md | lg |
| --- | --- | --- | --- | --- |
| 消息页 |  |  |  |  |

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 使用[Row](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md)组件自定义TitleView实现。在不同的设备宽度下组件自适应占满一屏。 |
| 2 | 底部/侧边工具栏 | 使用[Flex](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md)组件实现，通过窗口宽度与高宽比，控制窗口变化时，子组件排列方向为Row或Column。 |
| 3 | 图片内容区 | 使用堆叠容器[Stack](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Stack/ts-container-stack.md)组件嵌套[Image](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md)组件实现，设置图片的[aspectioRatio](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/布局约束/ts-universal-attributes-layout-constraints.md#aspectratio)属性固定宽高比。并通过监听断点变化，动态调整两侧边距。 |
| 4 | 警告弹窗 | 使用[警告弹窗AlertDialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/警告弹窗 (AlertDialog)/ts-methods-alert-dialog-box.md>)实现，仅在PuraX外屏等小屏场景弹出。 |

### 交互开发

在照片浏览页面，用户可通过双指缩放手势动态调整图片宫格布局的显示大小。双指向外张开时，宫格放大，每行图片数量减少；双指向内捏合时，宫格缩小，每行图片数量增多。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/mFp3Z7oMT1qR8E9rdDD4YA/zh-cn_image_0000002579625672.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021131Z&HW-CC-Expire=86400&HW-CC-Sign=1BECC709C9AD3B5F0687F90FA6FFE21082BB3C2CE931C3F5F8D23FA6CB8FF3A9 "点击放大")

使用[PinchGesture](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/基础手势/PinchGesture/ts-basic-gestures-pinchgesture.md)实现双指捏合手势触发时，动态修改Grid组件的显示列数。开发详情请参考[多设备交互](../../多设备交互/多设备交互/bpta-multi-interaction.md#section182814229423)或[示例代码](multi-picture-app.md#section23671643329)。

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案实现布局复用，以高效完成电脑设备上图片美化应用的界面开发，同时介绍电脑端的窗口适配方案。

### 窗口适配

* 窗口模式

  适配设备支持全屏与自由窗口模式，详情请参考[窗口模式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode)。应用内监听窗口尺寸变化，[通过断点刷新UI](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配全屏与自由窗口模式下的布局。
* 窗口方向

  电脑设备上应用的窗口方向跟随屏幕方向显示，不支持开发者自定义，相关内容请参考[窗口方向](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction)。
* 窗口沉浸式

  根据UX设计要求，需在自由窗口模式下实现沉浸式效果。推荐开发者使用window.setWindowDecorVisible(false)隐藏标题栏，仅保留右上角三键，并设置三键大小及右侧进行。此时应用页面拓展至标题栏区域，实现沉浸式显示效果，详情可参考[窗口沉浸式](../../多设备窗口形态/窗口沉浸式/bpta-multi-device-window-immersive.md)。

### 照片浏览页

图片美化应用的照片浏览页主要用于展示照片及分类导航，以满足用户查看不同相册照片的需求。根据功能设计，将照片浏览页相关内容划分为3个区域，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/EPmPiJJzQOiUipL0VjzwBw/zh-cn_image_0000002579785584.png?HW-CC-KV=V1&HW-CC-Date=20260612T021131Z&HW-CC-Expire=86400&HW-CC-Sign=61B65932872E5317AFDB477043CDD7AD2433182F88F1D4B5D9F6475A79605A43 "点击放大")

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 侧边导航栏 | 同移动端[照片浏览页](multi-picture-app.md#section6120145294418)对应区域的布局实现方案一致。 |
| 2 | 顶部标题栏 |
| 3 | 图片内容区 |

### 照片编辑页

图片美化应用的照片编辑页主要用于一键套用预设滤镜，以满足用户的个性化表达需求。根据功能设计，将照片编辑页的相关内容划分为3个区域，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/0JKnU9bzQpmBrtrA3pKJ1A/zh-cn_image_0000002610065459.png?HW-CC-KV=V1&HW-CC-Date=20260612T021131Z&HW-CC-Expire=86400&HW-CC-Sign=6ADAD6B44A19D694CB0CD47EB127465C737127BBC48669495465DDFA44B95A1D "点击放大")

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 同移动端[照片编辑页](multi-picture-app.md#section36831643877)对应区域的布局实现方案一致。 |
| 2 | 底部/侧边工具栏 |
| 3 | 图片内容区 |

### 交互开发

在照片浏览页面，电脑端支持通过触控屏或触控板的双指捏合操作实现图片宫格布局的动态缩放切换，两种交互事件均可由PinchGesture实现，详情可参考移动端[交互开发](multi-picture-app.md#section4985124512505)。

## 示例代码

* [多设备图片美化界面](https://gitcode.com/HarmonyOS_Samples/MultiPictureBeautification)
