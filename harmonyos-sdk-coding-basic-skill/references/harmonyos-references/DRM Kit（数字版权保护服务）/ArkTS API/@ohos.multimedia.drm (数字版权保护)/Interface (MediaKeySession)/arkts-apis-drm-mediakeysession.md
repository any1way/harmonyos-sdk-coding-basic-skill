---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-mediakeysession
title: Interface (MediaKeySession)
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > Interface (MediaKeySession)
category: harmonyos-references
scraped_at: 2026-06-01T16:21:35+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:cc084d2b5023077b717784be3168ee0207e1e01c1ee17925f6af247e985cb36d
---
支持媒体密钥管理。在调用MediaKeySession方法之前，必须使用[createMediaKeySession](<../Interface (MediaKeySystem)/arkts-apis-drm-mediakeysystem.md#createmediakeysession>)获取一个MediaKeySession实例。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drm } from '@kit.DrmKit';
```

## generateMediaKeyRequest

PhonePC/2in1TabletTVWearable

generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: number, options?: OptionsData[]): Promise<MediaKeyRequest>

生成媒体密钥请求。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 媒体类型，DRM解决方案名称，可通过[isMediaKeySystemSupported](../Functions/arkts-apis-drm-f.md#drmismediakeysystemsupported-1)查询。 |
| initData | Uint8Array | 是 | 初始数据，即加密流中的PSSH box中的实际PSSH数据。可通过监听AVPlayer的'mediaKeySystemInfoUpdate'事件（[on('mediaKeySystemInfoUpdate')](<../../../../Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md#onmediakeysysteminfoupdate11>)）获取DRM信息，从中提取pssh字段生成initData。具体开发流程可参考[基于AVPlayer播放DRM节目(ArkTS)](<../../../../../harmonyos-guides/媒体/DRM Kit（数字版权保护服务）/基于AVPlayer播放DRM节目(ArkTS)/drm-avplayer-arkts-integration.md>)。 |
| mediaKeyType | number | 是 | 媒体密钥类型。取值范围为[0, 1]。0表示在线，1表示离线。  传入指定范围外的参数会导致参数校验失败，抛出错误码401。 |
| options | [OptionsData[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i#optionsdata) | 否 | 可选数据。默认值为空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MediaKeyRequest](<../Interfaces (其他)/arkts-apis-drm-i.md#mediakeyrequest>)> | Promise对象，媒体密钥请求。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. // pssh数据为版权保护系统描述头，封装在加密码流中，mp4文件中位于pssh box、dash码流中位于mpd及mp4的pssh box、hls+ts的码流位于m3u8及每个ts片段中，请按实际值传入。
6. let uint8pssh = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
7. mediaKeySession.generateMediaKeyRequest("video/avc", uint8pssh, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE).then((mediaKeyRequest: drm.MediaKeyRequest) =>{
8. console.info('generateMediaKeyRequest' + mediaKeyRequest);
9. });
```

## processMediaKeyResponse

PhonePC/2in1TabletTVWearable

processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>

处理媒体密钥响应。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | Uint8Array | 是 | 媒体密钥响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，媒体密钥标识。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. // mediaKeyResponse是从DRM服务获取的媒体密钥响应，按实际值填入。
6. let mediaKeyResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
7. mediaKeySession.processMediaKeyResponse(mediaKeyResponse).then((mediaKeyId: Uint8Array) => {
8. console.info('processMediaKeyResponse:' + mediaKeyId);
9. });
```

## checkMediaKeyStatus

PhonePC/2in1TabletTVWearable

checkMediaKeyStatus(): MediaKeyStatus[]

检查当前媒体密钥状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeyStatus[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i#mediakeystatus) | 当前媒体密钥状态值。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. let keyStatus: drm.MediaKeyStatus[] =  mediaKeySession.checkMediaKeyStatus();
```

## clearMediaKeys

PhonePC/2in1TabletTVWearable

clearMediaKeys(): void

清除当前媒体密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. // mediaKeyResponse是从DRM服务获取的媒体密钥响应，按实际值填入。
6. let mediaKeyResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
7. mediaKeySession.processMediaKeyResponse(mediaKeyResponse).then((mediaKeyId: Uint8Array) => {
8. console.info('processMediaKeyResponse:' + mediaKeyId);
9. });
10. mediaKeySession.clearMediaKeys();
```

## generateOfflineReleaseRequest

PhonePC/2in1TabletTVWearable

generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>

生成离线媒体密钥释放请求。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，设备上的DRM解决方案支持离线媒体密钥释放处理，则返回离线媒体密钥释放请求。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. // mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际值传入。
6. let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
7. mediaKeySession.generateOfflineReleaseRequest(mediaKeyId).then((offlineReleaseRequest: Uint8Array) => {
8. console.info('generateOfflineReleaseRequest:' + offlineReleaseRequest);
9. });
```

## processOfflineReleaseResponse

PhonePC/2in1TabletTVWearable

processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>

处理离线媒体密钥释放响应。使用Promise异步回调。

如果设备上的DRM解决方案不支持离线媒体密钥释放，将抛出错误码24700101。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |
| response | Uint8Array | 是 | 离线媒体密钥释放响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. // mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际长度申请内存。
6. let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
7. mediaKeySession.generateOfflineReleaseRequest(mediaKeyId).then((offlineReleaseRequest: Uint8Array) => {
8. console.info('generateOfflineReleaseRequest:' + offlineReleaseRequest);
9. });
10. // offlineReleaseResponse是从DRM服务获取的离线媒体密钥释放响应，请按实际长度申请内存。
11. let offlineReleaseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
12. mediaKeySession.processOfflineReleaseResponse(mediaKeyId, offlineReleaseResponse).then(() => {
13. console.info('processOfflineReleaseResponse');
14. });
```

## restoreOfflineMediaKeys

PhonePC/2in1TabletTVWearable

restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>

恢复离线媒体密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. // mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际数据传入。
6. let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
7. mediaKeySession.restoreOfflineMediaKeys(mediaKeyId).then(() => {
8. console.info("restoreOfflineMediaKeys");
9. });
```

## getContentProtectionLevel

PhonePC/2in1TabletTVWearable

getContentProtectionLevel(): ContentProtectionLevel

获取当前会话的内容保护级别。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContentProtectionLevel](../Enums/arkts-apis-drm-e.md#contentprotectionlevel) | 返回当前会话内容保护级别。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. let contentProtectionLevel: drm.ContentProtectionLevel = mediaKeySession.getContentProtectionLevel();
6. console.info(`contentProtectionLevel: ${contentProtectionLevel}`);
```

## requireSecureDecoderModule

PhonePC/2in1TabletTVWearable

requireSecureDecoderModule(mimeType: string): boolean

是否需要安全解码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 媒体类型，支持的媒体类型取决于DRM解决方案，可通过[isMediaKeySystemSupported](../Functions/arkts-apis-drm-f.md#drmismediakeysystemsupported-1)查询。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否需要安全解码，true表示需要安全解码，false表示不需要安全解码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. let status: boolean = mediaKeySession.requireSecureDecoderModule("video/avc");
```

## on('keyRequired')

PhonePC/2in1TabletTVWearable

on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void

监听密钥请求事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定为'keyRequired'，当播放DRM节目需要获取媒体密钥时触发。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.on('keyRequired', (eventInfo: drm.EventInfo) => {
6. console.info('keyRequired ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
7. });
```

## off('keyRequired')

PhonePC/2in1TabletTVWearable

off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void

注销密钥请求事件监听。使用callback异步回调。

该接口用于注销已在on('keyRequired')中注册的监听，当播放DRM节目需要获取媒体密钥时触发的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keyRequired'。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 否 | 回调函数，返回事件信息。可选参数，不传时注销该事件类型的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.off('keyRequired');
```

## on('keyExpired')

PhonePC/2in1TabletTVWearable

on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void

监听密钥过期事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keyExpired'。密钥过期时触发。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.on('keyExpired', (eventInfo: drm.EventInfo) => {
6. console.info('keyExpired ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
7. });
```

## off('keyExpired')

PhonePC/2in1TabletTVWearable

off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void

注销密钥过期事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keyExpired'。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 否 | 回调函数，返回事件信息。可选参数，不传时注销该事件类型的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.off('keyExpired');
```

## on('vendorDefined')

PhonePC/2in1TabletTVWearable

on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void

监听DRM解决方案自定义事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'vendorDefined'。自定义事件发生时触发。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.on('vendorDefined', (eventInfo: drm.EventInfo) => {
6. console.info('vendorDefined ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
7. });
```

## off('vendorDefined')

PhonePC/2in1TabletTVWearable

off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void

注销DRM解决方案自定义事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'vendorDefined'。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 否 | 回调函数，返回事件信息。可选参数，不传时注销该事件类型的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.off('vendorDefined');
```

## on('expirationUpdate')

PhonePC/2in1TabletTVWearable

on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void

监听密钥过期更新事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'expirationUpdate'。密钥过期更新时触发。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.on('expirationUpdate', (eventInfo: drm.EventInfo) => {
6. console.info('expirationUpdate ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
7. });
```

## off('expirationUpdate')

PhonePC/2in1TabletTVWearable

off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void

注销过期更新事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'expirationUpdate'。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 否 | 回调函数，返回事件信息。可选参数，不传时注销该事件类型的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.off('expirationUpdate');
```

## on('keysChange')

PhonePC/2in1TabletTVWearable

on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void

监听密钥变化事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keysChange'。密钥变化时触发。 |
| callback | (keyInfo: [KeysInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i#keysinfo), newKeyAvailable: boolean) => void | 是 | 回调函数，返回事件信息，包含密钥标识和密钥状态描述的列表及密钥是否可用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.on('keysChange', (keyInfo: drm.KeysInfo[], newKeyAvailable: boolean) => {
6. for (let i = 0; i < keyInfo.length; i++) {
7. console.info('keysChange' + 'keyId:' + keyInfo[i].keyId + ' data:' + keyInfo[i].value);
8. }
9. });
```

## off('keysChange')

PhonePC/2in1TabletTVWearable

off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void

注销密钥变化事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keysChange'。 |
| callback | (keyInfo: [KeysInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i#keysinfo), newKeyAvailable: boolean) => void | 否 | 回调函数，返回事件信息，包含密钥标识和密钥状态描述的列表及密钥是否可用。  可选参数，不传时注销该事件类型的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.off('keysChange');
```

## destroy

PhonePC/2in1TabletTVWearable

destroy(): void

销毁MediaKeySession实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
5. mediaKeySession.destroy();
```
