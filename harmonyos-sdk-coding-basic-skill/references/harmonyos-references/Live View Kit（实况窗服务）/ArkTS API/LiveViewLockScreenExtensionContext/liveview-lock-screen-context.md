---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-context
title: LiveViewLockScreenExtensionContext
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > LiveViewLockScreenExtensionContext
category: harmonyos-references
scraped_at: 2026-06-01T16:35:11+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:6d04f6bc4de1722d54c7cd3e2d9a1eb829aaa8b112c9d0fe470ba8e462f46347
---
LiveViewLockScreenExtensionContext继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)，作为 [LiveViewLockScreenExtensionAbility](../LiveViewLockScreenExtensionAbility/liveview-lock-screen-ability.md)的上下文环境，为开发者提供在锁屏场景下访问 锁屏沉浸态实况窗的上下文能力。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { LiveViewLockScreenExtensionContext } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## LiveViewLockScreenExtensionContext

PhonePC/2in1Tablet

[LiveViewLockScreenExtensionAbility](../LiveViewLockScreenExtensionAbility/liveview-lock-screen-ability.md)的上下文环境，继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)，未新增内容。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

**主要用途**：

该类作为锁屏扩展的上下文基类，提供锁屏环境下的扩展管理功能。开发者通过[LiveViewLockScreenExtensionAbility](../LiveViewLockScreenExtensionAbility/liveview-lock-screen-ability.md)实例的context属性访问该上下文对象，获取锁屏场景下的资源和能力。

由于该类在 API 定义中未显式定义具体的属性和方法，其功能主要通过继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)的通用上下文能力实现。
