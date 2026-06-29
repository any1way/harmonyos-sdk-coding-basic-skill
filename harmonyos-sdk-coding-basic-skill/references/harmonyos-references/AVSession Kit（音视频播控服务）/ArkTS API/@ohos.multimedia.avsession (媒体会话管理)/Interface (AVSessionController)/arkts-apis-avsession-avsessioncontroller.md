---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller
title: Interface (AVSessionController)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Interface (AVSessionController)
category: harmonyos-references
scraped_at: 2026-06-01T16:19:04+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:00910a4c9b5ca1b141de2919c1a4f1cf37a7732a853fc16439ef3e27d11ca443
---
AVSessionController控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 10开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { avSession } from '@kit.AVSessionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId10+ | string | 是 | 否 | AVSessionController对象唯一的会话标识。 |

**示例：**

```
1. // Index.ets
2. import { avSession } from '@kit.AVSessionKit';

4. @Entry
5. @Component
6. struct Index {
7. private tag: string = "createNewSession";
8. private sessionId: string = "";
9. private AVSessionController?: avSession.AVSessionController;
10. private currentAVSession?: avSession.AVSession;
11. context = this.getUIContext();

13. aboutToAppear(): void {

15. avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio").then(async (data: avSession.AVSession) => {
16. this.currentAVSession = data;
17. this.sessionId = this.currentAVSession.sessionId;
18. this.avsessionController = await this.currentAVSession.getController();
19. console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
20. });
21. }

23. build() {
24. Column() {
25. Text('AVSession Demo')
26. .fontSize(20)
27. .margin(10)
28. }
29. .width('100%')
30. .height('100%')
31. .justifyContent(FlexAlign.Center)
32. }
33. }
```

## getAVPlaybackState10+

PhonePC/2in1TabletTVWearable

getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>)> | 是 | 回调函数，返回远端播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVPlaybackState((err: BusinessError, state: avSession.AVPlaybackState) => {
2. if (err) {
3. console.error(`Failed to get AV playback state, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info('Succeeded in getting AV playback state.');
7. });
```

## getAVPlaybackState10+

PhonePC/2in1TabletTVWearable

getAVPlaybackState(): Promise<AVPlaybackState>

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>)> | Promise对象,返回远端播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
2. console.info('Succeeded in getting AV playback state.');
3. });
```

## getAVMetadata10+

PhonePC/2in1TabletTVWearable

getAVMetadata(): Promise<AVMetadata>

获取会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>)> | Promise对象，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVMetadata().then((metadata: avSession.AVMetadata) => {
2. console.info(`Succeeded in getting AV metadata, assetId: ${metadata.assetId}`);
3. });
```

## getAVMetadata10+

PhonePC/2in1TabletTVWearable

getAVMetadata(callback: AsyncCallback<AVMetadata>): void

获取会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>)> | 是 | 回调函数，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVMetadata((err: BusinessError, metadata: avSession.AVMetadata) => {
2. if (err) {
3. console.error(`Failed to get AV metadata, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting AV metadata, assetId: ${metadata.assetId}`);
7. });
```

## getAVQueueTitle10+

PhonePC/2in1TabletTVWearable

getAVQueueTitle(): Promise<string>

获取当前会话播放列表的名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVQueueTitle().then((title: string) => {
2. console.info(`Succeeded in getting AV queue title: ${title}`);
3. });
```

## getAVQueueTitle10+

PhonePC/2in1TabletTVWearable

getAVQueueTitle(callback: AsyncCallback<string>): void

获取当前播放列表的名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVQueueTitle((err: BusinessError, title: string) => {
2. if (err) {
3. console.error(`Failed to get AV queue title, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting AV queue title: ${title}`);
7. });
```

## getAVQueueItems10+

PhonePC/2in1TabletTVWearable

getAVQueueItems(): Promise<Array<AVQueueItem>>

获取当前会话播放列表相关信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)>> | Promise对象。返回播放列表队列。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVQueueItems().then((items: avSession.AVQueueItem[]) => {
2. console.info(`Succeeded in getting AV queue items, length: ${items.length}`);
3. });
```

## getAVQueueItems10+

PhonePC/2in1TabletTVWearable

getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void

获取当前播放列表相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)>> | 是 | 回调函数，返回播放列表队列。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVQueueItems((err: BusinessError, items: avSession.AVQueueItem[]) => {
2. if (err) {
3. console.error(`Failed to get AV queue items, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting AV queue items, length: ${items.length}`);
7. });
```

## skipToQueueItem10+

PhonePC/2in1TabletTVWearable

skipToQueueItem(itemId: number): Promise<void>

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemId | number | 是 | 播放列表单项的ID值，用以表示选中的播放列表单项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放列表单项ID设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let queueItemId = 0;
2. avcontroller.skipToQueueItem(queueItemId).then(() => {
3. console.info('Succeeded in skipping to queue item.');
4. });
```

## skipToQueueItem10+

PhonePC/2in1TabletTVWearable

skipToQueueItem(itemId: number, callback: AsyncCallback<void>): void

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemId | number | 是 | 播放列表单项的ID值，用以表示选中的播放列表单项。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let queueItemId = 0;
2. avcontroller.skipToQueueItem(queueItemId, (err: BusinessError) => {
3. if (err) {
4. console.error(`Failed to skip to queue item, code: ${err.code}, message: ${err.message}`);
5. return;
6. }
7. console.info('Succeeded in skipping to queue item.');
8. });
```

## getOutputDevice10+

PhonePC/2in1TabletTVWearable

getOutputDevice(): Promise<OutputDeviceInfo>

获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)> | Promise对象，返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getOutputDevice().then((deviceInfo: avSession.OutputDeviceInfo) => {
2. console.info('Succeeded in getting output device.');
3. });
```

## getOutputDevice10+

PhonePC/2in1TabletTVWearable

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

获取播放设备信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)> | 是 | 回调函数，返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getOutputDevice((err: BusinessError, deviceInfo: avSession.OutputDeviceInfo) => {
2. if (err) {
3. console.error(`Failed to get output device, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info('Succeeded in getting output device.');
7. });
```

## sendAVKeyEvent10+

PhonePC/2in1TabletTVWearable

sendAVKeyEvent(event: KeyEvent): Promise<void>

发送按键事件到控制器对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [KeyEvent](<../../../../基础功能/Input Kit（多模输入服务）/ArkTS API/@ohos.multimodalInput.keyEvent (按键输入事件)/js-apis-keyevent.md>) | 是 | 按键事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当事件发送成功，无返回结果，否则返回错误对象。 |

**示例：**

```
1. import { Key, KeyEvent } from '@kit.InputKit';

3. let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
4. let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

6. avcontroller.sendAVKeyEvent(event).then(() => {
7. console.info('Succeeded in sending AV key event.');
8. });
```

## sendAVKeyEvent10+

PhonePC/2in1TabletTVWearable

sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void

发送按键事件到会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [KeyEvent](<../../../../基础功能/Input Kit（多模输入服务）/ArkTS API/@ohos.multimodalInput.keyEvent (按键输入事件)/js-apis-keyevent.md>) | 是 | 按键事件。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当事件发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |

**示例：**

```
1. import { Key, KeyEvent } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
5. let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};
6. avcontroller.sendAVKeyEvent(event, (err: BusinessError) => {
7. if (err) {
8. console.error(`Failed to send AV key event, code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in sending AV key event.');
12. });
```

## getLaunchAbility10+

PhonePC/2in1TabletTVWearable

getLaunchAbility(): Promise<WantAgent>

获取应用在会话中保存的WantAgent对象。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WantAgent](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md>)> | Promise对象，返回在[setLaunchAbility](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#setlaunchability10>)保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getLaunchAbility().then((agent: object) => {
2. console.info(`Succeeded in getting launch ability: ${agent}`);
3. });
```

## getLaunchAbility10+

PhonePC/2in1TabletTVWearable

getLaunchAbility(callback: AsyncCallback<WantAgent>): void

获取应用在会话中保存的WantAgent对象。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WantAgent](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md>)> | 是 | 回调函数。返回在[setLaunchAbility](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#setlaunchability10>)保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getLaunchAbility((err: BusinessError, agent: object) => {
2. if (err) {
3. console.error(`Failed to get launch ability, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting launch ability: ${agent}`);
7. });
```

## getRealPlaybackPositionSync10+

PhonePC/2in1TabletTVWearable

getRealPlaybackPositionSync(): number

获取当前播放位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 时间节点，毫秒数。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let time: number = avcontroller.getRealPlaybackPositionSync();
```

## isActive10+

PhonePC/2in1TabletTVWearable

isActive(): Promise<boolean>

获取会话是否被激活。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回会话是否为激活状态，true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.isActive().then((isActive: boolean) => {
2. console.info(`Succeeded in checking active state: ${isActive}`);
3. });
```

## isActive10+

PhonePC/2in1TabletTVWearable

isActive(callback: AsyncCallback<boolean>): void

判断会话是否被激活。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回会话是否为激活状态，true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.isActive((err: BusinessError, isActive: boolean) => {
2. if (err) {
3. console.error(`Failed to check active state, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in checking active state: ${isActive}`);
7. });
```

## destroy10+

PhonePC/2in1TabletTVWearable

destroy(): Promise<void>

销毁当前控制器，销毁后当前控制器不可再用。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当控制器销毁成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.destroy().then(() => {
2. console.info('Succeeded in destroying.');
3. });
```

## destroy10+

PhonePC/2in1TabletTVWearable

destroy(callback: AsyncCallback<void>): void

销毁当前控制器，销毁后当前控制器不可再用。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当控制器销毁成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.destroy((err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to destroy controller, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info('Succeeded in destroying.');
7. });
```

## getValidCommands10+

PhonePC/2in1TabletTVWearable

getValidCommands(): Promise<Array<AVControlCommandType>>

获取会话支持的有效命令。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AVControlCommandType](../Types/arkts-apis-avsession-t.md#avcontrolcommandtype10)>> | Promise对象。返回有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getValidCommands().then((validCommands: avSession.AVControlCommandType[]) => {
2. console.info(`Succeeded in getting valid commands, size: ${validCommands.length}`);
3. });
```

## getValidCommands10+

PhonePC/2in1TabletTVWearable

getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void

获取会话支持的有效命令。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[AVControlCommandType](../Types/arkts-apis-avsession-t.md#avcontrolcommandtype10)>> | 是 | 回调函数，返回有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getValidCommands((err: BusinessError, validCommands: avSession.AVControlCommandType[]) => {
2. if (err) {
3. console.error(`Failed to get valid commands, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting valid commands, size: ${validCommands.length}`);
7. });
```

