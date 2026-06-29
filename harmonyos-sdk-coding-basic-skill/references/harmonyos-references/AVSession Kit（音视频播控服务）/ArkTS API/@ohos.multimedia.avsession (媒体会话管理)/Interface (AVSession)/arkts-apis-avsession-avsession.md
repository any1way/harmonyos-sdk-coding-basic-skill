---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession
title: Interface (AVSession)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Interface (AVSession)
category: harmonyos-references
scraped_at: 2026-06-01T16:19:02+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:c1fff7660fcc2eb618559704d245812c559a2354b4a62c80680c64b1bb1c0630
---
调用[avSession.createAVSession](../Functions/arkts-apis-avsession-f.md#avsessioncreateavsession10)后，返回会话的实例，可以获得会话ID，完成设置元数据，播放状态信息等操作。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 10开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { avSession } from '@kit.AVSessionKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId10+ | string | 是 | 否 | AVSession对象唯一的会话标识。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sessionType10+ | [AVSessionType](../Types/arkts-apis-avsession-t.md#avsessiontype10) | 是 | 否 | AVSession会话类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sessionTag22+ | string | 是 | 否 | AVSession会话的自定义标签信息。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let sessionId: string = currentAVSession.sessionId;
2. let sessionType: avSession.AVSessionType = currentAVSession.sessionType;
```

## setAVMetadata10+

PhonePC/2in1TabletTVWearable

setAVMetadata(data: AVMetadata): Promise<void>

设置会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>) | 是 | 会话元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let metadata: avSession.AVMetadata = {
2. assetId: "121278",
3. title: "lose yourself",
4. artist: "Eminem",
5. author: "ST",
6. album: "Slim shady",
7. writer: "ST",
8. composer: "ST",
9. duration: 2222,
10. mediaImage: "https://www.example.com/example.jpg",
11. subtitle: "8 Mile",
12. description: "Rap",
13. // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
14. // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
15. lyric: "lrc格式歌词内容",
16. // singleLyricText字段存储单条歌词文本，不包含时间戳。
17. // 例如："单条歌词内容"。
18. singleLyricText: "单条歌词内容",
19. previousAssetId: "121277",
20. nextAssetId: "121279"
21. };
22. currentAVSession.setAVMetadata(metadata).then(() => {
23. console.info('Succeeded in setting AVMetadata.');
24. });
```

## setAVMetadata10+

PhonePC/2in1TabletTVWearable

setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void

设置会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [AVMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#avmetadata10>) | 是 | 会话元数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let metadata: avSession.AVMetadata = {
4. assetId: "121278",
5. title: "lose yourself",
6. artist: "Eminem",
7. author: "ST",
8. album: "Slim shady",
9. writer: "ST",
10. composer: "ST",
11. duration: 2222,
12. mediaImage: "https://www.example.com/example.jpg",
13. subtitle: "8 Mile",
14. description: "Rap",
15. // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
16. // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
17. lyric: "lrc格式歌词内容",
18. // singleLyricText字段存储单条歌词文本，不包含时间戳。
19. // 例如："单条歌词内容"。
20. singleLyricText: "单条歌词内容",
21. previousAssetId: "121277",
22. nextAssetId: "121279"
23. };
24. currentAVSession.setAVMetadata(metadata, (err: BusinessError) => {
25. if (err) {
26. console.error(`Failed to set AVMetadata, code: ${err.code}, message: ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in setting AVMetadata.');
30. });
```

## setCallMetadata11+

PhonePC/2in1TabletTVWearable

setCallMetadata(data: CallMetadata): Promise<void>

设置通话会话元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#callmetadata11>) | 是 | 通话会话元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. // Index.ets
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import { avSession } from '@kit.AVSessionKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. @Entry
8. @Component
9. struct Index {
10. build() {
11. Column() {
12. Text('Hello World')
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }

21. class CallManager {
22. private currentAVSession: avSession.AVSession | null = null;

24. async setCallMetadata() {
25. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
26. let imageSource = await image.createImageSource(value.buffer);
27. let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
28. let calldata: avSession.CallMetadata = {
29. name: "xiaoming",
30. phoneNumber: "111xxxxxxxx",
31. avatar: imagePixel
32. };
33. this.currentAVSession?.setCallMetadata(calldata, (err: BusinessError) => {
34. if (err) {
35. console.error(`Failed to set call metadata, code: ${err.code}, message: ${err.message}`);
36. return;
37. }
38. console.info('Succeeded in setting call metadata.');
39. });
40. }
41. }
```

## setCallMetadata11+

PhonePC/2in1TabletTVWearable

setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void

设置通话会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](<../Interfaces (其他)/arkts-apis-avsession-i.md#callmetadata11>) | 是 | 通话会话元数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. // Index.ets
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import { avSession } from '@kit.AVSessionKit';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. Column() {
11. Text('Hello World')
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. }
15. .width('100%')
16. .height('100%')
17. }
18. }

20. class CallManager {
21. private currentAVSession: avSession.AVSession | null = null;

23. async setCallMetadata() {
24. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
25. let imageSource = await image.createImageSource(value.buffer);
26. let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
27. let calldata: avSession.CallMetadata = {
28. name: "xiaoming",
29. phoneNumber: "111xxxxxxxx",
30. avatar: imagePixel
31. };
32. this.currentAVSession?.setCallMetadata(calldata, (err: BusinessError) => {
33. if (err) {
34. console.error(`Failed to set call metadata, code: ${err.code}, message: ${err.message}`);
35. return;
36. }
37. console.info('Succeeded in setting call metadata.');
38. });
39. }
40. }
```

## setAVCallState11+

PhonePC/2in1TabletTVWearable

setAVCallState(state: AVCallState): Promise<void>

设置通话状态。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcallstate11>) | 是 | 通话状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let calldata: avSession.AVCallState = {
2. state: avSession.CallState.CALL_STATE_ACTIVE,
3. muted: false
4. };
5. currentAVSession.setAVCallState(calldata).then(() => {
6. console.info('Succeeded in setting AVCallState.');
7. });
```

## setAVCallState11+

PhonePC/2in1TabletTVWearable

setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void

设置通话状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avcallstate11>) | 是 | 通话状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avcalldata: avSession.AVCallState = {
4. state: avSession.CallState.CALL_STATE_ACTIVE,
5. muted: false
6. };
7. currentAVSession.setAVCallState(avcalldata, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to set AVCallState, code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info('Succeeded in setting AVCallState.');
13. });
```

## setAVPlaybackState10+

PhonePC/2in1TabletTVWearable

setAVPlaybackState(state: AVPlaybackState): Promise<void>

设置会话播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放状态设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let playbackState: avSession.AVPlaybackState = {
2. state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
3. speed: 1.0,
4. position:{elapsedTime:10, updateTime:(new Date()).getTime()},
5. bufferedTime:1000,
6. loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
7. isFavorite:true
8. };
9. currentAVSession.setAVPlaybackState(playbackState).then(() => {
10. console.info('Succeeded in setting AVPlaybackState.');
11. });
```

## setAVPlaybackState10+

PhonePC/2in1TabletTVWearable

setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void

设置会话播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](<../Interfaces (其他)/arkts-apis-avsession-i.md#avplaybackstate10>) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let PlaybackState: avSession.AVPlaybackState = {
4. state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
5. speed: 1.0,
6. position:{elapsedTime:10, updateTime:(new Date()).getTime()},
7. bufferedTime:1000,
8. loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
9. isFavorite:true
10. };
11. currentAVSession.setAVPlaybackState(PlaybackState, (err: BusinessError) => {
12. if (err) {
13. console.error(`Failed to set AVPlaybackState, code: ${err.code}, message: ${err.message}`);
14. return;
15. }
16. console.info('Succeeded in setting AVPlaybackState.');
17. });
```

## setLaunchAbility10+

PhonePC/2in1TabletTVWearable

setLaunchAbility(ability: WantAgent): Promise<void>

设置一个WantAgent用于拉起会话的Ability。结果通过Promise异步回调方式返回。

通过点击播控组件可以跳转到对应的播放界面，默认跳转到[avSession.createAVSession](../Functions/arkts-apis-avsession-f.md#avsessioncreateavsession10)接口传入的context所属的UIAbility界面。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md>) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当Ability设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { wantAgent } from '@kit.AbilityKit';

3. // WantAgentInfo对象。
4. let wantAgentInfo: wantAgent.WantAgentInfo = {
5. wants: [
6. {
7. deviceId: "deviceId",
8. bundleName: "com.example.myapplication",
9. abilityName: "EntryAbility",
10. action: "action1",
11. entities: ["entity1"],
12. type: "MIMETYPE",
13. uri: "key = {true,true,false}",
14. parameters:
15. {
16. mykey0: 2222,
17. mykey1: [1, 2, 3],
18. mykey2: "[1, 2, 3]",
19. mykey3: "ssssssssssssssssssssssssss",
20. mykey4: [false, true, false],
21. mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
22. mykey6: true
23. }
24. }
25. ],
26. operationType: wantAgent.OperationType.START_ABILITIES,
27. requestCode: 0,
28. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
29. }

31. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
32. currentAVSession.setLaunchAbility(agent).then(() => {
33. console.info('Succeeded in setting launch ability.');
34. });
35. });
```

## setLaunchAbility10+

PhonePC/2in1TabletTVWearable

setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void

设置一个WantAgent用于拉起会话的Ability。结果通过callback异步回调方式返回。

通过点击播控组件可以跳转到对应的播放界面，默认跳转到[avSession.createAVSession](../Functions/arkts-apis-avsession-f.md#avsessioncreateavsession10)接口传入的context所属的UIAbility界面。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md>) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当Ability设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { wantAgent } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // WantAgentInfo对象。
5. let wantAgentInfo: wantAgent.WantAgentInfo = {
6. wants: [
7. {
8. deviceId: "deviceId",
9. bundleName: "com.example.myapplication",
10. abilityName: "EntryAbility",
11. action: "action1",
12. entities: ["entity1"],
13. type: "MIMETYPE",
14. uri: "key = {true,true,false}",
15. parameters:
16. {
17. mykey0: 2222,
18. mykey1: [1, 2, 3],
19. mykey2: "[1, 2, 3]",
20. mykey3: "ssssssssssssssssssssssssss",
21. mykey4: [false, true, false],
22. mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
23. mykey6: true
24. }
25. }
26. ],
27. operationType: wantAgent.OperationType.START_ABILITIES,
28. requestCode: 0,
29. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
30. }

32. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
33. currentAVSession.setLaunchAbility(agent, (err: BusinessError) => {
34. if (err) {
35. console.error(`Failed to set launch ability, code: ${err.code}, message: ${err.message}`);
36. return;
37. }
38. console.info('Succeeded in setting launch ability.');
39. });
40. });
```

## dispatchSessionEvent10+

PhonePC/2in1TabletTVWearable

dispatchSessionEvent(event: string, args: {[key: string]: Object}): Promise<void>

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |

说明

参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当事件设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let eventName = "dynamic_lyric";
2. currentAVSession.dispatchSessionEvent(eventName, {lyric : "This is lyric"}).then(() => {
3. console.info('Succeeded in dispatching session event.');
4. });
```

## dispatchSessionEvent10+

PhonePC/2in1TabletTVWearable

dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当会话事件设置成功，err为undefined，否则返回错误对象。 |

说明

参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let eventName: string = "dynamic_lyric";
4. currentAVSession.dispatchSessionEvent(eventName, {lyric : "This is lyric"}, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to dispatch session event, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in dispatching session event.');
10. });
```

## setAVQueueItems10+

PhonePC/2in1TabletTVWearable

setAVQueueItems(items: Array<AVQueueItem>): Promise<void>

设置媒体播放列表。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)> | 是 | 播放列表单项的队列，用以表示播放列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. // Index.ets
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
6. let imageSource = await image.createImageSource(value.buffer);
7. let imagePixel = await imageSource.createPixelMap({desiredSize:{width: 150, height: 150}});
8. let queueItemDescription_1: avSession.AVMediaDescription = {
9. assetId: '001',
10. title: 'music_name',
11. subtitle: 'music_sub_name',
12. description: 'music_description',
13. mediaImage : imagePixel,
14. extras: {extras:'any'}
15. };
16. let queueItem_1: avSession.AVQueueItem = {
17. itemId: 1,
18. description: queueItemDescription_1
19. } as avSession.AVQueueItem;
20. let queueItemDescription_2: avSession.AVMediaDescription = {
21. assetId: '002',
22. title: 'music_name',
23. subtitle: 'music_sub_name',
24. description: 'music_description',
25. mediaImage: imagePixel,
26. extras: {extras:'any'}
27. };
28. let queueItem_2: avSession.AVQueueItem = {
29. itemId: 2,
30. description: queueItemDescription_2
31. } as avSession.AVQueueItem;
32. let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
33. currentAVSession.setAVQueueItems(queueItemsArray).then(() => {
34. console.info('Succeeded in setting AVQueueItems.');
35. });
```

## setAVQueueItems10+

PhonePC/2in1TabletTVWearable

setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void

设置媒体播放列表。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array<[AVQueueItem](<../Interfaces (其他)/arkts-apis-avsession-i.md#avqueueitem10>)> | 是 | 播放列表单项的队列，用以表示播放列表。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. // Index.ets
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
7. let imageSource = await image.createImageSource(value.buffer);
8. let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
9. let queueItemDescription_1: avSession.AVMediaDescription = {
10. assetId: '001',
11. title: 'music_name',
12. subtitle: 'music_sub_name',
13. description: 'music_description',
14. mediaImage: imagePixel,
15. extras: { extras: 'any' }
16. };
17. let queueItem_1: avSession.AVQueueItem = {
18. itemId: 1,
19. description: queueItemDescription_1
20. };
21. let queueItemDescription_2: avSession.AVMediaDescription = {
22. assetId: '002',
23. title: 'music_name',
24. subtitle: 'music_sub_name',
25. description: 'music_description',
26. mediaImage: imagePixel,
27. extras: { extras: 'any' }
28. };
29. let queueItem_2: avSession.AVQueueItem = {
30. itemId: 2,
31. description: queueItemDescription_2
32. };
33. let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
34. currentAVSession.setAVQueueItems(queueItemsArray, (err: BusinessError) => {
35. if (err) {
36. console.error(`Failed to set AVQueueItems, code: ${err.code}, message: ${err.message}`);
37. return;
38. }
39. console.info('Succeeded in setting AVQueueItems.');
40. });
```

## setAVQueueTitle10+

PhonePC/2in1TabletTVWearable

setAVQueueTitle(title: string): Promise<void>

设置媒体播放列表名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let queueTitle = 'QUEUE_TITLE';
2. currentAVSession.setAVQueueTitle(queueTitle).then(() => {
3. console.info('Succeeded in setting AVQueueTitle.');
4. });
```

## setAVQueueTitle10+

PhonePC/2in1TabletTVWearable

setAVQueueTitle(title: string, callback: AsyncCallback<void>): void

设置媒体播放列表名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表名称字段。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let queueTitle = 'QUEUE_TITLE';
4. currentAVSession.setAVQueueTitle(queueTitle, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to set AVQueueTitle, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in setting AVQueueTitle.');
10. });
```

## setExtras10+

PhonePC/2in1TabletTVWearable

setExtras(extras: {[key: string]: Object}): Promise<void>

媒体提供方设置键值对形式的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。  **说明：** 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.setExtras({extras : "This is custom media packet"}).then(() => {
2. console.info('Succeeded in setting extras.');
3. });
```

## setExtras10+

PhonePC/2in1TabletTVWearable

setExtras(extras:{[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置键值对形式的自定义媒体数据包，使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。  **说明：** 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want (Want)](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当自定义媒体数据包设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. currentAVSession.setExtras({extras : "This is custom media packet"}, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set extras, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in setting extras.');
9. })
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

**示例：**

```
1. currentAVSession.sendCustomData({customData : "This is custom data"}).then(() => {
2. console.info('Succeeded in sending custom data.');
3. });
```

## enableDesktopLyric23+

PhonePC/2in1TabletTVWearable

enableDesktopLyric(enable: boolean): Promise<void>

当前会话是否启用桌面歌词功能。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用桌面歌词。true表示启用，false表示不启用。 |

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
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).enableDesktopLyric(true).then(() => {
3. console.info('Succeeded in enabling desktop lyric.');
4. })
5. }
```

## setDesktopLyricVisible23+

PhonePC/2in1TabletTVWearable

setDesktopLyricVisible(visible: boolean): Promise<void>

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. currentAVSession.setDesktopLyricVisible(true).then(() => {
2. console.info('Succeeded in setting desktop lyric visible.');
3. });
```

## isDesktopLyricVisible23+

PhonePC/2in1TabletTVWearable

isDesktopLyricVisible(): Promise<boolean>

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).isDesktopLyricVisible().then((visible: boolean) => {
3. console.info(`isDesktopLyricVisible: ${visible}`);
4. })
5. }
```

## onDesktopLyricVisibilityChanged23+

PhonePC/2in1TabletTVWearable

onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示开启显示桌面歌词状态；返回false表示关闭显示桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).onDesktopLyricVisibilityChanged((visible: boolean) => {
3. console.info(`desktop lyric visible state: ${visible}`);
4. });
5. }
```

## offDesktopLyricVisibilityChanged23+

PhonePC/2in1TabletTVWearable

offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有显示桌面歌词状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).offDesktopLyricVisibilityChanged();
3. }
```

## setDesktopLyricState23+

PhonePC/2in1TabletTVWearable

setDesktopLyricState(state: DesktopLyricState): Promise<void>

设置当前会话桌面歌词状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. let state: avSession.DesktopLyricState = {
2. isLocked: true,
3. };
4. currentAVSession.setDesktopLyricState(state).then(() => {
5. console.info('Succeeded in setting desktop lyric state.');
6. })
```

## getDesktopLyricState23+

PhonePC/2in1TabletTVWearable

getDesktopLyricState(): Promise<DesktopLyricState>

获取当前会话桌面歌词状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).getDesktopLyricState()
3. .then((state: avSession.DesktopLyricState) => {
4. console.info(`getDesktopLyricState: ${state.isLocked}`);
5. })
6. }
```

## onDesktopLyricStateChanged23+

PhonePC/2in1TabletTVWearable

onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void

桌面歌词状态变更的监听事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DesktopLyricState](<../Interfaces (其他)/arkts-apis-avsession-i.md#desktoplyricstate23>)> | 是 | 回调函数。返回桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
3. console.info(`desktop lyric isLocked : ${state.isLocked}`);
4. })
5. }
```

## offDesktopLyricStateChanged23+

PhonePC/2in1TabletTVWearable

offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DesktopLyricState](<../Interfaces (其他)/arkts-apis-avsession-i.md#desktoplyricstate23>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. if (currentAVSession !== undefined) {
2. (currentAVSession as avSession.AVSession).offDesktopLyricStateChanged();
3. }
```

