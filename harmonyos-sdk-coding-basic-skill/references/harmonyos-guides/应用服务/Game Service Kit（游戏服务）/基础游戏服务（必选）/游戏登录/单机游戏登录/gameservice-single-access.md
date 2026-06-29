---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-single-access
title: 单机游戏登录
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 游戏登录 > 单机游戏登录
category: harmonyos-guides
scraped_at: 2026-06-11T15:07:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:54464b939133ef98d666578c68b0e3e1db3ad64db16c6636ffd9d53897a6a348
---
单机游戏是指数据本地化存储，不依赖服务器的游戏。

单机游戏接入基础游戏服务后，支持玩家使用华为账号快速进入游戏，且单机游戏的华为账号实名认证、未成年人防沉迷功能由基础游戏服务实现。

## 开发准备

### 创建游戏

在华为应用市场发布游戏，要求前往AppGallery Connect创建游戏类应用，具体操作请参见[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。其中：

* “应用类型”：选择“HarmonyOS应用”。
* “应用分类”：选择“游戏”。

说明

用于正式上架的游戏包名建议不要包含test、dev等信息。

### 申请版署实名认证

按照版署《关于开展网络游戏防沉迷实名认证系统接口对接工作的通知》，各游戏出版运营企业均要求在2021年6月1日前完成接入[网络游戏防沉迷实名认证系统](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/)，并获取“bizID（游戏备案识别码）”，再将bizID配置到AppGallery Connect，华为将为游戏自动对接国家新闻出版署的实名认证系统并开启强制实名认证，开发者无需进行额外的开发。具体操作请参见[版署实名认证申请](https://developer.huawei.com/consumer/cn/doc/games-guides/game-center-identification-applyfor-0000002392353221)。

### 生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性：

* 调试阶段：[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)、[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)、[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。
* 发布阶段：[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)、[申请发布证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-cert-0000002283336729)、[申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)。

### 配置签名证书指纹

AppGallery Connect会自动生成证书对应的公钥信息，并计算出对应的SHA256指纹。开发者前往AppGallery Connect获取并配置SHA256指纹，且每个游戏至多添加4个签名证书指纹，配置签名证书指纹的具体操作请参见[配置公钥指纹](https://developer.huawei.com/consumer/cn/doc/app/agc-help-cert-fingerprint-0000002278002933)。

说明

请在调试阶段添加调试证书对应的指纹，在发布阶段添加发布证书对应的指纹。

### 配置APP ID和Client ID

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏，获取“应用”下的APP ID和Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/JqrtftpzRJiIze02Ivo5rg/zh-cn_image_0000002592379254.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=661CD23D0B177A379E88C26B6D9D50DE805C842E73FEF41B7A293B0F1721860B)
2. 在工程的entry模块module.json5文件中，新增metadata并配置client\_id和app\_id，同时新增requestPermissions以配置网络权限。如下所示：

   ```
   1. "module": {
   2. "name": "entry",
   3. "type": "xxx",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [],
   7. "pages": "xxxx",
   8. "abilities": [],
   9. "metadata": [ // 配置如下信息
   10. {
   11. "name": "client_id",
   12. "value": "xxxxxx" // 配置为前面步骤中获取的Client ID
   13. },
   14. {
   15. "name": "app_id",
   16. "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
   17. }
   18. ],
   19. "requestPermissions": [ // 配置网络权限
   20. {
   21. "name": "ohos.permission.INTERNET"
   22. }
   23. ]
   24. }
   ```

### 配置APP ID映射关系

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏，左侧菜单选择“构建 > 游戏服务”，在右侧点击“新增配置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Nwz5vGjyRqebrSwMHR0Q2A/zh-cn_image_0000002622858763.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=7925256FCA230755DB3AEFA0DEE9DC26BB76631360EA6963D999702997CCBDA4)
2. 在弹出的“新增配置信息”窗口中选择HAP游戏和APK游戏，完成后点击“下一步”。

   说明

   请正确配置HAP游戏与APK游戏的映射关系。若开发者配置错误类型的游戏，将有提示框提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/dGc8YmMiRmeVVWCsBjOqLA/zh-cn_image_0000002622698883.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=A9A8B0438C32FAC12CCCD7104737225E165B288832329351BAB61CC3014AF4D2)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或待上架的APK游戏。 |
3. 在弹出的窗口中继续填写信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Dvi7T98aQxmpZbL3DGw9sw/zh-cn_image_0000002592219322.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=C7FA27E860DC839C7EDCA2ECB5628E45AF0E509B306560C8459655CF4DCD8C52)
4. （可选）填写开发者服务器的回调地址，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/ZHZgJ--JT2K072ro_urJWQ/zh-cn_image_0000002592379256.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=8E9112350D782A6A43C829EF421BABA2675AF5EF66553472AA2CE3C012682462)
5. 若出现异常情况（例如在架状态不符合要求），将在提示框以红字提醒，建议点击“取消”并重新配置映射关系。若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/qUB_0_QkT2iPs36v6Gz-xQ/zh-cn_image_0000002622858765.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=B9FB0EC86E3590F11577DE36399A05C9793155149DC4F0E7198C026199F48C0B)
6. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。

   APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/h9PwV6ZISMal7Fprg0s1jA/zh-cn_image_0000002622698885.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=A2CDB9416CEE467F474F9BDDF0305B32513A3A12A980EA5ACCAD10B1E66B1304)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/X5VEb-hJS9aPFKoGbvWUnA/zh-cn_image_0000002592219324.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=634968211DBB2799C66701533B511E4FAF6A9B92511D95390C9B9EC2C99B578B)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/yo0rhj6ZRoGjU43k2P5Q9A/zh-cn_image_0000002622698891.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=7A79023B34C16E27AA33A19E145B00FF021A9459765156CABB7A818B952FCEFB)

