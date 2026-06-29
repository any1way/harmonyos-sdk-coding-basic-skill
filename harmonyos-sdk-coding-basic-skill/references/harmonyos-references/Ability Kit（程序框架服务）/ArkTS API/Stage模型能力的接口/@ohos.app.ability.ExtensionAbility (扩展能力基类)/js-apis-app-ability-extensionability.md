---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability
title: @ohos.app.ability.ExtensionAbility (扩展能力基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ExtensionAbility (扩展能力基类)
category: harmonyos-references
scraped_at: 2026-06-01T15:29:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c3b1d427b4e7c26bdc930037d9af043e5b5e2bf75e6bf1577f8506f773c8377b
---
ExtensionAbility是特定场景扩展能力的基类，继承自[Ability](<../@ohos.app.ability.Ability (Ability基类)/js-apis-app-ability-ability.md>)，未新增属性和方法。不支持开发者直接继承ExtensionAbility。各类Ability的继承关系详见[继承关系说明](<../@ohos.app.ability.Ability (Ability基类)/js-apis-app-ability-ability.md#ability的继承关系说明>)。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ExtensionAbility } from '@kit.AbilityKit';
```

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
