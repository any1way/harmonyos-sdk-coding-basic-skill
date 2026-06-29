---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager
title: @ohos.bundle.bundleManager (应用程序包管理模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.bundleManager (应用程序包管理模块)
category: harmonyos-references
scraped_at: 2026-06-11T15:35:25+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:64182aa33bfcfb8f024b5b777b80e463adf740fc7159b161f25d913fa64f59f2
---
本模块提供应用信息的查询能力，支持应用包信息[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)、应用程序信息[ApplicationInfo](../../接口依赖的元素及定义/bundleManager/ApplicationInfo/js-apis-bundlemanager-applicationinfo.md)、UIAbility组件信息[AbilityInfo](../../接口依赖的元素及定义/bundleManager/AbilityInfo/js-apis-bundlemanager-abilityinfo.md)、ExtensionAbility组件信息[ExtensionAbilityInfo](../../接口依赖的元素及定义/bundleManager/ExtensionAbilityInfo/js-apis-bundlemanager-extensionabilityinfo.md)等信息的查询。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## BundleFlag

PhonePC/2in1TabletTVWearable

包信息标志，指示需要获取的包信息的内容。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET\_BUNDLE\_INFO\_DEFAULT | 0x00000000 | 获取默认包信息，不包含signatureInfo、applicationInfo、hapModuleInfo、ability、extensionAbility和permission的信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_APPLICATION | 0x00000001 | 用于获取包含applicationInfo的bundleInfo，获取的bundleInfo不包含signatureInfo、hapModuleInfo、ability、extensionAbility和permission的信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE | 0x00000002 | 用于获取包含hapModuleInfo的bundleInfo，获取的bundleInfo不包含signatureInfo、applicationInfo、ability、extensionAbility和permission的信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_ABILITY | 0x00000004 | 用于获取包含ability的bundleInfo，获取的bundleInfo不包含signatureInfo、applicationInfo、extensionAbility和permission的信息。单独使用不生效，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE一起使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY | 0x00000008 | 用于获取包含extensionAbility的bundleInfo，获取的bundleInfo不包含signatureInfo、applicationInfo、ability 和permission的信息。单独使用不生效，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE一起使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION | 0x00000010 | 用于获取包含permission的bundleInfo。获取的bundleInfo不包含signatureInfo、applicationInfo、hapModuleInfo、extensionAbility和ability的信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_METADATA | 0x00000020 | 用于获取applicationInfo、moduleInfo、abilityInfo和extensionAbilityInfo中包含的metadata。单独使用不生效，它需要与GET\_BUNDLE\_INFO\_WITH\_APPLICATION、GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE、GET\_BUNDLE\_INFO\_WITH\_ABILITY、GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY配合使用，其中：  - 获取applicationInfo中包含的metadata，需要与GET\_BUNDLE\_INFO\_WITH\_APPLICATION一起使用。  - 获取moduleInfo中包含的metadata，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE一起使用。  - 获取abilityInfo中包含的metadata，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE、GET\_BUNDLE\_INFO\_WITH\_ABILITY一起使用。  - 获取extensionAbilityInfo中包含的metadata，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE、GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY一起使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_DISABLE | 0x00000040 | 用于获取application被禁用的BundleInfo和被禁用的Ability信息。获取的bundleInfo不包含signatureInfo、applicationInfo、hapModuleInfo、ability、extensionAbility和permission的信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO | 0x00000080 | 用于获取包含signatureInfo的bundleInfo。获取的bundleInfo不包含applicationInfo、hapModuleInfo、extensionAbility、ability和permission的信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_MENU11+ | 0x00000100 | 用于获取包含fileContextMenuConfig的bundleInfo。单独使用不生效，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE一起使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_ROUTER\_MAP12+ | 0x00000200 | 用于获取包含routerMap的bundleInfo。单独使用不生效，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE一起使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_SKILL12+ | 0x00000800 | 用于获取包含skills的bundleInfo。单独使用不生效，需要与GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE、GET\_BUNDLE\_INFO\_WITH\_ABILITY、GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY一起使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| GET\_BUNDLE\_INFO\_WITH\_ENTRY\_MODULE23+ | 0x00010000 | 用于获取包含hapModuleInfo的bundleInfo，仅支持entry模块对应的bundleInfo.hapModulesInfo，如果entry模块不存在，bundleInfo.hapModulesInfo列表为空。获取的bundleInfo不包含signatureInfo、applicationInfo、ability、extensionAbility和permission的信息。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## ExtensionAbilityType

PhonePC/2in1TabletTVWearable

扩展组件的类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORM | 0 | [FormExtensionAbility](<../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)：卡片扩展能力，提供卡片开发能力。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| WORK\_SCHEDULER | 1 | [WorkSchedulerExtensionAbility](<../../../../Background Tasks Kit（后台任务开发服务）/ArkTS API/@ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)/js-apis-workschedulerextensionability.md>)：延时任务扩展能力，允许应用在系统闲时执行实时性不高的任务。 |
| INPUT\_METHOD | 2 | [InputMethodExtensionAbility](<../../../../IME Kit（输入法开发服务）/ArkTS API/@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)/js-apis-inputmethod-extension-ability.md>)：输入法扩展能力，用于开发输入法应用。 |
| ACCESSIBILITY | 4 | [AccessibilityExtensionAbility](<../../../../Accessibility Kit（无障碍服务）/ArkTS API/@ohos.application.AccessibilityExtensionAbility (辅助功能扩展能力)/js-apis-application-accessib_81754614.md>)：无障碍服务扩展能力，支持访问与操作前台界面。 |
| BACKUP | 9 | [BackupExtensionAbility](<../../../../Core File Kit（文件基础服务）/ArkTS API/@ohos.application.BackupExtensionAbility (备份恢复扩展能力)/js-apis-application-backupextensionability.md>)：数据备份扩展能力，提供应用数据的备份恢复能力。 |
| ENTERPRISE\_ADMIN | 11 | [EnterpriseAdminExtensionAbility](<../../../../基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）/js-apis-enterpriseadminextensionability.md>)：企业设备管理扩展能力，提供企业管理时处理管理事件的能力。 |
| SHARE10+ | 16 | [ShareExtensionAbility](<../../Stage模型能力的接口/@ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)/js-apis-_56257748.md>)：提供分享业务能力，为开发者提供基于UIExtension的分享业务模板。 |
| DRIVER10+ | 18 | [DriverExtensionAbility](<../../../../Driver Development Kit（驱动开发服务）/ArkTS API/@ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)/js-apis-app-ability-driverextensionability.md>)：驱动扩展能力，提供外设驱动扩展能力。应用配置了driver类型的ExtensionAbility后会被视为驱动应用，驱动应用在安装、卸载和恢复时不会区分用户，且创建新用户时也会安装设备上已有的驱动应用。例如，创建子用户时会默认安装主用户已有的驱动应用，在子用户上卸载驱动应用时，主用户上对应的驱动应用也会同时被卸载。 |
| ACTION10+ | 19 | [ActionExtensionAbility](<../../Stage模型能力的接口/@ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)/js-apis_45990614.md>)：自定义服务扩展能力，为开发者提供基于UIExtension的自定义操作业务模板。 |
| EMBEDDED\_UI12+ | 21 | [EmbeddedUIExtensionAbility](<../../Stage模型能力的接口/@ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)/js-apis_26985710.md>)：嵌入式UI扩展能力，提供跨进程界面嵌入的能力。 |
| INSIGHT\_INTENT\_UI12+ | 22 | InsightIntentUIExtensionAbility：为开发者提供能被小艺意图调用，以窗口形态呈现内容的扩展能力。 |
| FENCE18+ | 24 | [FenceExtensionAbility](<../../../../Location Kit（位置服务）/ArkTS API/@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)/js-apis-app-ability-fenceextensionability.md>)：为开发者提供地理围栏相关的能力，继承自ExtensionAbility。 |
| ASSET\_ACCELERATION18+ | 26 | AssetAccelerationExtensionAbility：资源预下载扩展能力，提供在设备闲时状态，进行后台资源预下载的能力。 |
| FORM\_EDIT18+ | 27 | [FormEditExtensionAbility](<../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility)/js-apis-app-form-formeditextensionability.md>)：为开发者提供卡片编辑的能力，继承自UIExtensionAbility。 |
| DISTRIBUTED20+ | 28 | [DistributedExtensionAbility](<../../../../Distributed Service Kit（分布式管理服务）/ArkTS API/@ohos.application.DistributedExtensionAbility (协同Extension)/js-apis-distributedextensionability.md>)：提供分布式相关扩展能力，提供分布式创建、销毁、连接的生命周期回调。 |
| APP\_SERVICE20+ | 29 | [AppServiceExtensionAbility](<../../Stage模型能力的接口/@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)/js-apis-app-ability-a_17903419.md>)：为企业普通应用提供后台服务能力。 |
| LIVE\_FORM20+ | 30 | [LiveFormExtensionAbility](<../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)/js-apis-app-form-liveformextensionability.md>)：互动卡片相关扩展能力，提供互动卡片创建、销毁的生命周期回调。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| SELECTION24+ | 31 | [SelectionExtensionAbility](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)/js-apis-selectioninput-s_31342665.md>)：为开发者提供划词弹窗能力的ExtensionAbility。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WEB\_NATIVE\_MESSAGING21+ | 32 | [WebNativeMessagingExtensionAbility](<../../../../ArkWeb（方舟Web）/ArkTS API/@ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)/arkts-apis-w_26610392.md>)：为开发者提供Web原生消息通信能力的ExtensionAbility。 |
| FAULT\_LOG21+ | 33 | [FaultLogExtensionAbility](<../../../../Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)/js-apis-hiviewdfx-faultlogextensionability.md>)：提供故障延迟通知的能力。 |
| NOTIFICATION\_SUBSCRIBER22+ | 34 | [NotificationSubscriberExtensionAbility](<../../../../Notification Kit（用户通知服务）/ArkTS API/@ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)/js-apis-notificatio_96645684.md>)：提供通知订阅的相关功能。 |
| CRYPTO22+ | 35 | [CryptoExtensionAbility](<../../../../../harmonyos-guides/系统/安全/Universal Keystore Kit（密钥管理服务）/外部密钥管理扩展/驱动HAP ExtensionAbility适配指导/CryptoExtensionAbility适配开发指导/huks-extension-ability-support-dev.md>)：提供外部密钥管理扩展的相关功能。 |
| PARTNER\_AGENT23+ | 36 | [PartnerAgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragentextensionability)：基于蓝牙通信技术，提供设备发现与设备下线的通知功能。  **模型约束**：此接口仅可在Stage模型下使用。 |
| AGENT24+ | 37 | [AgentExtensionAbility](<../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)：提供智能体扩展能力，包括智能体服务的创建、销毁、连接、断开的生命周期回调接口，以及接收客户端所发送数据和安全认证的回调接口。  **模型约束**：此接口仅可在Stage模型下使用。 |
| AGENT\_UI24+ | 38 | [AgentUIExtensionAbility](<../../Stage模型能力的接口/@ohos.app.ability.AgentUIExtensionAbility (带界面的智能体拓展组件)/js-apis-agent-agentuiextensionability.md>)：为开发者提供接入端侧Agent UI界面显示能力。  **模型约束**：此接口仅可在Stage模型下使用。 |
| UNSPECIFIED | 255 | 不指定类型。 |
| CALLER\_INFO\_QUERY19+ | 25 | [CallerInfoQueryExtensionAbility](<../../../../Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md>)：为开发者提供来去电信息查询能力。 |