## sendControlCommand10+

PhonePC/2in1TabletTVWearable

sendControlCommand(command: AVControlCommand): Promise<void>

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

说明

媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口[on('play')](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#onplay10>)、[on('pause')](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#onpause10>)等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [AVControlCommand](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcontrolcommand10>) | 是 | 会话的相关命令和命令相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
1. let avCommand: avSession.AVControlCommand = {command:'play'};
2. avcontroller.sendControlCommand(avCommand).then(() => {
3. console.info('Succeeded in sending control command.');
4. });
```

## sendControlCommand10+

PhonePC/2in1TabletTVWearable

sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

说明

媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口[on('play')](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#onplay10>)、[on('pause')](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#onpause10>)等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [AVControlCommand](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcontrolcommand10>) | 是 | 会话的相关命令和命令相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
1. let avCommand: avSession.AVControlCommand = {command:'play'};
2. avcontroller.sendControlCommand(avCommand, (err: BusinessError) => {
3. if (err) {
4. console.error(`Failed to send control command, code: ${err.code}, message: ${err.message}`);
5. return;
6. }
7. console.info('Succeeded in sending control command.');
8. });
```

## sendCommonCommand10+

PhonePC/2in1TabletTVWearable

sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>

通过会话控制器发送自定义控制命令到其对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 需要设置的自定义控制命令的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的控制命令键值对。 |

说明

参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
1. let commandName = "my_command";
2. avcontroller.sendCommonCommand(commandName, {command : "This is my command"}).then(() => {
3. console.info('Succeeded in sending common command.');
4. });
```

## sendCommonCommand10+

PhonePC/2in1TabletTVWearable

sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void

通过会话控制器发送自定义命令到其对应的会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 需要设置的自定义控制命令的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的控制命令键值对。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

说明

参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
1. let commandName = "my_command";
2. avcontroller.sendCommonCommand(commandName, {command : "This is my command"}, (err: BusinessError) => {
3. if (err) {
4. console.error(`Failed to send common command, code: ${err.code}, message: ${err.message}`);
5. return;
6. }
7. console.info('Succeeded in sending common command.');
8. })
```

## sendCustomData20+

PhonePC/2in1TabletTV

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. // Index.ets
2. import { avSession } from '@kit.AVSessionKit';

4. @Entry
5. @Component
6. struct Index {
7. private tag: string = "createNewSession";
8. private sessionId: string = "";
9. private controller: avSession.AVSessionController | undefined = undefined;
10. private currentAVSession?: avSession.AVSession;
11. context = this.getUIContext();

13. aboutToAppear(): void {
14. avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
15. .then(async (data: avSession.AVSession) => {
16. this.currentAVSession = data;
17. this.sessionId = this.currentAVSession.sessionId;
18. this.controller = await this.currentAVSession.getController();
19. console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
20. });

22. if (this.controller !== undefined) {
23. (this.controller as avSession.AVSessionController).sendCustomData({ customData: "This is my data" })
24. }
25. }

27. build() {
28. Column() {
29. Text('AVSession Demo')
30. .fontSize(20)
31. .margin(10)
32. }
33. .width('100%')
34. .height('100%')
35. .justifyContent(FlexAlign.Center)
36. }
37. }
```

## getExtras10+

PhonePC/2in1TabletTVWearable

getExtras(): Promise<{[key: string]: Object}>

获取媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<{[key: string]: Object}> | Promise对象，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

**示例：**

```
1. // Index.ets
2. import { avSession } from '@kit.AVSessionKit';

4. @Entry
5. @Component
6. struct Index {
7. private tag: string = "createNewSession";
8. private sessionId: string = "";
9. private controller: avSession.AVSessionController | undefined = undefined;
10. private currentAVSession?: avSession.AVSession;
11. context = this.getUIContext();

13. aboutToAppear(): void {

15. avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
16. .then(async (data: avSession.AVSession) => {
17. this.currentAVSession = data;
18. this.sessionId = this.currentAVSession.sessionId;
19. this.controller = await this.currentAVSession.getController();
20. console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
21. });
22. if (this.controller !== undefined) {
23. (this.controller as avSession.AVSessionController).getExtras().then((extras) => {
24. console.info(`Succeeded in getting extras: ${extras}`);
25. });
26. }
27. }

29. build() {
30. Column() {
31. Text('AVSession Demo')
32. .fontSize(20)
33. .margin(10)
34. }
35. .width('100%')
36. .height('100%')
37. .justifyContent(FlexAlign.Center)
38. }
39. }
```

## getExtras10+

PhonePC/2in1TabletTVWearable

getExtras(callback: AsyncCallback<{[key: string]: Object}>): void

获取媒体提供方设置的自定义媒体数据包。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<{[key: string]: Object}> | 是 | 回调函数，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

**示例：**

```
1. avcontroller.getExtras((err: BusinessError, extras) => {
2. if (err) {
3. console.error(`Failed to get extras, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting extras: ${extras}`);
7. });
```

## getExtrasWithEvent18+

PhonePC/2in1TabletTVWearable

getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>

根据远端分布式事件类型，获取远端分布式媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extraEvent | string | 是 | 远端分布式事件类型。可获取的事件类型来自于[setExtras](<../Interface (AVSession)/arkts-apis-avsession-avsession.md#setextras10>)。  对Wearable设备类型，额外提供以下预设的事件类型：  'AUDIO\_GET\_VOLUME'：获取远端设备音量。  'AUDIO\_GET\_AVAILABLE\_DEVICES'：获取远端所有可连接设备。  'AUDIO\_GET\_PREFERRED\_OUTPUT\_DEVICE\_FOR\_RENDERER\_INFO'：获取远端实际发声设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ExtraInfo](../Types/arkts-apis-avsession-t.md#extrainfo18)> | Promise对象，返回远端分布式媒体提供方设置的自定义媒体数据包。  参数ExtraInfo支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |

**示例：**

```
1. let controller: avSession.AVSessionController | ESObject;
2. const COMMON_COMMAND_STRING_1 = 'AUDIO_GET_VOLUME';
3. const COMMON_COMMAND_STRING_2 = 'AUDIO_GET_AVAILABLE_DEVICES';
4. const COMMON_COMMAND_STRING_3 = 'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO';
5. if (controller !== undefined) {
6. controller.getExtrasWithEvent(COMMON_COMMAND_STRING_1).then(() => {
7. console.info(`${[COMMON_COMMAND_STRING_1]}`);
8. })

10. controller.getExtrasWithEvent(COMMON_COMMAND_STRING_2).then(() => {
11. console.info(`${[COMMON_COMMAND_STRING_2]}`);
12. })

14. controller.getExtrasWithEvent(COMMON_COMMAND_STRING_3).then(() => {
15. console.info(`${[COMMON_COMMAND_STRING_3]}`);
16. })
17. }
```

## isDesktopLyricEnabled23+

PhonePC/2in1TabletTVWearable

isDesktopLyricEnabled(): Promise<boolean>

查询是否启用桌面歌词功能。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示启用桌面歌词功能；返回false表示不启用桌面歌词功能。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600111 | The desktop lyrics feature is not supported. |

```
1. avcontroller.isDesktopLyricEnabled();
```

## onDesktopLyricEnabled23+

PhonePC/2in1TabletTVWearable

onDesktopLyricEnabled(callback: Callback<boolean>): void

桌面歌词功能启用状态变更的监听事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示桌面歌词功能启用；返回false表示桌面歌词功能未启用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.onDesktopLyricEnabled((enabled: boolean) => {
2. console.info(`desktop lyric enabled state : ${enabled}`);
3. })
```

## offDesktopLyricEnabled23+

PhonePC/2in1TabletTVWearable

offDesktopLyricEnabled(callback?: Callback<boolean>): void

取消桌面歌词启用状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词功能启用状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.offDesktopLyricEnabled();
```

## setDesktopLyricVisible23+

PhonePC/2in1TabletTVWearable

setDesktopLyricVisible(visible: boolean): Promise<void>

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示桌面歌词。true表示显示；false表示不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. avcontroller.setDesktopLyricVisible(true);
```

## isDesktopLyricVisible23+

PhonePC/2in1TabletTVWearable

isDesktopLyricVisible(): Promise<boolean>

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示显示桌面歌词；返回false表示不显示桌面歌词。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. avcontroller.isDesktopLyricVisible();
```

## onDesktopLyricVisibilityChanged23+

PhonePC/2in1TabletTVWearable

onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示开启显示桌面歌词状态；返回false表示关闭显示桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.onDesktopLyricVisibilityChanged((visible: boolean) => {
2. console.info(`desktop lyric visible state: ${visible}`);
3. });
```

## offDesktopLyricVisibilityChanged23+

PhonePC/2in1TabletTVWearable

offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有显示桌面歌词状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.offDesktopLyricVisibilityChanged();
```

## setDesktopLyricState23+

PhonePC/2in1TabletTVWearable

setDesktopLyricState(state: DesktopLyricState): Promise<void>

设置当前会话桌面歌词状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [DesktopLyricState](<../Interfaces (其他)/arkts-apis-avsession-i.md#desktoplyricstate23>) | 是 | 桌面歌词状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. let state: avSession.DesktopLyricState = {
2. isLocked: true,
3. };
4. avcontroller.setDesktopLyricState(state);
```

## getDesktopLyricState23+

PhonePC/2in1TabletTVWearable

getDesktopLyricState(): Promise<DesktopLyricState>

获取当前会话桌面歌词状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DesktopLyricState](<../Interfaces (其他)/arkts-apis-avsession-i.md#desktoplyricstate23>)> | Promise对象。返回桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. avcontroller.getDesktopLyricState();
```

## onDesktopLyricStateChanged23+

PhonePC/2in1TabletTVWearable

onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void

桌面歌词状态变更的监听事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DesktopLyricState](<../Interfaces (其他)/arkts-apis-avsession-i.md#desktoplyricstate23>)> | 是 | 回调函数。返回桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
2. console.info(`desktop lyric isLocked : ${state.isLocked}`);
3. })
```

## offDesktopLyricStateChanged23+

PhonePC/2in1TabletTVWearable

offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DesktopLyricState](<../Interfaces (其他)/arkts-apis-avsession-i.md#desktoplyricstate23>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.offDesktopLyricStateChanged();
```

## on('metadataChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)

设置元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'metadataChange'：当元数据需要更新时，触发该事件。  需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。 |
| filter | Array<keyof AVMetadata>|'all' | 是 | 'all'表示关注通话状态所有字段变化；Array<keyof AVMetadata>表示关注Array中的字段变化。 |
| callback | (data: [AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>)) => void | 是 | 回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，不代表当前全量的元数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('metadataChange', 'all', (metadata: avSession.AVMetadata) => {
2. console.info(`on metadataChange assetId : ${metadata.assetId}`);
3. });

5. avcontroller.on('metadataChange', ['assetId', 'title', 'description'], (metadata: avSession.AVMetadata) => {
6. console.info(`on metadataChange assetId : ${metadata.assetId}`);
7. });
```

## off('metadataChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'metadataChange', callback?: (data: AVMetadata) => void)

取消元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'metadataChange'。 |
| callback | (data: [AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>)) => void | 否 | 回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，并不代表当前全量的元数据。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('metadataChange');
```

## on('playbackStateChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)

设置播放状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'playbackStateChange'，当播放状态需要更新时，触发该事件。  需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。 |
| filter | Array<keyof AVPlaybackState>|'all' | 是 | 'all'表示关注播放状态所有字段更新。  Array<keyof AVPlaybackstate> 表示关注Array中的字段更新。 |
| callback | (state: [AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>)) => void | 是 | 回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
2. console.info(`on playbackStateChange state : ${playbackState.state}`);
3. });

5. avcontroller.on('playbackStateChange', ['state', 'speed', 'loopMode'], (playbackState: avSession.AVPlaybackState) => {
6. console.info(`on playbackStateChange state : ${playbackState.state}`);
7. });
```

## off('playbackStateChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'playbackStateChange'。 |
| callback | (state: [AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>)) => void | 否 | 回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('playbackStateChange');
```

## on('callMetadataChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void

设置通话元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'callMetadataChange'：当通话元数据变化时，触发该事件。 |
| filter | Array<keyof CallMetadata>|'all' | 是 | 'all'表示关注通话元数据所有字段变化；Array<keyof CallMetadata> 表示关注Array中的字段变化。| 'all'。 |
| callback | Callback<[CallMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#callmetadata11>)> | 是 | 回调函数，参数callmetadata是变化后的通话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('callMetadataChange', 'all', (callmetadata: avSession.CallMetadata) => {
2. console.info(`on callMetadataChange state : ${callmetadata.name}`);
3. });

5. avcontroller.on('callMetadataChange', ['name'], (callmetadata: avSession.CallMetadata) => {
6. console.info(`on callMetadataChange state : ${callmetadata.name}`);
7. });
```

## off('callMetadataChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void

取消设置通话元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'callMetadataChange'。 |
| callback | Callback<[CallMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#callmetadata11>)> | 否 | 回调函数，参数calldata是变化后的通话原数据。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('callMetadataChange');
```

## on('callStateChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void

设置通话状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'callStateChange'：当通话状态变化时，触发该事件。 |
| filter | Array<keyof AVCallState>|'all' | 是 | 'all' 表示关注通话状态所有字段变化；Array<keyof AVCallState>表示关注Array中的字段变化。| 'all'。 |
| callback | Callback<[AVCallState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcallstate11>)> | 是 | 回调函数，参数callstate是变化后的通话状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('callStateChange', 'all', (callstate: avSession.AVCallState) => {
2. console.info(`on callStateChange state : ${callstate.state}`);
3. });

5. avcontroller.on('callStateChange', ['state'], (callstate: avSession.AVCallState) => {
6. console.info(`on callStateChange state : ${callstate.state}`);
7. });
```

## off('callStateChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'callStateChange', callback?: Callback<AVCallState>): void

取消设置通话状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'callStateChange'。 |
| callback | Callback<[AVCallState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcallstate11>)> | 否 | 回调函数，参数callstate是变化后的通话状态。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('callStateChange');
```

## on('sessionDestroy')10+

PhonePC/2in1TabletTVWearable

on(type: 'sessionDestroy', callback: () => void)

会话销毁的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'sessionDestroy'：当检测到会话销毁时，触发该事件。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('sessionDestroy', () => {
2. console.info('Succeeded in session destroy.');
3. });
```

## off('sessionDestroy')10+

PhonePC/2in1TabletTVWearable

off(type: 'sessionDestroy', callback?: () => void)

取消监听会话的销毁事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'sessionDestroy'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('sessionDestroy');
```

## on('activeStateChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'activeStateChange', callback: (isActive: boolean) => void)

会话的激活状态的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'activeStateChange'：当检测到会话的激活状态发生改变时，触发该事件。 |
| callback | (isActive: boolean) => void | 是 | 回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('activeStateChange', (isActive: boolean) => {
2. console.info(`Succeeded in active state change: ${isActive}`);
3. });
```

## off('activeStateChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'activeStateChange', callback?: (isActive: boolean) => void)

取消监听会话激活状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'activeStateChange'。 |
| callback | (isActive: boolean) => void | 否 | 回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('activeStateChange');
```

## on('validCommandChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'validCommandChange'：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | (commands: Array<[AVControlCommandType](../Types/arkts-apis-avsession-t.md#avcontrolcommandtype10)>) => void | 是 | 回调函数。参数commands是有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('validCommandChange', (validCommands: avSession.AVControlCommandType[]) => {
2. console.info(`Succeeded in valid command change, size: ${validCommands.length}`);
3. console.info(`Succeeded in valid command change, validCommands: ${validCommands.values()}`);
4. });
```

## off('validCommandChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)

取消监听会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'validCommandChange'。 |
| callback | (commands: Array<[AVControlCommandType](../Types/arkts-apis-avsession-t.md#avcontrolcommandtype10)>) => void | 否 | 回调函数。参数commands是有效命令的集合。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('validCommandChange');
```

## on('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件为'outputDeviceChange'：当播放设备变化时，触发该事件）。 |
| callback | (state: [ConnectionState](../Enums/arkts-apis-avsession-e.md#connectionstate10), device: [OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)) => void | 是 | 回调函数，参数device是设备相关信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
2. console.info(`on outputDeviceChange state: ${state}, device : ${device}`);
3. });
```

## off('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消监听分布式设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'outputDeviceChange'。 |
| callback | (state: [ConnectionState](../Enums/arkts-apis-avsession-e.md#connectionstate10), device: [OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)) => void | 否 | 回调函数，参数device是设备相关信息。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('outputDeviceChange');
```

## on('sessionEvent')10+

PhonePC/2in1TabletTVWearable

on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void

媒体控制器设置会话自定义事件变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'sessionEvent'：当会话事件变化时，触发该事件。 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) => void | 是 | 回调函数，sessionEvent为变化的会话事件名，args为事件的参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. // Index.ets
2. avcontroller.on('sessionEvent', (sessionEvent, args) => {
3. console.info(`OnSessionEvent, sessionEvent is ${sessionEvent}, args: ${JSON.stringify(args)}`);
4. });
```

## off('sessionEvent')10+

PhonePC/2in1TabletTVWearable

off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void

取消会话事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'sessionEvent'。 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) => void | 否 | 回调函数，参数sessionEvent是变化的事件名，args为事件的参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('sessionEvent');
```

## on('queueItemsChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'queueItemsChange', callback: (items: Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)>) => void): void

媒体控制器设置会话自定义播放列表变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'queueItemsChange'：当session修改播放列表时，触发该事件。 |
| callback | (items: Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)>) => void | 是 | 回调函数，items为变化的播放列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('queueItemsChange', (items: avSession.AVQueueItem[]) => {
2. console.info(`OnQueueItemsChange, items length is ${items.length}`);
3. });
```

## off('queueItemsChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'queueItemsChange', callback?: (items: Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)>) => void): void

取消播放列表变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'queueItemsChange'。 |
| callback | (items: Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)>) => void | 否 | 回调函数，参数items是变化的播放列表。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('queueItemsChange');
```

## on('queueTitleChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'queueTitleChange', callback: (title: string) => void): void

媒体控制器设置会话自定义播放列表的名称变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'queueTitleChange'：当session修改播放列表名称时，触发该事件。 |
| callback | (title: string) => void | 是 | 回调函数，title为变化的播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('queueTitleChange', (title: string) => {
2. console.info(`queueTitleChange, title is ${title}`);
3. });
```

## off('queueTitleChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'queueTitleChange', callback?: (title: string) => void): void

取消播放列表名称变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'queueTitleChange'。 |
| callback | (title: string) => void | 否 | 回调函数，参数items是变化的播放列表名称。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('queueTitleChange');
```

## on('extrasChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void

媒体控制器设置自定义媒体数据包事件变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'extrasChange'：当媒体提供方设置自定义媒体数据包时，触发该事件。 |
| callback | (extras: {[key: string]: Object}) => void | 是 | 回调函数，extras为媒体提供方新设置的自定义媒体数据包，该自定义媒体数据包与dispatchSessionEvent方法设置的数据包完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('extrasChange', (extras) => {
2. console.info(`Caught extrasChange event,the new extra is: ${JSON.stringify(extras)}`);
3. });
```

## off('extrasChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void

取消自定义媒体数据包变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'extrasChange'。 |
| callback | (extras: {[key: string]: Object}) => void | 否 | 注册监听事件时的回调函数。  该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('extrasChange');
```

## on('customDataChange')20+

PhonePC/2in1TabletTV

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远程设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。 |
| callback | Callback<Record<string, Object>> | 是 | 回调函数，用于接收自定义数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.on('customDataChange', (callback) => {
2. console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
3. });
```

## off('customDataChange')20+

PhonePC/2in1TabletTV

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消自定义数据监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | Callback<Record<string, Object>> | 否 | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.off('customDataChange');
```

## getAVPlaybackStateSync10+

PhonePC/2in1TabletTVWearable

getAVPlaybackStateSync(): AVPlaybackState;

使用同步方法获取当前会话的播放状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>) | 当前会话的播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let playbackState: avSession.AVPlaybackState = avcontroller.getAVPlaybackStateSync();
```

## getAVMetadataSync10+

PhonePC/2in1TabletTVWearable

getAVMetadataSync(): AVMetadata

使用同步方法获取会话元数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>) | 会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let metaData: avSession.AVMetadata = avcontroller.getAVMetadataSync();
```

## getAVCallState11+

PhonePC/2in1TabletTVWearable

getAVCallState(): Promise<AVCallState>

获取通话状态数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVCallState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcallstate11>)> | Promise对象，返回通话状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVCallState().then((callstate: avSession.AVCallState) => {
2. console.info(`Succeeded in getting AV call state: ${callstate.state}`);
3. });
```

## getAVCallState11+

PhonePC/2in1TabletTVWearable

getAVCallState(callback: AsyncCallback<AVCallState>): void

获取通话状态数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVCallState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcallstate11>)> | 是 | 回调函数，返回通话状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getAVCallState((err: BusinessError, callstate: avSession.AVCallState) => {
2. console.info(`Succeeded in getting AV call state: ${callstate.state}`);
3. });
```

## getCallMetadata11+

PhonePC/2in1TabletTVWearable

getCallMetadata(): Promise<CallMetadata>

获取通话会话的元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CallMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#callmetadata11>)> | Promise对象，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getCallMetadata().then((calldata: avSession.CallMetadata) => {
2. console.info(`Succeeded in getting call metadata, name: ${calldata.name}`);
3. });
```

## getCallMetadata11+

PhonePC/2in1TabletTVWearable

getCallMetadata(callback: AsyncCallback<CallMetadata>): void

获取通话会话的元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[CallMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#callmetadata11>)> | 是 | 回调函数，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avcontroller.getCallMetadata((calldata: avSession.CallMetadata) => {
2. console.info(`Succeeded in getting call metadata, name: ${calldata.name}`);
3. });
```

## getAVQueueTitleSync10+

PhonePC/2in1TabletTVWearable

getAVQueueTitleSync(): string

使用同步方法获取当前会话播放列表的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前会话播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let currentQueueTitle: string = avcontroller.getAVQueueTitleSync();
```

## getAVQueueItemsSync10+

PhonePC/2in1TabletTVWearable

getAVQueueItemsSync(): Array<AVQueueItem>

使用同步方法获取当前会话播放列表相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)> | 当前会话播放列表队列。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let currentQueueItems: Array<avSession.AVQueueItem> = avcontroller.getAVQueueItemsSync();
```

## getOutputDeviceSync10+

PhonePC/2in1TabletTVWearable

getOutputDeviceSync(): OutputDeviceInfo

使用同步方法获取当前输出设备信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>) | 当前输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let currentOutputDevice: avSession.OutputDeviceInfo = avcontroller.getOutputDeviceSync();
```

## isActiveSync10+

PhonePC/2in1TabletTVWearable

isActiveSync(): boolean

使用同步方法判断会话是否被激活。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 会话是否为激活状态，true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let isActive: boolean = avcontroller.isActiveSync();
```

## getValidCommandsSync10+

PhonePC/2in1TabletTVWearable

getValidCommandsSync(): Array<AVControlCommandType>

使用同步方法获取会话支持的有效命令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[AVControlCommandType](../Types/arkts-apis-avsession-t.md#avcontrolcommandtype10)> | 会话支持的有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. let validCommands: Array<avSession.AVControlCommandType> = avcontroller.getValidCommandsSync();
```
