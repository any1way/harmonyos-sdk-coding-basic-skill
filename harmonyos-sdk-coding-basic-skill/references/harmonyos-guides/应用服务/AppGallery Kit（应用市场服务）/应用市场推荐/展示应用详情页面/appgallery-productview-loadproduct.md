---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-loadproduct
title: 展示应用详情页面
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 展示应用详情页面
category: harmonyos-guides
scraped_at: 2026-06-11T15:03:58+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:1308abd780f15f0a1131eb0519eb29012535d1b848a62be4bf0b2d6a3eaf089f
---
## 场景介绍

通过应用内调用[loadProduct](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadproduct>)接口或者在网页嵌入跳转链接的方式，用户可直接进入应用详情页，简化应用下载流程，增加应用的下载量和用户活跃度。

说明

应用内打开应用市场App，通过应用市场下载推荐应用，推荐使用loadProduct方式；Web页面打开应用市场App，推荐使用[App Linking](appgallery-productview-loadproduct.md#app-linking方式)链接方式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/aV097SrIQZ-r9cqEX5I7iw/zh-cn_image_0000002592379142.png?HW-CC-KV=V1&HW-CC-Date=20260611T070357Z&HW-CC-Expire=86400&HW-CC-Sign=815B98DC4268316B76AD4AC3B13F70E6172009A3D99539FFF74C199FECC9569C)

1. 用户使用打开应用详情页功能。
2. 应用调用AppGallery Kit的[loadProduct](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadproduct>)接口。
3. AppGallery Kit API获取应用传入的信息，生成展示页面。
4. 展示生成的页面给用户使用。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md>)。

| 接口名 | 描述 |
| --- | --- |
| [loadProduct](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadproduct>)(context: [common.UIAbilityContext](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>), want: [Want](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>), callback?: [ProductViewCallback](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewcallback>)): void | 加载应用详情页面接口。 |

## 开发步骤

### loadProduct接口调用

1. 导入productViewManager模块及相关公共模块。

   ```
   1. import { productViewManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import type { common, Want } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造应用详情页参数。

   ```
   1. @Entry
   2. @Component
   3. struct LoadProductView {
   4. @State message: string = '拉起应用市场详情页';

   6. build() {
   7. Row() {
   8. Column() {
   9. Button(this.message)
   10. .fontSize(24)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(() => {
   13. const exposureData: productViewManager.SKExposure = {
   14. adTechId: '20****e8',
   15. campaignId: '123456',
   16. destinationId: '10******',
   17. mmpIds: ['2f****5', '2f7***5'],
   18. serviceTag: '123***2',
   19. nonce: '123***2',
   20. timestamp: 1705536488,
   21. signature: 'MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg=='
   22. };
   23. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext
   24. const wantParam: Want = {
   25. parameters: {
   26. // 必填，此处填入要加载的应用包名，例如： bundleName: 'com.huawei.hmsapp.books'
   27. bundleName: 'com.xxx',
   28. // 可选，向应用归因服务传递登记归因来源数据
   29. skExposure: exposureData
   30. }
   31. }
   32. const callback: productViewManager.ProductViewCallback = {
   33. onError: (error: BusinessError) => {
   34. hilog.error(0, 'TAG',
   35. `loadProduct onError.code is ${error.code}, message is ${error.message}`)
   36. },
   37. // 当应用详情页成功打开时回调
   38. onAppear: () => {
   39. hilog.info(0, 'TAG', `loadProduct onAppear.`);
   40. },
   41. // 当应用详情页关闭时回调
   42. onDisappear: () => {
   43. hilog.info(0, 'TAG', `loadProduct onDisappear.`);
   44. }
   45. }
   46. })
   47. .width('100%')
   48. }
   49. .height('100%')
   50. }
   51. }
   52. }
   ```
3. 调用[loadProduct](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerloadproduct>)方法，将步骤2中构造的参数依次传入接口中。

   ```
   1. productViewManager.loadProduct(uiContext, wantParam, callback);
   ```

### Deep Linking方式

1. 构造拼接bundleName的Deep Linking链接，其中bundleName为需要打开的应用包名，其格式为：

   ```
   1. uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName,
   ```
2. 在应用中调用[startAbility](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#startability-2>)方法，拉起应用市场应用详情页：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import type { common, Want } from '@kit.AbilityKit';

   5. // 拉起应用市场对应的应用详情页面
   6. function startAppGalleryDetailAbility(context: common.UIAbilityContext, bundleName: string): void {
   7. let want: Want = {
   8. action: 'ohos.want.action.appdetail', // 隐式指定action为ohos.want.action.appdetail
   9. uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName, // bundleName为需要打开应用详情的应用包名
   10. };
   11. context.startAbility(want).then(() => {
   12. hilog.info(0x0001, 'TAG', "Succeeded in starting Ability successfully.")
   13. }).catch((error: BusinessError) => {
   14. hilog.error(0x0001, 'TAG', `Failed to startAbility.Code: ${error.code}, message is ${error.message}`);
   15. });
   16. }

   18. @Entry
   19. @Component
   20. struct StartAppGalleryDetailAbilityView {
   21. @ State message: string = '拉起应用市场详情页';

   23. build() {
   24. Row() {
   25. Column() {
   26. Button(this.message)
   27. .fontSize(24)
   28. .fontWeight(FontWeight.Bold)
   29. .onClick(() => {
   30. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   31. // 按实际需求获取应用的bundleName，例如bundleName: 'com.huawei.hmsapp.books'
   32. const bundleName = 'xxxx';
   33. startAppGalleryDetailAbility(context, bundleName);
   34. })
   35. }
   36. .width('100%')
   37. }
   38. .height('100%')
   39. }
   40. }
   ```
