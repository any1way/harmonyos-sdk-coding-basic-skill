---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-8
title: 录屏帧率是否有限制，如何设置最大帧率
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 录屏帧率是否有限制，如何设置最大帧率
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:39ee43111e188547bbe077f714711e23089e0076fe13359343a2f1d2af172711
---
可以调用OH\_AVScreenCapture\_SetMaxVideoFrameRate()设置录屏时的最大帧率，实际帧率受限于设备能力，具体规格可参考[设置录屏时的最大帧率](<../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_setmaxvideoframerate>)。录屏的帧率需同时满足编解码的规格，请参考[设置正确的视频帧率](<../../../../../harmonyos-guides/媒体/AVCodec Kit（音视频编解码服务）/音视频编解码/获取支持的编解码能力/obtain-supported-codecs.md#设置正确的视频帧率>)。
