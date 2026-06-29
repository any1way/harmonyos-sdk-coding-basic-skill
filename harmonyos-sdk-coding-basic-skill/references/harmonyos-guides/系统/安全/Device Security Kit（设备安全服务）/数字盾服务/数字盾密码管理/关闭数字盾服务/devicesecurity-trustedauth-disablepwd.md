---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-disablepwd
title: 关闭数字盾服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾密码管理 > 关闭数字盾服务
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:03+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:15c5383ee95c048a4a11f7a187590dfbf4a6ce7e2cb2a5b5de2c0c9831e63dde
---
## 场景介绍

当用户不再使用数字盾时，可以通过密码认证主动发起关闭数字盾的操作；若用户忘记密码或连续密码认证失败次数达到最大限制导致数字盾密码锁定，当应用将在重新激活数字盾时，无需进行密码认证直接关闭最初激活的数字盾，并通过[设置数字盾密码](../设置数字盾密码/devicesecurity-trustedauth-setpwd.md)重新创建新的数字盾密码。

## 约束与限制

本功能在API 24之前版本仅支持Phone；API24及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#checkconfirmuitextformat>)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/CdGHCz5uQymQtcg32AATjw/zh-cn_image_0000002592218812.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T064402Z&HW-CC-Expire=86400&HW-CC-Sign=5202A570AFD6BE6C87AEE31D0E5A385F288879A0C168A69A40D0EBC4FEFA66B8)

当不需要密码认证进行关闭数字盾申请时，则无需和Universal Keystore Kit交互，使用随机生成的challenge完成关闭数字盾操作。

## 接口说明

接口及使用方法请参见[API参考](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md>)。

| 接口名 | 描述 |
| --- | --- |
| [disableTrustedAuthentication](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#disabletrustedauthentication>)(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken> | 关闭数字盾服务 |

## 关闭数字盾服务界面介绍

如图为需要进行密码认证的方式关闭数字盾服务时对应的TUI界面示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/rE5YZH2yStGEBbCBqo0abg/zh-cn_image_0000002592378746.png?HW-CC-KV=V1&HW-CC-Date=20260611T064402Z&HW-CC-Expire=86400&HW-CC-Sign=917E1190E34B7211443109BD37F18E893E28CC78D9C8968C57DD09EC1CC259DF)

## 开发步骤

### 密码认证方式关闭数字盾服务

1. 导入huks 、trustedAuthentication 和相关依赖模块。

   ```
   1. import { resourceManager } from '@kit.LocalizationKit'
   2. import { huks } from '@kit.UniversalKeystoreKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   6. import { hilog } from '@kit.PerformanceAnalysisKit';
   7. import { common } from '@kit.AbilityKit';
   ```
2. 关闭数字盾前，需从服务器获取当前账号在[设置数字盾密码](../设置数字盾密码/devicesecurity-trustedauth-setpwd.md)时获取的authID。
3. 参考密钥管理服务提供的[签名/验签指导](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>)，初始化签名会话。
4. 调用关闭数字盾服务接口，发起数字盾服务关闭申请。

   ```
   1. // 关闭数字盾服务
   2. async function DisablePwd(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
   3. try {
   4. const authID: bigint = 1687413472599354502n;//实际填充为从服务器获取到的账号对应的authID值
   5. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   6. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
   7. const buffer = fileData.buffer;
   8. const label:trustedAuthentication.TUILable = {
   9. image: buffer as ArrayBuffer,
   10. title: "关闭数字盾",
   11. }
   12. const authToken = await trustedAuthentication.disableTrustedAuthentication(challenge, true, authID, label);
   13. return authToken;
   14. } catch (err) {
   15. hilog.error(0x0000, 'testTag', `Failed to disableTrustedAuthentication, code:${err.code}, message:${err.message}`);
   16. throw new Error('Close trusted authentication failed:' + (err as BusinessError).message);
   17. }
   18. }
   19. const rand = cryptoFramework.createRandom();
   20. const len: number = 32;
   21. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;//实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   22. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   23. const authToken: trustedAuthentication.AuthToken = await DisablePwd(challenge, context);
   ```
5. 参考密钥管理服务提供的[签名/验签指导](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>), 对通过关闭数字盾获取到的authToken数据进行签名，并结束会话。

### 无需密码认证方式关闭数字盾服务

使用cryptoFramework生成的32字节随机数作为challenge，直接调用关闭数字盾服务接口即可，生成的authToken信息未经过密码认证，不可进行签名校验。

```
1. // 关闭数字盾服务
2. async function DisablePwd(challenge: Uint8Array):Promise<trustedAuthentication.AuthToken> {
3. try {
4. const authID: bigint = 1687413472599354502n;//实际填充为从服务器获取到的账号对应的authID值
5. let emptyBuffer = new ArrayBuffer(0);
6. const label:trustedAuthentication.TUILable = {
7. image: emptyBuffer,
8. title: "",
9. }
10. const authToken = await trustedAuthentication.disableTrustedAuthentication(challenge, false, authID, label);
11. return authToken;
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to disableTrustedAuthentication, code:${err.code}, message:${err.message}`);
14. throw new Error('Close trusted authentication failed:' + (err as BusinessError).message);
15. }
16. }
17. const rand = cryptoFramework.createRandom();
18. const len: number = 32;
19. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;//此处使用的challenge为通过cryptoFramework生成的32字节随机数即可
20. const authToken: trustedAuthentication.AuthToken = await DisablePwd(challenge);
```
