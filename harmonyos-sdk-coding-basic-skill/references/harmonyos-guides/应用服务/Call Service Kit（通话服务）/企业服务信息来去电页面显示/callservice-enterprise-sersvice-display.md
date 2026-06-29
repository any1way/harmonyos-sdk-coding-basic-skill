---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-sersvice-display
title: 企业服务信息来去电页面显示
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 企业服务信息来去电页面显示
category: harmonyos-guides
scraped_at: 2026-06-11T15:05:20+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:883967ef1bca6394c00c7f88a6321f82017891c619685120fe7108a9764c681e
---
从6.1.1(24)版本开始，新增支持企业服务信息来去电页面显示。

本功能仅供企业应用开发者接入。

## 场景介绍

来去电时，通过对端手机号，查询获取对应的企业服务信息，方便企业员工快速了解通话号码相关的服务数据，例如快递员在给客户打电话或者接电话时可以显示客户的快递信息，包括单号，地址等。

说明

来去电页面仅展示第一条企业服务信息数据，对于多个应用里同时存在数据时，按照应用包名的字典序排序，展示首个查询结果。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [queryNumberIdentifySwitchState](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/numberIdentify (号码识别查询基本能力)/callservicekit-numberldentify.md#querynumberidentifyswitchstate>) (context: Context):SwitchState | 查询陌生号码与信息识别总开关状态以及调用该接口的应用号码识别开关状态。 |
| [onQueryBusinessServiceData](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#onquerybusinessservicedata>)(phoneNumber: string): Promise<Array<BusinessServiceData>> | 查询企业服务信息。 |

## 申请接入

企业服务信息展示能力使用受限，如需接入，需要在AGC网站申请对应权限。

1.登录[AGC网站](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”。

2.在项目列表选择项目，并在应用列表下选择需要申请企业服务信息展示的应用。

3.进入“项目设置 > 开放能力管理”页面，点击“企业服务信息展示”对应的“申请”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/CfunH8nVT_OtqndMLyoZtA/zh-cn_image_0000002622698833.png?HW-CC-KV=V1&HW-CC-Date=20260611T070519Z&HW-CC-Expire=86400&HW-CC-Sign=101503215849E9518A0B942CCBCF7F6727D6B82DC98681C0523322CE415DA3F7)

4.请根据实际业务需求在弹框中填写对应信息，完成后，点击右上角“提交”，提交后将在3个工作日内完成审核，审核结果请在[互动中心](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/interactive)查看。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/vTCjnYo-QEmNgNo5vobThw/zh-cn_image_0000002592219272.png?HW-CC-KV=V1&HW-CC-Date=20260611T070519Z&HW-CC-Expire=86400&HW-CC-Sign=A01E30722613B1393D065448F26E3EAB6A188B98F0CBBB564B1C6E6702B7A678)

## 替换调试Profile

当企业服务信息展示能力申请成功后，需要重新[申请Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。并且在DevEco Studio中替换新申请的调试Profile。

说明

在应用正式发布前，需要替换成[发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)。

## 开发步骤

1. 在工程内创建一个ExtensionAbility类型的自定义组件并继承[CallerInfoQueryExtensionAbility](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#callerinfoqueryextensionability>)，完成[onQueryBusinessServiceData](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#onquerybusinessservicedata>)方法的复写。

   说明

   由于调用[onQueryBusinessServiceData](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#onquerybusinessservicedata>)方法时，系统先创建应用的AbilityStage实例，请勿在AbilityStage中添加过于复杂耗时的逻辑，避免调用超时。

   代码示例：

   ```
   1. import { CallerInfoQueryExtensionAbility, numberIdentify } from '@kit.CallServiceKit';

   3. export default class EntryBusinessServiceDataQueryExtAbility extends CallerInfoQueryExtensionAbility {
   4. // 来去电时由系统通话应用主动调用该接口查询企业联系人信息
   5. async onQueryBusinessServiceData(phoneNumber: string): Promise<Array<numberIdentify.BusinessServiceData>> {
   6. return new Promise<Array<numberIdentify.BusinessServiceData>>((resolve, reject) => {
   7. let isSuccess = true;
   8. // 在此处实现根据号码查询企业服务信息的业务逻辑
   9. if (isSuccess) {
   10. // 查询成功，返回结果
   11. resolve([{
   12. type: numberIdentify.BusinessServiceType.DELIVERY,
   13. delivery: {
   14. customerName: "xxxx",
   15. deliveryNumber: "xxxx",
   16. deliveryStatus: "xxxx",
   17. deliveryAddress: "xxxx",
   18. deliveryTimeout: "xxxx",
   19. deliveryStatusColor: numberIdentify.DeliveryStatusColor.GREEN
   20. }
   21. }]);
   22. } else {
   23. // 查询失败，返回错误原因
   24. reject("error reason");
   25. }
   26. });
   27. }
   28. }
   ```
2. 在应用配置文件module.json5中注册extensionAbilities，具体详见[module.json5配置](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)。

   配置文件示例：

   ```
   1. {
   2. "extensionAbilities": [
   3. {
   4. "name": "EntryBusinessServiceDataQueryExtAbility",
   5. "srcEntry": "./ets/businessservicedataquery/EntryBusinessServiceDataQueryExtAbility.ets",
   6. "type": "callerInfoQuery"
   7. }
   8. ]
   9. }
   ```

   * type标签需设为"callerInfoQuery"，表示该拓展类型为CallerInfoQueryExtensionAbility。
   * srcEntry标签表示上述ExtensionAbility组件所对应的代码路径。
3. 在调试设备上，前往“电话”，点击右上角的“更多”图标，前往“设置”>“陌生号码和信息识别”，或者通过[应用跳转陌生号码和信息识别页面](../应用跳转陌生号码和信息识别页面/callservice-enterprise-app-redirection.md)，打开对应陌生号码信息识别功能开关，再根据需要打开企业服务信息展示对应企业的开关，进行调试。
