---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-avsession-metadata-check
title: @correctness/avsession-metadata-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/avsession-metadata-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5ebe22cdcc26df435d250776ce8f59729f85bbbd382b5dc6b5ff75333788b421
---
建议音视频应用接入AVSession场景下，提供基础的媒体会话元数据和媒体会话播放状态，包含封面、标题、歌曲作者/副标题、时长、播放状态（暂停、播放）、播放位置。

改善[音视频播放](<../../../../../../媒体/AVSession Kit（音视频播控服务）/本地媒体会话/应用接入AVSession场景介绍/avsession-access-scene.md#设置元数据>)体验场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/avsession-metadata-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { avSession } from '@kit.AVSessionKit';
3. let tag = "createNewSession";
4. let context: Context = getContext(this);
5. let metadata: avSession.AVMetadata = {
6. assetId: "121278",
7. // Title
8. title: "lose yourself",
9. artist: "Eminem",
10. // Lyrics generator
11. author: "ST",
12. album: "Slim shady",
13. writer: "",
14. composer: "ST",
15. // Subtitle
16. subtitle: "8 Mile",
17. // Duration
18. duration: 2222,
19. // Cover art
20. mediaImage: "https://www.example.com/example.jpg",
21. description: "Rap",
22. // The LRC format contains two types of elements: time tag + lyrics, and ID tag.
23. // Example: [00:25.44]xxx\r\n[00:26.44]xxx\r\n
24. lyric: "Lyrics in LRC format",
25. previousAssetId: "121277",
26. nextAssetId: "121279"
27. };
28. let playbackState: avSession.AVPlaybackState = {
29. // Playing state.
30. state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
31. speed: 1.0,
32. // Playback position.
33. position:{elapsedTime:10, updateTime:(new Date()).getTime()},
34. bufferedTime:1000,
35. loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
36. isFavorite:true
37. };
38. avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
39. if (err) {
40. console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
41. } else {
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
69. }
70. });
```

## 反例

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { avSession } from '@kit.AVSessionKit';
3. let tag = "createNewSession";
4. let context: Context = getContext(this);
5. let metadata: avSession.AVMetadata = {
6. assetId: "121278",
7. // Title
8. title: "lose yourself",
9. artist: "Eminem",
10. // Lyrics generator
11. author: "ST",
12. album: "Slim shady",
13. writer: "",
14. composer: "ST",
15. // Subtitle
16. subtitle: "8 Mile",
17. description: "Rap",
18. // The LRC format contains two types of elements: time tag + lyrics, and ID tag.
19. // Example: [00:25.44]xxx\r\n[00:26.44]xxx\r\n
20. lyric: "Lyrics in LRC format",
21. previousAssetId: "121277",
22. nextAssetId: "121279"
23. };
24. let playbackState: avSession.AVPlaybackState = {
25. // Playing state.
26. state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
27. speed: 1.0,
28. // Playback position.
29. position:{elapsedTime:10, updateTime:(new Date()).getTime()},
30. bufferedTime:1000,
31. loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
32. isFavorite:true
33. };
34. // warning
35. avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
36. if (err) {
37. console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
38. } else {
39. data.setAVMetadata(metadata, (err: BusinessError) => {
40. if (err) {
41. console.error(`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
42. } else {
43. console.info('SetAVMetadata successfully');
44. }
45. });
46. data.setAVPlaybackState(playbackState).then(() => {
47. console.info('SetAVPlaybackState successfully');
48. }).catch((err: BusinessError) => {
49. console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
50. });
51. // Process the play command.
52. data.on('play', () => {
53. });
54. // Process the pause command.
55. data.on('pause', () => {
56. });
57. // Process the stop command.
58. data.on('stop', () => {
59. });
60. // Process the play-next command.
61. data.on('playNext', () => {
62. });
63. // Process the play-previous command.
64. data.on('playPrevious', () => {
65. });
66. }
67. });
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
