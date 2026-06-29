---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-request-user-auth
title: 请求用户授权
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 请求用户授权
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:39+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:01872da431d60be769e27b2b3f61f8bb97d4a9f219a1c02266b59bd3659289b4
---
## 场景介绍

Screen Time Guard Kit支持对用户设备的时间管理和应用限制，因此在功能启用前，必须获得用户的明确授权。应用可以调用请求用户授权接口，系统会弹出授权请求界面，明确告知用户功能的作用和必要性，并在用户允许之后，才可正常访问。如果用户未同意授权，则无法再提供相关管控能力，此时如果继续调用管控相关接口，会抛出用户未授权使用的错误码。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/7vpqS6zuTVWc60HA64olIA/zh-cn_image_0000002592379532.png?HW-CC-KV=V1&HW-CC-Date=20260611T071438Z&HW-CC-Expire=86400&HW-CC-Sign=740BBBD7CAC9F270ABF036B81EC152C4B1AB105A9F898874D2172C93723FE180)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/DdZ-DvOIRIC8j_h_c-X3kw/zh-cn_image_0000002622859041.png?HW-CC-KV=V1&HW-CC-Date=20260611T071438Z&HW-CC-Expire=86400&HW-CC-Sign=3D381AF29E945406577D8D4AEBBE43E4B2E307F3EE688FC5A4A8C25F481E05AF)

流程说明：

1. 应用请求访问Screen Time Guard Kit的权限，需要调用拉起请求用户授权的接口，拉起健康使用设备查询本地数据库中该应用的授权状态。
2. 若状态为已授权，则直接正常返回；若状态为未授权，则拉起授权弹框。
3. 若用户取消授权，则抛出对应错误码，若用户允许授权，则正常返回。

## 接口说明

请求用户授权关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [requestUserAuth](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#requestuserauth>)(context: [common.UIAbilityContext](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>)): Promise<void> | 请求用户授权访问Screen Time Guard Kit的相关管控接口。 |
| [requestUserAuth](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#requestuserauth>)(context: [common.UIAbilityContext](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>), appConfig: [AppConfig](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#appconfig>)): Promise<void> | 请求用户授权访问Screen Time Guard Kit的相关管控接口，同时设置授权应用相关配置。 |
| [getUserAuthStatus](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#getuserauthstatus>)(): Promise<[AuthStatus](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#authstatus>)> | 获取用户授权状态。 |

说明

若需更改授权应用配置信息，需要[取消用户授权](../取消用户授权/screentimeguard-revoke-user-auth.md)后，重新调用接口请求用户授权，同时设置授权应用相关配置。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. 调用requestUserAuth，请求用户授权。

   ```
   1. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. guardService.requestUserAuth(context, { isSupportAppUninstall: this.isUninstallable })
   3. .then(async () => {
   4. // ...
   5. })
   6. .catch((error: BusinessError) => {
   7. hilog.error(this.domainId, this.logTag,
   8. `requestUserAuth fail, errCode is ${error.code}, errMessage is ${error.message}`);
   9. })
   ```
3. 获取用户授权状态。

   ```
   1. public async getUserAuthStatus(): Promise<void> {
   2. try {
   3. const status = await guardService.getUserAuthStatus();
   4. hilog.info(0x0000, 'GuardService', `user auth status: ${status}`);
   5. } catch (error) {
   6. let err: BusinessError = error as BusinessError;
   7. hilog.error(0x0000, 'GuardService',
   8. `removeGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
   9. }
   10. }
   ```
