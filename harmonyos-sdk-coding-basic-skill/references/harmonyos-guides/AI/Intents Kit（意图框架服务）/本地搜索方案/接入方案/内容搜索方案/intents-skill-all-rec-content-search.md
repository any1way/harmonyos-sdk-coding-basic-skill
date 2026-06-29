---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-content-search
title: 内容搜索方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 本地搜索方案 > 接入方案 > 内容搜索方案
category: harmonyos-guides
scraped_at: 2026-06-11T15:19:04+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:76485ea4beaf11369d57d41ad1d3ed6496cc67e42b52473503f01002f2c76300
---
## 方案概述

当用户使用应用/元服务时，开发者可以按照标准意图Schema（具体意图详见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)）向系统共享数据（数据包含用户行为和内容实体），并实现意图调用（空调用与传参调用）。已实现用户点击卡片后，可后台执行功能（例如播放指定歌曲）或跳转至指定内容页面（例如指定的歌曲播放页面）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Dil1wcmiTMiLC5nTFiREKg/zh-cn_image_0000002592219778.png?HW-CC-KV=V1&HW-CC-Date=20260611T071901Z&HW-CC-Expire=86400&HW-CC-Sign=51C1C29573AE1707A174D5E6FFD6C570BF5DA506E01E01AC1400AB06543FEF4D)

## 意图声明

以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。

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
9. "intentName": "PlayMusic",
10. // 意图所属的垂域
11. "domain": "MusicDomain",
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
25. }
26. }
27. ]
28. }
```

## 意图共享

构建意图对象，并且调用[insightIntent.shareIntent](<../../../../../../harmonyos-references/Intents Kit（意图框架服务）/ArkTS API/insightIntent/intents-arkts-api-insightintent.md#shareintent-1>)，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。

以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图，并进行了shareIntent调用。

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
14. intentVersion: '1.0',
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

开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）或后台执行的能力，PlayMusic的意图调用字段定义见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别播放歌曲意图（PlayMusic），在对应的方法中传递意图参数（param），并拉起对应落地页（如播放歌曲落地页）或后台执行（播放歌曲）。

```
1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. /**
6. * 意图调用样例
7. */
8. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
9. private static readonly PLAY_MUSIC = 'PlayMusic';

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
23. case InsightIntentExecutorImpl.PLAY_MUSIC:
24. return this.playMusic(param, pageLoader);
25. default:
26. break;
27. }
28. const data: insightIntent.ExecuteResult = {
29. code: -1,
30. result: {
31. message: 'unknown intent'
32. }
33. };
34. return Promise.resolve(data);
35. }

37. /**
38. * 实现调用播放歌曲功能
39. *
40. * @param param 意图参数
41. * @param pageLoader 窗口
42. */
43. private playMusic(param: Record<string, Object>,
44. pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
45. return new Promise((resolve, reject) => {
46. pageLoader.loadContent('pages/SongPage')
47. .then(() => {
48. const items: Array<PlayMusicEntity> = (param.items instanceof Array) ? param.items : [];
49. const entityId: string = items[0]?.entityId;
50. console.info(`Intent param, entityId: ${entityId}`);
51. const data: insightIntent.ExecuteResult = {
52. code: 0,
53. result: {
54. message: 'Intent execute succeed'
55. }
56. };
57. resolve(data);
58. })
59. .catch((err: BusinessError) => {
60. console.error(`Intent execute failed, Code: ${err?.code}, message: ${err?.message}`);
61. const data: insightIntent.ExecuteResult = {
62. code: -1,
63. result: {
64. message: 'Intent execute failed'
65. }
66. };
67. reject(data);
68. });
69. });
70. }
71. }

73. interface PlayMusicEntity {
74. entityId: string;
75. }
```
