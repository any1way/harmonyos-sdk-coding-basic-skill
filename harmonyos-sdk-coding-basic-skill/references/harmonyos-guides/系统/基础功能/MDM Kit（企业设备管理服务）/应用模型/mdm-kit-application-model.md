---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-application-model
title: 应用模型
breadcrumb: 指南 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > 应用模型
category: harmonyos-guides
scraped_at: 2026-06-11T14:50:43+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:ee2bcf5537a49435ed90378e03f8b01f0b302dc174c5de8357bc4a6128519063
---
## 概述

应用模型是系统为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必需的组件和运行机制。借助应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。

## Admin组件的基础概念

[企业设备管理扩展组件](<../MDM Kit术语/mdm-kit-term.md#企业设备管理扩展能力>)，是[MDM应用](<../MDM Kit术语/mdm-kit-term.md#mdm应用设备管理应用>)的必备组件。开发MDM应用时，需要定义一个[EnterpriseAdminExtensionAbility](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）/js-apis-enterpriseadminextensionability.md>)类型的[ExtensionAbility](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)组件用于激活MDM应用，该组件被激活后将作为独立的后台进程存在。

### 进程模型

MDM应用进程模型继承于普通应用[进程模型](<../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/进程模型/process-model-stage.md#进程模型-1>)，在普通应用模型基础上MDM应用会多一个独立的EnterpriseAdmin进程，MDM应用的Admin组件被激活后，EnterpriseAdmin进程会被创建，EnterpriseAdmin进程作为设备管理应用的后台进程，用于接收MDM应用的激活、取消激活等事件的回调。EnterpriseAdmin进程的生命周期不受到主进程的影响，由系统管理其生命周期。Admin组件的激活方式不同，EnterpriseAdmin进程的生命周期的[管理方式](mdm-kit-application-model.md#admin组件激活规格的差异)也不同。

**图1** MDM应用进程模型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/XaW_noh5QnWn4TcAv-WcaA/zh-cn_image_0000002622858329.png?HW-CC-KV=V1&HW-CC-Date=20260611T065042Z&HW-CC-Expire=86400&HW-CC-Sign=365F5FD9A556E083929699722E78BA8D80A5A48823CFDA56E98CA107932E80FD)

### EnterpriseAdmin进程的生命周期

Admin组件被激活后有独立的进程，支持系统状态变更回调。与应用的主进程分属不同的进程，进程的启停由[EDM](<../MDM Kit术语/mdm-kit-term.md#edm>)服务管理，应用处于后台时Admin进程也可以运行。

**图2** MDM应用处于前台并且已经激活时

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/yO-LvVfAQualboPa7JdOnQ/zh-cn_image_0000002622698451.png?HW-CC-KV=V1&HW-CC-Date=20260611T065042Z&HW-CC-Expire=86400&HW-CC-Sign=2FE45D0B8E3997724065BADD3BBFD28077F8E77E6501FC6322DD2F0D7B7716B8)

**图3** 存在MDM应用的前台进程和EnterpriseAdmin进程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/LtBx0s6TShmt77DyGv4lPw/zh-cn_image_0000002592218890.png?HW-CC-KV=V1&HW-CC-Date=20260611T065042Z&HW-CC-Expire=86400&HW-CC-Sign=536BD8AF0BF372CC11F6B248B27C4A56958FB8DB870ACABEE582DDDFC64A8BF4)

**图4** 应用主进程停止时，EnterpriseAdmin进程仍然运行

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/PQuBpR5WRgmul3GPCzpMeQ/zh-cn_image_0000002592378824.png?HW-CC-KV=V1&HW-CC-Date=20260611T065042Z&HW-CC-Expire=86400&HW-CC-Sign=F9A741624D7705188D265C854DA36251ED91C79BB8E6AB7970F4D632A2D7E4AF)

**图5** EnterpriseAdmin进程支持系统事件回调

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/XlCr54-oS8CCCchd8-EBmw/zh-cn_image_0000002622858331.png?HW-CC-KV=V1&HW-CC-Date=20260611T065042Z&HW-CC-Expire=86400&HW-CC-Sign=90A8C910D79EF844095CEBE9C9F9B6A89954C0D549F53C82DC2877A2D598D697)

