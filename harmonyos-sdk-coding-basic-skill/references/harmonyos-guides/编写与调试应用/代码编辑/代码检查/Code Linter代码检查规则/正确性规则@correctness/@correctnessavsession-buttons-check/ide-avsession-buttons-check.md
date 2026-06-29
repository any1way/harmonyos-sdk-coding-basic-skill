---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-avsession-buttons-check
title: @correctness/avsession-buttons-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/avsession-buttons-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c28a58ec8573dbf949833a16a8e04fce08c56c68372eec1dc5e2b2bf730a5dc4
---
建议音乐、视频、听书类应用通过AVSession监听播放、暂停、停止、下一首、上一首按键事件，并响应。

改善[音视频播放](<../../../../../../媒体/AVSession Kit（音视频播控服务）/本地媒体会话/应用接入AVSession场景介绍/avsession-access-scene.md#注册控制命令>)体验场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/avsession-buttons-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { avSession } from '@kit.AVSessionKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'hello world';

10. build() {
11. Column() {
12. Text(this.message)
13. .onClick(async () => {
14. let context = this.getUIContext().getHostContext() as Context;
15. let tag = "createNewSession";
16. let metadata: avSession.AVMetadata = {
17. assetId: "121278",
18. title: "lose yourself",
19. artist: "Eminem",
20. author: "ST",
21. album: "Slim shady",
22. writer: "",
23. composer: "ST",
24. duration: 2222,
25. mediaImage: "https://www.example.com/example.jpg",
26. subtitle: "8 Mile",
27. description: "Rap",
28. lyric: "lrc",
29. previousAssetId: "121277",
30. nextAssetId: "121279"
31. };
32. let playbackState: avSession.AVPlaybackState = {
33. state: avSession.PlaybackState.PLAYBACK_STATE_PLAY,
34. speed: 1.0,
35. position: { elapsedTime: 10, updateTime: (new Date()).getTime() },
36. bufferedTime: 1000,
37. loopMode: avSession.LoopMode.LOOP_MODE_SINGLE,
38. isFavorite: true
39. };

41. avSession.createAVSession(context, tag, "audio").then((data: avSession.AVSession) => {
42. data.setAVMetadata(metadata, (err: BusinessError) => {
43. if (err) {
44. console.error(`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
45. } else {
46. console.info('SetAVMetadata successfully');
47. }
48. });
49. data.setAVPlaybackState(playbackState).then(() => {
50. console.info('SetAVPlaybackState successfully');
51. }).catch((err: BusinessError) => {
52. console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
53. });
54. // Process the play command.
55. data.on('play', () => {
56. });
57. // Process the pause command.
58. data.on('pause', () => {
59. });
60. // Process the stop command.
61. data.on('stop', () => {
62. });
63. // Process the play-next command.
64. data.on('playNext', () => {
65. });
66. // Process the play-previous command.
67. data.on('playPrevious', () => {
68. });
69. console.info(`CreateAVSession : SUCCESS : sessionId = ${data.sessionId}`);
70. }).catch((err: BusinessError) => {
71. console.info(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
72. })
73. });
74. }
75. .width('100%')
76. .height('100%')
77. }
78. }
```

## 反例

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { avSession } from '@kit.AVSessionKit';
3. let tag = "createNewSession";
4. let context: Context = getContext(this);
5. let metadata: avSession.AVMetadata = {
6. assetId: "121278",
7. title: "lose yourself",
8. artist: "Eminem",
9. author: "ST",
10. album: "Slim shady",
11. writer: "",
12. composer: "ST",
13. duration: 2222,
14. mediaImage: "https://www.example.com/example.jpg",
15. subtitle: "8 Mile",
16. description: "Rap",
17. lyric: "lrc",
18. previousAssetId: "121277",
19. nextAssetId: "121279"
20. };
21. let playbackState: avSession.AVPlaybackState = {
22. state: avSession.PlaybackState.PLAYBACK_STATE_PLAY,
23. speed: 1.0,
24. position: { elapsedTime: 10, updateTime: (new Date()).getTime() },
25. bufferedTime: 1000,
26. loopMode: avSession.LoopMode.LOOP_MODE_SINGLE,
27. isFavorite: true
28. };
29. // Warning
30. avSession.createAVSession(context, tag, "audio").then((data: avSession.AVSession) => {
31. data.setAVMetadata(metadata, (err: BusinessError) => {
32. if (err) {
33. console.error(`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
34. } else {
35. console.info('SetAVMetadata successfully');
36. }
37. });
38. data.setAVPlaybackState(playbackState).then(() => {
39. console.info('SetAVPlaybackState successfully');
40. }).catch((err: BusinessError) => {
41. console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
42. });
43. // Process the play command.
44. data.on('play', () => {
45. });
46. // Process the pause command.
47. data.on('pause', () => {
48. });
49. // Process the stop command.
50. data.on('stop', () => {
51. });
52. // Process the seek command.
53. data.on('seek', () => {
54. });
55. // Process the favorite/like command for the audio session.
56. data.on('toggleFavorite', () => {
57. });
58. console.info(`CreateAVSession : SUCCESS : sessionId = ${data.sessionId}`);
59. }).catch((err: BusinessError) => {
60. console.info(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
61. })
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