## PermissionGrantState

PhonePC/2in1TabletTVWearable

权限授予状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERMISSION\_DENIED | -1 | 拒绝授予权限。 |
| PERMISSION\_GRANTED | 0 | 授予权限。 |

## SupportWindowMode

PhonePC/2in1TabletTVWearable

标识该组件所支持的窗口模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULL\_SCREEN | 0 | 窗口支持全屏显示。 |
| SPLIT | 1 | 窗口支持分屏显示。 |
| FLOATING | 2 | 支持窗口化显示，即显示悬浮窗口。 |

## LaunchType

PhonePC/2in1TabletTVWearable

标识组件的[启动模式](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件启动模式/uiability-launch-type.md>)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLETON | 0 | UIAbility的启动模式，表示单实例。 |
| MULTITON | 1 | UIAbility的启动模式，表示普通多实例。 |
| SPECIFIED | 2 | UIAbility的启动模式，表示该UIAbility内部根据业务自己指定多实例。 |

## AbilityType

PhonePC/2in1TabletTVWearable

标识Ability组件的类型。

**模型约束：** 仅可在FA模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAGE | 1 | UI界面类型的Ability。表示基于Page模板开发的FA，用于提供与用户交互的能力。 |
| SERVICE | 2 | 后台服务类型的Ability，无UI界面。表示基于Service模板开发的[PA（ParticleAbility）](<../../FA模型能力的接口/@ohos.ability.particleAbility (ParticleAbility模块)/js-apis-ability-particleability.md>)，用于提供后台运行任务的能力，例如后台下载或者播放音乐。 |
| DATA | 3 | 表示基于Data模板开发的[PA（ParticleAbility）](<../../FA模型能力的接口/@ohos.ability.particleAbility (ParticleAbility模块)/js-apis-ability-particleability.md>)，用于对外部提供统一的数据访问对象。 |

