---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-privacy-authorization
title: 拉起运动健康App隐私授权
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Phone/Tablet应用开发 > 拉起运动健康App隐私授权
category: harmonyos-guides
scraped_at: 2026-06-11T15:07:46+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:250791a5b3777370b201a6e5b60ca1dc9d8e1c422e2401378a8916d48927a804
---
## 场景介绍

用户在设备上首次使用运动健康服务时，需要用户同意运动健康服务隐私协议，当前隐私授权依赖运动健康App，需引导用户打开运动健康App并完成隐私授权。

开发者调用后续章节的接口后，如果返回错误码[1002703001](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API错误码/errorcode-healthservice.md#section1002703001-用户隐私未同意>)，可参考本章节，引导用户同意运动健康服务隐私授权。

## 开发步骤

1. 在module.json5文件中增加querySchemes字段，并在列表中配置"huaweischeme"。"huaweischeme"为需要跳转到的运动健康App首页的scheme，页面参考如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/WajVRxgFQYCJZcUi67eBrw/zh-cn_image_0000002592379282.png?HW-CC-KV=V1&HW-CC-Date=20260611T070745Z&HW-CC-Expire=86400&HW-CC-Sign=7376974630FB77135E847BB122C3AB38DB4EB24D45103E4BAABCC9BA29BBE24F)
2. 导入相关功能模块。

   ```
   1. import { bundleManager, common, Want } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { productViewManager } from '@kit.AppGalleryKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 调用[canOpenLink](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md#bundlemanagercanopenlink12>)判断运动健康App是否安装。

   * 已安装则调用[openLink](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#openlink12>)接口拉起运动健康App；
   * 未安装调用[应用市场推荐](<../../../../AppGallery Kit（应用市场服务）/应用市场推荐/展示应用详情页面/appgallery-productview-loadproduct.md>)接口，引导用户下载运动健康App。

   ```
   1. try {
   2. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
   3. let result = bundleManager.canOpenLink('huaweischeme://healthapp/home/main');
   4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   5. if (result) {
   6. // 拉起运动健康App首页，进行隐私授权
   7. let link: string = 'huaweischeme://healthapp/home/main';
   8. await context.openLink(link)
   9. } else {
   10. // 拉起应用市场推荐，引导用户下载运动健康App，进行隐私授权
   11. const wantParam: Want = {
   12. parameters: {
   13. bundleName: 'com.huawei.hmos.health'
   14. }
   15. };
   16. const callback: productViewManager.ProductViewCallback = {
   17. onError: (error: BusinessError) => {
   18. hilog.error(0x0001, 'TAG', `Failed to open AppGallery.Code: ${error.code}, message: ${error.message}`);
   19. }
   20. }
   21. productViewManager.loadProduct(context, wantParam, callback);
   22. }
   23. } catch (err) {
   24. hilog.error(0x0000, 'testTag', `Failed to agree user privacy.Code: ${err.code}, message: ${err.message}`);
   25. }
   ```
