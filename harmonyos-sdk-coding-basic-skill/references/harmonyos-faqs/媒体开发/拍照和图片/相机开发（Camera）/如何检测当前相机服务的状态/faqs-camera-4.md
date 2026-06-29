---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-4
title: 如何检测当前相机服务的状态
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何检测当前相机服务的状态
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bc3980cb92f7f71466fbf484f86d69dc17df5b2dbcc7afff639b9bf0076ea9e6
---
设置状态回调以返回相机状态。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. const context = AppStorage.get("context") as UIContext;
4. let cameraManager = camera.getCameraManager(context.getHostContext()!);
5. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
6. console.log(`camera : ${cameraStatusInfo.camera.cameraId}`);
7. console.log(`status: ${cameraStatusInfo.status}`);
8. });
```

[GetCameraStatus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetCameraStatus.ets#L21-L28)

相机状态：CameraStatus

CameraStatus是一个枚举，表示相机状态。

**参考链接**

[CameraStatus](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Enums/arkts-apis-camera-e.md#camerastatus>)