## DisplayOrientation

PhonePC/2in1TabletTVWearable

标识该Ability的显示模式。仅适用于FA模型的[PageAbility](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/FA模型开发指导/FA模型应用组件/PageAbility组件开发指导/PageAbility组件概述/pageability-overview.md>)。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 表示未定义方向模式，由系统判定。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LANDSCAPE | 1 | 表示横屏显示模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PORTRAIT | 2 | 表示竖屏显示模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FOLLOW\_RECENT | 3 | 表示跟随上一个显示模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LANDSCAPE\_INVERTED | 4 | 表示反向横屏显示模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PORTRAIT\_INVERTED | 5 | 表示反向竖屏显示模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION | 6 | 表示传感器在旋转到横向和竖向时，页面会自动旋转。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_LANDSCAPE | 7 | 表示传感器在旋转到横向时，页面会自动旋转。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_PORTRAIT | 8 | 表示传感器在旋转到竖向时，页面会自动旋转。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_RESTRICTED | 9 | 表示受开关控制的自动旋转模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | 表示受开关控制的自动横向旋转模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 11 | 表示受开关控制的自动竖向旋转模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LOCKED | 12 | 表示锁定模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_UNSPECIFIED12+ | 13 | 受开关控制和由系统判定的自动旋转模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FOLLOW\_DESKTOP12+ | 14 | 跟随桌面的旋转模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## CompatiblePolicy10+

PhonePC/2in1TabletTVWearable

标识动态共享库的版本兼容类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKWARD\_COMPATIBILITY | 1 | 共享库是向后兼容类型。 |

## ModuleType

PhonePC/2in1TabletTVWearable

标识模块类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTRY | 1 | 应用的主模块，作为应用的入口，提供了应用的基础功能。 |
| FEATURE | 2 | 应用的动态特性模块，作为应用能力的扩展，可以根据用户的需求和设备类型进行选择性安装。 |
| SHARED | 3 | 应用的[动态共享库](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)模块。 |

## BundleType

PhonePC/2in1TabletTVWearable

标识应用的类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP | 0 | 该Bundle是应用。 |
| ATOMIC\_SERVICE | 1 | 该Bundle是元服务。 |

## MultiAppModeType12+

PhonePC/2in1TabletTVWearable

标识应用多开的模式类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 未指定类型，表示[multiAppMode配置](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/app.json5配置文件/app-configuration-file.md#multiappmode标签)未配置时的默认状态。 |
| MULTI\_INSTANCE | 1 | [多实例模式](../../../../../harmonyos-guides/基础入门/开发基础知识/典型场景的开发指导/创建应用多实例/multiinstance.md)。常驻进程不支持该字段。 |
| APP\_CLONE | 2 | [分身模式](../../../../../harmonyos-guides/基础入门/开发基础知识/典型场景的开发指导/创建应用分身/app-clone.md)。 |

## AbilityFlag20+

PhonePC/2in1TabletTVWearable

Ability组件信息标志，指示需要获取的Ability组件信息的内容。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET\_ABILITY\_INFO\_DEFAULT | 0x00000000 | 获取默认[AbilityInfo](../../接口依赖的元素及定义/bundleManager/AbilityInfo/js-apis-bundlemanager-abilityinfo.md)，获取的AbilityInfo不包含permissions、metadata、被禁用Ability对应的AbilityInfo。 |
| GET\_ABILITY\_INFO\_WITH\_PERMISSION | 0x00000001 | 获取包含permissions的AbilityInfo。 |
| GET\_ABILITY\_INFO\_WITH\_APPLICATION | 0x00000002 | 获取包含applicationInfo的AbilityInfo。 |
| GET\_ABILITY\_INFO\_WITH\_METADATA | 0x00000004 | 获取包含metadata的AbilityInfo。 |
| GET\_ABILITY\_INFO\_WITH\_DISABLE | 0x00000008 | 获取被禁用Ability对应的AbilityInfo。 |
| GET\_ABILITY\_INFO\_ONLY\_SYSTEM\_APP | 0x00000010 | 获取系统应用对应的AbilityInfo。 |
| GET\_ABILITY\_INFO\_WITH\_APP\_LINKING | 0x00000040 | 获取通过[域名校验](<../../../../../harmonyos-guides/应用服务/App Linking Kit（应用链接服务）/通过App Linking应用链接拉起指定应用/app-linking-startupapp.md#在modulejson5中配置关联的网址域名>)筛选的AbilityInfo。 |
| GET\_ABILITY\_INFO\_WITH\_SKILL | 0x00000080 | 获取包含skills的AbilityInfo。 |

## bundleManager.getBundleInfoForSelf

PhonePC/2in1TabletTVWearable

getBundleInfoForSelf(bundleFlags: number): Promise<BundleInfo>

根据给定的bundleFlags获取当前应用的BundleInfo。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)> | Promise对象，返回当前应用的BundleInfo。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. // 获取bundleInfo，包含带有metadataArray信息的appInfo信息
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let bundleFlags =
7. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;

9. try {
10. bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
11. hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
14. });
15. } catch (err) {
16. let message = (err as BusinessError).message;
17. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
18. }
```

## bundleManager.getBundleInfoForSelf

PhonePC/2in1TabletTVWearable

getBundleInfoForSelf(bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

根据给定的bundleFlags获取当前应用的BundleInfo。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |
| callback | AsyncCallback<[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)> | 是 | [回调函数](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#asynccallback>)，当获取成功时，err为undefined，data为获取到的当前应用的BundleInfo；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. // 获取bundleInfo，包含permissions信息的abilitiesInfo信息
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let bundleFlags =
7. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_HAP_MODULE | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_ABILITY |
8. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;

10. try {
11. bundleManager.getBundleInfoForSelf(bundleFlags, (err, data) => {
12. if (err) {
13. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', err.message);
14. } else {
15. hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully: %{public}s', JSON.stringify(data));
16. }
17. });
18. } catch (err) {
19. let message = (err as BusinessError).message;
20. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
21. }
```

## bundleManager.getProfileByAbility

PhonePC/2in1TabletTVWearable