## setBackgroundPlayMode24+

PhonePC/2in1TabletTVWearable

setBackgroundPlayMode(mode: BackgroundPlayMode): Promise<void>

设置后台播放模式。使用promise异步回调。

建议与应用内"是否支持后台播放开关"关联。如未设置，'audio'类型会话默认值为ENABLE\_BACKGROUND\_PLAY；'video'类型会话默认值为DISABLE\_BACKGROUND\_PLAY。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BackgroundPlayMode](../Enums/arkts-apis-avsession-e.md#backgroundplaymode24) | 是 | 后台播放模式。 |

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

**示例：**

```
1. try {
2. currentAVSession.setBackgroundPlayMode(avSession.BackgroundPlayMode.ENABLE_BACKGROUND_PLAY);
3. } catch (err) {
4. console.error(`setBackgroundPlayMode BusinessError: code: ${err.code}, message: ${err.message}`);
5. }
```

## getController10+

PhonePC/2in1TabletTVWearable

getController(): Promise<AVSessionController>

获取本会话对应的控制器。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVSessionController](<../Interface (AVSessionController)/arkts-apis-avsession-avsessioncontroller.md>)> | Promise对象。返回会话控制器。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.getController().then((avcontroller: avSession.AVSessionController) => {
2. console.info(`Succeeded in getting controller, sessionid: ${avcontroller.sessionId}`);
3. });
```

## getController10+

PhonePC/2in1TabletTVWearable

getController(callback: AsyncCallback<AVSessionController>): void

获取本会话相应的控制器。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVSessionController](<../Interface (AVSessionController)/arkts-apis-avsession-avsessioncontroller.md>)> | 是 | 回调函数。返回会话控制器。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.getController((err: BusinessError, avcontroller: avSession.AVSessionController) => {
2. if (err) {
3. console.error(`Failed to get controller, code: ${err.code}, message: ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting controller, sessionid: ${avcontroller.sessionId}`);
7. });
```

