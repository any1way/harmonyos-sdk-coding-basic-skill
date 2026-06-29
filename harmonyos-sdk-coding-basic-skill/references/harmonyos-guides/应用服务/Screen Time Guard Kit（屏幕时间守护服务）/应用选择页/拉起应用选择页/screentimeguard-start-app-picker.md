---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-picker
title: 拉起应用选择页
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用选择页 > 拉起应用选择页
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:46+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:f17dbbda03e85261fb92d340e73044794b7fe64ccebb5bbb069380437d9d563a
---
## 场景介绍

在用户需要为特定应用设置使用时长或使用限制策略的场景下，开发者通过调用拉起应用选择页的接口拉起选择页后，使得用户能够选择目标应用。在用户选择完毕并点击完成按钮后，接口会返回应用的token。开发者获取到目标应用的token后，可以根据token为选定应用配置管控策略。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Im6DSyDiQum4RPVAkge3VA/zh-cn_image_0000002622699163.png?HW-CC-KV=V1&HW-CC-Date=20260611T071445Z&HW-CC-Expire=86400&HW-CC-Sign=1ED25467DACE399D9F5935F67347D4C355BDDBFBEFB80858FC5EE6AD35C606D2)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/mV_ApBmKR0aEP4Lp6LH17A/zh-cn_image_0000002592219602.png?HW-CC-KV=V1&HW-CC-Date=20260611T071445Z&HW-CC-Expire=86400&HW-CC-Sign=60FD82AF4893C67BB2C7E8A778149ABF085A3858BE3B0C7FD603979A995CB34E)

流程说明：

1. 应用调用拉起应用选择页的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若状态为未授权，则抛出对应错误码；若状态为已授权，应用将拉起应用选择列表，并根据传入应用token信息预勾选对应应用。
3. 应用选择页将用户选中的应用列表转化为token列表返回给调用接口的应用。

## 接口说明

拉起应用选择页关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startAppPicker](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/AppPicker（应用选择页）/screentimeguard-app-picker.md#startapppicker>)(context: [common.Context](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), appSelection: [guardService.AppInfo](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#appinfo>)): Promise<string[]> | 拉起应用选择页。 |

说明

1. 应用选择页面中的应用列表不包含的系统应用包括：电话、联系人、设置、未成年模式等。
2. 应用选择页面中的应用列表不包含管控发起应用本身和已授权的管控应用。

## 开发前提

拉起应用选择页需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { appPicker } from '@kit.ScreenTimeGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用startAppPicker，拉起应用选择页。

   ```
   1. private async getAppTokens(selectedAppTokens: string[]): Promise<string[]> {
   2. try {
   3. let newSelectedAppTokens: string[] =
   4. await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: selectedAppTokens });
   5. return newSelectedAppTokens;
   6. } catch(error) {
   7. let err: BusinessError = error as BusinessError;
   8. hilog.error(this.domainId, this.logTag,
   9. `startAppPicker fail, errCode is ${err.code}, errMessage is ${err.message}`);
   10. return selectedAppTokens;
   11. }
   12. }
   ```
