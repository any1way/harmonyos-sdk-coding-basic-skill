---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photosession
title: Interface (PhotoSession)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (PhotoSession)
category: harmonyos-references
scraped_at: 2026-06-01T16:20:20+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:acb0e75444c708d6df85f61b9cef9fef422351ba219e9c46e844f78f986b7ef0
---
PhotoSession继承自[Session](<../Interface (Session)/arkts-apis-camera-session.md>)、[Flash](<../Interface (Flash)/arkts-apis-camera-flash.md>)、[AutoExposure](<../Interface (AutoExposure)/arkts-apis-camera-autoexposure.md>)、[WhiteBalance](<../Interface (WhiteBalance)/arkts-apis-camera-whitebalance.md>)、[Focus](<../Interface (Focus)/arkts-apis-camera-focus.md>)、[Zoom](<../Interface (Zoom)/arkts-apis-camera-zoom.md>)、[ColorManagement](<../Interface (ColorManagement)/arkts-apis-camera-colormanagement.md>)、[AutoDeviceSwitch](<../Interface (AutoDeviceSwitch)/arkts-apis-camera-autodeviceswitch.md>)、[Macro](<../Interface (Macro)/arkts-apis-camera-macro.md>)、[ManualExposure](<../Interface (ManualExposure)/arkts-apis-camera-manualexposure.md>)、[ManualFocus](<../Interface (ManualFocus)/arkts-apis-camera-manualfocus.md>)、[ManualIso](<../Interface (ManualIso)/arkts-apis-camera-manualiso.md>)、[OIS](<../Interface (OIS)/arkts-apis-camera-ois.md>)、[Aperture](<../Interface (Aperture)/arkts-apis-camera-aperture.md>)。

普通拍照模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、色彩空间、微距、手动曝光、手动对焦、手动ISO、光学防抖及光圈的操作。

默认的拍照模式，用于拍摄标准照片。支持多种照片格式和分辨率，适合大多数日常拍摄场景。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## canPreconfig12+

PhonePC/2in1TabletTVWearable

canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean

查询当前Session是否支持指定的预配置类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preconfigType | [PreconfigType](../Enums/arkts-apis-camera-e.md#preconfigtype12) | 是 | 指定配置预期分辨率。 |
| preconfigRatio | [PreconfigRatio](../Enums/arkts-apis-camera-e.md#preconfigratio12) | 否 | 可选画幅比例，默认为4:3。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持指定预配置类型。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../../错误码/Camera错误码/errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testCanPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
4. preconfigRatio: camera.PreconfigRatio): void {
5. try {
6. let result = photoSession.canPreconfig(preconfigType, preconfigRatio);
7. console.info(`canPreconfig ${preconfigType} ${preconfigRatio} result is : ${result}`);
8. } catch (error) {
9. let err = error as BusinessError;
10. console.error(`The canPreconfig call failed. error code: ${err.code}`);
11. }
12. }
```

## preconfig12+

PhonePC/2in1TabletTVWearable

preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void

对当前Session进行预配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preconfigType | [PreconfigType](../Enums/arkts-apis-camera-e.md#preconfigtype12) | 是 | 指定配置预期分辨率。 |
| preconfigRatio | [PreconfigRatio](../Enums/arkts-apis-camera-e.md#preconfigratio12) | 否 | 可选画幅比例，默认为4:3。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../../错误码/Camera错误码/errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
4. preconfigRatio: camera.PreconfigRatio): void {
5. try {
6. photoSession.preconfig(preconfigType, preconfigRatio);
7. console.info(`preconfig success preconfigType: ${preconfigType}, preconfigRatio: ${preconfigRatio}`);
8. } catch (error) {
9. let err = error as BusinessError;
10. console.error(`The preconfig call failed. error code: ${err.code}`);
11. }
12. }
```

## on('error')11+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听普通拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](<../Interface (Session)/arkts-apis-camera-session.md#beginconfig11>)，[commitConfig](<../Interface (Session)/arkts-apis-camera-session.md#commitconfig11>)，[addInput](<../Interface (Session)/arkts-apis-camera-session.md#addinput11>)等接口发生错误时返回错误信息。 |
| callback | [ErrorCallback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#errorcallback>) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](../Enums/arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. console.error(`Photo session error code: ${err.code}`);
5. }

7. function registerSessionError(photoSession: camera.PhotoSession): void {
8. photoSession.on('error', callback);
9. }
```

## off('error')11+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听普通拍照会话的错误事件，通过注册回调函数获取结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。 |
| callback | [ErrorCallback](<../../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md#errorcallback>) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSessionError(photoSession: camera.PhotoSession): void {
2. photoSession.off('error');
3. }
```

## on('focusStateChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。 |
| callback | AsyncCallback<[FocusState](../Enums/arkts-apis-camera-e.md#focusstate)> | 是 | 回调函数，用于获取当前对焦状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, focusState: camera.FocusState): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`Focus state: ${focusState}`);
9. }

11. function registerFocusStateChange(photoSession: camera.PhotoSession): void {
12. photoSession.on('focusStateChange', callback);
13. }
```

## off('focusStateChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

注销监听相机聚焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session创建成功可监听。 |
| callback | AsyncCallback<[FocusState](../Enums/arkts-apis-camera-e.md#focusstate)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterFocusStateChange(photoSession: camera.PhotoSession): void {
2. photoSession.off('focusStateChange');
3. }
```

## on('smoothZoomInfoAvailable')11+

PhonePC/2in1TabletTVWearable

on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void

监听相机平滑变焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。 |
| callback | AsyncCallback<[SmoothZoomInfo](<../Interfaces (其他)/arkts-apis-camera-i.md#smoothzoominfo11>)> | 是 | 回调函数，用于获取当前平滑变焦状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, smoothZoomInfo: camera.SmoothZoomInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`The duration of smooth zoom: ${smoothZoomInfo.duration}`);
9. }

11. function registerSmoothZoomInfo(photoSession: camera.PhotoSession): void {
12. photoSession.on('smoothZoomInfoAvailable', callback);
13. }
```

## off('smoothZoomInfoAvailable')11+

PhonePC/2in1TabletTVWearable

off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void

注销监听相机平滑变焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。 |
| callback | AsyncCallback<[SmoothZoomInfo](<../Interfaces (其他)/arkts-apis-camera-i.md#smoothzoominfo11>)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
2. photoSession.off('smoothZoomInfoAvailable');
3. }
```

## on('autoDeviceSwitchStatusChange')13+

PhonePC/2in1TabletTVWearable

on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void

监听相机自动切换镜头状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback<[AutoDeviceSwitchStatus](<../Interfaces (其他)/arkts-apis-camera-i.md#autodeviceswitchstatus13>)> | 是 | 回调函数，用于获取当前自动切换镜头的状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}`);
9. }

11. function registerAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
12. photoSession.on('autoDeviceSwitchStatusChange', callback);
13. }
```

## off('autoDeviceSwitchStatusChange')13+

PhonePC/2in1TabletTVWearable

off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void

注销监听相机自动切换镜头状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback<[AutoDeviceSwitchStatus](<../Interfaces (其他)/arkts-apis-camera-i.md#autodeviceswitchstatus13>)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
2. photoSession.off('autoDeviceSwitchStatusChange');
3. }
```

