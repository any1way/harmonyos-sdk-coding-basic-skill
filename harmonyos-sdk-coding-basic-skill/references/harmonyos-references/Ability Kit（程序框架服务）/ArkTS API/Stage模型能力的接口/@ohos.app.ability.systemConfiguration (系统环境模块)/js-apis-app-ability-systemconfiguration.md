---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-systemconfiguration
title: @ohos.app.ability.systemConfiguration (系统环境模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.systemConfiguration (系统环境模块)
category: harmonyos-references
scraped_at: 2026-06-01T15:29:55+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:865aae8c547993b16172adf3bef2d0403a9574fa45904d7ac377133ce1ed0f6b
---
systemConfiguration模块提供系统环境变化监听回调能力，包括系统深浅色模式、系统语言、系统字体大小缩放比例等变化的回调。

例如，通过对系统深浅色模式变化的监听，应用可感知系统的深浅色模式变化，并动态调整自身应用的深浅色主题以适配系统环境。

该模块与[EnvironmentCallback](<../@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)/js-apis-app-ability-environmentcallback.md>)模块的区别在于：

* systemConfiguration模块：用于监听系统环境变量[Configuration](<../../通用能力的接口(推荐)/@ohos.app.ability.Configuration (环境变量)/js-apis-app-ability-configuration.md>)的变化。
* [EnvironmentCallback](<../@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)/js-apis-app-ability-environmentcallback.md>)模块：用于监听某个应用环境变量[Configuration](<../../通用能力的接口(推荐)/@ohos.app.ability.Configuration (环境变量)/js-apis-app-ability-configuration.md>)的变化。

说明