3. 在网页中打开Deep Linking链接拉起应用市场应用详情页：

   ```
   1. <html lang="en">
   2. <head>
   3. <meta charset="UTF-8">
   4. </head>
   5. <body>
   6. <div>
   7. <button type="button" onclick="openDeepLink()">拉起应用详情页</button>
   8. </div>
   9. </body>
   10. </html>
   11. <script>
   12. function openDeepLink() {
   13. window.open('store://appgallery.huawei.com/app/detail?id=com.xxxx.xxxx')
   14. }
   15. </script>
   ```

### App Linking方式

1. 构造拼接bundleName的App Linking链接，其中bundleName为需要打开的应用包名，其格式为：

   ```
   1. let link: string = 'https://appgallery.huawei.com/app/detail?id=' + bundleName;
   ```
2. 在应用中调用[openLink](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#openlink12>)接口拉起App Linking链接：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import type { common } from '@kit.AbilityKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Button('start app linking', { type: ButtonType.Capsule, stateEffect: true })
   10. .width('87%')
   11. .height('5%')
   12. .margin({ bottom: '12vp' })
   13. .onClick(() => {
   14. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   15. // 需要拼接不同的应用包名，用以打开不同的应用详情页,例如：bundleName: 'com.huawei.hmsapp.books'
   16. let bundleName: string = 'xxxx';
   17. let link: string = 'https://appgallery.huawei.com/app/detail?id=' + bundleName;
   18. // 以App Linking优先的方式在应用市场打开指定包名的应用详情页
   19. context.openLink(link, { appLinkingOnly: false })
   20. .then(() => {
   21. hilog.info(0x0001, 'TAG', 'openlink success.');
   22. })
   23. .catch((error: BusinessError) => {
   24. hilog.error(0x0001, 'TAG', `openlink failed. Code: ${error.code}, message is ${error.message}`);
   25. });
   26. })
   27. }
   28. }
   ```
3. 在网页中打开App Linking链接：

   ```
   1. <html lang="en">
   2. <head>
   3. <meta charset="UTF-8">
   4. <title>跳转示例</title>
   5. </head>
   6. <body>
   7. <a href='https://appgallery.huawei.com/app/detail?id=bundleName'>AppLinking跳转示例</a>
   8. </body>
   9. </html>
   ```
