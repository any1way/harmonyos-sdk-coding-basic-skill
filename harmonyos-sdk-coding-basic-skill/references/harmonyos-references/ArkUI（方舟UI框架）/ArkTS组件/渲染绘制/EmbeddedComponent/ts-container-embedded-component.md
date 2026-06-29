---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component
title: EmbeddedComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 渲染绘制 > EmbeddedComponent
category: harmonyos-references
scraped_at: 2026-06-11T15:48:48+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:31adad379f3862ac10f4b5a7f0ce715622b6c7fb627b3725b35106cef75f4d50
---
EmbeddedComponent用于支持在当前页面嵌入本应用内其他[EmbeddedUIExtensionAbility](<../../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)/js-apis_26985710.md>)提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，完成页面布局和渲染。

通常用于有进程隔离诉求的模块化开发场景。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 使用约束

PhonePC/2in1TabletTVWearable

EmbeddedComponent仅支持在拥有多进程权限的设备上使用。

EmbeddedComponent只能在UIAbility中使用，且被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

EmbeddedComponent(loader: Want, type: EmbeddedType)

创建跨进程嵌入式组件，用于显示同包名EmbeddedUIExtensionAbility的UI。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loader | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 要加载的EmbeddedUIExtensionAbility。 |
| type | [EmbeddedType](../../公共定义/枚举说明/ts-appendix-enums.md#embeddedtype12) | 是 | 提供方的类型。 |

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](../../通用属性/ts-component-general-attributes.md)。

说明

EmbeddedComponent组件宽高默认值和最小值均为10vp。不支持如下与宽高相关的属性："constraintSize"、"aspectRatio"、"layoutWeight"、"flexBasis"、"flexGrow"和"flexShrink"。

## 事件

PhonePC/2in1TabletTVWearable

与屏幕坐标相关的事件信息会基于EmbeddedComponent的位置宽高进行坐标转换后传递给被拉起的EmbeddedUIExtensionAbility处理。

不支持[点击](../../通用事件/交互响应事件/点击事件/ts-universal-events-click.md)等通用事件。仅支持以下事件：

### onTerminated

PhonePC/2in1TabletTVWearable

onTerminated(callback: Callback<TerminationInfo>)

