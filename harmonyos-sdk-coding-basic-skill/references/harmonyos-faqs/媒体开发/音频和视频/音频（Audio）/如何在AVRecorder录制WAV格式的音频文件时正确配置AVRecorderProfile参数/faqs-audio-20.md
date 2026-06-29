---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-20
title: 如何在AVRecorder录制WAV格式的音频文件时正确配置AVRecorderProfile参数
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何在AVRecorder录制WAV格式的音频文件时正确配置AVRecorderProfile参数
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:db5b545abfbee7b1cdecde85991afb77925c67c8698b2ee528d03c2b0d7e7712
---
**问题现象**

使用AVRecorder录制WAV格式音频时，发生异常错误。

**问题原因**

AVRecorderProfile参数配置错误，WAV格式需要匹配相应的比特率、声道数、编码格式、采样率和封装格式。

**解决措施**

给[AVRecorderProfile](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interfaces (其他)/arkts-apis-media-i.md#avrecorderprofile9>)配置相应的比特率、声道数、编码格式、采样率和封装格式。

```
1. private avProfile: media.AVRecorderProfile = {
2. audioBitrate: 64000, // set audioBitrate according to device ability.
3. audioChannels: 1, // set audioChannels,valid value 1-8,CFT_WAV supports 1.
4. audioCodec: media.CodecMimeType.AUDIO_G711MU, // set audioCodec,AUDIO_G711MU matching CFT_WAV.
5. audioSampleRate: 8000, // set audioSampleRate according to device ability.
6. fileFormat: media.ContainerFormatType.CFT_WAV // set fileFormat,CFT_WAV.
7. }
```

[AVRecorderProfile.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/AVRecorderProfile.ets#L26-L33)
