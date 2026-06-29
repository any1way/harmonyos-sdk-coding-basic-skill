---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-ability
title: 添加Ability
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 添加Ability
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:08+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:d8f6e9fda020c8965b11e2fba8dd38555938f282257b2be32434132ec444d1d4
---
Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* FA（Feature Ability）模型： API 7开始支持的模型，已经不再主推。
* Stage模型：HarmonyOS 3.1 Developer Preview版本开始新增的模型，是目前主推且会长期演进的模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Windows窗口的“舞台”，因此称这种应用模型为Stage模型。

  Stage模型包含两种Ability组件类型：

  + UIAbility组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。详细介绍请参见[UIAbility组件概述](<../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件概述/uiability-overview.md>)。
  + ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。详细介绍请参见[ExtensionAbility概述](<../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/extensionability-overview.md>)。元服务暂不支持使用ExtensionAbility组件。

## Stage模型添加Ability

### 在模块中添加UIAbility

1. 选中对应的模块，单击鼠标右键，选择**New > Ability**。
2. 设置Ability名称，选择是否在设备主屏幕上显示该功能的启动图标，单击**Finish**完成Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ppcSfzs1Qdacb8FWyrr0KA/zh-cn_image_0000002571387590.png?HW-CC-KV=V1&HW-CC-Date=20260611T072208Z&HW-CC-Expire=86400&HW-CC-Sign=FCDDEC609B4C7D3AFBBDF7C9974F7F8101D59BF7FBFA3F23F817E8CAA72426B3)

### 在模块中添加Extension Ability

从DevEco Studio 6.1.0 Beta2版本开始，支持在API 23及以上Car设备工程的模块中添加RemoteNotificationAbility。

1. 在工程中选中对应的模块，单击鼠标右键，选择**New > Extension Ability**，选择不同的场景类型 。当前仅Application工程支持创建Extension Ability。
   * 若创建的模块类型为HAP，支持创建如下Extension Ability：
     + **EmbeddedUIExtensionAbility**：用于提供[跨进程界面嵌入](<../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/EmbeddedUIExtensionAbility/embeddeduiextensionability.md>)的能力。
     + **Backup****Ability**：用于提供[备份及恢复应用数据](<../../../../应用框架/Core File Kit（文件基础服务）/应用文件/应用数据备份恢复/应用数据备份恢复概述/app-file-backup-overview.md>)的能力。
     + **WorkScheduler**：用于提供[延迟任务](<../../../../应用框架/Background Tasks Kit（后台任务开发服务）/延迟任务(ArkTS)/work-scheduler.md>)的相关能力。
     + **RemoteNotificationAbility**：用于提供获取场景化消息数据和生命周期销毁的回调的通知能力，当前仅支持在Phone、Tablet、2in1、Car设备中使用。
     + **Driver**：用于提供[驱动相关扩展框架](<../../../../系统/硬件/Driver Development Kit（驱动开发服务）/扩展外设基础驱动开发/开发无UI界面基础驱动/driverextensionability.md>)。仅在当前工程的设备类型只含有2in1设备时，支持创建该类型。
   * 若创建的模块类型为HAR或HSP，支持创建以下两种Extension Ability：
     + **EmbeddedUIExtensionAbility**：用于提供[跨进程界面嵌入](<../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/EmbeddedUIExtensionAbility/embeddeduiextensionability.md>)的能力。
     + **WorkScheduler**：用于提供[延迟任务](<../../../../应用框架/Background Tasks Kit（后台任务开发服务）/延迟任务(ArkTS)/work-scheduler.md>)的相关能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/-Q0PdIrtREKrzs1YCvhcCw/zh-cn_image_0000002602066703.png?HW-CC-KV=V1&HW-CC-Date=20260611T072208Z&HW-CC-Expire=86400&HW-CC-Sign=B72200E46725ECE0523A85F6AC994EEEEDCFE602FD6FE77CE0D233CB3C07835F)
2. 设置Ability名称，单击Finish完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/2uK5whAGTjuNNr-7E9XwNw/zh-cn_image_0000002602066697.png?HW-CC-KV=V1&HW-CC-Date=20260611T072208Z&HW-CC-Expire=86400&HW-CC-Sign=DCB7A0A6E4B5674DF9634B393A60AA0D38F73EFC2755897658E8D699A9973D32)

## FA模型添加Ability

### 创建Particle Ability

1. 选中对应的模块，单击鼠标右键，选择**New > Ability** ，然后选择对应的Data Ability/Service Ability模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/shprzc6kSLGBG0AqynjNhA/zh-cn_image_0000002571547228.png?HW-CC-KV=V1&HW-CC-Date=20260611T072208Z&HW-CC-Expire=86400&HW-CC-Sign=97CDC9CD3E76B0F0DBBC9D69DD7C95B6202A7867EA51719F6A3EECAF70D40C40)
2. 根据选择的Ability模板，设置Ability的基本信息。
   * **Ability name**：Ability类名称，由大小写字母、数字和下划线组成。
   * **Language**：该Ability使用的开发语言。
3. 单击**Finish**完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。

### 创建Feature Ability

1. 选中对应的模块，单击鼠标右键，选择**New > Ability** ，然后选择对应的Page Ability模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Wtjpr2B0QGqvzDLFj29G6A/zh-cn_image_0000002571387580.png?HW-CC-KV=V1&HW-CC-Date=20260611T072208Z&HW-CC-Expire=86400&HW-CC-Sign=E903A139C5799577094B3FA12FCEB76431EC6386A6BD20A41B43029347E2C06D)
2. 根据选择的Ability模板，设置Ability的基本信息。
   * **Ability name**：Ability类名称，由大小写字母、数字和下划线组成。
   * **Launcher ability**：表示该Ability在终端桌面上是否有启动图标，一个HAP可以有多个启动图标，来启动不同的FA。
   * **Language**：该Ability使用的开发语言。
3. 单击**Finish**完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。
