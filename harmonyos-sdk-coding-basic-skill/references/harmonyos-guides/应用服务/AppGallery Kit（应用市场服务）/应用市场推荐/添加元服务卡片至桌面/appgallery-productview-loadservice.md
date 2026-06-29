---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-loadservice
title: 添加元服务卡片至桌面
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 添加元服务卡片至桌面
category: harmonyos-guides
scraped_at: 2026-06-11T15:03:58+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:13b894ecf4c38ca2c3e2a25e83fa49384814ce452475940eb9725c9debd05957
---
## 场景介绍

为了快速访问和管理元服务卡片信息，用户可以将常用的元服务卡片添加到桌面。应用可通过调用应用市场服务提供的[loadService](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadservice>)接口来加载元服务卡片加桌页面，用户点击“添加至桌面”按钮，将元服务卡片添加至桌面。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/3mrQoDgFTEqEfjHpXd09kg/zh-cn_image_0000002592379142.png?HW-CC-KV=V1&HW-CC-Date=20260611T070357Z&HW-CC-Expire=86400&HW-CC-Sign=03BA5CB9ACBA9034F70031FBBDAF92D4AFF7C03312707C6BA97211078137F24D)

1. 用户使用元服务卡片加桌功能。
2. 应用调用AppGallery Kit的[loadService](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadservice>)接口。
3. AppGallery Kit API获取应用传入的信息，生成展示页面。
4. 展示生成的页面给用户，用户点击“添加至桌面”按钮，将元服务卡片添加至桌面。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md>)。

| 接口名 | 描述 |
| --- | --- |
| [loadService](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadservice>)(context: [common.UIAbilityContext](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>), want: [Want](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>), callback?: [ServiceViewCallback](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#serviceviewcallback>)): void | 加载元服务加桌页面接口。 |

## 开发步骤

1. 导入productViewManager模块及相关公共模块。

   ```
   1. import { productViewManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import type { common, Want } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造元服务卡片参数。

   ```
   1. @Entry
   2. @Component
   3. struct LoadServiceView {
   4. @State message: string = '拉起应用市场详情页';

   6. build() {
   7. Row() {
   8. Column() {
   9. Button(this.message)
   10. .fontSize(24)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(() => {
   13. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   14. const wantParam: Want = {
   15. // 此处填入要加载的元服务的加桌链接
   16. uri: 'xxx'
   17. }
   18. const callback: productViewManager.ServiceViewCallback = {
   19. // 接收元服务卡片加桌结果信息
   20. onReceive: (data: productViewManager.ServiceViewReceiveData) => {
   21. hilog.info(0x0001, 'TAG', `loadService onReceive.result is ${data.result}, msg is ${data.msg}, formInfo is ${JSON.stringify(data.formInfo)}`);
   22. },
   23. onError: (error: BusinessError) => {
   24. hilog.error(0, 'TAG', `loadService onError.code is ${error.code}, message is ${error.message}`)
   25. },
   26. // 当元服务卡片加桌页成功打开时回调
   27. onAppear: () => {
   28. hilog.info(0, 'TAG', `loadService onAppear.`);
   29. },
   30. // 当元服务卡片加桌页关闭时回调
   31. onDisappear: () => {
   32. hilog.info(0, 'TAG', `loadService onDisappear.`);
   33. }
   34. }
   35. })
   36. }
   37. .width('100%')
   38. }
   39. .height('100%')
   40. }
   41. }
   ```
3. 调用[productViewManager.loadService](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadservice>)方法，将步骤2中构造的参数依次传入接口中。

   ```
   1. // 调用接口，加载元服务加桌页面
   2. productViewManager.loadService(uiContext, wantParam, callback);
   ```
