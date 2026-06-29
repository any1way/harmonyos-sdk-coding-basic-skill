---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-sec-panel
title: 分享详情页处理分享内容
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 分享详情页处理分享内容
category: harmonyos-guides
scraped_at: 2026-06-01T15:11:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dd3f79e235bec70dae9a7567fbf44acd7d3f7db0a2a5d40b23e928a50b439fc4
---
分享详情页能力基于[UIExtensionAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)/js-apis-app-abili_64670486.md>)界面嵌入能力。目标应用可以通过[ShareExtensionAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)/js-apis-_56257748.md>)构建接收分享内容的分享详情页，并将应用显示到分享面板应用推荐区内，通过分享详情页便捷的处理分享内容。开发时需要接入方实现[ShareExtensionAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)/js-apis-_56257748.md>)并于module.json5中注册支持分享内容的能力。

通过此方式注册的应用，点击时将跳转到分享详情页，也可返回分享面板。参见：[分享详情页面](https://developer.huawei.com/consumer/cn/doc/design-guides/share-0000001957076313#section27599419404)。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
   2. import { systemShare } from '@kit.ShareKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 目标应用可以使用[ShareExtensionAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)/js-apis-_56257748.md>)为基类构建分享能力Ability。在Ability被启动后，可以在其[onSessionCreate](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)/js-apis-app-abili_64670486.md#onsessioncreate>)回调中获取传入的want参数，将want参数通过[getSharedData](<../../../../../../harmonyos-references/Share Kit（分享服务）/ArkTS API/systemShare（分享）/share-system-share.md#getshareddata>)解析后得到分享数据。

   ```
   1. export default class TestShareAbility extends ShareExtensionAbility {
   2. onSessionCreate(want: Want, session: UIExtensionContentSession) {
   3. systemShare.getSharedData(want)
   4. .then((data: systemShare.SharedData) => {
   5. data.getRecords().forEach((record: systemShare.SharedRecord) => {
   6. // 处理分享数据
   7. });
   8. session.loadContent('pages/Index');
   9. })
   10. .catch((error: BusinessError) => {
   11. console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
   12. session.terminateSelf();
   13. });
   14. }
   15. }
   ```
3. （可选）社交类应用可通过[意图框架](<../../../../../AI/Intents Kit（意图框架服务）/Intents Kit简介/intents-introduction.md>)捐献联系人推荐信息。当用户在推荐区选择联系人进行内容分享时，社交应用注册的Ability可从接收的want数据中获取到联系人信息，直接分享数据到指定用户。

   ```
   1. export default class TestShareAbility extends ShareExtensionAbility {
   2. onSessionCreate(want: Want, session: UIExtensionContentSession) {
   3. systemShare.getContactInfo(want)
   4. .then(async (contact: systemShare.ContactInfo) => {
   5. // 处理联系人信息，可通过联系人类型（如：个人，群组等），联系人ID，进行指定用户分享。
   6. // 获取分享数据
   7. let data = await systemShare.getSharedData(want);
   8. })
   9. .catch((error: BusinessError) => {
   10. console.error(`Failed to getContactInfo. Code: ${error.code}, message: ${error.message}`);
   11. // 联系人不存在或数据获取异常
   12. session.terminateSelf();
   13. });
   14. }
   15. }
   ```
4. 构建完分享能力Ability，需要在应用配置文件（src/main/module.json5）的[skills](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#skills标签)配置中注册。配置actions为ohos.want.action.sendData，并且uris需穷举所有支持的数据类型。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "TestShareAbility",
   4. "srcEntry": "./ets/abilities/TestShareAbility.ts",
   5. "type": "share", // 支持分享数据处理
   6. "description": "xxx",
   7. "exported": true,
   8. "label": "$string:xx_label",
   9. "icon": "$media:icon",
   10. "skills": [
   11. {
   12. "actions": [
   13. "ohos.want.action.sendData"
   14. ],
   15. // scheme为预留字段，在此处不生效，配置file仅为示例
   16. // 目标应用在配置支持接收的数据类型时，需穷举支持的UTD，比如：支持全部图片类型，可声明：general.image
   17. // maxFileSupported 对于归属指定类型的文件，标识一次支持接收的最大数量。默认为0，代表不支持此类文件的分享。
   18. // 文件类型归属关系参考：@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)
   19. "uris": [
   20. {
   21. "scheme": "file",
   22. "utd": "general.text",
   23. "maxFileSupported": 1
   24. },
   25. {
   26. "scheme": "file",
   27. "utd": "general.png",
   28. "maxFileSupported": 1
   29. },
   30. {
   31. "scheme": "file",
   32. "utd": "general.jpeg",
   33. "maxFileSupported": 1
   34. }
   35. ]
   36. }
   37. ]
   38. }
   39. ]
   ```