## getAVCastController10+

PhonePC/2in1TabletTV

getAVCastController(): Promise<AVCastController>

设备建立连接后，获取投播控制器。结果通过Promise异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVCastController](<../Interface (AVCastController)/arkts-apis-avsession-avcastcontroller.md>)> | Promise对象。返回投播控制器实例。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. let avCastController: avSession.AVCastController;
2. currentAVSession.getAVCastController().then((avcontroller: avSession.AVCastController) => {
3. avCastController = avcontroller;
4. console.info('Succeeded in getting AV cast controller.');
5. });
```

## getAVCastController10+

PhonePC/2in1TabletTV

getAVCastController(callback: AsyncCallback<AVCastController>): void

设备建立连接后，获取投播控制器。结果通过callback异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVCastController](<../Interface (AVCastController)/arkts-apis-avsession-avcastcontroller.md>)> | 是 | 回调函数，返回投播控制器实例。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avCastController: avSession.AVCastController;
4. currentAVSession.getAVCastController((err: BusinessError, avcontroller: avSession.AVCastController) => {
5. if (err) {
6. console.error(`Failed to get AV cast controller, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. avCastController = avcontroller;
10. console.info('Succeeded in getting AV cast controller.');
11. });
```

## getOutputDevice10+

PhonePC/2in1TabletTVWearable

getOutputDevice(): Promise<OutputDeviceInfo>

通过会话获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)> | Promise对象。返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
2. console.info(`Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`);
3. })
```