本模块首批接口从API version 24 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { systemConfiguration } from '@kit.AbilityKit';
```

## UpdatedCallback

PhonePC/2in1TabletTVWearable

UpdatedCallback是监听系统环境变化的回调函数，开发者可通过[ApplicationContext.onSystemConfigurationUpdated](<../../接口依赖的元素及定义/application/ApplicationContext (应用上下文)/js-apis-inner-application-applicationcontext.md#applicationcontextonsystemconfigurationupdated24>)方法注册自定义的UpdatedCallback，来监听系统环境变化。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onColorModeUpdated | [OnColorModeUpdatedFn](js-apis-app-ability-systemconfiguration.md#oncolormodeupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当系统深浅色模式变化时会触发回调。 |
| onFontSizeScaleUpdated | [OnFontSizeScaleUpdatedFn](js-apis-app-ability-systemconfiguration.md#onfontsizescaleupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当系统字体大小缩放比例变化时触发回调。 |
| onFontWeightScaleUpdated | [OnFontWeightScaleUpdatedFn](js-apis-app-ability-systemconfiguration.md#onfontweightscaleupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当系统字体粗细缩放比例变化时触发回调。 |
| onLanguageUpdated | [OnLanguageUpdatedFn](js-apis-app-ability-systemconfiguration.md#onlanguageupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当系统语言变化时触发回调。 |
| onFontIdUpdated | [OnFontIdUpdatedFn](js-apis-app-ability-systemconfiguration.md#onfontidupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当系统字体ID变化时触发回调。 |
| onMCCUpdated | [OnMCCUpdatedFn](js-apis-app-ability-systemconfiguration.md#onmccupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当移动设备国家代码变化时触发回调。 |
| onMNCUpdated | [OnMNCUpdatedFn](js-apis-app-ability-systemconfiguration.md#onmncupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当移动设备网络代码变化时触发回调。 |
| onHasPointerDeviceUpdated | [OnHasPointerDeviceUpdatedFn](js-apis-app-ability-systemconfiguration.md#onhaspointerdeviceupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当指针设备连接或者断开时触发回调。 |
| onLocaleUpdated | [OnLocaleUpdatedFn](js-apis-app-ability-systemconfiguration.md#onlocaleupdatedfn) | 否 | 是 | 在注册系统环境变化的监听后，当系统区域设置变化时触发回调。 |

**示例：**

```
1. import { UIAbility, systemConfiguration, ConfigurationConstant } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let CallBack: systemConfiguration.UpdatedCallback = {
7. onColorModeUpdated(colorMode: ConfigurationConstant.ColorMode) {
8. console.info(`system configuration updated colormode:` + colorMode);
9. },
10. onFontSizeScaleUpdated(fontSizeScale: number) {
11. console.info(`system configuration updated fontSizeScale:` + fontSizeScale);
12. },
13. onFontWeightScaleUpdated(fontWeightScale: number) {
14. console.info(`system configuration updated fontWeightScale:` + fontWeightScale);
15. },
16. onLanguageUpdated(language: string) {
17. console.info(`system configuration updated language:` + language);
18. },
19. onFontIdUpdated(fontId: string) {
20. console.info(`system configuration updated fontId:` + fontId);
21. },
22. onMCCUpdated(mcc: string) {
23. console.info(`system configuration updated mcc:` + mcc);
24. },
25. onMNCUpdated(mnc: string) {
26. console.info(`system configuration updated mnc:` + mnc);
27. },
28. onHasPointerDeviceUpdated(hasPointerDevice: boolean) {
29. console.info(`system configuration updated hasPointerDevice:` + hasPointerDevice);
30. },
31. onLocaleUpdated(locale: string) {
32. console.info(`system configuration updated locale:` + locale);
33. }
34. }
35. // 1.通过context属性获取applicationContext
36. let applicationContext = this.context.getApplicationContext();
37. try {
38. // 2.通过applicationContext注册监听
39. applicationContext.onSystemConfigurationUpdated(CallBack);
40. } catch (paramError) {
41. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
42. }
43. console.info(`onSystemConfigurationUpdated finish`);
44. }
45. }
```

## OnColorModeUpdatedFn

PhonePC/2in1TabletTVWearable

type OnColorModeUpdatedFn = (colorMode: ConfigurationConstant.ColorMode) => void

在注册系统环境变化的监听后，当系统深浅色模式变化时会触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | [ConfigurationConstant.ColorMode](<../../通用能力的接口(推荐)/@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)/js-apis-app-ability-configurationconstant.md#colormode>) | 是 | 变化后的系统深浅色模式。 |

## OnFontSizeScaleUpdatedFn

PhonePC/2in1TabletTVWearable

type OnFontSizeScaleUpdatedFn = (fontSizeScale: number) => void

在注册系统环境变化的监听后，当系统字体大小缩放比例变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontSizeScale | number | 是 | 变化后的系统字体大小缩放比例。 |

## OnFontWeightScaleUpdatedFn

PhonePC/2in1TabletTVWearable

type OnFontWeightScaleUpdatedFn = (fontWeightScale: number) => void

在注册系统环境变化的监听后，当系统字体粗细缩放比例变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontWeightScale | number | 是 | 变化后的系统字体粗细缩放比例。 |

## OnLanguageUpdatedFn

PhonePC/2in1TabletTVWearable

type OnLanguageUpdatedFn = (language: string) => void

在注册系统环境变化的监听后，当系统语言变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| language | string | 是 | 变化后的系统语言。 |

## OnFontIdUpdatedFn

PhonePC/2in1TabletTVWearable

type OnFontIdUpdatedFn = (fontId: string) => void

在注册系统环境变化的监听后，当系统字体ID变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontId | string | 是 | 变化后的系统字体ID。 |

## OnMCCUpdatedFn

PhonePC/2in1TabletTVWearable

type OnMCCUpdatedFn = (mcc: string) => void

在注册系统环境变化的监听后，当移动设备国家代码变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mcc | string | 是 | 变化后的移动设备国家代码。 |

## OnMNCUpdatedFn

PhonePC/2in1TabletTVWearable

type OnMNCUpdatedFn = (mnc: string) => void

在注册系统环境变化的监听后，当移动设备网络代码变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mnc | string | 是 | 变化后的移动设备网络代码。 |

## OnHasPointerDeviceUpdatedFn

PhonePC/2in1TabletTVWearable

type OnHasPointerDeviceUpdatedFn = (hasPointerDevice: boolean) => void

在注册系统环境变化的监听后，当指针设备连接或者断开时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hasPointerDevice | boolean | 是 | 指针设备是否已连接，如键鼠、触控板等。true表示设备已连接，false表示设备未连接。 |

## OnLocaleUpdatedFn

PhonePC/2in1TabletTVWearable

type OnLocaleUpdatedFn = (locale: string) => void

在注册系统环境变化的监听后，当系统区域设置变化时触发回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | 是 | 变化后的系统区域设置，该字段具体解释可以参考[Configuration](<../../通用能力的接口(推荐)/@ohos.app.ability.Configuration (环境变量)/js-apis-app-ability-configuration.md>)。 |