1. 玩家启动游戏。
2. 游戏调用[init](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerinit-1>)接口初始化Game Service Kit。初始化后，弹出华为隐私协议窗口，玩家确认同意后，则继续往下执行。
3. 游戏调用[unionLogin](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerunionlogin>)接口，要求showLoginDialog参数为false，thirdAccountInfos参数传空数组。
4. 游戏顶部弹出欢迎横幅，并向游戏返回accountName（使用华为账号登录返回值为hw\_account）、accountIdentifier（选择华为账号登录返回值为hw\_account）、gamePlayerId等信息。
5. 调用[verifyLocalPlayer](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerverifylocalplayer>)接口，对用户设备登录的华为账号进行如下合规校验。合规校验通过后，玩家进入游戏。

   1. 若玩家未完成实名认证，[verifyLocalPlayer](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerverifylocalplayer>)接口自动弹出实名认证窗口要求玩家进行实名认证。
   2. 若玩家账号实名认证为未成年人，[verifyLocalPlayer](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerverifylocalplayer>)接口将自动检测未成年人的游戏时间。若玩家不在指定时间内登录游戏，将强制玩家退出游戏并返回[1002000006](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/ArkTS API错误码/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间>)错误码。

## 接口说明

具体API说明请详见[接口文档](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md>)。