## getOutputDevice10+

PhonePC/2in1TabletTVWearable

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

通过会话获取播放设备相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)> | 是 | 回调函数，返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. currentAVSession.getOutputDevice((err: BusinessError, outputDeviceInfo: avSession.OutputDeviceInfo) => {
4. if (err) {
5. console.error(`Failed to get output device, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`);
9. });
```

## activate10+

PhonePC/2in1TabletTVWearable

activate(): Promise<void>

激活会话，激活后可正常使用会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当会话激活成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.activate().then(() => {
2. console.info('Succeeded in activating.');
3. });
```

## activate10+

PhonePC/2in1TabletTVWearable

activate(callback: AsyncCallback<void>): void

激活会话，激活后可正常使用会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当会话激活成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. currentAVSession.activate((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to activate, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in activating.');
9. });
```

## deactivate10+

PhonePC/2in1TabletTVWearable

deactivate(): Promise<void>

禁用当前会话的功能，可通过[activate](arkts-apis-avsession-avsession.md#activate10)恢复。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当禁用会话成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.deactivate().then(() => {
2. console.info('Succeeded in deactivating.');
3. });
```

## deactivate10+

PhonePC/2in1TabletTVWearable

deactivate(callback: AsyncCallback<void>): void

禁用当前会话。结果通过callback异步回调方式返回。

禁用当前会话的功能，可通过[activate](arkts-apis-avsession-avsession.md#activate10)恢复。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当禁用会话成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. currentAVSession.deactivate((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to deactivate, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in deactivating.');
9. });
```

## destroy10+

PhonePC/2in1TabletTVWearable

destroy(): Promise<void>

销毁当前会话，使当前会话完全失效。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当会话销毁成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.destroy().then(() => {
2. console.info('Succeeded in destroying.');
3. });
```