getProfileByAbility(moduleName: string, abilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void

根据给定的moduleName、abilityName和metadataName（module.json5中[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)下的metadata标签的name）获取自身相应配置文件的json格式字符串。使用callback异步回调。

说明：

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res\_id），开发者可以通过[资源管理模块](<../../../../Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)的相关接口，来获取引用的资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 表示Module名称。 |
| abilityName | string | 是 | 表示UIAbility组件的名称。 |
| metadataName | string | 是 | 表示UIAbility组件的[元信息名称](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)，即module.json5配置文件中[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)下的metadata标签的name。 |
| callback | AsyncCallback<Array<string>> | 是 | [回调函数](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#asynccallback>)，当获取成功时，err为undefined，data为获取到的Array<string>；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified abilityName is not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |
| 17700029 | The specified ability is disabled. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let abilityName = 'EntryAbility';
7. let metadataName = 'ability_metadata';

9. try {
10. bundleManager.getProfileByAbility(moduleName, abilityName, metadataName, (err, data) => {
11. if (err) {
12. hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', err.message);
13. } else {
14. hilog.info(0x0000, 'testTag', 'getProfileByAbility successfully: %{public}s', JSON.stringify(data));
15. }
16. });
17. } catch (err) {
18. let message = (err as BusinessError).message;
19. hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', message);
20. }
```

## bundleManager.getProfileByAbility

PhonePC/2in1TabletTVWearable

getProfileByAbility(moduleName: string, abilityName: string, metadataName?: string): Promise<Array<string>>

根据给定的moduleName、abilityName和metadataName（module.json5中[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)下的metadata标签的name）获取自身相应配置文件的json格式字符串。使用Promise异步回调。

说明：

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res\_id），开发者可以通过[资源管理模块](<../../../../Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)的相关接口，来获取引用的资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 表示Module名称。 |
| abilityName | string | 是 | 表示UIAbility组件的名称。 |
| metadataName | string | 否 | 表示UIAbility组件的元信息名称，即module.json5配置文件中[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)下的metadata标签的name，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回Array<string>。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified abilityName is not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |
| 17700029 | The specified ability is disabled. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let abilityName = 'EntryAbility';

8. try {
9. // 通过模块名称和ability名称获取相应配置文件的json格式字符串信息
10. bundleManager.getProfileByAbility(moduleName, abilityName).then((data) => {
11. hilog.info(0x0000, 'testTag', 'getProfileByAbility successfully. Data: %{public}s', JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', err.message);
14. });
15. } catch (err) {
16. let message = (err as BusinessError).message;
17. hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', message);
18. }
```

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let abilityName = 'EntryAbility';
7. let metadataName = 'ability_metadata';

9. try {
10. // 通过模块名称，ability名称和UIAbility组件的元信息名称获取自身相应配置文件的json格式字符串信息
11. bundleManager.getProfileByAbility(moduleName, abilityName, metadataName).then((data) => {
12. hilog.info(0x0000, 'testTag', 'getProfileByAbility successfully. Data: %{public}s', JSON.stringify(data));
13. }).catch((err: BusinessError) => {
14. hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', err.message);
15. });
16. } catch (err) {
17. let message = (err as BusinessError).message;
18. hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', message);
19. }
```

## bundleManager.getProfileByAbilitySync10+

PhonePC/2in1TabletTVWearable

getProfileByAbilitySync(moduleName: string, abilityName: string, metadataName?: string): Array<string>

以同步方法根据给定的moduleName、abilityName和metadataName（module.json5中[metadata标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)下的name）获取自身相应配置文件的json格式字符串，返回对象为string数组。

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res\_id），开发者可以通过[资源管理模块](<../../../../Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)的相关接口，来获取引用的资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 表示Module名称。 |
| abilityName | string | 是 | 表示UIAbility组件的名称。 |
| metadataName | string | 否 | 表示UIAbility组件的元信息名称，即module.json5配置文件中[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)下的metadata标签的name，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 数组对象，返回Array<string>。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified abilityName is not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |
| 17700029 | The specified ability is disabled. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let abilityName = 'EntryAbility';

8. try {
9. // 通过模块名称和ability名称获取相应配置文件的json格式字符串信息
10. let data = bundleManager.getProfileByAbilitySync(moduleName, abilityName);
11. hilog.info(0x0000, 'testTag', 'getProfileByAbilitySync successfully. Data: %{public}s', JSON.stringify(data));
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. hilog.error(0x0000, 'testTag', 'getProfileByAbilitySync failed. Cause: %{public}s', message);
15. }
```

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName: string = 'entry';
6. let abilityName: string = 'EntryAbility';
7. let metadataName: string = 'ability_metadata';

9. try {
10. // 通过模块名称，ability名称和UIAbility组件的元信息名称获取相应配置文件的json格式字符串信息
11. let data = bundleManager.getProfileByAbilitySync(moduleName, abilityName, metadataName);
12. hilog.info(0x0000, 'testTag', 'getProfileByAbilitySync successfully. Data: %{public}s', JSON.stringify(data));
13. } catch (err) {
14. let message = (err as BusinessError).message;
15. hilog.error(0x0000, 'testTag', 'getProfileByAbilitySync failed. Cause: %{public}s', message);
16. }
```

## bundleManager.getProfileByExtensionAbility

PhonePC/2in1TabletTVWearable

getProfileByExtensionAbility(moduleName: string, extensionAbilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void

根据给定的moduleName、extensionAbilityName和metadataName（module.json5中[metadata标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)下的name）获取自身相应配置文件的json格式字符串。使用callback异步回调。

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res\_id），开发者可以通过[资源管理模块](<../../../../Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)的相关接口，来获取引用的资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 表示Module名称。 |
| extensionAbilityName | string | 是 | 表示ExtensionAbility组件的名称。 |
| metadataName | string | 是 | 表示ExtensionAbility组件的元信息名称，即module.json5配置文件中[extensionAbilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#extensionabilities标签)下的metadata标签的name。 |
| callback | AsyncCallback<Array<string>> | 是 | [回调函数](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#asynccallback>)，当获取成功时，err为undefined，data为获取到的Array<string>；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified extensionAbilityName not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let extensionAbilityName = 'com.example.myapplication.extension';
7. let metadataName = 'ability_metadata';

9. try {
10. bundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName, metadataName, (err, data) => {
11. if (err) {
12. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed: %{public}s', err.message);
13. } else {
14. hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbility successfully: %{public}s', JSON.stringify(data));
15. }
16. });
17. } catch (err) {
18. let message = (err as BusinessError).message;
19. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed: %{public}s', message);
20. }
```

## bundleManager.getProfileByExtensionAbility

PhonePC/2in1TabletTVWearable

getProfileByExtensionAbility(moduleName: string, extensionAbilityName: string, metadataName?: string): Promise<Array<string>>

根据给定的moduleName、extensionAbilityName和metadataName（module.json5中[metadata标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)下的name）获取自身相应配置文件的json格式字符串。使用Promise异步回调。

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res\_id），开发者可以通过[资源管理模块](<../../../../Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)的相关接口，来获取引用的资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 表示Module名称。 |
| extensionAbilityName | string | 是 | 表示ExtensionAbility组件的名称。 |
| metadataName | string | 否 | 表示ExtensionAbility组件的元信息名称，即module.json5配置文件中[extensionAbilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#extensionabilities标签)下的metadata标签的name，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回Array<string>对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified extensionAbilityName not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let extensionAbilityName = 'com.example.myapplication.extension';
7. let metadataName = 'ability_metadata';

9. try {
10. bundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName).then((data) => {
11. hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbility successfully. Data: %{public}s', JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', err.message);
14. });
15. } catch (err) {
16. let message = (err as BusinessError).message;
17. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', message);
18. }

20. try {
21. bundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName, metadataName).then((data) => {
22. hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbility successfully. Data: %{public}s', JSON.stringify(data));
23. }).catch((err: BusinessError) => {
24. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', err.message);
25. });
26. } catch (err) {
27. let message = (err as BusinessError).message;
28. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', message);
29. }
```

## bundleManager.getProfileByExtensionAbilitySync10+

PhonePC/2in1TabletTVWearable

getProfileByExtensionAbilitySync(moduleName: string, extensionAbilityName: string, metadataName?: string): Array<string>

以同步方法根据给定的moduleName、extensionAbilityName和metadataName（module.json5中[metadata标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)下的name）获取自身相应配置文件的json格式字符串，返回对象为string数组。

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res\_id），开发者可以通过[资源管理模块](<../../../../Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)的相关接口，来获取引用的资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 表示Module名称。 |
| extensionAbilityName | string | 是 | 表示ExtensionAbility组件的名称。 |
| metadataName | string | 否 | 表示ExtensionAbility组件的元信息名称，即module.json5配置文件中[extensionAbilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#extensionabilities标签)下的metadata标签的name，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回Array<string>对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified extensionAbilityName not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let moduleName = 'entry';
6. let extensionAbilityName = 'com.example.myapplication.extension';
7. let metadataName = 'ability_metadata';

9. try {
10. let data = bundleManager.getProfileByExtensionAbilitySync(moduleName, extensionAbilityName);
11. hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbilitySync successfully. Data: %{public}s',
12. JSON.stringify(data));
13. } catch (err) {
14. let message = (err as BusinessError).message;
15. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbilitySync failed. Cause: %{public}s', message);
16. }

18. try {
19. let data = bundleManager.getProfileByExtensionAbilitySync(moduleName, extensionAbilityName, metadataName);
20. hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbilitySync successfully. Data: %{public}s',
21. JSON.stringify(data));
22. } catch (err) {
23. let message = (err as BusinessError).message;
24. hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbilitySync failed. Cause: %{public}s', message);
25. }
```

