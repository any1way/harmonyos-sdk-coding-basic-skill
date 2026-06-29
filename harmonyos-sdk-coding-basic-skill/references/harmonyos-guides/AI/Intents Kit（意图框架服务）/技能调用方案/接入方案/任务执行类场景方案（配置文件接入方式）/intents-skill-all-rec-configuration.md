---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-configuration
title: 任务执行类场景方案（配置文件接入方式）
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 任务执行类场景方案（配置文件接入方式）
category: harmonyos-guides
scraped_at: 2026-06-11T15:18:50+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:00caee768fa4e8d9cd2bccd7ca2270ee7c78f7521abab185038b354848fbb79b
---

## 方案概述

开发者需要按照意图定义，进行意图注册并实现意图调用；用户通过对小艺对话进行自然语言输入，小艺理解语义转换成意图调用（含意图参数），执行意图调用实现对应交互体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/pXLmJY0lR1qweOfo_t3M0g/zh-cn_image_0000002622859199.png?HW-CC-KV=V1&HW-CC-Date=20260611T071849Z&HW-CC-Expire=86400&HW-CC-Sign=1A613C8DB1EF5AE259E2A7B297C84BF0E848312FB8451762B505E97E21E61974)

## 意图声明

以“搜索旅游攻略”特性为例，开发者首先要注册“查看旅游攻略”（viewTravelGuides），其他意图见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```
1. {
2. // 应用支持的意图列表
3. // 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
4. "insightIntents": [
5. {
6. // 意图名称
7. // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
8. // 应用内意图名称唯一，不允许出现相同的名称定义
9. "intentName": "ViewTravelGuides",
10. // 意图所属的垂域
11. "domain": "TravelDomain",
12. // 意图版本号
13. // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
14. "intentVersion": "1.0.1",
15. // 意图调用逻辑入口
16. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
17. "uiAbility": {
18. // 意图所在ability
19. "ability": "EntryAbility",
20. // UIAbility支持前后台两种执行模式
21. "executeMode": [
22. "background",
23. "foreground"
24. ]
25. },
26. "uiExtension": {// 提供意图执行的窗口化界面时需要进行的声明配置
27. "ability": "insightIntentUIExtensionAbility" // 意图调用API所在ability名称
28. }
29. }
30. ]
31. }
```

## 端侧前台意图调用

开发者需自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面，如旅游攻略详情页）的能力，ViewTravelGuides的意图调用字段定义见查看旅游攻略（ViewTravelGuides）。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别查看旅游攻略意图（ViewTravelGuides），在对应的方法中传递意图参数（param），并拉起对应落地页（点击推荐卡片跳转的界面，如旅游攻略页面）。

```
1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. /**
6. * 意图调用样例
7. */
8. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
9. private static readonly VIEW_TRAVEL_GUIDES = 'ViewTravelGuides';

11. /**
12. * override 执行前台UIAbility意图
13. *
14. * @param name 意图名称
15. * @param param 意图参数
16. * @param pageLoader 窗口
17. * @returns 意图调用结果
18. */
19. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
20. Promise<insightIntent.ExecuteResult> {
21. // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
22. switch (name) {
23. case InsightIntentExecutorImpl.VIEW_TRAVEL_GUIDES:
24. return this.viewTravelGuides(param, pageLoader);
25. default:
26. break;
27. }
28. const data: insightIntent.ExecuteResult = {
29. code: -1,
30. result: {
31. message: 'unknown intent'
32. }
33. }
34. return Promise.resolve(data);
35. }

37. /**
38. * 实现调用查看旅游攻略功能
39. *
40. * @param param 意图参数
41. * @param pageLoader 窗口
42. */
43. private viewTravelGuides(param: Record<string, Object>,
44. pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
45. return new Promise((resolve, reject) => {
46. pageLoader.loadContent('pages/TravelGuidePage')
47. .then(() => {
48. const entityId: string = (typeof param.entityId === 'string') ? param.entityId : '';
49. console.info(`Intent param, entityId: ${entityId}`);
50. const data: insightIntent.ExecuteResult = {
51. code: 0,
52. result: {
53. message: 'Intent execute succeed'
54. }
55. }
56. resolve(data);
57. })
58. .catch((err: BusinessError) => {
59. console.error(`Intent execute failed, Code: ${err?.code}, message: ${err?.message}`);
60. const data: insightIntent.ExecuteResult = {
61. code: -1,
62. result: {
63. message: 'Intent execute failed'
64. }
65. }
66. reject(data);
67. });
68. })
69. }
70. }
```

## 端侧前台窗口意图调用

开发者需自己实现InsightIntentExecutor，并在对应回调实现窗口页面内容加载的能力。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台窗口化页面，则可重写onExecuteInUIExtensionAbility方法。
3. 通过意图名称，识别打开蓝牙意图（LoadBluetoothCard）调用扩展意图，在对应的方法中传递意图参数（param），并拉起对应窗口化页面（如打开蓝牙窗口化页面）。

```
1. import { insightIntent, InsightIntentExecutor, UIExtensionContentSession } from '@kit.AbilityKit';

3. /**
4. * 意图调用样例
5. */
6. export default class IntentExecutorImpl extends InsightIntentExecutor {
7. private static readonly TAG: string = 'IntentExecutorImpl';
8. private static readonly LOAD_BLUETOOTH_CARD: string = 'LoadBluetoothCard';
9. /**
10. * override 执行前台UI扩展意图
11. *
12. * @param name 意图名称
13. * @param param 意图参数
14. * @param pageLoader 窗口
15. * @returns 意图调用结果
16. */
17. async onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
18. pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
19. console.info(IntentExecutorImpl.TAG, `onExecuteInUIExtensionAbility`);
20. switch (name) {
21. case IntentExecutorImpl.LOAD_BLUETOOTH_CARD:
22. console.info(IntentExecutorImpl.TAG, `onExecuteInUIAbilityForegroundMode::ForegroundUiAbility intent`);
23. return this.openLoadBluetoothCard(pageLoader);
24. default:
25. console.error(IntentExecutorImpl.TAG, `onExecuteInUIAbilityForegroundMode::invalid intent`);
26. break;
27. }
28. let result: insightIntent.ExecuteResult = {
29. code: -1,
30. result: {
31. message: 'onExecuteInUIExtensionAbility failed'
32. }
33. };
34. return result;
35. }
36. /**
37. * 打开加载蓝牙卡片意图
38. *
39. * @param pageLoader 意图内容Session对象
40. * @returns 执行结果
41. */
42. private async openLoadBluetoothCard(pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
43. return new Promise((resolve, reject) => {
44. try {
45. pageLoader.loadContent('pages/UiExtensionPage');
46. const data: insightIntent.ExecuteResult = {
47. code: 0,
48. result: {
49. message: 'Intent execute succeed'
50. }
51. };
52. resolve(data);
53. } catch (err) {
54. console.error(`Intent execute failed, Code: ${err?.code}, message: ${err?.message}`);
55. const data: insightIntent.ExecuteResult = {
56. code: -1,
57. result: {
58. message: 'Intent execute failed'
59. }
60. };
61. reject(data);
62. }
63. });
64. }
65. }
```