## destroy10+

PhonePC/2in1TabletTVWearable

destroy(callback: AsyncCallback<void>): void

销毁当前会话，使当前会话完全失效。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当会话销毁成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. currentAVSession.destroy((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to destroy, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in destroying.');
9. });
```

## on('play')10+

PhonePC/2in1TabletTVWearable

on(type: 'play', callback: () => void): void

设置播放命令监听事件。注册该监听，说明应用支持播放指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'play'，当播放命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('play', () => {
2. console.info('on play entry');
3. });
```

## onPlay22+

PhonePC/2in1TabletTVWearable

onPlay(callback: Callback<CommandInfo>): void

设置播放命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onPlay((info: avSession.CommandInfo) => {
2. console.info('on play entry');
3. });
```

## on('pause')10+

PhonePC/2in1TabletTVWearable

on(type: 'pause', callback: () => void): void

设置暂停命令监听事件。注册该监听，说明应用支持暂停指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pause'，当暂停命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('pause', () => {
2. console.info('on pause entry');
3. });
```

## on('stop')10+

PhonePC/2in1TabletTVWearable

on(type:'stop', callback: () => void): void

设置停止命令监听事件。注册该监听，说明应用支持停止指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'stop'，当停止命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('stop', () => {
2. console.info('on stop entry');
3. });
```

## on('playNext')10+

PhonePC/2in1TabletTVWearable

on(type:'playNext', callback: () => void): void

设置播放下一首命令监听事件。注册该监听，说明应用支持下一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playNext'，当播放下一首命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('playNext', () => {
2. console.info('on playNext entry');
3. });
```

## onPlayNext22+

PhonePC/2in1TabletTVWearable

onPlayNext(callback: Callback<CommandInfo>): void

设置播放下一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onPlayNext((info: avSession.CommandInfo) => {
2. console.info('on playNext entry');
3. });
```

## on('playPrevious')10+

PhonePC/2in1TabletTVWearable

on(type:'playPrevious', callback: () => void): void

设置播放上一首命令监听事件。注册该监听，说明应用支持上一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playPrevious'，当播放上一首命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('playPrevious', () => {
2. console.info('on playPrevious entry');
3. });
```

## onPlayPrevious22+

PhonePC/2in1TabletTVWearable

onPlayPrevious(callback: Callback<CommandInfo>): void

设置播放上一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onPlayPrevious((info: avSession.CommandInfo) => {
2. console.info('on playPrevious entry');
3. });
```

## on('fastForward')10+

PhonePC/2in1TabletTVWearable

on(type: 'fastForward', callback: (time?: number) => void): void

设置快进命令监听事件。注册该监听，说明应用支持快进指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是 'fastForward'，当快进命令被发送到会话时，触发该事件回调。 |
| callback | (time?: number) => void | 是 | 回调函数。参数time是时间节点，单位为秒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('fastForward', (time?: number) => {
2. console.info('on fastForward entry');
3. });
```

## onFastForward22+

PhonePC/2in1TabletTVWearable

onFastForward(callback: TwoParamCallback<number, CommandInfo>): void

