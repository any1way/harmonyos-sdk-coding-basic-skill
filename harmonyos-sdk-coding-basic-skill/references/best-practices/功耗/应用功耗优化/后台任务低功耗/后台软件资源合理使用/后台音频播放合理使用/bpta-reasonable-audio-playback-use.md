---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-audio-playback-use
title: 后台音频播放合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台音频播放合理使用
category: best-practices
scraped_at: 2026-06-01T17:01:43+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:c4c004d691d34e4971d95f3d0d78b9e07a482b153d8e1de9378cdf555874ca5b
---
申请音频播放长时任务的应用退到后台后，禁止不写入数据或写入静音数据等恶意行为。

## 约束

系统检测到应用后台行为时，将挂起或清理应用。

## 示例

```
1. import { fileIo } from '@kit.CoreFileKit';
2. // ...

4. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
5. let context = uiContext!.getHostContext()!;

7. async function read() {
8. const bufferSize: number = await audioRenderer.getBufferSize();
9. let path = context.filesDir; // Path of the file

11. const filePath = path + '/voice_call_data.wav'; // Prohibit the file from being played silently
12. try {
13. let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY); // Open the file
14. let buf = new ArrayBuffer(bufferSize);
15. let readSize: number = await fileIo.read(file.fd, buf); // Read the file content
16. } catch (error) {
17. let err = error as BusinessError;
18. hilog.warn(0x000, 'testTag', `openSync or read failed, code=${err.code}, message=${err.message}`);
19. }
20. }
```

[Audio.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/Audio.ets#L21-L71)

有关AudioRenderer开发相关接口的使用，详情可以参考[使用AudioRenderer开发音频播放功能](<../../../../../../harmonyos-guides/媒体/Audio Kit（音频服务）/音频播放/使用AudioRenderer开发音频播放功能(ArkTs)/using-audiorenderer-for-playback.md>)。
