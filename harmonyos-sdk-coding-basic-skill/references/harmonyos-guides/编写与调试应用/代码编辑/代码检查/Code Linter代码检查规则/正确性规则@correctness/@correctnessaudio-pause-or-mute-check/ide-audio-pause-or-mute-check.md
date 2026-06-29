---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-audio-pause-or-mute-check
title: @correctness/audio-pause-or-mute-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/audio-pause-or-mute-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6887877ac820d3b6eb2fcdc0202b4def485f0fd5fd95ebc924051d3896921705
---
建议应用在播放声音的场景下，监听音频发声设备变化。

改善[音视频播放](<../../../../../../媒体/Audio Kit（音频服务）/音频设备路由管理/响应输出设备变更时合理暂停/audio-output-device-change.md#音频流输出设备变更原因>)体验场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/audio-pause-or-mute-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { media } from '@kit.MediaKit';
2. import { audio } from '@kit.AudioKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. export class AudioPauseNoReport {
5. demoCallBack() {
6. let audioStreamInfo1: audio.AudioStreamInfo = {
7. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
8. channels: audio.AudioChannel.CHANNEL_1,
9. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
10. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
11. };
12. let audioRendererInfo: audio.AudioRendererInfo = {
13. usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
14. rendererFlags: 0
15. };
16. let audioRendererOptions: audio.AudioRendererOptions = {
17. streamInfo: audioStreamInfo1,
18. rendererInfo: audioRendererInfo
19. };
20. media.createAVPlayer((error: BusinessError, player) => {
21. if (player) {
22. player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
23. console.info('Succeeded');
24. });
25. player.on('audioOutputDeviceChangeWithInfo', ()=>{
26. console.error(`createAVPlayer audioOutputDeviceChangeWithInfo`);
27. });
28. console.info('Succeeded in creating AVPlayer.');
29. } else {
30. console.error(`Failed to create AVPlayer, error message:${error.message}`);
31. }
32. });
33. audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
34. if (err) {
35. console.error(`AudioRenderer Created: Error: ${err}`);
36. } else {
37. audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
38. console.info('Succeeded');
39. });
40. audioRenderer.on('outputDeviceChangeWithInfo', ()=>{
41. console.error(`createAudioRenderer outputDeviceChangeWithInfo`);
42. })
43. console.info('AudioRenderer Created: Success: SUCCESS');
44. }
45. });
46. }
47. }
```

## 反例

```
1. import { media } from '@kit.MediaKit';
2. import { audio } from '@kit.AudioKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. let audioStreamInfo1: audio.AudioStreamInfo = {
5. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
6. channels: audio.AudioChannel.CHANNEL_1,
7. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
8. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
9. };
10. let audioRendererInfo: audio.AudioRendererInfo = {
11. usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
12. rendererFlags: 0
13. };
14. let audioRendererOptions: audio.AudioRendererOptions = {
15. streamInfo: audioStreamInfo1,
16. rendererInfo: audioRendererInfo
17. };
18. function demoCallBack() {
19. // warning line
20. media.createAVPlayer((error: BusinessError, player: media.AVPlayer) => {
21. if (player != null) {
22. player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
23. console.info('Succeeded');
24. });
25. console.info('Succeeded in creating AVPlayer.');
26. } else {
27. console.error(`Failed to create AVPlayer, error message:${error.message}`);
28. }
29. });
30. // warning line
31. audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
32. if (err) {
33. console.error(`AudioRenderer Created: Error: ${err}`);
34. } else {
35. audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
36. console.info('Succeeded');
37. });
38. console.info('AudioRenderer Created.');
39. }
40. });
41. }
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
