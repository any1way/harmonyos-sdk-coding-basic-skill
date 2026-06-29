---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-verifybypwd
title: 交易信息密码认证
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 交易信息密码认证
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:05+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:884cc4fca40f7637fecdf497d50463c4e7f5245fa3106bd83c3cf5c2c583c05b
---
## 场景介绍

在交易信息密码认证场景中，可以利用创建的数字盾密码对交易信息进行认证，可通过密钥管理服务提供的签名认证功能来确认交易内容是否被篡改，以确保整个交易过程的安全性。

## 约束与限制

本功能在API 24之前版本仅支持Phone；API24及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#checkconfirmuitextformat>)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/P78WExFuSi-P7VVW2HnfFw/zh-cn_image_0000002622858253.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T064403Z&HW-CC-Expire=86400&HW-CC-Sign=F86C1568D2D07164AA6B195016D8459AE674CBFA8CB8894A06C5B58AE5A3C4F1)

## 接口说明

接口及使用方法请参见[API参考](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/ArkTS API错误码/TrustedAuthentication （数字盾服务）/devicesecurity-arktsapi-errcode-trusted-auth.md>)。

| 接口名 | 描述 |
| --- | --- |
| [procContentAuthentication](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#proccontentauthentication>)(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken> | 交易信息处理接口 |

## 交易信息密码认证界面介绍

如图1、图2、图3为手机端使用数字盾密码进行交易认证时对应的TUI界面示例，其中交易信息密码认证分为两种场景：

1. 当用户交易信息不超过6行时，则以下图1中无翻页形式进行密码认证。
2. 当用户交易信息超过6行时，则以下图2-3中翻页形式进行密码认证，且当交易信息超过19行时，则Device Security Kit拒绝拉起TUI界面。

**图1** 无翻页密码认证

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/gP5wb6JWQdeNf-8jvh_wBA/zh-cn_image_0000002622698375.png?HW-CC-KV=V1&HW-CC-Date=20260611T064403Z&HW-CC-Expire=86400&HW-CC-Sign=31FA429269DB5E627481A5FA38AA822C1ADDF53FD5286A047E892AD5E7B8BDA3)

**图2** 翻页密码认证-1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/dJ_k6R6pTGS7CWXegUYiXw/zh-cn_image_0000002592218814.png?HW-CC-KV=V1&HW-CC-Date=20260611T064403Z&HW-CC-Expire=86400&HW-CC-Sign=0FD5A80D621187B0EF914DA804D54C5B56404AC4DE2BBB7760BF8A914B7E396D)

**图3** 翻页密码认证-2

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WgJdHCcCS0WcmP9lBV8wag/zh-cn_image_0000002592378748.png?HW-CC-KV=V1&HW-CC-Date=20260611T064403Z&HW-CC-Expire=86400&HW-CC-Sign=D2C50396D430C66BBC69833BD4C6EC26295A2C1E36C20B090353C7755E81D89A)

交易信息格式说明如下：

1. **带标记格式**，以key:value|flag形式，flag取值如下：

   * 0：表示不展示该行内容。
   * 1：单行截断展示（若内容超出一行则截断）。
   * 2：自动换行展示（若内容超出一行则换行）。

   如当交易信息为“收款户名：王\*\*|1”，表示key为“收款户名”， value为“王\*\*”，flag为1，该内容若超过一行则截断显示。

   说明

   * 当行内出现“|”符号时，系统默认按此格式解析，若交易内容格式未全部以该格式输出，则会显示失败。
   * 若flag=1（截断模式）的key过长导致value无法显示时，则会显示失败。
2. **无标记格式**，直接输入内容（无“|”符号）。

   * 系统将完整展示所有内容，超出一行时自动换行。
3. **文本显示规格**。

   * 输入字体要求utf-8。
   * 当输入字符为生僻字时，显示\*。

如图为PC端使用数字盾密码进行交易认证时对应的TUI界面示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/nprOzWoNT92XFrCl0NqXGw/zh-cn_image_0000002622858255.png?HW-CC-KV=V1&HW-CC-Date=20260611T064403Z&HW-CC-Expire=86400&HW-CC-Sign=D4E6755A509AB68F80EAC9E8036AC53456AC1046E116EA528303EDBDFFAEEDA0)

PC场景数字盾规格说明如下：

1. **界面布局与显示**。

   * TUI界面显示在屏幕中央，背景透明区域为富执行环境（Rich Execution Environment，REE）。
