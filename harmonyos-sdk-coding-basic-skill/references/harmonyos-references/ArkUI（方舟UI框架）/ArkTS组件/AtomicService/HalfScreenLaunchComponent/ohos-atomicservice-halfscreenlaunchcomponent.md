---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-halfscreenlaunchcomponent
title: HalfScreenLaunchComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > HalfScreenLaunchComponent
category: harmonyos-references
scraped_at: 2026-06-11T15:49:39+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:a9608c9c451e62c4445269db43654cdce89a108041c597e6c93ef6c92ae8d82c
---
半屏嵌入式启动元服务组件，当被拉起方未授权嵌入式运行元服务时，宿主将使用跳出式拉起元服务。

说明

该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

如果需要在该组件中实现一个可嵌入式运行的元服务时，元服务必须继承自[EmbeddableUIAbility](<../../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)/js-apis-app-ability-embeddableuiability.md>)。若不继承自EmbeddableUIAbility，系统无法确保元服务正常运行。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](../../通用属性/ts-component-general-attributes.md)

## HalfScreenLaunchComponent

PhonePC/2in1TabletTVWearable

HalfScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<TerminationInfo>, onReceive?: Callback<Record<string, Object>> })

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | Callback<void> | 是 | @BuilderParam | 组件显示内容。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| appId | string | 是 | - | 元服务appId。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| options | [AtomicServiceOptions](<../../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数)/js-apis-app-abil_98646972.md>) | 否 | - | 拉起元服务参数，默认为空。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onError | [ErrorCallback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#errorcallback>) | 否 | - | 被拉起的元服务扩展在运行过程中发生异常时触发本回调。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onTerminated | [Callback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#callback>)<[TerminationInfo](../../渲染绘制/EmbeddedComponent/ts-container-embedded-component.md#terminationinfo)> | 否 | - | 回调函数，入参用于接收元服务的返回结果，类型为TerminationInfo。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onReceive20+ | [Callback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#callback>)<Record<string, Object>> | 否 | - | 被拉起的嵌入式运行元服务通过[Window](../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/窗口管理/管理应用窗口（Stage模型）/application-window-stage.md)调用API时，触发本回调。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例展示如何嵌入式拉起手机充值服务。

```
1. import { HalfScreenLaunchComponent } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. appId: string = "576****************"; // 元服务appId。

8. build() {
9. Column() {
10. HalfScreenLaunchComponent({
11. appId: this.appId,
12. options: {},
13. onTerminated:  (info:TerminationInfo)=> {
14. console.info('onTerminated info = '+ info.want);
15. },
16. onError: (err) => {
17. console.error(" onError code: " + err.code + ", message: ", err.message);
18. },
19. onReceive: (data) => {
20. console.info("onReceive, data: " + data['ohos.atomicService.window']);
21. }
22. }) {
23. Column() {
24. Image($r('app.media.app_icon'))
25. Text('拉起手机充值')
26. }.width("80vp").height("80vp").margin({bottom:30})
27. } // 通过尾随闭包形式传入content。
28. }
29. }

31. }
```
