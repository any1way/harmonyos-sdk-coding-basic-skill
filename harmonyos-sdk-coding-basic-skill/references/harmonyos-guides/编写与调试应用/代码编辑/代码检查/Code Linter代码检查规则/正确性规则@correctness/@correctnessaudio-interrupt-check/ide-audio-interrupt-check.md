---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-audio-interrupt-check
title: @correctness/audio-interrupt-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/audio-interrupt-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:36+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ab6c8db4a12b3d97d26a14dc205232227298c65940c0b63a119e0ac3ac831ea6
---
建议应用在播放或录制音频的场景中，监听音频焦点中断回调事件，并响应。

改善[音视频播放](<../../../../../../媒体/Audio Kit（音频服务）/音频焦点和音频会话管理/音频焦点介绍/audio-playback-concurrency.md#处理音频焦点变化>)体验场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/audio-interrupt-check": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { audio } from '@kit.AudioKit';
2. import { media } from '@kit.MediaKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. // An identifier specifying whether the audio stream is being played. In actual development, this parameter corresponds to the module related to the audio playback state.
5. let isPlay: boolean;
6. // An identifier specifying whether to duck the volume down. In actual development, this parameter corresponds to the module related to the audio volume.
7. let isDucked: boolean;
8. // An identifier specifying whether the start operation is successful.
9. let started: boolean;
10. media.createAVPlayer((error: BusinessError, player) => {
11. if (player) {
12. console.info('Succeeded in creating AVPlayer');
13. player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
14. // When audio focus changes, the AudioRenderer receives the interruptEvent callback and performs processing based on the content in the callback.
15. // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
16. // Note: In the default focus strategy, INTERRUPT_HINT_RESUME maps to the force type INTERRUPT_SHARE, and others map to INTERRUPT_FORCE. Therefore, the value of forceType does not need to be checked.
17. // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
18. if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
19. // If the value of interruptEvent.forceType is INTERRUPT_FORCE, the system has performed audio-related processing, and the application needs to update its state and make adjustments accordingly.
20. switch (interruptEvent.hintType) {
21. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
22. // The system has paused the audio stream (focus is temporarily lost). To ensure state consistency, the application needs to switch to the audio paused state.
23. // Temporarily losing focus: After other audio streams release focus, the current audio stream will receive the audio focus event corresponding to resume and automatically resume the playback.
24. // A simplified processing indicating several operations for switching the application to the audio paused state.
25. isPlay = false;
26. break;
27. case audio.InterruptHint.INTERRUPT_HINT_STOP:
28. // The system has stopped the audio stream (focus is permanently lost). To ensure state consistency, the application needs to switch to the audio paused state.
29. // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
30. // A simplified processing indicating several operations for switching the application to the audio paused state.
31. isPlay = false;
32. break;
33. case audio.InterruptHint.INTERRUPT_HINT_DUCK:
34. // The system has ducked the volume down (to 20% of the normal volume by default).
35. // A simplified processing indicating several operations for switching the application to the volume decreased state.
36. isDucked = true;
37. break;
38. case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
39. // The system has restored the audio volume to normal.
40. // A simplified processing indicating several operations for switching the application to the normal volume state.
41. isDucked = false;
42. break;
43. default:
44. break;
45. }
46. } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
47. // If the value of interruptEvent.forceType is INTERRUPT_SHARE, the application can take action or ignore as required.
48. switch (interruptEvent.hintType) {
49. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
50. // The paused audio stream can be played. It is recommended that the application continue to play the audio stream and switch to the audio playing state.
51. // If the application does not want to continue the playback, it can ignore the event.
52. // To continue the playback, the application needs to call start(), and use the identifier variable started to record the execution result of start().
53. isPlay = true;
54. started = true;
55. break;
56. default:
57. break;
58. }
59. }
60. });
61. player.on('audioOutputDeviceChangeWithInfo', ()=>{
62. console.error(`createAVPlayer audioOutputDeviceChangeWithInfo`);
63. });
64. } else {
65. console.error(`Failed to create AVPlayer, error message:${error.message}`);
66. }
67. });
```

## 反例

```
1. import { media } from '@kit.MediaKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. export class AudioInterruptReport {
4. demoCallBack() {
5. media.createAVPlayer((error: BusinessError, player) => {
6. if (player) {
7. player.on('audioOutputDeviceChangeWithInfo', ()=>{
8. console.error(`createAudioRenderer outputDeviceChangeWithInfo`);
9. })
10. console.info('Succeeded in creating AVPlayer');
11. } else {
12. console.error(`Failed to create AVPlayer, error message:${error.message}`);
13. }
14. });
15. }
16. }
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
