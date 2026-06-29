---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturephoto
title: Interface (CapturePhoto)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (CapturePhoto)
category: harmonyos-references
scraped_at: 2026-06-01T16:20:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e790fc790b593b08d9e11010656a9d933ceea0260c98b579d3ff60b8f0824a8a
---
获取全质量图和未压缩图的对象。

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | [ImageType](../Types/arkts-apis-camera-t.md#imagetype) | 否 | 否 | 全质量图和未压缩图的对象。 |

## release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放输出资源。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { camera } from '@kit.CameraKit';

3. async function releaseCapturePhoto(capturePhoto: camera.CapturePhoto): Promise<void> {
4. await capturePhoto.release();
5. }
```
