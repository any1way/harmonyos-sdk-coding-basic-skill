---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-modifypwd
title: 修改数字盾密码
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾密码管理 > 修改数字盾密码
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:02+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:94cca56c42513e13ded7eaae678d9c050f89c1f44490604f37f7fa0b595943ee
---
## 场景介绍

激活数字盾后，用户可在完成旧密码认证后，修改数字盾密码信息。

## 约束与限制

本功能在API 24之前版本仅支持Phone；API24及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#checkconfirmuitextformat>)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/JcFkTxxeT1ahCm6hfuKKiw/zh-cn_image_0000002592378744.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T064401Z&HW-CC-Expire=86400&HW-CC-Sign=DBAB15201409D8629CDA182F2D9FA7AA447B6164D7EACA9735F868C00199A0B0)

## 接口说明

接口及使用方法请参见[API参考](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md>)。

| 接口名 | 描述 |
| --- | --- |
| [modifyTrustedAuthenticationPwd](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#modifytrustedauthenticationpwd>)(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken> | 修改数字盾密码 |

## 修改数字盾密码界面介绍

如图1、图2为修改数字盾密码时对应的TUI界面示例，用户需使用旧密码认证通过后，方可设置新密码。密码认证失败时，剩余认证次数减1，当剩余认证次数为0时，则锁定数字盾服务。新密码长度、对应TUI应用图标以及当前应用场景说明均由开发者调用接口时传入。

**图1** 旧密码认证

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/BZl2ClsyRIeT21oHManrzg/zh-cn_image_0000002622858251.png?HW-CC-KV=V1&HW-CC-Date=20260611T064401Z&HW-CC-Expire=86400&HW-CC-Sign=F8F5865D25E7DE07101CC456EBE1AB107FC6B73D56F7E0A074DA97E7B9731EA6)

**图2** 新密码设置

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/fxBrFUDbTSiwNu19-aqzsQ/zh-cn_image_0000002622698373.png?HW-CC-KV=V1&HW-CC-Date=20260611T064401Z&HW-CC-Expire=86400&HW-CC-Sign=01CD8449DFAFE42EADB8D8657ACFED89A209F71A220E219CF0A60CC7C7F8552A)

## 开发步骤

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
2. 修改密码前，需从服务器获取当前账号在[设置数字盾密码](../设置数字盾密码/devicesecurity-trustedauth-setpwd.md)时获取的authID。
3. 参考密钥管理服务提供的[签名/验签指导](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>)，初始化签名会话。
4. 调用数字盾服务修改密码接口，发起数字盾密码修改申请。

   ```
   1. // 修改数字盾密码
   2. async function ModifyPwd(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
   3. try {
   4. const passwordInfo: trustedAuthentication.PasswordInfo = {
   5. pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_DIGITAL,
   6. pwdMaxLength: 10,
   7. pwdMinLength: 6,
   8. maxAuthFailCount: 6,
   9. };
   10. const authID: bigint = 1687413472599354502n;//实际填充为从服务器获取到的账号对应的authID值
   11. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   12. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
   13. const buffer = fileData.buffer;
   14. const label:trustedAuthentication.TUILable = {
   15. image: buffer as ArrayBuffer,
   16. title: "修改密码",
   17. }
   18. const authToken = await trustedAuthentication.modifyTrustedAuthenticationPwd(challenge, passwordInfo, authID, label);
   19. return authToken;
   20. } catch (err) {
   21. hilog.error(0x0000, 'testTag', `Failed to modifyTrustedAuthenticationPwd, code:${err.code}, message:${err.message}`);
   22. throw new Error('Modify password failed:' + (err as BusinessError).message);
   23. }
   24. }
   25. const rand = cryptoFramework.createRandom();
   26. const len: number = 32;
   27. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;//实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   28. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   29. const authToken: trustedAuthentication.AuthToken = await ModifyPwd(challenge, context);
   ```
5. 参考密钥管理服务提供的[签名/验签指导](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>), 对通过修改密码获取到的authToken数据进行签名，并结束会话。
