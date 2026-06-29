---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/transferabled-object
title: Transferable对象 (NativeBinding对象)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Transferable对象 (NativeBinding对象)
category: harmonyos-guides
scraped_at: 2026-06-12T11:58:19+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:f62e72df35c40751c7f553770e84eb2331c964a2a5b44048c2c16029aab7683e
---

Transferable对象，也称为NativeBinding对象，是指绑定C++对象的JS对象，其主要功能由C++提供，JS对象壳则分配在虚拟机的本地堆（LocalHeap）中。跨线程传输时复用同一个C++对象，相比JS对象的拷贝模式，传输效率更高。因此，可共享或转移的NativeBinding对象被称为Transferable对象。开发者可以自定义Transferable对象，详细示例请参考[自定义Native Transferable对象的多线程操作场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-coerce-to-native-binding-object)。

## 共享模式

如果C++实现能够确保线程安全性，则NativeBinding对象的C++部分支持跨线程共享。NativeBinding对象跨线程传输后，只需重新创建JS壳即可桥接到同一个C++对象上，实现C++对象的共享。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/6-qHFdxWQo26Oe7EEEybnQ/zh-cn_image_0000002622857363.png?HW-CC-KV=V1&HW-CC-Date=20260612T035818Z&HW-CC-Expire=86400&HW-CC-Sign=7AB5AA49787DDF5221906E9A1CF2EBF93A42E0FF279DC4B5FAF30EB5E95C0220)

常见的共享模式NativeBinding对象包括：应用上下文（ApplicationContext）、窗口上下文（WindowContext）、组件上下文（AbilityContext或ComponentContext）等Context类型对象。这些上下文对象封装了应用程序组件的上下文信息，提供了访问系统服务和资源的能力，使得应用程序组件可以与系统进行交互。获取Context信息的方法可以参考[获取上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage)。

示例可参考[使用TaskPool进行频繁数据库操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/batch-database-operations-guide#使用taskpool进行频繁数据库操作)。

## 转移模式

如果C++实现包含数据且无法保证线程安全性，则NativeBinding对象的C++部分需要采用转移方式传输。NativeBinding对象跨线程传输后，重新创建JS壳可桥接到C++对象上，但需移除原JS壳与C++对象的绑定关系。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/vUbmzXieToG_8lY7aIG58A/zh-cn_image_0000002622697485.png?HW-CC-KV=V1&HW-CC-Date=20260612T035818Z&HW-CC-Expire=86400&HW-CC-Sign=2D41F49E35EF864D298EAC31906C0AB9A67ACBE7E8AC8017CCAAF15898D19340)

常见的转移模式NativeBinding对象包括[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)对象，它可以读取或写入图像数据，获取图像信息，常用于显示图片。

这里提供了一个跨线程传递PixelMap对象的示例。首先从rawfile文件夹中获取图片资源，然后在子线程中创建PixelMap对象并传递给主线程，具体实现如下：

```
1. import { taskpool } from '@kit.ArkTS';
2. import { loadPixelMap } from './pixelMapTest';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. uiContext = this.getUIContext();
9. @State message: string = 'Hello World';
10. @State pixelMap: PixelMap | undefined = undefined;

12. private loadImageFromThread(): void {
13. const resourceMgr = this.uiContext?.getHostContext()?.resourceManager;
14. // 此处‘startIcon.png’为media下复制到rawfile文件夹中，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
15. resourceMgr?.getRawFd('startIcon.png').then(rawFileDescriptor => {
16. taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
17. if (pixelMap) {
18. this.pixelMap = pixelMap as PixelMap;
19. console.info('Succeeded in creating pixelMap.');
20. // 主线程释放pixelMap。由于子线程返回pixelMap时已调用setTransferDetached，所以此处能够立即释放pixelMap。
21. this.pixelMap.release();
22. } else {
23. console.error('Failed to create pixelMap.');
24. }
25. }).catch((e: BusinessError) => {
26. console.error('taskpool execute loadPixelMap failed. Code: ' + e.code + ', message: ' + e.message);
27. });
28. }).catch(() => {
29. console.error(`Failed to get RawFd`);
30. });
31. }

33. build() {
34. RelativeContainer() {
35. Text(this.message)
36. .id('HelloWorld')
37. .fontSize(50)
38. .fontWeight(FontWeight.Bold)
39. .alignRules({
40. center: { anchor: '__container__', align: VerticalAlign.Center },
41. middle: { anchor: '__container__', align: HorizontalAlign.Center }
42. })
43. .onClick(() => {
44. this.loadImageFromThread();
45. this.message = 'success';
46. })
47. }
48. .height('100%')
49. .width('100%')
50. }
51. }
```

[TransferabledObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationObjects/CommunicationObjects/entry/src/main/ets/managers/TransferabledObject.ets#L16-L68)

```
1. import { image } from '@kit.ImageKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. @Concurrent
5. export async function loadPixelMap(rawFileDescriptor: resourceManager.RawFileDescriptor): Promise<PixelMap> {
6. // 创建imageSource。
7. const imageSource = image.createImageSource(rawFileDescriptor);
8. // 创建pixelMap。
9. const pixelMap = imageSource.createPixelMapSync();
10. // 释放imageSource。
11. imageSource.release();
12. // 使pixelMap在跨线程传输完成后，脱离原线程的引用。
13. pixelMap.setTransferDetached(true);
14. // 返回pixelMap给主线程。
15. return pixelMap;
16. }
```

[pixelMapTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationObjects/CommunicationObjects/entry/src/main/ets/managers/pixelMapTest.ets#L16-L33)