## bundleManager.getBundleInfoForSelfSync10+

PhonePC/2in1TabletTVWearable

getBundleInfoForSelfSync(bundleFlags: number): BundleInfo

以同步方法根据给定的bundleFlags获取当前应用的BundleInfo。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md) | 返回BundleInfo对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;

7. try {
8. let data = bundleManager.getBundleInfoForSelfSync(bundleFlags);
9. hilog.info(0x0000, 'testTag', 'getBundleInfoForSelfSync successfully: %{public}s', JSON.stringify(data));
10. } catch (err) {
11. let message = (err as BusinessError).message;
12. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelfSync failed: %{public}s', message);
13. }
```

## bundleManager.canOpenLink12+

PhonePC/2in1TabletTVWearable

canOpenLink(link: string): boolean

根据给定的链接判断目标应用是否可访问，链接中的scheme需要在[module.json5文件](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)的querySchemes字段下配置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| link | string | 是 | 表示需要查询的链接。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示给定的链接可以打开，返回false表示给定的链接不能打开。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700055 | The specified link is invalid. |
| 17700056 | The scheme of the specified link is not in the querySchemes. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let link = 'welink://';
7. let data = bundleManager.canOpenLink(link);
8. hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(data));
9. } catch (err) {
10. let message = (err as BusinessError).message;
11. hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
12. }
```

## bundleManager.getLaunchWant13+

PhonePC/2in1TabletTVWearable

getLaunchWant(): Want

获取本应用[入口UIAbility](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包术语/application-package-glossary.md#uiability)的Want参数。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Want](<../@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 返回仅包含bundleName和abilityName的Want对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17700072 | The launch want is not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { bundleManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let want = bundleManager.getLaunchWant();
7. hilog.info(0x0000, 'testTag', 'getLaunchWant ability name: %{public}s', want.abilityName);
8. hilog.info(0x0000, 'testTag', 'getLaunchWant bundle name: %{public}s', want.bundleName);
9. } catch (error) {
10. let message = (error as BusinessError).message;
11. hilog.error(0x0000, 'testTag', 'getLaunchWant failed: %{public}s', message);
12. }
```

## bundleManager.getBundleInfo14+

PhonePC/2in1TabletTVWearable

getBundleInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<BundleInfo>): void

根据给定的bundleName、bundleFlags和userId获取[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)。使用callback异步回调。

获取调用方自身信息时不需要权限。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示要查询的应用Bundle名称。 |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |
| userId | number | 是 | 表示用户ID，可以通过[getOsAccountLocalId接口](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md#getosaccountlocalid9>)获取。 |
| callback | AsyncCallback<[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)> | 是 | [回调函数](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#asynccallback>)，当获取成功时，err为undefined，data为获取到的bundleInfo；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |
| 17700026 | The specified bundle is disabled. |

**示例：**

```
1. // 额外获取包含AbilityInfo信息的bundleInfo
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let bundleName = 'com.example.myapplication';
7. let bundleFlags =
8. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_HAP_MODULE | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_ABILITY;
9. let userId = 100;

11. try {
12. bundleManager.getBundleInfo(bundleName, bundleFlags, userId, (err, data) => {
13. if (err) {
14. hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', err.message);
15. } else {
16. hilog.info(0x0000, 'testTag', 'getBundleInfo successfully: %{public}s', JSON.stringify(data));
17. }
18. });
19. } catch (err) {
20. let message = (err as BusinessError).message;
21. hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', message);
22. }
```

```
1. // 额外获取包含ApplicationInfo中的metadata的bundleInfo
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let bundleName = 'com.example.myapplication';
7. let bundleFlags =
8. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
9. let userId = 100;