| 接口名 | 描述 |
| --- | --- |
| [init](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerinit-1>)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void | 游戏初始化接口，使用默认的上下文信息，使用callback回调。 |
| [unionLogin](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerunionlogin>)(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult> | 登录接口，通过Promise对象获取返回值。 |
| [verifyLocalPlayer](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerverifylocalplayer>)(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void> | 合规校验接口，校验当前设备登录的华为账号的实名认证、游戏防沉迷信息，通过Promise对象获取返回值。 |

## 开发步骤

### 导入模块

导入Game Service Kit模块及相关公共模块。

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';
```

### 初始化

调用[init](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerinit-1>)接口初始化Game Service Kit。

说明

* 调用接口时严格要求继承UIAbility，并且获取上下文的时机是onWindowStageCreate生命周期中页面加载成功后。
* 要求游戏先成功调用初始化[init](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerinit-1>)接口后再调用其他接口，否则将导致审核被驳回。

```
1. onWindowStageCreate(windowStage: window.WindowStage) {
2. windowStage.loadContent("pages/index", (err, data) => {
3. try {
4. gamePlayer.init(this.context,()=>{
5. hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
6. });
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
10. }
11. });
12. }
```

初始化后，游戏弹出华为隐私协议窗口，用户同意签署协议，则继续往下执行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/R0VpFIkwTtelUHPKBz7YlQ/zh-cn_image_0000002622698887.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=DB1C101507C381667668215526D7E339809D793CDB7866806B21A14E4ED09C57)

若当前华为账号同意过游戏服务隐私协议，后续使用该华为账号登录的游戏将不会再弹出隐私协议窗口。

### 登录游戏

调用[unionLogin](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerunionlogin>)接口登录游戏。

```
1. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
2. let request: gamePlayer.UnionLoginParam = {
3. showLoginDialog: false, // 是否弹出联合登录面板。true表示强制弹出面板，false表示优先使用玩家上一次的登录选择，不弹出联合登录面板，若玩家首次登录或卸载重装，则正常弹出
4. thirdAccountInfos: [] // 单机游戏请传空数组
5. };
6. try {
7. gamePlayer.unionLogin(context, request).then((result: gamePlayer.UnionLoginResult) => {
8. hilog.info(0x0000, 'testTag', `Succeeded in logging in: ${result?.accountName}`);
9. }).catch((error: BusinessError) => {
10. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
11. });
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
15. }
```

用户完成登录流程后，游戏顶部弹出欢迎横幅，并向游戏返回accountName（华为账号登录返回值为hw\_account）、gamePlayerId等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/27FphYblTVGgw2mV7u1kJA/zh-cn_image_0000002592219326.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=CD646476678E731BC2946D1B83B74DCF43E035FD766A3A46F6B44778CC2CB940)

### 合规校验

调用[verifyLocalPlayer](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerverifylocalplayer>)接口对用户设备登录华为账号的实名认证和未成年人防沉迷进行合规校验，校验通过后，玩家进入游戏。

```
1. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
2. let request: gamePlayer.ThirdUserInfo = {
3. thirdOpenId: '' // 单机游戏传空
4. };
5. try {
6. gamePlayer.verifyLocalPlayer(context, request).then(() => {
7. hilog.info(0x0000, 'testTag', `Succeeded in verifying.`);
8. }).catch((error: BusinessError) => {
9. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
10. });
11. } catch (error) {
12. let err = error as BusinessError;
13. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${err.code}, message: ${err.message}`);
14. }
```

华为账号的实名认证、未成年人防沉迷由基础游戏服务实现，华为账号的支付合规控制（例如未成年人支付限额）由IAP Kit（应用内支付服务）实现。

| 合规校验 | 校验项 | 国家政策 | 解决方案 |
| --- | --- | --- | --- |
| 华为账号实名认证 | 校验用户设备登录的华为账号是否已实名认证。 | 根据相关法律法规要求，所有网络游戏玩家必须使用真实有效身份信息注册并登录网络游戏。 | 若玩家使用未实名认证的华为账号登录游戏时，基础游戏服务向玩家弹出实名认证窗口，要求玩家进行实名认证。若玩家取消实名认证，则返回[1002000004](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/ArkTS API错误码/gameservice-error-code.md#section1002000004-实名认证返回强制实名但用户取消或需要强制实名但没有实名>)错误码。 |
| 未成年人防沉迷 | 校验已实名认证为未成年人的华为账号是否在规定时间内登录游戏。 | 根据国家新闻出版署的最新规定，所有网络游戏企业仅可在周五、周六、周日和法定节假日每日20时至21时向未成年人提供1小时网络游戏服务，其他时间均不得以任何形式向未成年人提供网络游戏服务。 | - 已实名认证为未成年人的华为账号在规定时间内登录游戏，当游戏进行到晚上21时，基础游戏服务会弹窗提示玩家已到游戏时间，强制玩家退出游戏并返回[1002000006](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/ArkTS API错误码/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间>)错误码。  - 已实名认证为未成年人的华为账号在非规定游戏时间内登录游戏，基础游戏服务会弹框提示玩家不允许游戏，强制玩家退出游戏并返回[1002000006](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/ArkTS API错误码/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间>)错误码。 |
| 未成年人支付限额 | 校验已实名认证为未成年人的华为账号是否限额付费。 | 根据国家新闻出版署的最新规定，网络游戏企业不得为未满8周岁的用户提供游戏付费服务。同一网络游戏企业所提供的游戏付费服务，8周岁以上未满16周岁的用户，单次充值金额不得超过50元人民币，每月充值金额累计不得超过200元人民币；16周岁以上未满18周岁的用户，单次充值金额不得超过100元人民币，每月充值金额累计不得超过400元人民币。 | 已实名认证为未成年人的华为账号在游戏内超额付费，IAP Kit会弹窗提示消费金额超出限制。  用户在使用华为应用内支付时，华为会自动根据国家新闻出版署的要求进行支付限额控制，开发者无需处理。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/NxbJ3nZmQ8GA0yB2Xz1b_w/zh-cn_image_0000002622858769.png?HW-CC-KV=V1&HW-CC-Date=20260611T070709Z&HW-CC-Expire=86400&HW-CC-Sign=4CC27CA4A848AD60317C491B09A01F0F1404E1E1569B6D0A3306646D97E490A4)