2. **交互方式**。

   * 鼠标操作：当TUI界面拉起后，鼠标仅可点击REE侧界面，无法操作TUI界面。
   * 触控操作：当TUI界面拉起后，设备仅响应TUI区域内的触控操作。
   * 键盘操作：当TUI界面拉起后，用户仅可通过内置键盘输入，为确保用户使用安全性，暂不支持外置键盘输入。
3. **数字盾服务键盘使用场景规格说明**

   * TUI界面支持数字、大小写字母及 !、@ 等特殊符号输入，同样具备Backspace键删除、ESC键退出和Enter键换行或确认功能。
   * TUI运行于可信执行环境（TEE），内置键盘处于安全状态，无法对TUI界面之外的区域进行输入操作，确保敏感数据在可信执行环境中得到保护。

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
   8. import { util } from '@kit.ArkTS';
   ```
2. 发起交易认证前，需从服务器获取当前账号在[设置数字盾密码](../数字盾密码管理/设置数字盾密码/devicesecurity-trustedauth-setpwd.md)时获取的authID。
3. 参考密钥管理服务提供的[签名/验签指导](<../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>)，初始化签名会话。

   说明

   * 设置签名密钥时密钥属性集合中需要指定tag: huks.HuksTag.HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE值为huks.HuksSecureSignType.HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO，即可对附加的交易信息做签名认证。

   ```
   1. // 设置签名密钥属性示例
   2. let properties: Array<huks.HuksParam> = [{
   3. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   4. value: huks.HuksKeyAlg.HUKS_ALG_ECC
   5. }, {
   6. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   7. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
   8. }, {
   9. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   10. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
   11. }, {
   12. tag: huks.HuksTag.HUKS_TAG_DIGEST,
   13. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
   14. },
   15. // 表示对附加的交易信息做签名认证
   16. {
   17. tag: huks.HuksTag.HUKS_TAG_KEY_SECURE_SIGN_TYPE,
   18. value: huks.HuksSecureSignType.HUKS_SECURE_SIGN_WITH_AUTHINFO
   19. }];
   ```
4. 调用交易认证接口，发起密码认证交易申请，当用户密码认证通过后，即可获得携带交易信息hash的authToken。

   ```
   1. async function ContentVerifyByPwd(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
   2. try {
   3. const authID: bigint = 11842183505170721246n; // 实际填充为从服务器获取到的账号对应的authID值
   4. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   5. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); // 实际使用时请替换为应用要在TUI界面展示的logo图片名称
   6. const reqParams:trustedAuthentication.AuthReqParams = {
   7. reqType: trustedAuthentication.AuthType.AUTH_TYPE_TUI_PIN,
   8. authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"], // 实际使用时填充为交易信息，每一行交易信息为其中的一个字符串成员
   9. }
   10. const buffer = fileData.buffer;
   11. const label:trustedAuthentication.TUILable = {
   12. image: buffer as ArrayBuffer,
   13. title: "密码交易认证",
   14. }
   15. const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
   16. return result;
   17. } catch (err) {
   18. hilog.error(0x0000, 'testTag', `Failed to procContentAuthentication, code:${err.code}, message:${err.message}`);
   19. throw new Error('Content verify by password failed:' + (err as BusinessError).message);
   20. }
   21. }
   22. const rand = cryptoFramework.createRandom();
   23. const len: number = 32;
   24. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data; // 实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   25. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   26. const authToken: trustedAuthentication.AuthToken = await ContentVerifyByPwd(challenge, context);
   ```
5. 参考密钥管理服务提供的[针对携带认证信息的签名/验签指导](<../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md#eccsha256携带认证信息的签名类型>), 对交易信息authToken数据进行签名验证，并结束会话。

   说明

   需要注意的是，在交易认证过程中输入的交易信息格式如下：

   ```
   1. // 示例交易信息
   2. authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"];
   ```

   而密钥管理服务验签时的inputData信息为Uint8Array，需要将所有信息按照\n拼接，并将UTF-8信息转换为Uint8Array

   ```
   1. function encodeUtf8(s: string): number[] {
   2. const encoder = new util.TextEncoder();

   4. const dest = new Uint8Array(s.length * 4);
   5. const result = encoder.encodeIntoUint8Array(s, dest);
   6. const encodedBytes = dest.subarray(0, result.written);
   7. return Array.from(encodedBytes);
   8. };
   9. // 实际为应用向密钥管理服务传入的验签数据
   10. let str = "用户：王xx\n账号：95588180804408xxxx\n交易金额：1000000000";
   11. const utf8Bytes = new Uint8Array(encodeUtf8(str));
   ```
6. 参考密钥管理服务提供的[签名/验签指导](<../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>), 对签名数据进行验签操作，验签通过后可完成对应账户的转账扣款。