11. try {
12. bundleManager.getBundleInfo(bundleName, bundleFlags, userId, (err, data) => {
13. if (err) {
14. hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', err.message);
15. } else {
16. hilog.info(0x0000, 'testTag', 'getBundleInfo successfully: %{public}s', JSON.stringify(data));
17. }
18. });
19. } catch (err) {
20. let message = (err as BusinessError).message;
21. hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', message);
22. }
```

## bundleManager.getBundleInfo14+

PhonePC/2in1TabletTVWearable

getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

根据给定的bundleName和bundleFlags获取BundleInfo。使用callback异步回调。

获取调用方自身的信息时不需要权限。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示要查询的应用Bundle名称。 |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |
| callback | AsyncCallback<[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)> | 是 | [回调函数](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#asynccallback>)，当获取成功时，err为undefined，data为获取到的BundleInfo；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700026 | The specified bundle is disabled. |

**示例：**

```
1. // 额外获取extensionAbility
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let bundleName = 'com.example.myapplication';
7. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_HAP_MODULE |
8. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY;

10. try {
11. bundleManager.getBundleInfo(bundleName, bundleFlags, (err, data) => {
12. if (err) {
13. hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', err.message);
14. } else {
15. hilog.info(0x0000, 'testTag', 'getBundleInfo successfully: %{public}s', JSON.stringify(data));
16. }
17. });
18. } catch (err) {
19. let message = (err as BusinessError).message;
20. hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', message);
21. }
```

## bundleManager.getBundleInfo14+

PhonePC/2in1TabletTVWearable

getBundleInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<BundleInfo>

根据给定的bundleName、bundleFlags和userId获取BundleInfo。使用Promise异步回调。

获取调用方自身的信息时不需要权限。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示要查询的应用Bundle名称。 |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |
| userId | number | 否 | 表示用户ID，可以通过[getOsAccountLocalId接口](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md#getosaccountlocalid9>)获取，默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md)> | Promise对象，返回BundleInfo。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |
| 17700026 | The specified bundle is disabled. |

**示例：**

```
1. // 额外获取ApplicationInfo和SignatureInfo
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let bundleName = 'com.example.myapplication';
7. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
8. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
9. let userId = 100;

11. try {
12. bundleManager.getBundleInfo(bundleName, bundleFlags, userId).then((data) => {
13. hilog.info(0x0000, 'testTag', 'getBundleInfo successfully. Data: %{public}s', JSON.stringify(data));
14. }).catch((err: BusinessError) => {
15. hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', err.message);
16. });
17. } catch (err) {
18. let message = (err as BusinessError).message;
19. hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', message);
20. }
```

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let bundleName = 'com.example.myapplication';
6. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;

8. try {
9. bundleManager.getBundleInfo(bundleName, bundleFlags).then((data) => {
10. hilog.info(0x0000, 'testTag', 'getBundleInfo successfully. Data: %{public}s', JSON.stringify(data));
11. }).catch((err: BusinessError) => {
12. hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', err.message);
13. });
14. } catch (err) {
15. let message = (err as BusinessError).message;
16. hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', message);
17. }
```

## bundleManager.getBundleInfoSync14+

PhonePC/2in1TabletTVWearable

getBundleInfoSync(bundleName: string, bundleFlags: number, userId: number): BundleInfo

以同步方法根据给定的bundleName、bundleFlags和userId获取BundleInfo。

