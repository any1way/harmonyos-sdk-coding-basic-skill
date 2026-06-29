---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-useriam-userauthicon
title: @ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)
breadcrumb: API参考 > 系统 > 安全 > User Authentication Kit（用户认证服务） > ArkTS组件 > @ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)
category: harmonyos-references
scraped_at: 2026-06-11T16:13:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0cd48ce7391fc4a0845f5a18abfdae7a5440d1f49f84aa76e1edc2edc04bc03b
---
提供应用界面上展示的人脸、指纹认证图标，具体功能如下：

1. 提供嵌入式的人脸、指纹认证控件图标，可被应用集成。
2. 支持自定义图标的颜色和大小，但图标样式不可变更。
3. 点击控件图标后将以系统弹窗的方式，拉起人脸、指纹认证控件。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';
```

## 子组件

PhonePC/2in1TabletWearable

无

## 属性

PhonePC/2in1TabletWearable

不支持通用属性。

## UserAuthIcon

PhonePC/2in1TabletWearable

```
1. UserAuthIcon({
2. authParam: userAuth.AuthParam,
3. widgetParam: userAuth.WidgetParam,
4. iconHeight?: Dimension,
5. iconColor?: ResourceColor,
6. onIconClick?: ()=>void,
7. onAuthResult: (result: userAuth.UserAuthResult)=>void
8. })
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authParam | [userAuth.AuthParam](<../../ArkTS API/@ohos.userIAM.userAuth (用户认证)/js-apis-useriam-userauth.md#authparam10>) | 是 | 用户认证相关参数。 |
| widgetParam | [userAuth.WidgetParam](<../../ArkTS API/@ohos.userIAM.userAuth (用户认证)/js-apis-useriam-userauth.md#widgetparam10>) | 是 | 用户认证界面配置相关参数。 |
| iconHeight | [Dimension](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#dimension10) | 否 | 设置icon的高度，宽高比1:1，默认64fp，不支持百分比字符串。 |
| iconColor | [ResourceColor](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 设置icon的颜色，默认值：$r('sys.color.ohos\_id\_color\_activated')。 |
| onIconClick | ()=>void | 否 | 用户点击icon回调接口。 |
| onAuthResult | (result: [userAuth.UserAuthResult](<../../ArkTS API/@ohos.userIAM.userAuth (用户认证)/js-apis-useriam-userauth.md#userauthresult10>))=>void | 是 | 用户认证结果信息回调接口。  应用需要申请ohos.permission.ACCESS\_BIOMETRIC权限，否则应用将仅展示图标，无法正常拉起身份认证控件。 |

## 事件

PhonePC/2in1TabletWearable

不支持通用事件。

## 示例

PhonePC/2in1TabletWearable

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

4. @Entry
5. @Component
6. struct Index {
7. rand = cryptoFramework.createRandom();
8. len: number = 16;
9. randData: Uint8Array = this.rand?.generateRandomSync(this.len)?.data;
10. authParam: userAuth.AuthParam = {
11. challenge: this.randData,
12. authType: [userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN],
13. authTrustLevel: userAuth.AuthTrustLevel.ATL3
14. };
15. widgetParam: userAuth.WidgetParam = {
16. title: '请进行身份认证'
17. };

19. build() {
20. Row() {
21. Column() {
22. UserAuthIcon({
23. authParam: this.authParam,
24. widgetParam: this.widgetParam,
25. iconHeight: 200,
26. iconColor: Color.Blue,
27. onIconClick: () => {
28. console.info('The user clicked the icon.');
29. },
30. onAuthResult: (result: userAuth.UserAuthResult) => {
31. console.info(`Get user auth result, result = ${result.result}`);
32. }
33. })
34. }
35. }
36. }
37. }
```

调用onAuthResult可能会抛出错误码，错误码详细介绍请参见[通用错误码](../../../通用错误码/errorcode-universal.md)和[用户认证错误码](../../错误码/用户认证错误码/errorcode-useriam.md)。

**人脸认证图例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/NbevedbGSE2G5NIiWdE3qQ/zh-cn_image_0000002592221006.png?HW-CC-KV=V1&HW-CC-Date=20260611T081340Z&HW-CC-Expire=86400&HW-CC-Sign=DDA1734BF90D58054F38679D941DF8A46DD1A9DB388B180FC5029DADD17F7C9E)

**指纹认证图例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/8F9L1ZkrQUqRajW8iwmCNA/zh-cn_image_0000002592380938.png?HW-CC-KV=V1&HW-CC-Date=20260611T081340Z&HW-CC-Expire=86400&HW-CC-Sign=356FAA8C1C21EA138E6A50BC3EE5CE5BF5F2EC24726111E6942AEBF97866FDF7)
