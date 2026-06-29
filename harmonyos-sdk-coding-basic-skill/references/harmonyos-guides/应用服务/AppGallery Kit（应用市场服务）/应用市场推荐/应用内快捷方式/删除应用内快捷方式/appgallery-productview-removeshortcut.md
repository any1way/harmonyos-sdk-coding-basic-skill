---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-removeshortcut
title: 删除应用内快捷方式
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 应用内快捷方式 > 删除应用内快捷方式
category: harmonyos-guides
scraped_at: 2026-06-11T15:04:02+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:26a9df4b1a77e2af1ba55777d11b2af1a251d80562bd2d99bc1faef666788ad1
---
说明

6.1.1(24)版本开始，新增删除桌面快捷方式接口，支持用户删除桌面快捷方式。

## 场景介绍

当应用的桌面快捷方式功能发生变化或者用户希望删除不再使用的桌面快捷方式时，用户可以通过调用[removePinShortcut](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerremovepinshortcut>)接口删除当前应用的桌面快捷方式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/2vJg_au4RK22qkL5DVEmLg/zh-cn_image_0000002592219210.png?HW-CC-KV=V1&HW-CC-Date=20260611T070401Z&HW-CC-Expire=86400&HW-CC-Sign=4A9F99EEAC4F5EB9E767D5C083640E109DA1BBE622E7A173D2E6E4591296713F)

1. 用户需要删除桌面快捷方式。
2. 应用调用[removePinShortcut](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerremovepinshortcut>)接口删除快捷方式。
3. AppGallery Kit向应用弹出快捷方式删除确认框。
4. 用户确认是否删除快捷方式。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md>)。

| 接口名 | 描述 |
| --- | --- |
| [removePinShortcut](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerremovepinshortcut>)(context: [common.UIAbilityContext](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>), shortcutId: string): Promise<void> | 删除桌面快捷方式。 |

## 开发准备

### （可选）静默删除桌面快捷方式开放能力申请

当应用已有自己的删除确认弹框并在弹框中提示用户删除桌面快捷方式时，开发者可以申请静默删除权限，实现在不显示系统确认弹框的情况下完成删除操作。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/HzoQs6WYTkahh39M5Y9OsA/zh-cn_image_0000002622858647.png?HW-CC-KV=V1&HW-CC-Date=20260611T070401Z&HW-CC-Expire=86400&HW-CC-Sign=2DEB0926E2FED6DD250215E5A49A45D2B87FF300A837A66D715E2E5A417FA0E2)
2. 在项目列表中找到您的项目，并点击选择需申请静默删除桌面快捷方式能力的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/EEgw6UNmR2anMllR4bdtXQ/zh-cn_image_0000002592379144.png?HW-CC-KV=V1&HW-CC-Date=20260611T070401Z&HW-CC-Expire=86400&HW-CC-Sign=B5C2275BDEE5B83EA03F41B0F2F0FE3428108679A50C5BC83A5CAB7B91FE541D)
3. 在“开放能力管理”页面，点击静默删除桌面快捷方式对应的“申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/vIluYy6YQPq47YdqpKsNUA/zh-cn_image_0000002622858651.png?HW-CC-KV=V1&HW-CC-Date=20260611T070401Z&HW-CC-Expire=86400&HW-CC-Sign=78FFF0CFBC28AC21E7BDB0200A51E129C5C5FA178AB5F0D0314EC67692161CAE)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，包括应用介绍、使用场景，不超过256个字符。上传附件：必填，提供应用的使用场景录屏，录屏中需要体现应用自己的弹框以及在弹框中显示提示用户删除桌面快捷方式，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/KRGF6-h0Ty2fIMPwZ0Uzkg/zh-cn_image_0000002622698773.png?HW-CC-KV=V1&HW-CC-Date=20260611T070401Z&HW-CC-Expire=86400&HW-CC-Sign=58DB5E62EABB336929A631D6CDA4B18C759AB69A02EAC653C019CC1949706D68)
5. 返回“开放能力管理”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/UDFbxpnNTEuRwR1EPTCazA/zh-cn_image_0000002592219212.png?HW-CC-KV=V1&HW-CC-Date=20260611T070401Z&HW-CC-Expire=86400&HW-CC-Sign=ACE457DFE0C271D485BCE3D062A42BD599689E14C103F182C288AD5702C731CA)
6. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。
7. 能力申请通过后，勾选删除桌面快捷方式的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。

## 开发步骤

1. 导入productViewManager模块及相关公共模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { productViewManager } from '@kit.AppGalleryKit';
   ```
2. 调用[removePinShortcut](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerremovepinshortcut>)方法删除桌面快捷方式。

   ```
   1. const TAG: string = 'RemovePinShortcut';

   3. @Entry
   4. @Component
   5. struct RemovePinShortcut {

   7. build() {
   8. Column() {
   9. Button("RemovePinShortcut")
   10. .onClick(() => {
   11. try {
   12. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   13. const shortcutId = 'xxx'; // 通过checkPinShortcutPermitted接口获取
   14. productViewManager.removePinShortcut(uiContext, shortcutId)
   15. .then(() => {
   16. hilog.info(0x0001, TAG, `removePinShortcut success.`);
   17. }).catch((error: BusinessError) => {
   18. hilog.error(0x0001, TAG, `removePinShortcut error. code is ${error.code}, message is ${error.message}`);
   19. })
   20. } catch (err) {
   21. hilog.error(0x0001, TAG, `removePinShortcut failed, code is ${err.code}, message is ${err.message}`);
   22. }
   23. })
   24. .width('100%')
   25. }
   26. .margin(16)
   27. .height('100%')
   28. .justifyContent(FlexAlign.Center)
   29. }
   30. }
   ```