设置快进命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快进时间参数，以及对应的[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 是 | 回调函数。用于处理'fastForward'操作。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onFastForward((time: number, info: avSession.CommandInfo) => {
2. console.info('on fastForward entry');
3. });
```

## on('rewind')10+

PhonePC/2in1TabletTVWearable

on(type:'rewind', callback: (time?: number) => void): void

设置快退命令监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'rewind'，当快退命令被发送到会话时，触发该事件回调。 |
| callback | (time?: number) => void | 是 | 回调函数。参数time是时间节点，单位为秒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('rewind', (time?: number) => {
2. console.info('on rewind entry');
3. });
```

## onRewind22+

PhonePC/2in1TabletTVWearable

onRewind(callback: TwoParamCallback<number, CommandInfo>): void

设置快退命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快退时间参数，以及对应的[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 是 | 回调函数。用于处理'rewind'操作。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onRewind((time: number, info: avSession.CommandInfo) => {
2. console.info('on rewind entry');
3. });
```

## on('playWithAssetId')20+

PhonePC/2in1TabletTVWearable

on(type:'playWithAssetId', callback: Callback<string>): void

设置指定资源id进行播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playWithAssetId'，当指定资源id进行播放时，触发该事件回调。 |
| callback | Callback<string> | 是 | 回调函数。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let playWithAssetIdCallback = (assetId: string) => {
2. console.info(`on playWithAssetId entry,  assetId = ${assetId}`);
3. }
4. currentAVSession.on('playWithAssetId', playWithAssetIdCallback);
```

## off('playWithAssetId')20+

PhonePC/2in1TabletTVWearable

off(type: 'playWithAssetId', callback?: Callback<string>): void

取消指定资源id进行播放的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playWithAssetId'。 |
| callback | Callback<string> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playWithAssetId');
```

## on('seek')10+

PhonePC/2in1TabletTVWearable

on(type: 'seek', callback: (time: number) => void): void

设置跳转节点监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'seek'：当跳转节点命令被发送到会话时，触发该事件。 |
| callback | (time: number) => void | 是 | 回调函数。参数time是时间节点，单位为毫秒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('seek', (time: number) => {
2. console.info(`on seek entry time : ${time}`);
3. });
```

## on('setSpeed')10+

PhonePC/2in1TabletTVWearable

on(type: 'setSpeed', callback: (speed: number) => void): void

设置播放速率的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setSpeed'：当设置播放速率的命令被发送到会话时，触发该事件。 |
| callback | (speed: number) => void | 是 | 回调函数。参数speed是播放倍速。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('setSpeed', (speed: number) => {
2. console.info(`on setSpeed speed : ${speed}`);
3. });
```

## on('setLoopMode')10+

PhonePC/2in1TabletTVWearable

on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void

设置循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setLoopMode'：当设置循环模式的命令被发送到会话时，触发该事件。 |
| callback | (mode: [LoopMode](../Enums/arkts-apis-avsession-e.md#loopmode10)) => void | 是 | 回调函数。参数mode是循环模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('setLoopMode', (mode: avSession.LoopMode) => {
2. console.info(`on setLoopMode mode : ${mode}`);
3. });
```

## on('setTargetLoopMode')18+

PhonePC/2in1TabletTVWearable

on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void

设置目标循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setTargetLoopMode'。  - 'setTargetLoopMode'：当设置目标循环模式的命令被发送到会话时，触发该事件。 |
| callback | Callback<[LoopMode](../Enums/arkts-apis-avsession-e.md#loopmode10)> | 是 | 回调函数。参数表示目标循环模式。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('setTargetLoopMode', (mode: avSession.LoopMode) => {
2. console.info(`on setTargetLoopMode mode : ${mode}`);
3. });
```

## on('toggleFavorite')10+

PhonePC/2in1TabletTVWearable

on(type: 'toggleFavorite', callback: (assetId: string) => void): void

设置是否收藏的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'toggleFavorite'：当是否收藏的命令被发送到会话时，触发该事件。 |
| callback | (assetId: string) => void | 是 | 回调函数。参数assetId是媒体ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('toggleFavorite', (assetId: string) => {
2. console.info(`on toggleFavorite mode : ${assetId}`);
3. });
```

## on('skipToQueueItem')10+

PhonePC/2in1TabletTVWearable

on(type: 'skipToQueueItem', callback: (itemId: number) => void): void

设置播放列表其中某项被选中的监听事件，session端可以选择对这个单项歌曲进行播放。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'skipToQueueItem'：当播放列表选中单项的命令被发送到会话时，触发该事件。 |
| callback | (itemId: number) => void | 是 | 回调函数。参数itemId是选中的播放列表项的ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('skipToQueueItem', (itemId: number) => {
2. console.info(`on skipToQueueItem id : ${itemId}`);
3. });
```

## on('handleKeyEvent')10+

PhonePC/2in1TabletTVWearable

on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void

设置蓝牙/有线等外设接入的按键输入事件的监听，监听多媒体按键事件中播放、暂停、上下一首、快进、快退的指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'handleKeyEvent'：当按键事件被发送到会话时，触发该事件。 |
| callback | (event: [KeyEvent](<../../../../基础功能/Input Kit（多模输入服务）/ArkTS API/@ohos.multimodalInput.keyEvent (按键输入事件)/js-apis-keyevent.md>)) => void | 是 | 回调函数。参数event是按键事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { KeyEvent } from '@kit.InputKit';

3. currentAVSession.on('handleKeyEvent', (event: KeyEvent) => {
4. console.info(`on handleKeyEvent event : ${event}`);
5. });
```

## on('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。应用接入[multimedia.avCastPicker (投播组件)](<../../../ArkTS组件/@ohos.multimedia.avCastPicker (投播组件)/ohos-multimedia-avcastpicker.md>)，当用户通过组件切换设备时，会收到设备切换的回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'outputDeviceChange'：当播放设备变化时，触发该事件。 |
| callback | (state: [ConnectionState](../Enums/arkts-apis-avsession-e.md#connectionstate10), device: [OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)) => void | 是 | 回调函数，参数device是设备相关信息。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
2. console.info(`on outputDeviceChange device : ${device}`);
3. });
```

## on('commonCommand')10+

PhonePC/2in1TabletTVWearable

on(type: 'commonCommand', callback: (command :string, args:{[key: string]: Object}) => void): void

设置自定义控制命令变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'commonCommand'：当自定义控制命令变化时，触发该事件。 |
| callback | (command :string, args:{[key: string]: Object}) => void | 是 | 回调函数，command为变化的自定义控制命令名，args为自定义控制命令的参数，参数内容与[sendCommonCommand](<../Interface (AVSessionController)/arkts-apis-avsession-avsessioncontroller.md#sendcommoncommand10>)方法设置的参数内容完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('commonCommand', (commonCommand, args) => {
2. console.info(`OnCommonCommand, the command is ${commonCommand}, args: ${JSON.stringify(args)}`);
3. });
```

## off('play')10+

PhonePC/2in1TabletTVWearable

off(type: 'play', callback?: () => void): void

取消会话播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'play'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('play');
```

## offPlay22+

PhonePC/2in1TabletTVWearable

offPlay(callback?: Callback<CommandInfo>): void

取消会话播放事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offPlay();
```

## off('pause')10+

PhonePC/2in1TabletTVWearable

off(type: 'pause', callback?: () => void): void

取消会话暂停事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'pause'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('pause');
```

## off('stop')10+

PhonePC/2in1TabletTVWearable

off(type: 'stop', callback?: () => void): void

取消会话停止事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'stop'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('stop');
```

## off('playNext')10+

PhonePC/2in1TabletTVWearable

off(type: 'playNext', callback?: () => void): void

取消会话播放下一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是 'playNext'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playNext');
```

## offPlayNext22+

PhonePC/2in1TabletTVWearable

offPlayNext(callback?: Callback<CommandInfo>): void

取消会话播放下一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offPlayNext();
```

## off('playPrevious')10+

PhonePC/2in1TabletTVWearable

off(type: 'playPrevious', callback?: () => void): void

取消会话播放上一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playPrevious'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playPrevious');
```

## offPlayPrevious22+

PhonePC/2in1TabletTVWearable

offPlayPrevious(callback?: Callback<CommandInfo>): void

取消会话播放上一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offPlayPrevious();
```

