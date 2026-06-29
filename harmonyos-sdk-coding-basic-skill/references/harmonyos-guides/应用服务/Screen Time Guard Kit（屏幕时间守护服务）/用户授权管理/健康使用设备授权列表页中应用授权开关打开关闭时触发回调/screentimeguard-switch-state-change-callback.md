---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-switch-state-change-callback
title: 健康使用设备授权列表页中应用授权开关打开/关闭时触发回调
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 健康使用设备授权列表页中应用授权开关打开/关闭时触发回调
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:42+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:b01e92dd6fb184a6f19bc0c0a87f6619f7397ee572d0e254db7c9a343fc10edd
---
## 场景介绍

当通过健康使用设备授权列表页中的授权开关开启或者关闭应用授权时（设置-健康使用设备-右上角四点设置![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/cINInj30So2L8McrmKKSgA/zh-cn_image_0000002592219600.png?HW-CC-KV=V1&HW-CC-Date=20260611T071441Z&HW-CC-Expire=86400&HW-CC-Sign=D61680E279C9179DA7683C9CC8D7767B02DD7399A3976FA2543316B2AE960E3D)-可访问健康使用设备的应用），会执行TimeGuardExtensionAbility中的onUserAuthSwitchOn/onUserAuthSwitchOff回调方法，支持开发者在用户授予授权和撤销授权时执行特定逻辑。若之前已设置过健康使用设备的密码，则在此页面取消应用授权时需要输入健康使用设备的密码。

注意

应用调用Screen Time Guard Kit接口获取授权或者取消授权时，不会触发onUserAuthSwitchOn/onUserAuthSwitchOff回调方法。只有在健康使用设备授权列表页操作授权开关时才会触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/AWX2zNxqRU60GHN9G5nV3w/zh-cn_image_0000002592379534.png?HW-CC-KV=V1&HW-CC-Date=20260611T071441Z&HW-CC-Expire=86400&HW-CC-Sign=C7F018BD0257C4AA0C240CDD577815C8C24B7006D2F7294A0DB03F1FB315FB29)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/iyNu_WgOQUWF6pYpF-Ad4A/zh-cn_image_0000002622859043.png?HW-CC-KV=V1&HW-CC-Date=20260611T071441Z&HW-CC-Expire=86400&HW-CC-Sign=0AE7D594ECA7128AAFA3C1BA85F8137E840184C4ED9F92DF546D418AD81C13F0)

流程说明（以关闭授权开关为例）：

1. 应用继承TimeGuardExtensionAbility，实现onUserAuthSwitchOn、onUserAuthSwitchOff方法，以监听用户授权状态。
2. 用户在健康使用设备的授权列表页中关闭授权开关后会拉起extension进程，执行TimeGuardExtensionAbility的onUserAuthSwitchOff回调。
3. onUserAuthSwitchOff回调执行，应用可以在该回调中可以执行特定逻辑。

## 接口说明

授权开关打开/关闭时的回调关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [onUserAuthSwitchOn](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/TimeGuardExtensionAbility（屏幕时间守护扩展Ability）/screentimeguard-timeguardextensionability.md#onuserauthswitchon>)(): Promise<void> | 当用户授予授权时执行特定逻辑。 |
| [onUserAuthSwitchOff](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/TimeGuardExtensionAbility（屏幕时间守护扩展Ability）/screentimeguard-timeguardextensionability.md#onuserauthswitchoff>)(): Promise<void> | 当用户撤销授权时执行特定逻辑。 |

说明

1. TimeGuardExtensionAbility与应用运行在不同进程，但共用沙箱。
2. TimeGuardExtensionAbility与应用直接无法直接传递数据，如需传递数据可以通过[用户首选项](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.preferences (用户首选项)/js-apis-data-preferences.md>)/[数据库](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/js-apis-data-relationalstore.md>)等数据持久化手段进行传递，或者通过[公共事件模块](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md>)传递。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 继承TimeGuardExtensionAbility，重写onUserAuthSwitchOn和onUserAuthSwitchOff回调。

   ```
   1. export default class TimeGuardExtAbility extends TimeGuardExtensionAbility {
   2. async onUserAuthSwitchOn(): Promise<void> {
   3. hilog.info(0x0000, 'TimeGuardExtensionAbility', 'onUserAuthSwitchOn');
   4. }

   6. async onUserAuthSwitchOff(): Promise<void> {
   7. hilog.info(0x0000, 'TimeGuardExtensionAbility', 'onUserAuthSwitchOff');
   8. }
   9. }
   ```
3. 在工程中entry模块的module.json5文件中的"extensionAbilities"节点添加如下代码。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "TimeGuardExtAbility",
   4. "type": "screenTimeGuard",
   5. "srcEntry": "./ets/timeguardextability/TimeGuardExtAbility.ets",
   6. "exported": false,
   7. "skills": [
   8. {
   9. "actions": [
   10. "action.ohos.timeGuard.listener"
   11. ]
   12. }
   13. ],
   14. }
   15. ],
   ```
