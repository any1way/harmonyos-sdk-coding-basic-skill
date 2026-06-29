---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property
title: @Env：环境变量
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 响应式环境变量 > @Env：环境变量
category: harmonyos-references
scraped_at: 2026-06-01T15:45:21+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:71c1f5ff350185f13b1f01262a5566c59b0e4db6b6a3354cbff84c0fed1d08a0
---
说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[@Env开发者指南](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习响应式环境变量/@Env：环境变量/arkts-env-system-property.md>)。

## @Env

PhonePC/2in1TabletTVWearable

Env: EnvDecorator

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Env | [EnvDecorator](ts-env-system-property.md#envdecorator) | 环境变量装饰器。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // @Env读取系统环境变量
7. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

9. build() {}
10. }
```

## EnvDecorator

PhonePC/2in1TabletTVWearable

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义@Env装饰器类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SystemProperties](ts-env-system-property.md#systemproperties) | 是 | 环境变量属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器。 |

**错误码：**

详细介绍请参见[环境变量错误码](../../../错误码/UI界面/环境变量错误码/errorcode-env.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140000 | Invalid key for @Env |

## SystemProperties

PhonePC/2in1TabletTVWearable

定义环境变量枚举值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BREAK\_POINT | 'system.arkui.breakpoint' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.BREAK\_POINT)可获取[WindowSizeLayoutBreakpointInfo](<../../../ArkTS API/UI界面/@ohos.arkui.observer (无感监听)/js-apis-arkui-observer.md#windowsizelayoutbreakpointinfo22>)实例。  当该装饰器声明在[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)或[@ComponentV2](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2>)中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| WINDOW\_SIZE23+ | 'system.window.size' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE)可获取[SizeInVP](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#sizeinvp23>)实例。  当该装饰器声明在[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)或[@ComponentV2](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2>)中时，用于获取当前自定义组件所在窗口的大小信息，单位为vp。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_SIZE\_PX23+ | 'system.window.size.px' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE\_PX)可获取[Size](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#size7>)实例。  当该装饰器声明在[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)或[@ComponentV2](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2>)中时，用于获取当前自定义组件所在窗口的大小信息，单位为px。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA23+ | 'system.window.avoidarea' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA)可获取[UIEnvWindowAvoidAreaInfoVP](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#uienvwindowavoidareainfovp23>)实例。  当该装饰器声明在[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)或[@ComponentV2](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2>)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为vp。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA\_PX23+ | 'system.window.avoidarea.px' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA\_PX)可获取[UIEnvWindowAvoidAreaInfoPX](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#uienvwindowavoidareainfopx23>)实例。  当该装饰器声明在[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)或[@ComponentV2](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2>)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为px。  **模型约束**：此接口仅可在Stage模型下使用。 |
