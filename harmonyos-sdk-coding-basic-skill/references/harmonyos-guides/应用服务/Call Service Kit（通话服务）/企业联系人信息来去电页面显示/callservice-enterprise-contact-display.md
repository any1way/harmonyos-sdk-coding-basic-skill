---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-contact-display
title: 企业联系人信息来去电页面显示
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 企业联系人信息来去电页面显示
category: harmonyos-guides
scraped_at: 2026-06-11T15:05:20+08:00
doc_updated_at: 
content_hash: sha256:a086084e9cb8ba37933d7b756b14eab774ad0fc594cc0804adf4b7fe4378ed21
---
本功能仅供企业应用开发者接入。

## 场景介绍

来去电时，页面显示已安装企业应用的联系人信息，方便用户识别来去电人信息，快速回应，增强企业内部沟通效率。

说明

来去电页面或横幅仅展示一个联系人信息，对于多个应用里存在相同联系人的情况，按照应用包名的字典序排序，展示首个查询结果。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [onQueryCallerInfo](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo>)(phoneNumber: string)：Promise<CallerInfo> | 查询联系人信息接口。 |
| [queryNumberIdentifySwitchState](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/numberIdentify (号码识别查询基本能力)/callservicekit-numberldentify.md#querynumberidentifyswitchstate>) (context: Context):SwitchState | 查询陌生号码与信息识别总开关状态以及调用该接口的应用号码识别开关状态。 |
| [isSupportEnterpriseNumberIdentify](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/numberIdentify (号码识别查询基本能力)/callservicekit-numberldentify.md#issupportenterprisenumberidentify>)(context: Context): Promise<boolean> | 查询是否已开通企业来电显示权限。 |

## 申请接入

企业来电显示能力使用受限，如需接入，需要在AGC网站申请对应权限。

1.登录[AGC网站](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”。

2.在项目列表选择项目，并在应用列表下选择需要申请企业来电显示的应用。

3.进入“项目设置 > 开放能力管理”页面，点击“企业来电显示”对应的“申请”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/KDPdspquT2mCKgFnra-Peg/zh-cn_image_0000002592379204.png?HW-CC-KV=V1&HW-CC-Date=20260611T070519Z&HW-CC-Expire=86400&HW-CC-Sign=156FD74FF84B0ADF5F06607CB7001BFA51C7B555027A4422C46F6C90B58852FD)

4.请根据实际业务需求在弹框中填写对应信息，完成后，点击右上角“提交”，提交后将在3个工作日内回复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sdJVwcQFTaOxbYtZ7eP7Gw/zh-cn_image_0000002622858713.png?HW-CC-KV=V1&HW-CC-Date=20260611T070519Z&HW-CC-Expire=86400&HW-CC-Sign=144AFE5455D2237AA63574FDE7729D94C7DEE38220C176E571E268D389D8E721)

## 替换调试Profile

当企业来电显示能力申请成功后，需要重新[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)。并且在DevEco Studio中替换新申请的调试Profile。

## 开发步骤

1. 在工程内创建一个[ExtensionAbility](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/extensionability-overview.md>)类型的自定义组件并继承[CallerInfoQueryExtensionAbility](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#callerinfoqueryextensionability>)，完成onQueryCallerInfo方法的复写。

   说明：

   由于调用onQueryCallerInfo方法时，系统先创建应用的AbilityStage实例，请勿在AbilityStage中添加过于复杂耗时的逻辑，避免调用超时。

   代码示例：

   ```
   1. import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';

   3. export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
   4. // 来去电时由系统通话应用主动调用该接口查询企业联系人信息
   5. onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
   6. return new Promise<CallerInfo>((resolve, reject) => {
   7. let isSuccess = true;
   8. // 在此处实现根据号码查询企业联系人的业务逻辑
   9. if (isSuccess) {
   10. // 查询成功，返回结果
   11. resolve({
   12. contactName:"xxxx",
   13. employeeId:"xxxx",
   14. department:"xxxx",
   15. position:"xxxx"
   16. });
   17. } else {
   18. // 查询失败，返回错误原因
   19. reject("error reason");
   20. }
   21. });
   22. }
   23. }
   ```
2. 在应用配置文件module.json5中注册extensionAbilities，具体详见[module.json5配置](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)。

   配置文件示例：

   ```
   1. {
   2. "extensionAbilities": [
   3. {
   4. "name": "EntryCallerInfoQueryExtAbility",
   5. "srcEntry": "./ets/callerinfoquery/EntryCallerInfoQueryExtAbility.ets",
   6. "type": "callerInfoQuery"
   7. }
   8. ]
   9. }
   ```

   * type标签需设为"callerInfoQuery"，表示该拓展类型为CallerInfoQueryExtensionAbility。
   * srcEntry标签表示上述ExtensionAbility组件所对应的代码路径。
3. 在调试设备上，前往“电话”，点击右上角的“更多”图标，前往“设置”>“陌生号码和信息识别”，或者通过[应用跳转陌生号码和信息识别页面](../应用跳转陌生号码和信息识别页面/callservice-enterprise-app-redirection.md)，打开对应企业应用的号码识别功能开关，进行调试。