获取调用方自身的信息时不需要权限。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示要查询的应用Bundle名称。 |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |
| userId | number | 是 | 表示用户ID，可以通过[getOsAccountLocalId接口](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md#getosaccountlocalid9>)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md) | 返回BundleInfo对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |
| 17700026 | The specified bundle is disabled. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let bundleName = 'com.example.myapplication';
6. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
7. let userId = 100;

9. try {
10. let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
11. hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
15. }
```

## bundleManager.getBundleInfoSync14+

PhonePC/2in1TabletTVWearable

getBundleInfoSync(bundleName: string, bundleFlags: number): BundleInfo

以同步方法根据给定的bundleName、bundleFlags获取调用方所在用户下的BundleInfo。

获取调用方自身的信息时不需要权限。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示要查询的应用Bundle名称。 |
| [bundleFlags](js-apis-bundlemanager.md#bundleflag) | number | 是 | 指定返回的BundleInfo所包含的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md) | 返回BundleInfo对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700026 | The specified bundle is disabled. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let bundleName = 'com.example.myapplication';
6. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
7. try {
8. let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags);
9. hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
10. } catch (err) {
11. let message = (err as BusinessError).message;
12. hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
13. }
```

## bundleManager.getBundleNameByUid14+

PhonePC/2in1TabletTVWearable

getBundleNameByUid(uid: number, callback: AsyncCallback<string>): void

根据给定的uid获取对应应用的bundleName。使用callback异步回调。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 表示应用程序的UID。 |
| callback | AsyncCallback<string> | 是 | [回调函数](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#asynccallback>)，当获取成功时，err为undefined，data为获取到的BundleName；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let uid = 20010005;
6. try {
7. bundleManager.getBundleNameByUid(uid, (err, data) => {
8. if (err) {
9. hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed: %{public}s', err.message);
10. } else {
11. hilog.info(0x0000, 'testTag', 'getBundleNameByUid successfully: %{public}s', JSON.stringify(data));
12. }
13. });
14. } catch (err) {
15. let message = (err as BusinessError).message;
16. hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed: %{public}s', message);
17. }
```

## bundleManager.getBundleNameByUid14+

PhonePC/2in1TabletTVWearable

getBundleNameByUid(uid: number): Promise<string>

根据给定的uid获取对应应用的bundleName。使用Promise异步回调。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 表示应用程序的UID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回bundleName。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let uid = 20010005;
6. try {
7. bundleManager.getBundleNameByUid(uid).then((data) => {
8. hilog.info(0x0000, 'testTag', 'getBundleNameByUid successfully. Data: %{public}s', JSON.stringify(data));
9. }).catch((err: BusinessError) => {
10. hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed. Cause: %{public}s', err.message);
11. });
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed. Cause: %{public}s', message);
15. }
```

## bundleManager.getBundleNameByUidSync14+

PhonePC/2in1TabletTVWearable

getBundleNameByUidSync(uid: number): string

以同步方法根据给定的uid获取对应应用的bundleName。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 表示应用程序的UID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取到的bundleName。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let uid = 20010005;
6. try {
7. let data = bundleManager.getBundleNameByUidSync(uid);
8. hilog.info(0x0000, 'testTag', 'getBundleNameByUidSync successfully. Data: %{public}s', JSON.stringify(data));
9. } catch (err) {
10. let message = (err as BusinessError).message;
11. hilog.error(0x0000, 'testTag', 'getBundleNameByUidSync failed. Cause: %{public}s', message);
12. }
```

## bundleManager.getAppCloneIdentity14+

PhonePC/2in1TabletTVWearable

getAppCloneIdentity(uid: number): Promise<AppCloneIdentity>;

根据uid查询分身应用的包名和分身索引。使用Promise异步回调。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

* 当调用方为三方应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED权限。
* 当调用方为系统应用时，需要申请ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED或者ohos.permission.GET\_BUNDLE\_INFO权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 表示应用程序的UID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AppCloneIdentity](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#appcloneidentity14)> | Promise对象，返回<AppCloneIdentity>。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let uid = 20010005;

7. try {
8. bundleManager.getAppCloneIdentity(uid).then((res) => {
9. hilog.info(0x0000, 'testTag', 'getAppCloneIdentity res = %{public}s', JSON.stringify(res));
10. }).catch((err: BusinessError) => {
11. hilog.error(0x0000, 'testTag', 'getAppCloneIdentity failed. Cause: %{public}s', err.message);
12. });
13. } catch (err) {
14. let message = (err as BusinessError).message;
15. hilog.error(0x0000, 'testTag', 'getAppCloneIdentity failed. Cause: %{public}s', message);
16. }
```

## bundleManager.getSignatureInfo18+

PhonePC/2in1TabletTVWearable

getSignatureInfo(uid: number): SignatureInfo

根据给定的uid获取对应应用的[签名信息](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#signatureinfo)。

**需要权限：** ohos.permission.GET\_SIGNATURE\_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 表示应用程序的UID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SignatureInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#signatureinfo) | 返回SignatureInfo对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 17700021 | The uid is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let uid = 20010005; // uid需要替换为对应应用程序的UID。
6. try {
7. let data = bundleManager.getSignatureInfo(uid);
8. hilog.info(0x0000, 'testTag', 'getSignatureInfo successfully. Data: %{public}s', JSON.stringify(data));
9. } catch (err) {
10. let message = (err as BusinessError).message;
11. hilog.error(0x0000, 'testTag', 'getSignatureInfo failed. Cause: %{public}s', message);
12. }
```

## bundleManager.getAbilityInfo20+

PhonePC/2in1TabletTVWearable

getAbilityInfo(uri: string, abilityFlags: number): Promise<Array<AbilityInfo>>

获取指定资源标识符和组件信息标志对应的Ability信息。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.GET\_ABILITY\_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**设备行为差异：** 该接口仅在PC/2in1设备中可正常调用，在其他设备中返回201错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示统一资源标识符URI，取值与[module.json5配置文件中skills下的uris字段](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#skills标签)相对应。 |
| abilityFlags | number | 是 | 表示[Ability组件信息标志](js-apis-bundlemanager.md#abilityflag20)，指示需要获取的Ability组件信息的内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AbilityInfo](../../接口依赖的元素及定义/bundleManager/AbilityInfo/js-apis-bundlemanager-abilityinfo.md)>> | Promise对象，返回获取到的Ability信息数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 17700003 | The ability is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let abilityFlags = bundleManager.AbilityFlag.GET_ABILITY_INFO_WITH_APPLICATION;
6. let uri = "https://www.example.com";

8. try {
9. bundleManager.getAbilityInfo(uri, abilityFlags).then((data) => {
10. hilog.info(0x0000, 'testTag', 'getAbilityInfo successfully. Data: %{public}s', JSON.stringify(data));
11. }).catch((err: BusinessError) => {
12. let message = (err as BusinessError).message;
13. hilog.error(0x0000, 'testTag', 'getAbilityInfo failed. Cause: %{public}s', message);
14. });
15. } catch (err) {
16. let message = (err as BusinessError).message;
17. hilog.error(0x0000, 'testTag', 'getAbilityInfo failed. Cause: %{public}s', message);
18. }
```

## bundleManager.cleanBundleCacheFilesForSelf21+

PhonePC/2in1TabletTVWearable

cleanBundleCacheFilesForSelf(): Promise<void>

清理应用自身的缓存。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. bundleManager.cleanBundleCacheFilesForSelf().then(() => {
5. hilog.info(0x0000, 'testTag', 'cleanBundleCacheFilesForSelf complete.');
6. });
```

## bundleManager.getPluginBundlePathForSelf22+

PhonePC/2in1TabletTVWearable

getPluginBundlePathForSelf(pluginBundleName: string): string

获取指定插件在当前[应用沙箱](<../../../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md>)内的安装路径。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pluginBundleName | string | 是 | 目标插件的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 目标插件在当前应用沙箱内的安装路径。 |

**错误码：**

错误码请参见[ohos.bundle错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17700001 | The specified bundleName is not found. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 请开发者替换为实际插件对应的包名
6. let pluginBundleName = 'com.ohos.pluginDemo';
7. try {
8. let path = bundleManager.getPluginBundlePathForSelf(pluginBundleName);
9. hilog.info(0x0000, 'testTag', 'getPluginBundlePathForSelf successfully. path: %{public}s', path);
10. } catch (err) {
11. let message = (err as BusinessError).message;
12. hilog.error(0x0000, 'testTag', 'getPluginBundlePathForSelf failed. Cause: %{public}s', message);
13. }
```

## bundleManager.getLaunchWantForBundleSync24+

PhonePC/2in1TabletTVWearable

getLaunchWantForBundleSync(bundleName: string, userId?: number): Want

根据给定的包名和用户ID，获取用于启动应用程序的Want参数。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 (ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 和 ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS)

* 获取用于启动当前用户下的应用程序所需的Want参数时，需要申请权限ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED。
* 获取用于启动其他用户下的应用程序所需的Want参数时，如果调用方是系统应用，需要申请权限ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED，如果调用方是三方应用需要申请权限ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED和ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示应用的包名。 |
| userId | number | 否 | 表示用户ID，可以通过[getOsAccountLocalId接口](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md#getosaccountlocalid9>)获取。  默认值：调用方所在用户。  取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Want](<../@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md#want>) | Want对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[包管理子系统通用错误码](../../../错误码/包管理子系统通用错误码/errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundle is not found. |
| 17700004 | The specified user id is not found. |
| 17700026 | The specified bundle is disabled. |

**示例：**

```
1. // 示例接口含有userId参数，获取用于启动指定用户下的应用程序所需的Want参数
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { Want } from '@kit.AbilityKit';

7. let bundleName = 'com.example.myapplication';
8. let userId = 100;

10. try {
11. let want: Want = bundleManager.getLaunchWantForBundleSync(bundleName, userId);
12. hilog.info(0x0000, 'testTag', 'getLaunchWantForBundleSync successfully. Data: %{public}s', JSON.stringify(want));
13. } catch (err) {
14. let message = (err as BusinessError).message;
15. hilog.error(0x0000, 'testTag', 'getLaunchWantForBundleSync failed. Cause: %{public}s', message);
16. }
```

```
1. // 示例接口不含userId参数，获取用于启动当前用户下的应用程序所需的Want参数
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { Want } from '@kit.AbilityKit';

7. let bundleName = 'com.example.myapplication';

9. try {
10. let want: Want = bundleManager.getLaunchWantForBundleSync(bundleName);
11. hilog.info(0x0000, 'testTag', 'getLaunchWantForBundleSync successfully. Data: %{public}s', JSON.stringify(want));
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. hilog.error(0x0000, 'testTag', 'getLaunchWantForBundleSync failed. Cause: %{public}s', message);
15. }
```

## ApplicationInfo

PhonePC/2in1TabletTVWearable

type ApplicationInfo = \_ApplicationInfo

应用程序信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_ApplicationInfo](../../接口依赖的元素及定义/bundleManager/ApplicationInfo/js-apis-bundlemanager-applicationinfo.md#applicationinfo-1) | 应用程序信息。 |

## ModuleMetadata10+

PhonePC/2in1TabletTVWearable

type ModuleMetadata = \_ModuleMetadata

模块的元数据信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_ModuleMetadata](../../接口依赖的元素及定义/bundleManager/ApplicationInfo/js-apis-bundlemanager-applicationinfo.md#modulemetadata10) | 模块的元数据信息。 |

## Metadata

PhonePC/2in1TabletTVWearable

type Metadata = \_Metadata

元数据信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_Metadata](../../接口依赖的元素及定义/bundleManager/Metadata/js-apis-bundlemanager-metadata.md#metadata-1) | 元数据信息。 |

## BundleInfo

PhonePC/2in1TabletTVWearable

type BundleInfo = \_BundleInfo.BundleInfo

应用包信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_BundleInfo.BundleInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1) | 应用包信息。 |

## UsedScene

PhonePC/2in1TabletTVWearable

type UsedScene = \_BundleInfo.UsedScene

权限使用的场景和时机。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_BundleInfo.UsedScene](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#usedscene) | 权限使用的场景和时机。 |

## ReqPermissionDetail

PhonePC/2in1TabletTVWearable

type ReqPermissionDetail = \_BundleInfo.ReqPermissionDetail

应用运行时需向系统申请的权限集合的详细信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_BundleInfo.ReqPermissionDetail](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#reqpermissiondetail) | 应用运行时需向系统申请的权限集合的详细信息。 |

## SignatureInfo

PhonePC/2in1TabletTVWearable

type SignatureInfo = \_BundleInfo.SignatureInfo

应用包的签名信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_BundleInfo.SignatureInfo](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#signatureinfo) | 应用包的签名信息。 |

## HapModuleInfo

PhonePC/2in1TabletTVWearable

type HapModuleInfo = \_HapModuleInfo.HapModuleInfo

模块信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_HapModuleInfo.HapModuleInfo](../../接口依赖的元素及定义/bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md#hapmoduleinfo-1) | 模块信息。 |

## PreloadItem

PhonePC/2in1TabletTVWearable

type PreloadItem = \_HapModuleInfo.PreloadItem

元服务中模块的预加载模块信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_HapModuleInfo.PreloadItem](../../接口依赖的元素及定义/bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md#preloaditem) | 元服务中模块的预加载模块信息。 |

## Dependency

PhonePC/2in1TabletTVWearable

type Dependency = \_HapModuleInfo.Dependency

模块所依赖的动态共享库信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_HapModuleInfo.Dependency](../../接口依赖的元素及定义/bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md#dependency) | 模块所依赖的动态共享库信息。 |

## RouterItem12+

PhonePC/2in1TabletTVWearable

type RouterItem = \_HapModuleInfo.RouterItem

模块配置的路由表信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_HapModuleInfo.RouterItem](../../接口依赖的元素及定义/bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md#routeritem12) | 模块配置的路由表信息。 |

## DataItem12+

PhonePC/2in1TabletTVWearable

type DataItem = \_HapModuleInfo.DataItem

模块配置的路由表中的自定义数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_HapModuleInfo.DataItem](../../接口依赖的元素及定义/bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md#dataitem12) | 模块配置的路由表中的自定义数据。 |

## AbilityInfo

PhonePC/2in1TabletTVWearable

type AbilityInfo = \_AbilityInfo.AbilityInfo

Ability信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityInfo.AbilityInfo](../../接口依赖的元素及定义/bundleManager/AbilityInfo/js-apis-bundlemanager-abilityinfo.md#abilityinfo-1) | Ability信息。 |

## WindowSize

PhonePC/2in1TabletTVWearable

type WindowSize = \_AbilityInfo.WindowSize

窗口尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityInfo.WindowSize](../../接口依赖的元素及定义/bundleManager/AbilityInfo/js-apis-bundlemanager-abilityinfo.md#windowsize) | 窗口尺寸。 |

## ExtensionAbilityInfo

PhonePC/2in1TabletTVWearable

type ExtensionAbilityInfo = \_ExtensionAbilityInfo.ExtensionAbilityInfo

ExtensionAbility信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_ExtensionAbilityInfo.ExtensionAbilityInfo](../../接口依赖的元素及定义/bundleManager/ExtensionAbilityInfo/js-apis-bundlemanager-extensionabilityinfo.md#extensionabilityinfo-1) | ExtensionAbility信息。 |

## ElementName

PhonePC/2in1TabletTVWearable

type ElementName = \_ElementName

ElementName信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_ElementName](../../接口依赖的元素及定义/bundleManager/ElementName/js-apis-bundlemanager-elementname.md#elementname-1) | ElementName信息。 |

## Skill12+

PhonePC/2in1TabletTVWearable

type Skill = \_Skill.Skill

skill信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_Skill.Skill](../../接口依赖的元素及定义/bundleManager/Skill/js-apis-bundlemanager-skill.md#skill-1) | skill信息。 |

## SkillUrl12+

PhonePC/2in1TabletTVWearable

type SkillUrl = \_Skill.SkillUri

SkillUri信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_Skill.SkillUri](../../接口依赖的元素及定义/bundleManager/Skill/js-apis-bundlemanager-skill.md#skilluri) | SkillUri信息。 |

## AppCloneIdentity15+

PhonePC/2in1TabletTVWearable

type AppCloneIdentity = \_BundleInfo.AppCloneIdentity

描述应用包的身份信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_BundleInfo.AppCloneIdentity](../../接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#appcloneidentity14) | 应用包的身份信息。 |
