---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fenceextensionability
title: 云侧围栏开发指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 地理围栏开发指导 > 云侧围栏开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aa6adf1d2ca4b8f0fd714a6e922e753a2a680ba5ea7524d36554232f9fea6c9d
---
## 概述

云侧围栏是指开发者直接使用云侧公共围栏，当用户进入这个区域，在移动设备上进行有针对性的提醒。

## 开通云侧围栏服务

在开通定位服务前，请先参考“[应用开发准备](../../../../应用开发准备/应用开发准备/application-dev-overview.md)”创建项目和应用工程。

说明

从HarmonyOS NEXT Developer Beta2起，开发者无需配置公钥指纹和Client ID。

**操作步骤**

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/3hypjmHyRIO6KDM1mPvMDA/zh-cn_image_0000002622858871.png?HW-CC-KV=V1&HW-CC-Date=20260611T070933Z&HW-CC-Expire=86400&HW-CC-Sign=58E40AB1B193D3D690874D92C55C0FFA4378DA200852A09FD146C972C36AC115)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要配置定位服务参数的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/rRpX3gTaTFi69hCXBOOPQA/zh-cn_image_0000002622698991.png?HW-CC-KV=V1&HW-CC-Date=20260611T070933Z&HW-CC-Expire=86400&HW-CC-Sign=385407EF231BF200EC75F4D734873A6665B031C895A4400BADCC11BC278B589B)
3. 在左侧导航栏选择“定位服务”，并点击收藏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/zQeApAz0S0iwy4-iOzAi_g/zh-cn_image_0000002592219430.png?HW-CC-KV=V1&HW-CC-Date=20260611T070933Z&HW-CC-Expire=86400&HW-CC-Sign=B58ACF359F8BA7FA28F6AABA9085E17D07E8EEE808A0D6DF0E4CBF5907A505C4)
4. 在左侧导航栏选择“构建 > 定位服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/jU92SvvVQGmHzQ3-ONu-Yg/zh-cn_image_0000002592379364.png?HW-CC-KV=V1&HW-CC-Date=20260611T070933Z&HW-CC-Expire=86400&HW-CC-Sign=55665843795CF2AB1F9ECE197BEE4AC7A42FF1F2F78011A6BFF37AE757C38932)

## 使用场景

1. 开发者可以通过该围栏扩展能力来使用云侧公共围栏。
2. 开发者首先需要在AGC（AppGallery Connect）平台定位服务选择右侧“添加围栏组触发”开始创建地理围栏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/tl0PJcnhQ9maF6hzu12zGg/zh-cn_image_0000002622858873.png?HW-CC-KV=V1&HW-CC-Date=20260611T070933Z&HW-CC-Expire=86400&HW-CC-Sign=967DD88D9FB6F98B68EA19EAC51533CACAC4AB50CEE646729D54E8836A527C90)
3. 可以根据商圈、景点等类别，配置围栏组下发围栏策略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ly6pQKVRTv-x80E1AYygJg/zh-cn_image_0000002622698993.png?HW-CC-KV=V1&HW-CC-Date=20260611T070933Z&HW-CC-Expire=86400&HW-CC-Sign=C348D36341011A1F3DC64B2D585931F11B030BCE06E445E573135BA041FAEF7F)
4. 定位服务在满足围栏触发条件后，通过FenceExtensionAbility把围栏事件通知给APP，APP接收到围栏事件后完成相关的业务处理。

## 接口介绍

接口详情参见[FenceExtensionAbility](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)/js-apis-app-ability-fenceextensionability.md>)。

| 接口 | 描述 |
| --- | --- |
| onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void | 接收系统通知的地理围栏事件，根据围栏事件类型和数据进行相应处理。 |
| onDestroy(): void | 接收FenceExtensionAbility的销毁事件并处理，会在FenceExtensionAbility销毁前回调。 |

## 开发步骤

要实现一个地理围栏扩展服务，开发者需要实现[FenceExtensionAbility](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)/js-apis-app-ability-fenceextensionability.md>)的能力，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为fenceextensionability;
2. 在fenceextensionability目录，右键选择“New > File”，新建一个.ets文件并命名为MyFenceExtensionAbility.ets;
3. 打开MyFenceExtensionAbility.ets，导入FenceExtensionAbility的依赖包，自定义类继承FenceExtensionAbility并实现onFenceStatusChange和onDestroy接口;

   示例代码如下：

   ```
   1. import { FenceExtensionAbility, geoLocationManager } from '@kit.LocationKit';
   2. import { wantAgent } from '@kit.AbilityKit';
   3. import { notificationManager } from '@kit.NotificationKit';

   5. export default class MyFenceExtensionAbility extends FenceExtensionAbility {
   6. async onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): Promise<void> {
   7. super.onFenceStatusChange(transition, additions);

   9. // 接收围栏触发信息
   10. console.info('MyFenceExtensionAbility onFenceStatusChange');

   12. let poiId: string = additions['poiId'];// 围栏id，唯一标识，示例：'999287512272780934'
   13. let policyType: string = additions['policyType'];// 策略类型：'0'-普通策略;'1'-标签策略
   14. let policyResult: string = additions['policyResult'];// 策略结果：标签等策略的额外信息

   16. console.info(`poiId:${poiId},policyType:${policyType},policyResult:${policyResult}`);

   18. // 可以发送围栏业务通知
   19. let wantAgentInfo: wantAgent.WantAgentInfo = {
   20. wants: [
   21. {
   22. bundleName: 'com.huawei.hmos.locationtest.smartfence',
   23. abilityName: 'EntryAbility'
   24. } as Want
   25. ],
   26. actionType: wantAgent.OperationType.START_ABILITY,
   27. requestCode: 100
   28. };
   29. let wantAgentMy = await wantAgent.getWantAgent(wantAgentInfo);
   30. let notificationRequest: notificationManager.NotificationRequest = {
   31. id: 1,
   32. content: {
   33. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   34. normal: {
   35. title: `围栏通知`,
   36. text: `poiId:${poiId},policyType:${policyType},policyResult:${policyResult}`,
   37. }
   38. },
   39. notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
   40. wantAgent: wantAgentMy
   41. };
   42. notificationManager.publish(notificationRequest);
   43. }

   45. onDestroy(): void {
   46. super.onDestroy();
   47. console.info('MyFenceExtensionAbility onDestroy');
   48. }
   49. }
   ```
4. 在工程Module对应的[module.json5配置文件](../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#extensionabilities标签)中注册FenceExtensionAbility，type标签需要设置为fence，srcEntry标签表示当前FenceExtensionAbility组件所对应的代码路径。

   ```
   1. {
   2. "module": {
   3. "extensionAbilities": [
   4. {
   5. "name": "MyFenceExtensionAbility",
   6. "srcEntry": "./ets/fenceextensionability/MyFenceExtensionAbility.ets",
   7. "description": "MyFenceExtensionAbility",
   8. "type": "fence",
   9. "exported": false
   10. },
   11. ]
   12. }
   13. }
   ```
