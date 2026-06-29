---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-vpnextensioncontext
title: VpnExtensionContext
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > VpnExtensionContext
category: harmonyos-references
scraped_at: 2026-06-01T16:06:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:902102af5b66152b8b7f892d768d6f4037b14c457f2570ce6d2a3c20f18f3afc
---
VpnExtensionContext是VpnExtensionAbility的上下文环境，继承自[ExtensionContext](<../../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)。

VpnExtensionContext可直接作为VpnExtension的上下文环境，提供允许访问特定于VpnExtensionAbility的资源的能力。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { VpnExtensionAbility } from '@kit.NetworkKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

通过VpnExtensionAbility子类实例来获取。

```
1. import { VpnExtensionAbility, vpnExtension } from '@kit.NetworkKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class MyVpnExtAbility extends VpnExtensionAbility {
5. private vpnServerIp: string = 'xxx.xxx.x.x';
6. private tunIp: string = 'x.x.x.x';
7. private blockedAppName: string = 'xxxx';

9. onCreate(want: Want) {
10. let VpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(this.context);
11. console.info("vpn createVpnConnection: " + JSON.stringify(VpnConnection));
12. }
13. }
```

## VpnExtensionAbility

PhonePC/2in1TabletTVWearable

三方VPN拓展能力。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [VpnExtensionContext](js-apis-inner-application-vpnextensioncontext.md) | 否 | 否 | 指定context。 |

### onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want): void

拓展VPN启动初始化的时候进行回调。

说明

建议配对调用[onDestroy](js-apis-inner-application-vpnextensioncontext.md#ondestroy)监听拓展VPN的销毁，及时执行资源清理等操作。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 指示要启动的信息。 |

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

拓展VPN销毁之前进行回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。
