---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-habit-rec-access-programme
title: 接入方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 习惯推荐方案 > 接入方案
category: harmonyos-guides
scraped_at: 2026-06-11T15:18:11+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:ede708f014973a7b031d320857944dc9fa0a90abddbca43cb0bb946116a10b80
---
## 方案概述

当用户在应用/元服务内使用功能时，开发者需要按照标准意图Schema向系统共享行为数据，并支持意图调用（空调用与传参调用），以实现用户点击模板卡后跳转回对应页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/JhdREtZHRMWQryXULWwU4A/zh-cn_image_0000002622699311.png?HW-CC-KV=V1&HW-CC-Date=20260611T071808Z&HW-CC-Expire=86400&HW-CC-Sign=D67FF355633E520DB23CAEFF490650939C3D4AA57C006C6EC9C7F3AE22875B86)

## 意图注册

以歌曲续听推荐特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图声明。insight\_intent.json文件需要放置在任意一个module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```
1. {
2. // 应用支持的意图列表
3. // 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
4. "insightIntents": [
5. {
6. // 意图名称
7. // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
8. // 应用内意图名称唯一，不允许出现相同的名称定义
9. "intentName": "PlayMusic",
10. // 意图所属的垂域
11. "domain": "MusicDomain",
12. // 意图版本号
13. // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
14. "intentVersion": "1.0.1",
15. // 意图调用逻辑入口
16. // 根据意图调用文件实际路径和实际名称进行填写，此处文件仅做示意
17. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
18. "uiAbility": {
19. // 意图所在ability
20. "ability": "EntryAbility",
21. // UIAbility支持前后台两种执行模式
22. "executeMode": [
23. "background",
24. "foreground"
25. ]
26. }
27. }
28. ]
29. }
```

## 端侧意图共享