被拉起的EmbeddedUIExtensionAbility通过调用[terminateSelfWithResult](<../../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionContentSession (带界面扩展能力的界面操作类)/js-apis-app-ability_18888586.md#terminateselfwithresult>)或者[terminateSelf](<../../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionContentSession (带界面扩展能力的界面操作类)/js-apis-app-ability_18888586.md#terminateself>)正常退出时，触发本回调函数。

说明

该接口不支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#callback>)<[TerminationInfo](ts-container-embedded-component.md#terminationinfo)> | 是 | 回调函数，入参用于接收EmbeddedUIExtensionAbility的返回结果，类型为[TerminationInfo](ts-container-embedded-component.md#terminationinfo)。 |

说明

* 若EmbeddedUIExtensionAbility通过调用terminateSelfWithResult退出，其携带的信息会传给回调函数的入参；
* 若EmbeddedUIExtensionAbility通过调用terminateSelf退出，上述回调函数的入参中，"code"取默认值"0"，"want"为"undefined"。

### onError

PhonePC/2in1TabletTVWearable

onError(callback: ErrorCallback)

被拉起的EmbeddedUIExtensionAbility在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理，业务错误码详细介绍请参见[UIExtension错误码](../../../错误码/UI界面/UIExtension错误码/errorcode-uiextension.md)。

说明

该接口不支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#errorcallback>) | 是 | 回调函数，入参用于接收异常信息，类型为[BusinessError](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#businesserror>)，可通过参数中的code、name和message获取错误信息并做处理。 |

说明

如下情形会触发本回调：

* 通知提供方拉起EmbeddedUIExtensionAbility失败。
* 通知提供方EmbeddedUIExtensionAbility切后台失败。
* 通知提供方销毁EmbeddedUIExtensionAbility失败。
* 提供方EmbeddedUIExtensionAbility异常退出。
* 在EmbeddedUIExtensionAbility中嵌套使用EmbeddedComponent。

## TerminationInfo

PhonePC/2in1TabletTVWearable

用于表示被拉起的EmbeddedUIExtensionAbility的返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 被拉起EmbeddedUIExtensionAbility退出时返回的结果码，返回的结果码由terminateSelfWithResult或者terminateSelf被调用时传入的数据决定。 |
| want | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 否 | 是 | 被拉起EmbeddedUIExtensionAbility退出时返回的数据。 |

## 示例（加载EmbeddedComponent）

PhonePC/2in1TabletTVWearable

本示例展示EmbeddedComponent组件和EmbeddedUIExtensionAbility的基础使用方式，示例应用的bundleName为"com.example.embeddedComponent", 同应用下被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。本示例仅支持在拥有多进程权限的设备上运行，如2in1。

* 示例应用中的EntryAbility(UIAbility)加载首页文件ets/pages/Index.ets，其中内容如下：

  ```
  1. import { Want } from '@kit.AbilityKit';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @State message: string = 'Message: ';
  7. private want: Want = {
  8. bundleName: "com.example.embeddedComponent",
  9. abilityName: "ExampleEmbeddedAbility",
  10. };

  12. build() {
  13. Row() {
  14. Column() {
  15. Text(this.message)
  16. .fontSize(20)
  17. .fontWeight(FontWeight.Bold)
  18. EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
  19. .width('100%')
  20. .height('90%')
  21. .onTerminated((info) => {
  22. // 点击extension页面内的terminateSelfWithResult按钮后触发onTerminated回调，文本框显示如下信息
  23. this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
  24. })
  25. .onError((error) => {
  26. // 失败或异常触发onError回调，文本框显示如下报错内容
  27. this.message = 'Error: code = ' + error.code;
  28. })
  29. }
  30. .width('100%')
  31. }
  32. .height('100%')
  33. }
  34. }
  ```
* EmbeddedComponent拉起的ExampleEmbeddedAbility(EmbeddedUIExtensionAbility)在ets/extensionAbility/ExampleEmbeddedAbility.ets文件中实现，内容如下：

  ```
  1. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

  3. const TAG: string = '[ExampleEmbeddedAbility]';

  5. export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
  6. onCreate() {
  7. console.info(TAG, `onCreate`);
  8. }

  10. onForeground() {
  11. console.info(TAG, `onForeground`);
  12. }

  14. onBackground() {
  15. console.info(TAG, `onBackground`);
  16. }

  18. onDestroy() {
  19. console.info(TAG, `onDestroy`);
  20. }

  22. onSessionCreate(want: Want, session: UIExtensionContentSession) {
  23. console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
  24. let param: Record<string, UIExtensionContentSession> = {
  25. 'session': session
  26. };
  27. let storage: LocalStorage = new LocalStorage(param);
  28. // 加载pages/extension.ets页面内容
  29. session.loadContent('pages/extension', storage);
  30. }

  32. onSessionDestroy(session: UIExtensionContentSession) {
  33. console.info(TAG, `onSessionDestroy`);
  34. }
  35. }
  ```
* ExampleEmbeddedAbility(EmbeddedUIExtensionAbility)的入口页面文件ets/pages/extension.ets内容如下，同时需要在resources/base/profile/main\_pages.json文件中配置该页面路径：

  ```
  1. import { UIExtensionContentSession } from '@kit.AbilityKit';

  3. @Entry
  4. @Component
  5. struct Extension {
  6. @State message: string = 'EmbeddedUIExtensionAbility Index';
  7. private storage: LocalStorage | undefined = this.getUIContext()?.getSharedLocalStorage();
  8. private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');

  10. build() {
  11. Column() {
  12. Text(this.message)
  13. .fontSize(20)
  14. .fontWeight(FontWeight.Bold)
  15. Button("terminateSelfWithResult").fontSize(20).onClick(() => {
  16. // 点击按钮后调用terminateSelfWithResult退出
  17. this.session?.terminateSelfWithResult({
  18. resultCode: 1,
  19. want: {
  20. bundleName: "com.example.embeddedComponent",
  21. abilityName: "ExampleEmbeddedAbility",
  22. }
  23. });
  24. })
  25. }.width('100%').height('100%')
  26. }
  27. }
  ```
* 在module.json5配置文件的"extensionAbilities"标签下增加ExampleEmbeddedAbility配置，其type类型为embeddedUI，具体内容如下：

  ```
  1. {
  2. "name": "ExampleEmbeddedAbility",
  3. "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
  4. "type": "embeddedUI"
  5. }
  ```
* 文件目录结构如下：

  ```
  1. .
  2. └── main
  3. ├── ets
  4. │   ├── extensionAbility
  5. │   │   └── ExampleEmbeddedAbility.ets
  6. │   └── pages
  7. |       ├── extension.ets
  8. │       └── Index.ets
  9. ├── resources
  10. |   └── base
  11. |       └── profile
  12. |           └── main_pages.json
  13. └── module.json5
  ```
* 示例图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/TmVajk-JT8eYUnex4S6iAw/zh-cn_image_0000002592380422.png?HW-CC-KV=V1&HW-CC-Date=20260611T074847Z&HW-CC-Expire=86400&HW-CC-Sign=10F3A98453BA5ACF9FF1A927D0B792FFF4FEC3BEB18653662451A2351316A8AB)
