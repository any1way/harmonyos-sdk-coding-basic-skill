---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo
title: LauncherAbilityInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > LauncherAbilityInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:31:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b871e4f74011773c0bcdca3e527592e3db83530574e5d2b3fbc22629d16e0beb
---
桌面应用的Ability信息，可以通过[getLauncherAbilityInfoSync](<../../../通用能力的接口(推荐)/@ohos.bundle.launcherBundleManager (launcherBundleManager模块)/js-apis-launcherbundlemanager.md#launcherbundlemanagergetlauncherabilityinfosync>)获取。

说明

本模块首批接口从API version 18 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { launcherBundleManager } from '@kit.AbilityKit';
```

## LauncherAbilityInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| applicationInfo | [ApplicationInfo](../ApplicationInfo/js-apis-bundlemanager-applicationinfo.md) | 是 | 否 | launcher ability的应用程序配置信息。 |
| elementName | [ElementName](../ElementName/js-apis-bundlemanager-elementname.md) | 是 | 否 | launcher ability的ElementName信息。 |
| labelId | number | 是 | 否 | launcher ability的名称的资源ID值。 |
| iconId | number | 是 | 否 | launcher ability的图标的资源ID值。 |
| userId | number | 是 | 否 | launcher ability的用户ID。 |
| installTime | number | 是 | 否 | launcher ability的安装时间戳，单位毫秒。 |