构建意图对象，并且调用[shareIntent()](<../../../../../harmonyos-references/Intents Kit（意图框架服务）/ArkTS API/insightIntent/intents-arkts-api-insightintent.md#shareintent-1>)，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。PlayMusic的意图共享字段定义见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)定义，完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图，并进行了shareIntent调用。

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Column() {
9. Row() {
10. Button('shareIntent')
11. .onClick(() => {
12. let playMusicIntent: insightIntent.InsightIntent = {
13. intentName: 'PlayMusic',
14. intentVersion: '1.0.1',
15. identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
16. intentActionInfo: {
17. actionMode: 'EXECUTED',
18. executedTimeSlots: {
19. executedStartTime: 1637393112000,
20. executedEndTime: 1637393212000
21. },
22. currentPercentage: 50
23. },
24. intentEntityInfo: {
25. entityName: 'Music',
26. entityId: 'C10194368',
27. entityGroupId: 'C10194321312',
28. displayName: '测试歌曲1',
29. description: 'NA',
30. logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png',
31. keywords: ['华为音乐', '化妆'],
32. rankingHint: 99,
33. expirationTime: 1637393212000,
34. metadataModificationTime: 1637393212000,
35. activityType: ['1', '2', '3'],
36. artist: ['测试歌手1', '测试歌手2'],
37. lyricist: ['测试词作者1', '测试词作者2'],
38. composer: ['测试曲作者1', '测试曲作者2'],
39. albumName: '测试专辑',
40. duration: 244000,
41. playCount: 100000,
42. musicalGenre: ['流行', '华语', '金曲', '00后'],
43. isPublicData: false
44. }
45. };
46. // 共享数据接口  意图数组可以是更多的实体
47. // 根据实际代码上下文自行传入合适的context
48. insightIntent.shareIntent(this.getUIContext().getHostContext(), [playMusicIntent]).then(() => {
49. console.info('shareIntent succeed');
50. }).catch((err: BusinessError) => {
51. console.error(`shareIntent failed, Code: ${err?.code}, message: ${err?.message}`);
52. });
53. })
54. }
55. .justifyContent(FlexAlign.Center)
56. .alignItems(VerticalAlign.Center)
57. .width('100%')
58. }
59. .height('100%')
60. .width('100%')
61. }
62. }
```

## 端侧意图调用

### 意图执行组件为uiAbility的意图调用

如上文意图注册，当开发者注册的意图承载的运行组件为uiAbility时，开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）的能力，PlayMusic的意图调用字段定义见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别播放歌曲意图（PlayMusic），在对应的方法中传递意图参数（param），并拉起对应落地页（如歌曲落地页）。

   ```
   1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. /**
   6. * 意图调用样例
   7. */
   8. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
   9. private static readonly PLAY_MUSIC = 'PlayMusic';
   10. /**
   11. * override 执行前台UIAbility意图
   12. *
   13. * @param name 意图名称
   14. * @param param 意图参数
   15. * @param pageLoader 窗口
   16. * @returns 意图调用结果
   17. */
   18. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
   19. Promise<insightIntent.ExecuteResult> {
   20. // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
   21. switch (name) {
   22. case InsightIntentExecutorImpl.PLAY_MUSIC:
   23. return this.playMusic(param, pageLoader);
   24. default:
   25. break;
   26. }
   27. const data: insightIntent.ExecuteResult = {
   28. code: -1,
   29. result: {
   30. message: 'unknown intent'
   31. }
   32. };
   33. return Promise.resolve(data);
   34. }

   36. /**
   37. * 实现调用播放歌曲功能
   38. *
   39. * @param param 意图参数
   40. * @param pageLoader 窗口
   41. */
   42. private playMusic(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
   43. return new Promise((resolve, reject) => {
   44. let localStorage: LocalStorage = new LocalStorage(param);
   45. pageLoader.loadContent('pages/Index', localStorage)
   46. .then(() => {
   47. const items: Array<PlayMusicEntity> = (param.items instanceof Array) ? param.items : [];
   48. const entityId: string = items[0]?.entityId;
   49. console.info(`Intent param, entityId: ${entityId}`);
   50. const data: insightIntent.ExecuteResult = {
   51. code: 0,
   52. result: {
   53. message: 'Intent execute succeed'
   54. }
   55. };
   56. resolve(data);
   57. })
   58. .catch((err: BusinessError) => {
   59. console.error(`Intent execute failed, Code: ${err?.code}, message: ${err?.message}`);
   60. const data: insightIntent.ExecuteResult = {
   61. code: -1,
   62. result: {
   63. message: 'Intent execute failed'
   64. }
   65. };
   66. reject(data);
   67. });
   68. })
   69. }
   70. }

   72. interface PlayMusicEntity {
   73. entityId: string;
   74. }
   ```

### 意图执行组件为form的意图调用

如上文意图注册，当开发者注册的意图承载的运行组件为form（运行组件FormExtensionAbility）时，则需要开发者在实现的FormExtensionAbility中从want中获取并解析意图名和执行参数，用于卡片展示。

步骤如下：

1. 在意图执行绑定FormExtensionAbility的onAddForm(want: Want)中获取运行态意图框架传入的意图名（预定义keyName为ohos.insightIntent.executeParam.name）和意图执行参数（预定义keyName为ohos.insightIntent.executeParam.param）；
2. 通过意图名称，识别播放歌曲意图(PlayMusic)，在对应的方法中传递意图参数（param），并加载对应数据用于卡片展示。

```
1. import { Want } from '@kit.AbilityKit';
2. import { formBindingData, FormExtensionAbility } from '@kit.FormKit';

4. /**
5. * 卡片意图调用示例
6. */
7. export default class LoadCardFormAbility extends FormExtensionAbility {
8. private static readonly NAME = 'ohos.insightIntent.executeParam.name';
9. private static readonly PARAM = 'ohos.insightIntent.executeParam.param';

11. onAddForm(want: Want): formBindingData.FormBindingData {
12. if (want?.parameters?.[LoadCardFormAbility.NAME] != undefined) {
13. const intentName = want.parameters[LoadCardFormAbility.NAME]; // 意图名
14. // 根据意图名称分发处理逻辑，若仅一个卡片意图，则可以忽略
15. console.info(`intentName is ${intentName}`);
16. }

18. if (want?.parameters?.[LoadCardFormAbility.PARAM] != undefined) {
19. const executeParameter = want.parameters[LoadCardFormAbility.PARAM]; // 意图执行参数
20. // 从 executeParameter 中解析具体意图执行参数，用于卡片内容展示
21. console.info(`executeParameter is ${JSON.stringify(executeParameter)}`);
22. }

24. let formData = ''; // 仅示例，根据具体逻辑封装
25. return formBindingData.createFormBindingData(formData);
26. }
27. }
```
