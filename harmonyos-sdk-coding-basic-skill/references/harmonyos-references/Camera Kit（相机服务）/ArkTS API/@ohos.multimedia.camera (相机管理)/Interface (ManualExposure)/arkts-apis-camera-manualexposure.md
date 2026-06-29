---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposure
title: Interface (ManualExposure)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ManualExposure)
category: harmonyos-references
scraped_at: 2026-06-01T16:20:10+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1f31ae84efa42056ecf82a9a6f3bcdc7d95b1ea47571b9cf44782ff7305bd084
---
ManualExposure继承自[ManualExposureQuery](<../Interface (ManualExposureQuery)/arkts-apis-camera-manualexposurequery.md>)。

手动曝光对象。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 24开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## getExposureDuration24+

PhonePC/2in1TabletTVWearable

getExposureDuration(): number

获取当前曝光时长值。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前曝光时长值。单位：微秒。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../../错误码/Camera错误码/errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, session or inputdevice maybe abnormal. |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureDuration(photoSession: camera.PhotoSession): number {
4. let exposureDuration: number = 0;
5. try {
6. exposureDuration = photoSession.getExposureDuration();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getExposureDuration call failed. error code: ${err.code}`);
11. }
12. return exposureDuration;
13. }
```

## setExposureDuration24+

PhonePC/2in1TabletTVWearable

setExposureDuration(exposureDuration: number): void

设置曝光时长值。

仅在[ExposureMode](../Enums/arkts-apis-camera-e.md#exposuremode).EXPOSURE\_MODE\_MANUAL 手动曝光模式下设置生效。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exposureDuration | number | 是 | 曝光时长值。单位：微秒。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../../错误码/Camera错误码/errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setExposureDuration(photoSession: camera.PhotoSession, exposureDuration: number): void {
4. try {
5. photoSession.setExposureDuration(exposureDuration);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setExposureDuration call failed. error code: ${err.code}`);
10. }
11. }
```
