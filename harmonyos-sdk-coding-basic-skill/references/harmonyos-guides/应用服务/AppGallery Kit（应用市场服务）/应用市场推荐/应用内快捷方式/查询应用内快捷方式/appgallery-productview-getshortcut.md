---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-getshortcut
title: 查询应用内快捷方式
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 应用内快捷方式 > 查询应用内快捷方式
category: harmonyos-guides
scraped_at: 2026-06-11T15:04:01+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:d27a8b57ba27536f78c4b81464e458cbcd5c851a9048b0eb85766976e9de4cfe
---
说明

6.1.1(24)版本开始，新增查询桌面快捷方式接口，支持用户查询桌面快捷方式。

## 场景介绍

查询应用内快捷方式用于获取当前应用已固定在桌面上的所有快捷方式列表。用户可以在应用内查看已添加到桌面的快捷方式列表，快速找到特定的快捷方式。也可通过定期查看和管理这些快捷方式，确保桌面的整洁和高效。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/bVvGxsnuQ-OeBDEa3oCRjg/zh-cn_image_0000002622698771.png?HW-CC-KV=V1&HW-CC-Date=20260611T070400Z&HW-CC-Expire=86400&HW-CC-Sign=171EEA56BE2C89C342A1DBF57FFAFF3E49A63F73DF197E09DB5A1AC5C901774E)

1. 用户需要查询当前应用的快捷方式。
2. 应用调用[getPinShortcutInfos](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagergetpinshortcutinfos>)接口获取快捷方式信息。
3. AppGallery Kit返回查询结果信息给应用。
4. 应用将查询结果返回给用户。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md>)。

| 接口名 | 描述 |
| --- | --- |
| [getPinShortcutInfos](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagergetpinshortcutinfos>)(): Promise<[PinShortcutInfo](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#pinshortcutinfo>)[]> | 查询桌面快捷方式列表。 |

## 开发步骤

1. 导入productViewManager模块及相关公共模块。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { productViewManager } from '@kit.AppGalleryKit';
   ```
2. 调用[getPinShortcutInfos](<../../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagergetpinshortcutinfos>)方法查询当前应用所有桌面快捷方式列表信息。

   ```
   1. const TAG: string = 'GetPinShortcutInfos';

   3. @Entry
   4. @Component
   5. struct GetPinShortcutInfos {

   7. build() {
   8. Column() {
   9. Button("GetPinShortcutInfos")
   10. .onClick(() => {
   11. try {
   12. // 通过getPinShortcutInfos接口获取桌面快捷方式列表信息
   13. productViewManager.getPinShortcutInfos()
   14. .then(() => {
   15. hilog.info(0x0001, TAG, `getPinShortcutInfos success.`);
   16. }).catch((error: BusinessError) => {
   17. hilog.error(0x0001, TAG, `getPinShortcutInfos error. code is ${error.code}, message is ${error.message}`);
   18. })
   19. } catch (err) {
   20. hilog.error(0x0001, TAG, `getPinShortcutInfos failed, code is ${err.code}, message is ${err.message}`);
   21. }
   22. })
   23. .width('100%')
   24. }
   25. .margin(16)
   26. .height('100%')
   27. .justifyContent(FlexAlign.Center)
   28. }
   29. }
   ```
