---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent-uiextension
title: InsightIntentUIExtensionAbility (意图调用UI扩展能力)
breadcrumb: API参考 > AI > Intents Kit（意图框架服务） > ArkTS API > InsightIntentUIExtensionAbility (意图调用UI扩展能力)
category: harmonyos-references
scraped_at: 2026-06-01T16:40:29+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:89b22666dbe195e32492336dcab69427f57dcb2af6050040cd9875b4abaae7b1
---
InsightIntentUIExtensionAbility用于小艺对话过程中的意图调用时的信息展示，为意图调用UI扩展能力，应用可以声明一个或多个InsightIntentUI来展示其意图的窗口化界面，继承自[UIExtensionAbility](<../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)/js-apis-app-abili_64670486.md>)。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
```

## InsightIntentUIExtensionAbility

PhonePC/2in1Tablet

**模型约束：** 该类仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
2. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

4. const TAG: string = 'TestUiExtAbility';

6. // 此处以TestUiExtAbility继承InsightIntentUIExtensionAbility为例
7. export default class TestUiExtAbility extends InsightIntentUIExtensionAbility {
8. onCreate() {
9. console.info(TAG, `onCreate`);
10. }
11. onForeground() {
12. console.info(TAG, `onForeground`);
13. }
14. onBackground() {
15. console.info(TAG, `onBackground`);
16. }
17. onDestroy() {
18. console.info(TAG, `onDestroy`);
19. }
20. onSessionCreate(want: Want, session: UIExtensionContentSession) {
21. console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
22. session.loadContent('pages/Index');
23. }
24. onSessionDestroy(session: UIExtensionContentSession) {
25. console.info(TAG, `onSessionDestroy`);
26. }
27. }
```
