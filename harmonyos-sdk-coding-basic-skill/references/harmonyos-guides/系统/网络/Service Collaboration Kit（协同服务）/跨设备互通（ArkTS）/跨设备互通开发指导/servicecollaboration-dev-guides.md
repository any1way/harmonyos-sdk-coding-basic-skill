---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-dev-guides
title: 跨设备互通开发指导
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通（ArkTS） > 跨设备互通开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T14:49:22+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:01ccca28da520ada73152e7782427ec800ae37958058be119095b977986e93de
---
跨设备互通提供相机、扫描以及图库（图片和视频）的跨设备调用能力，例如：Tablet或PC/2in1设备可以调用Phone的相机、扫描、图库等功能。从API 6.1.0(23)开始，TV、Phone、Tablet或PC/2in1设备可调用具备如下能力的远程设备：支持拍照、扫描及图库（图片与视频）能力的Phone和Tablet，支持图库（图片与视频）能力的PC/2in1设备。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  + 本端设备：HarmonyOS版本为HarmonyOS 5及以上的Tablet或PC/2in1设备，从API 6.1.0(23)开始，支持HarmonyOS版本为HarmonyOS 5及以上的TV、Phone、Tablet或PC/2in1设备。
  + 远端设备：HarmonyOS版本为HarmonyOS 5及以上、具有相机能力的Phone或Tablet设备，从API 6.1.0(23)开始，支持HarmonyOS版本为HarmonyOS 5及以上的Phone、Tablet或PC/2in1设备。
* **使用限制**

  + 双端设备需要登录同一华为账号。
  + 跨设备互通API支持根据特定调用策略调用设备。调用策略：PC/2in1设备可以调用Tablet和Phone，Tablet可以调用Phone，并且从API 6.1.0(23)开始支持TV、Phone、Tablet或PC/2in1设备调用支持拍照、扫描、选择图库中图片与视频能力的Phone，支持拍照、扫描、选择图库中图片与视频能力的Tablet，以及支持选择图库中图片与视频能力的PC/2in1设备。
  + 本端和远端设备需要打开WLAN和蓝牙开关。条件允许时，推荐本端和远端设备接入同一个局域网，可提升唤醒相机的速度。
  + 若在跨设备调用视频选择器时遇到资源加载异常，建议在调用前确认本端和远端的设备调用能力是否匹配、系统状态是否正常，并在稳定环境下重试操作。

## 接口说明

在开发具体功能前，请先查阅[参考文档](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md>)。

| 接口名 | 描述 |
| --- | --- |
| [createCollaborationServiceMenuItems](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems>) | 设备列表选择器，用于获取组网内具有对应跨设备互通能力的设备列表。 |
| [CollaborationServiceStateDialog](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#collaborationservicestatedialog>) | 弹窗组件，用于提示对端业务状态。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { createCollaborationServiceMenuItems, CollaborationServiceStateDialog, CollaborationServiceFilter } from '@kit.ServiceCollaborationKit';
   ```

   [createCollaborationServiceMenuItems](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems>)是设备列表菜单项模块，传入[CollaborationServiceFilter](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#collaborationservicefilter>)的能力枚举值；[CollaborationServiceStateDialog](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#collaborationservicestatedialog>)是状态提示框模块。
2. 在Menu中调用createCollaborationServiceMenuItems添加设备列表选择器，在菜单项内显示设备列表。

   说明

   在调用[createCollaborationServiceMenuItems](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems>)前，需了解：

   * 该方法需要在[Menu](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/菜单/Menu/ts-basic-components-menu.md)组件内调用。
   * 该方法是自定义构建函数，您在使用前需要先了解[@Builder](<../../../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@Builder装饰器：自定义构建函数/arkts-builder.md>)。
3. 传入Array类型的[CollaborationServiceFilter](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#collaborationservicefilter>)枚举值即可使用对应能力，目前支持ALL、TAKE\_PHOTO、SCAN\_DOCUMENT、IMAGE\_PICKER、VIDEO\_PICKER和IMAGE\_VIDEO\_PICKER。

   ALL为预留值，匹配跨端拍照、文档扫描和图库选择器，功能将在后续拓展，TAKE\_PHOTO匹配跨设备拍照能力，SCAN\_DOCUMENT匹配跨设备扫描能力，IMAGE\_PICKER匹配跨设备图库能力，VIDEO\_PICKER匹配视频选择器，IMAGE\_VIDEO\_PICKER匹配图片和视频选择器。

   ```
   1. @Builder
   2. myTestMenu() {
   3. Menu() {
   4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL]);
   5. }
   6. }
   ```
4. 在build方法中添加弹窗组件[CollaborationServiceStateDialog](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#collaborationservicestatedialog>)，用于提示远端相机拍摄状态和回传数据，需要实现其中的[onState](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#onstate>)方法。[CollaborationServiceStateDialog](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#collaborationservicestatedialog>)是全局的提示框，不会对原有布局产生影响。
5. 为弹窗组件绑定和实现[onState](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#onstate>)方法，用于接收和处理照片数据。

   回调函数的传入参数stateCode是完成状态，buffer是回传的数据内容，可通过状态和数据内容结合自身的业务逻辑实现[onState](<../../../../../../harmonyos-references/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationService (跨设备互通组件)/servicecollaboration-collaborationservice.md#onstate>)方法。

   ```
   1. CollaborationServiceStateDialog({
   2. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer):void => this.doInsertPicture(stateCode, bufferType, buffer)
   3. })
   ```

## 跨设备互通完整示例

通过以下示例，您可以完成一次调用对端相机拍摄的操作。

```
1. import {
2. createCollaborationServiceMenuItems,
3. CollaborationServiceStateDialog,
4. CollaborationServiceFilter
5. } from '@kit.ServiceCollaborationKit';
6. import { image } from '@kit.ImageKit';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. @Entry
10. @Component
11. struct Index {
12. @State picture: PixelMap | undefined = undefined;

14. @Builder
15. myTestMenu() {
16. Menu() {
17. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL]);
18. }
19. }

21. build() {
22. Column({ space: 20 }) {
23. CollaborationServiceStateDialog({
24. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode,
25. bufferType, buffer)
26. })
27. Button('使用远端设备进行拍照')
28. .type(ButtonType.Normal)
29. .borderRadius(10)
30. .bindMenu(this.myTestMenu)

32. if (this.picture) {
33. Image(this.picture)
34. .borderStyle(BorderStyle.Dotted)
35. .borderWidth(1)
36. .objectFit(ImageFit.Contain)
37. .height('80%')
38. .onComplete((event) => {
39. if (event != undefined) {
40. hilog.info(0, 'MEMOMOCK', 'onComplete ' + event.loadingStatus);
41. }
42. })
43. }
44. }
45. .padding(20)
46. .width('100%')
47. .alignItems(HorizontalAlign.Center)
48. }

50. doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
51. if (stateCode != 0) {
52. return;
53. }
54. if (bufferType == 'general.image') {
55. let imageSource = image.createImageSource(buffer);
56. imageSource.createPixelMap().then((pixelMap) => {
57. this.picture = pixelMap;
58. }).catch((error: Error) => {
59. hilog.info(0, 'MEMOMOCK', 'Create pixel map failed: ' + error);
60. }).finally(() => {
61. imageSource.release();
62. });
63. }
64. }
65. }
```

## 示例代码

[跨设备互通](https://gitcode.com/harmonyos_samples/service-collaboration-kit-sample-code-arkts)
