---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-form
title: 拉起许可应用跳转页
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用选择页 > 拉起许可应用跳转页
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:46+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:657b7a412a25e642388b0cc36aaa646cbcd6150398da130e5aba49cefcd9049d
---
## 场景介绍

从6.0.2(22)版本开始，新增支持拉起许可应用跳转页功能。为实现用户在被管控期间快速跳转到许可应用的诉求，开发者可调用startAppForm接口拉起应用跳转页，页面中将展示通过接口参数传入的许可应用token对应的应用列表。用户点击其中的应用图标后能跳转到该应用。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/oB4ZU0G5TimPDiJ0HD5bTA/zh-cn_image_0000002592379536.png?HW-CC-KV=V1&HW-CC-Date=20260611T071445Z&HW-CC-Expire=86400&HW-CC-Sign=4910FF80565E1A546274F70E3E2AC1029CDCCB53FF1CF6D1DE58F6D297FCEB73)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/725jD7YOQcGv0vu20xZ62w/zh-cn_image_0000002622859045.png?HW-CC-KV=V1&HW-CC-Date=20260611T071445Z&HW-CC-Expire=86400&HW-CC-Sign=2E4F349C7ECE2CF621CB8923C599275A7717522176EBEE1773A81C22DEB5565C)

流程说明：

1. 应用调用拉起许可应用跳转页的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若状态为未授权，则抛出对应错误码；若状态为已授权，应用将根据传入的应用token信息获取全量应用信息，判断是否展示TrustApp，并拉起应用列表Form。
3. 用户点击跳转页中的应用，跳转到相应的应用。

## 接口说明

拉起许可应用跳转页的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startAppForm](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/AppPicker（应用选择页）/screentimeguard-app-picker.md#startappform>)(context: [common.Context](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), appSelection: [guardService.AppInfo](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#appinfo>), appSubTitle: string, displayTrustApp: boolean): Promise<void> | 拉起许可应用跳转页。 |

## 开发前提

拉起许可应用跳转页需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { appPicker } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用startAppForm，拉起许可应用跳转页。

   ```
   1. private async jumpTo3rdApp(selectedAppTokens: string[], subtitle: string): Promise<void> {
   2. try {
   3. await appPicker.startAppForm(
   4. this.getUIContext().getHostContext(), { appTokens: selectedAppTokens }, subtitle, true);
   5. } catch(error) {
   6. let err: BusinessError = error as BusinessError;
   7. hilog.error(this.domainId, this.logTag,
   8. `startAppForm fail, errCode is ${err.code}, errMessage is ${err.message}`);
   9. }
   10. }
   ```
