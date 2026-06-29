---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-13
title: 如何开关闪光灯
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何开关闪光灯
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b8ac2ec0ca6df196e595aa80567b6dbe74663a782e173e8fc153cd07d14814ae
---
使用[isFlashModeSupported](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (FlashQuery)/arkts-apis-camera-flashquery.md#isflashmodesupported11>)方法检测设备是否支持需要设置的闪光灯模式后，使用[setFlashMode](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (Flash)/arkts-apis-camera-flash.md#setflashmode11>)设置闪光灯模式。

**参考代码**

```
1. setFlash(captureSession: camera.PhotoSession,flashMode: camera.FlashMode) {
2. if (captureSession != null) {
3. let focusModeStatus: boolean = captureSession?.isFlashModeSupported(flashMode);
4. if (focusModeStatus) {
5. captureSession.setFlashMode(flashMode);
6. }
7. }
8. }
```

[SetFlash.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/SetFlash.ets#L22-L29)
