---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-navigation-scenarios
title: 导航定位场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 导航定位场景低功耗规则
category: best-practices
scraped_at: 2026-06-12T10:16:39+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:33c332c96121df7ea2d3a9e46385582635cbde14c9d6ec1dff96929610058eaf
---

## 规则

* 导航类应用需设置正确的应用类型，并使用系统自带的导航场景音效算法，避免冗余处理。
* 在导航类应用无语音播报等语音输出时，禁止持续向系统写入音频空数据。

## 开发步骤

为了避免导航类应用无法使用系统低功耗方案，确保正确设置usage类型。配置音频渲染参数并创建AudioRenderer实例时，设置usage类型为audio.StreamUsage.STREAM\_USAGE\_NAVIGATION。

```
1. import { audio } from '@kit.AudioKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let audioStreamInfo: audio.AudioStreamInfo = {
5. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
6. channels: audio.AudioChannel.CHANNEL_1,
7. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
8. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
9. };
10. let audioRendererInfo: audio.AudioRendererInfo = {
11. usage: audio.StreamUsage.STREAM_USAGE_NAVIGATION,
12. rendererFlags: 0
13. };
14. let audioRendererOptions: audio.AudioRendererOptions = {
15. streamInfo: audioStreamInfo,
16. rendererInfo: audioRendererInfo
17. };
18. audio.createAudioRenderer(audioRendererOptions, (err, data) => {
19. if (err) {
20. hilog.error(0x0000, 'Sample', `Invoke createAudioRenderer failed, code is ${err.code}, message is ${err.message}`);
21. return;
22. } else {
23. hilog.info(0x0000, 'Sample', 'Invoke createAudioRenderer succeeded.');
24. let audioRenderer = data;
25. }
26. });
```

[NavigationAndPositioningRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/NavigationAndPositioningRule.ets#L21-L46)

## 调测验证

* 通过以下命令查看日志确认：

  ```
  1. hdc shell
  2. hilog | grep usage
  ```
* 执行效果如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/QUrDOb0rTUugPTULJEPlTg/zh-cn_image_0000002229450993.png?HW-CC-KV=V1&HW-CC-Date=20260612T021638Z&HW-CC-Expire=86400&HW-CC-Sign=D817A82EE489377CE04936E18BE0AF851932FE81ECDE29187AB2DF9A97C54B51 "点击放大")

## 结果对比

* 优化前：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/jcZOpt0IR82f81ih-iKNzg/zh-cn_image_0000002193851136.png?HW-CC-KV=V1&HW-CC-Date=20260612T021638Z&HW-CC-Expire=86400&HW-CC-Sign=C41ACFE9995FAAB418EFB3D8EC7792BB5A0F92E1786328810C8911B43ADF9219 "点击放大")

* 优化后，图中字段证明系统低功耗方案使能成功（根据实验室测试功耗，功耗负载降低约43.89%。）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/-DV1I4oaQZiLYN9qvf-Xmw/zh-cn_image_0000002194010716.png?HW-CC-KV=V1&HW-CC-Date=20260612T021638Z&HW-CC-Expire=86400&HW-CC-Sign=85BA89226CE2FE4D227CC6FBDD942073979994A35BB7FC8955E3FB80A19930B7 "点击放大")
