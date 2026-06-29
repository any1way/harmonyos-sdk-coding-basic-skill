---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization-second
title: 再次向用户申请授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 再次向用户申请授权
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:55+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:14172e3238ef5c6acbb5deee734ad5a4099bfc78bb6142ab237a9eb6031a4a4c
---
当应用通过[requestPermissionsFromUser()](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.abilityAccessCtrl (程序访问控制管理)/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9>)拉起弹框[请求用户授权](../向用户申请授权/request-user-authorization.md)时，如果用户拒绝授权，应用将无法再次通过requestPermissionsFromUser()拉起弹框。用户需要在系统设置中手动授权。

在“设置”应用中的路径如下：

* 路径一：设置 > 隐私与安全 > 权限类型（如位置信息） > 具体应用
* 路径二：设置 > 应用和元服务 > 某个应用

应用也可以通过调用[requestPermissionOnSetting()](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.abilityAccessCtrl (程序访问控制管理)/js-apis-abilityaccessctrl.md#requestpermissiononsetting12>)，直接拉起权限设置弹框，引导用户授权。

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/HiBdRPykSwiYLtmgvzWcxw/zh-cn_image_0000002622858215.png?HW-CC-KV=V1&HW-CC-Date=20260611T063954Z&HW-CC-Expire=86400&HW-CC-Sign=610C205E5EF467B0B221058D29ED19429BE088B9C0BEDC19F6D2BC9D550FBBE2)

以下示例代码展示了如何再次拉起弹框申请ohos.permission.APPROXIMATELY\_LOCATION权限。

```
1. import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // ···
5. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
6. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. atManager.requestPermissionOnSetting(context, ['ohos.permission.APPROXIMATELY_LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
8. console.info(`requestPermissionOnSetting success, result: ${data}`);
9. }).catch((err: BusinessError) => {
10. console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
11. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/RequestUserAuthorization/entry/src/main/ets/secondpages/Index.ets#L18-L39)