* onAdminEnabled：当MDM应用的Admin组件被激活时的事件回调。
* onAdminDisabled：当MDM应用的Admin组件被取消激活时的事件回调。
* onAppStart：应用启动的事件回调，回调的参数中包含应用包名。需要通过[adminManager.subscribeManagedEventSync](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagersubscribemanagedeventsync>)接口注册MANAGED\_EVENT\_APP\_START事件才能收到此回调。
* onAppStop：应用停止的事件回调，回调的参数中包含应用包名。需要通过[adminManager.subscribeManagedEventSync](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagersubscribemanagedeventsync>)接口注册MANAGED\_EVENT\_APP\_STOP事件才能收到此回调。
* onBundleAdded：应用安装事件回调，回调的参数中包含应用包名和用户ID。需要通过[adminManager.subscribeManagedEventSync](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagersubscribemanagedeventsync>)接口注册MANAGED\_EVENT\_BUNDLE\_ADDED事件才能收到此回调。
* onBundleRemoved：应用卸载事件回调，回调的参数中包含应用包名和用户ID。需要通过[adminManager.subscribeManagedEventSync](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagersubscribemanagedeventsync>)接口注册MANAGED\_EVENT\_BUNDLE\_REMOVED事件才能收到此回调。
* 更多事件回调请参考[ManagedEvent](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#managedevent>)。

### Admin组件激活规格的差异

Admin组件有不同的激活方式，可以通过不同的接口，例如[adminManager.enableDeviceAdmin](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagerenabledeviceadmin23>)，[adminManager.startAdminProvision](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15>)，激活后所具备的能力也有不同。详情如下表所示：

| 特性 | SDA | DA | BDA |
| --- | --- | --- | --- |
| 防卸载能力 | 禁止用户卸载 | 默认情况下用户可以卸载 | 禁止卸载 |
| MDM管控接口调用权限 | 支持所有public管控接口 | 支持所有public管控接口 | 支持申请ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS权限可调用的接口 |
| 角色支持数量 | 最多1个 | 最多10个 | 无数量限制 |

说明

1.BDA与其他[admin角色](<../MDM Kit术语/mdm-kit-term.md#admin角色>)不能同时存在。

2.SDA和DA同时存在的数量加起来最多10个。SDA具备管理其他DA应用的能力（激活/去激活），而DA仅能对设备进行管控，无法管理其他DA应用。当MDM应用激活为SDA时，具备管控其他DA的能力，可以通过调用[adminManager.enableDeviceAdmin](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagerenabledeviceadmin23>)接口激活其他DA应用，或调用[adminManager.disableDeviceAdmin](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagerdisabledeviceadmin23>)接口去激活其他DA应用。

## 管控接口授权原理

MDM应用的Admin组件需经企业授权方可生效。具体而言，企业需要通过调用MDM Kit接口进行Admin组件的激活。在此操作之前，该组件仅处于声明状态，不具备实际能力，Admin组件激活之后，在MDM应用的任意进程，都可以调用MDM管控接口。

### 管控接口权限校验机制

MDM管控接口使用[ACL授权](../../../安全/程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md#权限机制中的基本概念)进行访问权限校验，同时会校验Admin组件的激活状态与激活类型。MDM应用调用MDM管控接口时须同时具备上述三个条件，否则调用会报错[9200001](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md#section9200001-应用没有激活成设备管理器>)、[201](../../../../../harmonyos-references/通用错误码/errorcode-universal.md#section201-权限校验失败)或[9200002](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md#section9200002-设备管理器权限不够>)。

**图6** EDM服务校验逻辑

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/MFaMBAG_Sw2uQdPNFYptuw/zh-cn_image_0000002622698453.png?HW-CC-KV=V1&HW-CC-Date=20260611T065042Z&HW-CC-Expire=86400&HW-CC-Sign=EB7FA69098227E0F371915BFA31834EB230BAB9581FCB9D001070765C64D1193)
