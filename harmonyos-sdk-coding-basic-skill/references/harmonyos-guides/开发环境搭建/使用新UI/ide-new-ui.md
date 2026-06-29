---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-06-11T15:21:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a708c194531c1bd4df8a2835000ff37d3d9ac73abbd94acf933c075ce318dd28
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

启动DevEco Studio时，将有弹窗提示是否启用新用户界面。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/nI7wGAeLSZilwV7imT2r7w/zh-cn_image_0000002602186555.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=E37B03007B2245960477B2B8341A9CCAF82B0EDE7362171F8219D8118B7A17C1)

此外，可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/55RqlDzeQgOHcHf55SCioQ/zh-cn_image_0000002602066505.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=E54D02DFB43808FF453120E55FACDC35EFEB85C8FDD8F5ADE01B57F464408801)

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/nhlY4NZ9TR2M-0j4ei0m6g/zh-cn_image_0000002602186569.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=A55F7C5F9C3492B141D56B2A73E0739276A28BACEE62F33EA3B102C089B13713)图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/H8y_CdJpROO5fei6R3H7YQ/zh-cn_image_0000002571387386.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=7123ECF30209FD4B3FCC534CFE7F65812F67C49161763E61BC1433C84B36A8E4)图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ixPe7jKOTm-CHBaSIP414A/zh-cn_image_0000002571387400.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=A812D389CC2B99B3B2CF18D63BEC6ED80C227BB53D0E69E85ABD2D64F6BBC909)

如需将菜单栏展开并固定在主界面，可以在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**中，勾选**Show main menu in a separate toolbar**，点击**Apply**在主界面固定显示菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/PJaYdJPUQUy9Y-LVmyV8_A/zh-cn_image_0000002602066503.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=1B8788BEB2FC9BE145DC7EF9F678AAEA00D086A56F1EC5C752B08F21F9C2D131)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/vT4iEaCtRs6tS1uMQ321Xw/zh-cn_image_0000002602066509.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=7A0AD941B2C52BAA1CBF3F9A660F839C633D1A2C85A681A7BCCE06FA60483400)图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/_KkLqwpDSKynJe7ogPLPzA/zh-cn_image_0000002571547028.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=5EB5DBD474ED6AF52B5E87AC2C821675746DAC268F3B13DAF4B0E8E21B7A12C3)

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/m9gYxvLGTzuPfW3XmbXvJA/zh-cn_image_0000002602066511.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=F869B67D4DB2C9D68DBA3CF3D3E956C478829275A15437444522229623654037)

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/HMaxdMqURT6mlMo7zfVIow/zh-cn_image_0000002602066513.png?HW-CC-KV=V1&HW-CC-Date=20260611T071803Z&HW-CC-Expire=86400&HW-CC-Sign=FFBE9F923CBE48CB204C40507C18674343E7ED7263B7F1914E2901EC2BF1CF3F "点击放大")

说明

更多新用户界面变化详情，请参见[new UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
