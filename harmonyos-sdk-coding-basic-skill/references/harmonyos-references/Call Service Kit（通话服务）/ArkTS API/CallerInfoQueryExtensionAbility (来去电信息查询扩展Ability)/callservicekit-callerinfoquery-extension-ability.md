---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-callerinfoquery-extension-ability
title: CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)
category: harmonyos-references
scraped_at: 2026-06-01T16:33:21+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:a0f5eb6d3519621ccda6774ff7e18f9fc930546ffdfdf9558c1805fbb2bd37cc
---
CallerInfoQueryExtensionAbility是来去电信息查询扩展Ability，提供通话来去电页面显示企业联系人信息的能力。有如下约束：

* CallerInfoQueryExtensionAbility需求场景面向企业，仅供企业应用开发者接入。
* CallerInfoQueryExtensionAbility为轻量级独立子进程，不允许唤醒主进程，进程存在最长时间为2秒，超时后自动销毁。
* CallerInfoQueryExtensionAbility支持在[HAP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAP/hap-package.md)和[HAR](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)中使用。

**起始版本：** 5.0.2(14)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { CallerInfoQueryExtensionAbility, CallerInfo, numberIdentify } from '@kit.CallServiceKit';
```

## CallerInfoQueryExtensionAbility

PhonePC/2in1TabletWearable

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 5.0.2(14)

说明

由于调用onQueryCallerInfo方法时，系统先创建应用的AbilityStage实例，请勿在AbilityStage中添加过于复杂耗时的逻辑，避免调用超时。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [CallerInfoQueryExtensionContext](<../CallerInfoQueryExtensionContext (来去电信息查询扩展Context)/callservicekit-callerinfoquery-extension-context.md>) | 否 | 否 | [CallerInfoQueryExtensionContext](<../CallerInfoQueryExtensionContext (来去电信息查询扩展Context)/callservicekit-callerinfoquery-extension-context.md#callerinfoqueryextensioncontext>)的上下文环境，继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)。 |

### onQueryCallerInfo

PhonePC/2in1TabletWearable

onQueryCallerInfo(phoneNumber: string):Promise<[CallerInfo](callservicekit-callerinfoquery-extension-ability.md#callerinfo)>

查询企业联系人接口，利用Promise返回查询结果，供来电和去电页面展示。企业应用需继承CallerInfoQueryExtensionAbility实现该接口，接口查询时间建议小于1s。由于通话应用会对已查询过的联系人进行缓存，若需清除该联系人缓存信息请使用resolve({ contactName: '' })。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 需要查询的号码 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CallerInfo](callservicekit-callerinfoquery-extension-ability.md#callerinfo)> | Promise对象，返回查询的号码信息。 |

**示例：**

```
1. import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';

3. export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
4. onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
5. return new Promise<CallerInfo>((resolve, reject) => {
6. let isSuccess = true;
7. // 在此处实现根据号码查询企业联系人的业务逻辑
8. if (isSuccess) {
9. // 查询成功，返回结果
10. resolve({
11. contactName:"xxxx",
12. employeeId:"xxxx",
13. department:"xxxx",
14. position:"xxxx"
15. });
16. } else {
17. // 查询失败，返回错误原因
18. reject("error reason");
19. }
20. });
21. }
22. }
```

**RDB场景示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { relationalStore } from '@kit.ArkData';
3. import { CallerInfo, CallerInfoQueryExtensionAbility } from '@kit.CallServiceKit';
4. export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
5. async onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
6. // 使用rdb场景需转化context类型
7. const context = (this.context as common.ExtensionContext).getApplicationContext();
8. let store = await relationalStore.getRdbStore(context, null);
9. // 查询rdb数据后返回
10. return new Promise<CallerInfo>((resolve, reject) => {
11. let isSuccess = true;
12. // 在此处实现根据号码查询企业联系人的业务逻辑
13. if (isSuccess) {
14. // 查询成功，返回结果
15. resolve({
16. contactName: "xxxx",
17. employeeId: "xxxx",
18. department: "xxxx",
19. position: "xxxx"
20. });
21. } else {
22. // 查询失败，返回错误原因
23. reject("error reason");
24. }
25. });
26. }
27. }
```

### onQueryBusinessServiceData

PhonePC/2in1TabletWearable

onQueryBusinessServiceData(phoneNumber: string): Promise<Array<BusinessServiceData>>

查询企业服务信息，用于来电和去电页面展示。使用Promise异步回调。

企业应用需继承CallerInfoQueryExtensionAbility实现该接口，接口查询时间建议小于1s。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 需要查询的号码 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[BusinessServiceData](<../numberIdentify (号码识别查询基本能力)/callservicekit-numberldentify.md#businessservicedata>)>> | Promise对象，返回查询的企业服务信息列表。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { relationalStore } from '@kit.ArkData';
3. import { CallerInfoQueryExtensionAbility, numberIdentify } from '@kit.CallServiceKit';

5. export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
6. async onQueryBusinessServiceData(phoneNumber: string): Promise<Array<numberIdentify.BusinessServiceData>> {
7. // 使用rdb场景需转化context类型
8. const context = (this.context as common.ExtensionContext).getApplicationContext();
9. let store = await relationalStore.getRdbStore(context, null);
10. // 查询rdb数据后返回
11. return new Promise<Array<numberIdentify.BusinessServiceData>>((resolve, reject) => {
12. let isSuccess = true;
13. // 在此处实现根据号码查询企业联系人的业务逻辑
14. if (isSuccess) {
15. // 查询成功，返回结果
16. resolve([{
17. type: numberIdentify.BusinessServiceType.DELIVERY,
18. delivery: {
19. customerName: "xxxx",
20. deliveryNumber: "xxxx",
21. deliveryStatus: "xxxx",
22. deliveryAddress: "xxxx",
23. deliveryTimeout: "xxxx",
24. deliveryStatusColor: numberIdentify.DeliveryStatusColor.GREEN
25. }
26. }]);
27. } else {
28. // 查询失败，返回错误原因
29. reject("error reason");
30. }
31. });
32. }
33. }
```

## CallerInfo

PhonePC/2in1TabletWearable

联系人信息。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contactName | string | 否 | 否 | 联系人姓名：为保证页面最佳显示效果，字数建议限制在20字以内。 |
| employeeId | string | 否 | 是 | 工号：为保证页面最佳显示效果，字数建议限制在20字以内。 |
| department | string | 否 | 是 | 部门：为保证页面最佳显示效果，字数建议限制在20字以内。 |
| position | string | 否 | 是 | 职位：为保证页面最佳显示效果，字数建议限制在20字以内。 |
