---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-mediakeysystem
title: Interface (MediaKeySystem)
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > Interface (MediaKeySystem)
category: harmonyos-references
scraped_at: 2026-06-01T16:21:37+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:3a0b96a0cb757f7f77cde2f1386990e73fecd1abb8d9f29145142858d005e6c2
---
支持MediaKeySystem实例管理、设备证书申请与处理、会话创建、离线媒体密钥管理、获取DRM度量记录、设备属性等。在调用MediaKeySystem方法之前，必须使用[createMediaKeySystem](../Functions/arkts-apis-drm-f.md#drmcreatemediakeysystem)创建一个MediaKeySystem实例。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drm } from '@kit.DrmKit';
```

## setConfigurationString

PhonePC/2in1TabletTVWearable

setConfigurationString(configName: string, value: string): void

设置字符串类型的配置信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | 配置属性名，不能为空，属性名参考[PreDefinedConfigName](../Enums/arkts-apis-drm-e.md#predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。 |
| value | string | 是 | 配置属性值。 |

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
4. mediaKeySystem.setConfigurationString("stringConfigName", "stringConfigValue"); // 确保stringConfigName是可配置的。
```

## getConfigurationString

PhonePC/2in1TabletTVWearable

getConfigurationString(configName: string): string

获取字符串类型的配置属性值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | 配置属性名，不能为空，长度不能超过4096字节。  如果参数长度超过4096字节，会抛出错误码401。  属性名参考[PreDefinedConfigName](../Enums/arkts-apis-drm-e.md#predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回字符串类型的配置属性值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param's length is zero or too big(exceeds 4096 Bytes). |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let configValue: string = mediaKeySystem.getConfigurationString("vendor");
```

## setConfigurationByteArray

PhonePC/2in1TabletTVWearable

setConfigurationByteArray(configName: string, value: Uint8Array): void

设置数组类型的配置信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | 配置属性名，不能为空，属性名参考[PreDefinedConfigName](../Enums/arkts-apis-drm-e.md#predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。 |
| value | Uint8Array | 是 | 数组类型的配置属性值，具体属性值由设备上DRM解决方案决定。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. // 按实际需求填写configValue属性值，请按实际值传入。
5. let configValue: Uint8Array = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
6. // 需确认当前DRM解决方案的byteArrayConfigName属性是可配置的。
7. mediaKeySystem.setConfigurationByteArray("byteArrayConfigName", configValue);
```

## getConfigurationByteArray

PhonePC/2in1TabletTVWearable

getConfigurationByteArray(configName: string): Uint8Array

获取数组类型的配置信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | 配置属性名，不能为空，属性名参考[PreDefinedConfigName](../Enums/arkts-apis-drm-e.md#predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 数组类型的配置属性值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let configValue: Uint8Array = mediaKeySystem.getConfigurationByteArray("deviceUniqueId"); // 确保deviceUniqueId属性是存在的。
```

## getStatistics

PhonePC/2in1TabletTVWearable

getStatistics(): StatisticKeyValue[]

获取性能度量记录。其中包括当前会话数、插件版本信息、每个会话最大三次解密耗时、解密次数和解密失败次数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StatisticKeyValue[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i#statistickeyvalue) | 度量记录。 |

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
4. let statisticKeyValue: drm.StatisticKeyValue[] = mediaKeySystem.getStatistics();
```

## getMaxContentProtectionLevel

PhonePC/2in1TabletTVWearable

getMaxContentProtectionLevel(): ContentProtectionLevel

获取当前DRM解决方案支持的最大内容保护级别。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContentProtectionLevel](../Enums/arkts-apis-drm-e.md#contentprotectionlevel) | 返回设备支持的最大内容保护级别。 |

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
4. let maxLevel: drm.ContentProtectionLevel = mediaKeySystem.getMaxContentProtectionLevel();
```

## generateKeySystemRequest

PhonePC/2in1TabletTVWearable

generateKeySystemRequest(): Promise<ProvisionRequest>

生成获取mediaKeySystem设备证书的请求。使用Promise异步回调。

如果设备上已存在设备证书，调用此接口会返回失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ProvisionRequest](<../Interfaces (其他)/arkts-apis-drm-i.md#provisionrequest>)> | Promise对象，mediaKeySystem设备证书的请求。设备上如果已存在设备证书，会返回失败。 |

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
4. // 设备上已有设备证书的情况下不需要调用。
5. mediaKeySystem.generateKeySystemRequest().then((provisionRequest: drm.ProvisionRequest) => {
6. // provisionRequest为接口返回的设备证书请求对象，包含请求数据和默认URL。
7. console.info("generateKeySystemRequest, defaultURL: " + provisionRequest.defaultURL);
8. });
```

## processKeySystemResponse

PhonePC/2in1TabletTVWearable

processKeySystemResponse(response: Uint8Array): Promise<void>

处理获得的设备证书请求的响应。使用Promise异步回调。

如果设备上已存在设备证书，调用此接口会返回失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | Uint8Array | 是 | 从DRM服务获取的设备证书响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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
4. // keySystemResponse是从DRM服务获取的设备证书响应，请按实际值传入。
5. let keySystemResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
6. mediaKeySystem.processKeySystemResponse(keySystemResponse).then(() => {
7. console.info("processKeySystemResponse");
8. });
```

## getCertificateStatus

PhonePC/2in1TabletTVWearable

getCertificateStatus():CertificateStatus

获取设备证书状态值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CertificateStatus](../Enums/arkts-apis-drm-e.md#certificatestatus) | 设备证书状态值。 |

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
4. let certificateStatus: drm.CertificateStatus = mediaKeySystem.getCertificateStatus();
```

## on('keySystemRequired')

PhonePC/2in1TabletTVWearable

on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void

监听设备证书请求事件，获取事件信息。使用callback异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，通过[createMediaKeySystem](../Functions/arkts-apis-drm-f.md#drmcreatemediakeysystem)成功创建MediaKeySystem实例后可监听，需要设备证书时触发该事件。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 是 | 回调函数，返回事件信息。只要有该事件返回就证明需请求设备证书。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. mediaKeySystem.on('keySystemRequired', (eventInfo: drm.EventInfo) => {
5. console.info('keySystemRequired ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
6. });
```

## off('keySystemRequired')

PhonePC/2in1TabletTVWearable

off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void

注销设备证书请求事件的监听。使用callback异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，通过[createMediaKeySystem](../Functions/arkts-apis-drm-f.md#drmcreatemediakeysystem)成功创建MediaKeySystem实例后可监听。 |
| callback | (eventInfo: [EventInfo](<../Interfaces (其他)/arkts-apis-drm-i.md#eventinfo>)) => void | 否 | 回调函数，返回事件信息。可选参数，不传时注销该事件类型的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 24700101 | All unknown errors |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
3. mediaKeySystem.off('keySystemRequired');
```

## createMediaKeySession

PhonePC/2in1TabletTVWearable

createMediaKeySession(level: ContentProtectionLevel): MediaKeySession

创建指定内容保护级别的MediaKeySession实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [ContentProtectionLevel](../Enums/arkts-apis-drm-e.md#contentprotectionlevel) | 是 | 内容保护级别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySession](<../Interface (MediaKeySession)/arkts-apis-drm-mediakeysession.md>) | MediaKeySession实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range, please use value in ContentProtectionLevel. |
| 24700101 | All unknown errors |
| 24700104 | Meet max MediaKeySession num limit |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession(drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
```

## createMediaKeySession

PhonePC/2in1TabletTVWearable

createMediaKeySession(): MediaKeySession

创建DRM解决方案默认内容保护级别的MediaKeySession实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySession](<../Interface (MediaKeySession)/arkts-apis-drm-mediakeysession.md>) | MediaKeySession实例。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700104 | Meet max MediaKeySession num limit |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
```

## getOfflineMediaKeyIds

PhonePC/2in1TabletTVWearable

getOfflineMediaKeyIds(): Uint8Array[]

获取离线媒体密钥标识列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array[] | 离线媒体密钥标识列表。 |

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
4. let offlineMediaKeyIds: Uint8Array[] = mediaKeySystem.getOfflineMediaKeyIds();
```

## getOfflineMediaKeyStatus

PhonePC/2in1TabletTVWearable

getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus

获取指定离线媒体密钥标识的媒体密钥的状态值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OfflineMediaKeyStatus](../Enums/arkts-apis-drm-e.md#offlinemediakeystatus) | 离线媒体密钥状态值。 |

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
4. // mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际值传入。
5. let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
6. let configValue: drm.OfflineMediaKeyStatus = mediaKeySystem.getOfflineMediaKeyStatus(mediaKeyId);
```

## clearOfflineMediaKeys

PhonePC/2in1TabletTVWearable

clearOfflineMediaKeys(mediaKeyId: Uint8Array): void

删除指定媒体密钥标识的离线媒体密钥。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[DRM错误码](../../../错误码/DRM错误码/errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
4. // mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际值传入。
5. let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
6. mediaKeySystem.clearOfflineMediaKeys(mediaKeyId);
```

## destroy

PhonePC/2in1TabletTVWearable

destroy(): void

销毁MediaKeySystem实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

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
4. mediaKeySystem.destroy();
```