## off('fastForward')10+

PhonePC/2in1TabletTVWearable

off(type: 'fastForward', callback?: () => void): void

取消会话快进事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'fastForward'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('fastForward');
```

## offFastForward22+

PhonePC/2in1TabletTVWearable

offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快进事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offFastForward();
```

## off('rewind')10+

PhonePC/2in1TabletTVWearable

off(type: 'rewind', callback?: () => void): void

取消会话快退事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'rewind'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('rewind');
```

## offRewind22+

PhonePC/2in1TabletTVWearable

offRewind(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快退事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#commandinfo22>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offRewind();
```

## off('seek')10+

PhonePC/2in1TabletTVWearable

off(type: 'seek', callback?: (time: number) => void): void

取消跳转节点事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'seek'。 |
| callback | (time: number) => void | 否 | 回调函数，参数time是时间节点，单位为毫秒。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('seek');
```

## off('setSpeed')10+

PhonePC/2in1TabletTVWearable

off(type: 'setSpeed', callback?: (speed: number) => void): void

取消播放速率变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setSpeed'。 |
| callback | (speed: number) => void | 否 | 回调函数，参数speed是播放倍速。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('setSpeed');
```

## off('setLoopMode')10+

PhonePC/2in1TabletTVWearable

off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void

取消循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setLoopMode'。 |
| callback | (mode: [LoopMode](../Enums/arkts-apis-avsession-e.md#loopmode10)) => void | 否 | 回调函数，参数mode是循环模式。  - 当监听事件取消成功，err为undefined，否则返回错误对象。  - 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('setLoopMode');
```

## off('setTargetLoopMode')18+

PhonePC/2in1TabletTVWearable

off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void

取消目标循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setTargetLoopMode'。 |
| callback | Callback<[LoopMode](../Enums/arkts-apis-avsession-e.md#loopmode10)> | 否 | 回调函数，参数表示目标循环模式。  - 当监听事件取消成功，err为undefined，否则返回错误对象。  - 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('setTargetLoopMode');
```

## off('toggleFavorite')10+

PhonePC/2in1TabletTVWearable

off(type: 'toggleFavorite', callback?: (assetId: string) => void): void

取消是否收藏的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'toggleFavorite'。 |
| callback | (assetId: string) => void | 否 | 回调函数，参数assetId是媒体ID。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('toggleFavorite');
```

## off('skipToQueueItem')10+

PhonePC/2in1TabletTVWearable

off(type: 'skipToQueueItem', callback?: (itemId: number) => void): void

取消播放列表单项选中的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'skipToQueueItem'。 |
| callback | (itemId: number) => void | 否 | 回调函数，参数itemId是播放列表单项ID。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('skipToQueueItem');
```

## off('handleKeyEvent')10+

PhonePC/2in1TabletTVWearable

off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void

取消按键事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'handleKeyEvent'。 |
| callback | (event: [KeyEvent](<../../../../基础功能/Input Kit（多模输入服务）/ArkTS API/@ohos.multimodalInput.keyEvent (按键输入事件)/js-apis-keyevent.md>)) => void | 否 | 回调函数，参数event是按键事件。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('handleKeyEvent');
```

## off('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消播放设备变化的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'outputDeviceChange'。 |
| callback | (state: [ConnectionState](../Enums/arkts-apis-avsession-e.md#connectionstate10), device: [OutputDeviceInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#outputdeviceinfo10>)) => void | 否 | 回调函数，参数device是设备相关信息。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('outputDeviceChange');
```

## off('commonCommand')10+

PhonePC/2in1TabletTVWearable

off(type: 'commonCommand', callback?: (command: string, args:{[key: string]: Object}) => void): void

取消自定义控制命令的变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'commonCommand'。 |
| callback | (command: string, args:{[key: string]: Object}) => void | 否 | 回调函数，参数command是变化的自定义控制命令名，args为自定义控制命令的参数。  该参数为可选参数，若不填写该参数，则认为取消所有对command事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('commonCommand');
```

## on('answer')11+

PhonePC/2in1TabletTVWearable

on(type: 'answer', callback: Callback<void>): void

设置通话接听的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'answer'：当通话接听时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('answer', () => {
2. console.info('on call answer');
3. });
```

## off('answer')11+

PhonePC/2in1TabletTVWearable

off(type: 'answer', callback?: Callback<void>): void

取消通话接听事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'answer'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('answer');
```

## on('hangUp')11+

PhonePC/2in1TabletTVWearable

on(type: 'hangUp', callback: Callback<void>): void

设置通话挂断的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'hangUp'：当通话挂断时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('hangUp', () => {
2. console.info('on call hangUp');
3. });
```

## off('hangUp')11+

PhonePC/2in1TabletTVWearable

off(type: 'hangUp', callback?: Callback<void>): void

取消通话挂断事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'hangUp'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('hangUp');
```

## on('toggleCallMute')11+

PhonePC/2in1TabletTVWearable

on(type: 'toggleCallMute', callback: Callback<void>): void

设置通话静音的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'toggleCallMute'：当通话静音或解除静音时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('toggleCallMute', () => {
2. console.info('on call toggleCallMute');
3. });
```

## off('toggleCallMute')11+

PhonePC/2in1TabletTVWearable

off(type: 'toggleCallMute', callback?: Callback<void>): void

取消通话静音事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'toggleCallMute'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('toggleCallMute');
```

## on('castDisplayChange')12+

PhoneTablet

on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void

设置扩展屏投播显示设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'castDisplayChange'：当扩展屏投播显示设备变化时触发事件。 |
| callback | Callback<[CastDisplayInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#castdisplayinfo12>)> | 是 | 回调函数。参数是扩展屏投播显示设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let castDisplay: avSession.CastDisplayInfo;
2. currentAVSession.on('castDisplayChange', (display: avSession.CastDisplayInfo) => {
3. if (display.state === avSession.CastDisplayState.STATE_ON) {
4. castDisplay = display;
5. console.info(`Succeeded in castDisplayChange display : ${display.id} ON`);
6. } else if (display.state === avSession.CastDisplayState.STATE_OFF){
7. console.info(`Succeeded in castDisplayChange display : ${display.id} OFF`);
8. }
9. });
```

## off('castDisplayChange')12+

PhoneTablet

off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void

取消扩展屏投播显示设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'castDisplayChange'。 |
| callback | Callback<[CastDisplayInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#castdisplayinfo12>)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('castDisplayChange');
```

## stopCasting10+

PhonePC/2in1TabletTV

stopCasting(callback: AsyncCallback<void>): void

结束投播。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. currentAVSession.stopCasting(() => {
2. console.info('Succeeded in stopping casting.');
3. });
```

## stopCasting10+

PhonePC/2in1TabletTV

stopCasting(): Promise<void>

结束投播。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当成功结束投播，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. currentAVSession.stopCasting().then(() => {
2. console.info('Succeeded in stopping casting.');
3. });
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
| 6600102 | The session does not exist. |

**示例：**

```
1. let currentOutputDevice: avSession.OutputDeviceInfo = currentAVSession.getOutputDeviceSync();
```

## getAllCastDisplays12+

PhoneTablet

getAllCastDisplays(): Promise<Array<CastDisplayInfo>>

获取当前系统中所有支持扩展屏投播的显示设备。通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[CastDisplayInfo](<../Interfaces (其他)/arkts-apis-avsession-i.md#castdisplayinfo12>)>> | Promise对象，返回当前系统中所有支持扩展屏投播的显示设备。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let castDisplay: avSession.CastDisplayInfo;
2. currentAVSession.getAllCastDisplays().then((data: Array< avSession.CastDisplayInfo >) => {
3. if (data.length >= 1) {
4. castDisplay = data[0];
5. }
6. });
```

## on('playFromAssetId')(deprecated)

PhonePC/2in1TabletTVWearable

on(type:'playFromAssetId', callback: (assetId: number) => void): void

设置媒体id播放监听事件。

说明

从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[on('playWithAssetId')](arkts-apis-avsession-avsession.md#onplaywithassetid20)设置媒体id播放监听事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playFromAssetId'，当媒体id播放时，触发该事件回调。 |
| callback | (assetId: number) => void | 是 | 回调函数。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('playFromAssetId', (assetId: number) => {
2. console.info('on playFromAssetId entry');
3. });
```

## off('playFromAssetId')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'playFromAssetId', callback?: (assetId: number) => void): void

取消媒体id播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

说明

从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[off('playWithAssetId')](arkts-apis-avsession-avsession.md#offplaywithassetid20)取消媒体id播放事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playFromAssetId'。 |
| callback | (assetId: number) => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)和[媒体会话管理错误码](../../../错误码/媒体会话管理错误码/errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playFromAssetId');
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
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('customDataChange', (callback) => {
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
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('customDataChange');
```