## on('systemPressureLevelChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void

监听系统压力状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemPressureLevelChange'，session创建成功可监听。 |
| callback | AsyncCallback<[SystemPressureLevel](../Enums/arkts-apis-camera-e.md#systempressurelevel20)> | 是 | 回调函数，用于获取当前系统压力状态. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, systemPressureLevel: camera.SystemPressureLevel): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`systemPressureLevel: ${systemPressureLevel}`);
9. }

11. function registerSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
12. photoSession.on('systemPressureLevelChange', callback);
13. }
```

## off('systemPressureLevelChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void

注销监听系统压力状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'systemPressureLevelChange'，session创建成功可触发此事件。 |
| callback | AsyncCallback<[SystemPressureLevel](../Enums/arkts-apis-camera-e.md#systempressurelevel20)> | 否 | 回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。 |

**示例：**

```
1. function unregisterSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
2. photoSession.off('systemPressureLevelChange');
3. }
```

## on('macroStatusChanged')20+

PhonePC/2in1TabletTVWearable

on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void

监听相机微距状态变化，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'macroStatusChanged'，session创建成功可监听。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，用于获取当前微距状态，返回true为开启状态，返回false为禁用状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, macroStatus: boolean): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`Macro state: ${macroStatus}`);
9. }

11. function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
12. photoSession.on('macroStatusChanged', callback);
13. }
```

## off('macroStatusChanged')20+

PhonePC/2in1TabletTVWearable

off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void

注销相机微距状态变化的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'macroStatusChanged'，session创建成功可触发此事件。 |
| callback | AsyncCallback<boolean> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则参数默认为空，取消所有callback。 |

**示例：**

```
1. function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
2. photoSession.off('macroStatusChanged');
3. }
```

## onIsoInfoChange24+

PhonePC/2in1TabletTVWearable

onIsoInfoChange(callback: Callback<IsoInfo>): void

订阅ISO信息变化事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IsoInfo](<../Interfaces (其他)/arkts-apis-camera-i.md#isoinfo22>)> | 是 | 回调函数，用于获取ISO信息变化信息。 |

**示例：**

```
1. function onIsoInfoChange(photoSession: camera.PhotoSession): void {
2. photoSession.onIsoInfoChange((isoInfo: camera.IsoInfo) => {
3. console.info(`ISO info changed, iso: ${isoInfo.iso}`);
4. });
5. }
```

## offIsoInfoChange24+

PhonePC/2in1TabletTVWearable

offIsoInfoChange(callback?: Callback<IsoInfo>): void

取消订阅ISO信息变化事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IsoInfo](<../Interfaces (其他)/arkts-apis-camera-i.md#isoinfo22>)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function offIsoInfoChange(photoSession: camera.PhotoSession): void {
2. photoSession.offIsoInfoChange();
3. }
```

## onExposureInfoChange24+

PhonePC/2in1TabletTVWearable

onExposureInfoChange(callback: Callback<ExposureInfo>): void

订阅曝光信息变化事件回调。曝光参数更改后，系统将返回更新后的曝光信息。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ExposureInfo](<../Interfaces (其他)/arkts-apis-camera-i.md#exposureinfo24>)> | 是 | 回调函数，用于获取曝光值变化信息。 |

**示例：**

```
1. function onExposureInfoChange(photoSession: camera.PhotoSession): void {
2. photoSession.onExposureInfoChange((exposureInfo: camera.ExposureInfo) => {
3. console.info(`Exposure info changed, exposureTime: ${exposureInfo.exposureTime}`);
4. });
5. }
```

## offExposureInfoChange24+

PhonePC/2in1TabletTVWearable

offExposureInfoChange(callback?: Callback<ExposureInfo>): void

取消订阅曝光信息变化事件回调。如果订阅了曝光信息，请在释放相机前取消订阅。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ExposureInfo](<../Interfaces (其他)/arkts-apis-camera-i.md#exposureinfo24>)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function offExposureInfoChange(photoSession: camera.PhotoSession): void {
2. photoSession.offExposureInfoChange();
3. }
```
