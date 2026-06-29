---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-resource-package
title: 传输资源包
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发指导 > 传输资源包
category: harmonyos-guides
scraped_at: 2026-06-11T15:07:26+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:0680036b251c3c7ea96f67211c8d03a1c23422cdc9c9f036a53d38c92ed169fb
---
游戏近场快传支持已安装游戏的玩家间传输游戏内资源包，节省玩家下载资源包所需的流量和时间。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/tMh60bb7RA-ritYsyDZ18g/zh-cn_image_0000002622698901.png?HW-CC-KV=V1&HW-CC-Date=20260611T070724Z&HW-CC-Expire=86400&HW-CC-Sign=562BA8F0A210BF34B355CCBA18AFB0EEF53B14913112FB76400678F21AB946EA)

1. 发送端和接收端调用[create](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfercreate>)创建游戏近场快传服务。
2. 创建成功后，游戏客户端调用以下接口注册监听。

   * 注册连接通知监听接口：[on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferonconnectnotify>)('connectNotify')
   * （发送端选择绑定接收端情况下需调用）注册发现结果事件监听接口：[on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferondiscovery>)('discovery')
   * 注册收到包信息监听接口：[on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferonreceivepackageinfo>)('receivePackageInfo')
   * 注册传输通知监听接口：[on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferontransfernotify>)('transferNotify')
   * 注册错误事件监听接口：[on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferonerror>)('error')
3. 接收端调用[publishNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferpublishnearbygame>)发布自身近场快传服务。
4. 绑定接收端，支持如下两种方式。

   * 自动绑定：

     发送端调用[autoBindNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferautobindnearbygame>)自动绑定附近设备（搜索并绑定附近10米内第一个发现的近场快传服务）。

     说明

     自动绑定操作2分钟内有效，超时需重新调用接口。
   * 选择绑定：

     发送端调用[discoveryNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferdiscoverynearbygame>)发现附近设备，发现操作完成后将收到discovery事件回调，获得可绑定的设备列表供玩家选择，调用[bindNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferbindnearbygame>)接口绑定玩家选定的接收端设备。

     说明

     发现操作2分钟内有效，超时需重新调用接口。
5. 接收端收到UIAbility的[onCollaborate](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#oncollaborate18>)回调后调用[acceptCollaboration](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferacceptcollaboration>)接受协同。
6. 接收端收到建链成功connectNotify事件回调。
7. 接收端调用[sendPackageInfo](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfersendpackageinfo>)发送自身文件信息，如版本信息、包信息。
8. 发送端收到receivePackageInfo事件回调。
9. 发送端比较版本并调用[replyPackageInfoResult](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferreplypackageinforesult>)上报对比结果。
10. 如发送端对比结果为需要发送，则调用[transferPackageData](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfertransferpackagedata>)向接收端发送需要传输的资源包。
11. 接收端可在transferNotify回调中获取当前已传输的包体大小、包体总大小、传输速率、传输剩余时间等信息，传输完成可获取已接收资源包的存储目录，对传输完成的资源文件做处理。
12. 处理传输完成的资源文件后，可调用[destroy](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferdestroy>)销毁服务。

    说明

    * destroy接口会清除已接收数据，请确保对已接收数据做好处理或转移后再调用该接口。
    * 每次调用[create](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfercreate>)接口会自动清理自身历史数据。

## 接口说明

具体API说明详见[接口文档](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md>)。

| 接口名 | 描述 |
| --- | --- |
| [create](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfercreate>)(createParameters: CreateParameters): Promise<CreateResult> | 创建游戏近场快传服务。 |
| [on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferonconnectnotify>)(type: 'connectNotify', callback: Callback<ConnectNotification>): void | 订阅连接通知事件。 |
| [off](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferoffconnectnotify>)(type: 'connectNotify', callback?: Callback<ConnectNotification>): void | 取消订阅连接通知事件。 |
| [on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferondiscovery>)(type: 'discovery', callback: Callback<DiscoveryResult>): void | 订阅发现结果事件。 |
| [off](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferoffdiscovery>)(type: 'discovery', callback?: Callback<DiscoveryResult>): void | 取消订阅发现结果事件。 |
| [on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferonreceivepackageinfo>)(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void | 订阅收到包信息事件。 |
| [off](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferoffreceivepackageinfo>)(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void | 取消订阅收到包信息事件。 |
| [on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferontransfernotify>)(type: 'transferNotify', callback: Callback<TransferNotification>): void | 订阅传输通知事件。 |
| [off](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferofftransfernotify>)(type: 'transferNotify', callback?: Callback<TransferNotification>): void | 取消订阅传输通知事件。 |
| [on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferonerror>)(type: 'error', callback: Callback<ReturnResult>): void | 订阅错误事件。 |
| [off](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferofferror>)(type: 'error', callback?: Callback<ReturnResult>): void | 取消订阅错误事件。 |
| [publishNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferpublishnearbygame>)(): Promise<void> | 发布近场快传服务。 |
| [autoBindNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferautobindnearbygame>)(): Promise<void> | 自动绑定近场快传服务。 |
| [discoveryNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferdiscoverynearbygame>)(): Promise<void> | 发现近场快传服务。 |
| [bindNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferbindnearbygame>)(bindParameters: BindParameters): Promise<void> | 绑定指定近场快传服务。 |
| [acceptCollaboration](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferacceptcollaboration>)(acceptParameters: Record<string, object>): Promise<void> | 接受协同。 |
| [sendPackageInfo](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfersendpackageinfo>)(packageInfo: PackageInfo): Promise<void> | 接收端发送自身文件信息。 |
| [replyPackageInfoResult](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferreplypackageinforesult>)(packageInfoResult: PackageInfoResult): Promise<void> | 上报包信息对比结果。 |
| [transferPackageData](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfertransferpackagedata>)(packageData: PackageData): Promise<void> | 传输包数据。 |
| [destroy](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferdestroy>)(): Promise<void> | 销毁游戏近场快传服务。 |

## 接入步骤

### 导入模块

导入Game Service Kit及公共模块。

```
1. import { abilityAccessCtrl, AbilityConstant, UIAbility, common } from "@kit.AbilityKit";
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { gameNearbyTransfer } from '@kit.GameServiceKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
```

### 申请权限

申请ohos.permission.DISTRIBUTED\_DATASYNC权限用于设备发现，详情可参考[向用户申请授权](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)。

```
1. let atManager = abilityAccessCtrl.createAtManager();
2. let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
3. try {
4. atManager.requestPermissionsFromUser(uiAbilityContext, ['ohos.permission.DISTRIBUTED_DATASYNC']).then((data) => {
5. if (data.authResults[0] === 0) {
6. // 用户授权，可以继续访问目标操作。
7. hilog.info(0x0000, 'nearby', `ohos.permission.DISTRIBUTED_DATASYNC is granted by user.`);
8. } else {
9. // 用户拒绝授权，提示用户必须授权才能访问当前功能，并引导用户到系统设置中打开相应的权限。
10. return;
11. }
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'nearby', '%{public}s', `Failed to request permissions from user, code: ${err.code}, message: ${err.message}`);
14. })
15. } catch (error) {
16. let err = error as BusinessError;
17. hilog.error(0x0000, 'nearby', `request permissions from user exception. Code: ${err.code}, message: ${err.message}`);
18. }
```

### 创建游戏近场快传服务并注册相关回调

导入相关模块后，需先调用[create](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfercreate>)接口创建游戏近场快传服务，然后注册各回调事件。

说明

[create](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfercreate>)接口是调用其他接口的前提，如果未创建游戏近场快传服务或创建失败，将无法调用其他接口。

```
1. public create() {
2. let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
3. let initParam: gameNearbyTransfer.CreateParameters = {
4. abilityName: uiAbilityContext.abilityInfo.name,
5. context: uiAbilityContext,
6. moduleName: uiAbilityContext.abilityInfo.moduleName,
7. needShowSystemUI: false,
8. };

10. try {
11. gameNearbyTransfer.create(initParam).then((createResult) => {
12. hilog.info(0x0000, 'nearby', `create success localDeviceName ${createResult.localDeviceName}`);
13. this.registerCallback();
14. }).catch((err: BusinessError) => {
15. hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
16. });
17. } catch (error) {
18. let err = error as BusinessError;
19. hilog.error(0x0000, 'nearby', `create exception. Code: ${err.code}, message: ${err.message}`);
20. }
21. }

23. // 注册监听
24. public registerCallback() {
25. try {
26. gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
27. gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
28. gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
29. gameNearbyTransfer.on('error', errorCallBack);
30. } catch (error) {
31. let err = error as BusinessError;
32. hilog.error(0x0000, 'nearby', `registerCallback error. Code: ${err.code}, message: ${err.message}`);
33. }
34. }

36. function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
37. // 连接状态回调，接收端收到建链成功回调后，在此处调用sendPackageInfo接口发送自身文件信息，如版本信息、包信息
38. hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
39. }

41. function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
42. // 接收包信息回调，发送端收到接收端发送的版本信息后进行对比，根据对比结果决定是否需要传输资源包数据。
43. hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
44. }

46. function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
47. // 传输回调，处理传输进度信息
48. hilog.info(0x0000, 'nearby', `get transfer state: ${callback.transferState}`);
49. }

51. function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
52. // 异常信息回调，处理相关异常信息
53. hilog.error(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
54. }
```

### 接收端接受协同

接收端实现[onCollaborate](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#oncollaborate18>)回调，回调中调用[acceptCollaboration](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferacceptcollaboration>)接口接受协同。

```
1. export default class EntryAbility extends UIAbility {
2. // 协同回调
3. onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
4. try {
5. // 接受协同
6. gameNearbyTransfer.acceptCollaboration(wantParam).catch((err: BusinessError) => {
7. hilog.error(0x0000, 'nearby', `acceptCollaboration failed. Code: ${err.code}, message: ${err.message}`);
8. });
9. } catch (error) {
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `acceptCollaboration exception. Code: ${err.code}, message: ${err.message}`);
12. }
13. return AbilityConstant.CollaborateResult.ACCEPT;
14. }
15. }
```

### 接收端发布自身游戏近场快传服务

接收端调用[publishNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferpublishnearbygame>)接口发布自身游戏近场快传服务。

```
1. try {
2. gameNearbyTransfer.publishNearbyGame().then(() => {
3. hilog.info(0x0000, 'nearby', `publishNearbyGame success`);
4. }).catch((err: BusinessError) => {
5. hilog.error(0x0000, 'nearby', `publishNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
6. });
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'nearby', `publishNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
10. }
```

### 发送端绑定接收端游戏近场快传服务

发送端绑定接收端游戏近场快传服务支持如下两种方式：

* 方式一：自动绑定

  发送端调用[autoBindNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferautobindnearbygame>)接口自动绑定接收端近场快传服务。

  ```
  1. try {
  2. // 自动绑定近场快传服务
  3. gameNearbyTransfer.autoBindNearbyGame().then(() => {
  4. hilog.info(0x0000, 'nearby', `autoBindNearbyGame success`);
  5. }).catch((err: BusinessError) => {
  6. hilog.error(0x0000, 'nearby', `autoBindNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
  7. });
  8. } catch (error) {
  9. let err = error as BusinessError;
  10. hilog.error(0x0000, 'nearby', `autoBindNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
  11. }
  ```
* 方式二：选择绑定

  1. 发送端调用[on](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferondiscovery>)('discovery')接口注册“发现设备”结果事件监听。

     ```
     1. try {
     2. // 订阅发现结果
     3. gameNearbyTransfer.on('discovery', discoveryCallBack);
     4. } catch (error) {
     5. // 订阅失败
     6. let err = error as BusinessError;
     7. hilog.error(0x0000, 'nearby', `Failed to subscribe discovery. Code: ${err.code}, message: ${err.message}`);
     8. }

     10. function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
     11. // 获取到发现的设备 展示设备列表
     12. callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
     13. hilog.info(0x0000, 'nearby', `device info. name: ${device.deviceName}, index: ${index}`);
     14. });
     15. }
     ```
  2. 发送端调用[discoveryNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferdiscoverynearbygame>)发现附近设备。

     ```
     1. try {
     2. gameNearbyTransfer.discoveryNearbyGame().then(() => {
     3. hilog.info(0x0000, 'nearby', `discoveryNearbyGame success.`);
     4. }).catch((err: BusinessError) => {
     5. hilog.error(0x0000, 'nearby', `discoveryNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
     6. });
     7. } catch (error) {
     8. let err = error as BusinessError;
     9. hilog.error(0x0000, 'nearby', `discoveryNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
     10. }
     ```
  3. “发现设备”操作完成后将收到discovery事件回调，获得发现的设备列表供玩家选择，调用[bindNearbyGame](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferbindnearbygame>)接口绑定玩家选定的接收端设备。

     ```
     1. public bindNearbyGame(deviceInfo: gameNearbyTransfer.NearbyGameDevice) {
     2. let bindInfo: gameNearbyTransfer.BindParameters = {
     3. deviceId: deviceInfo.deviceId,
     4. networkId: deviceInfo.networkId
     5. };
     6. try {
     7. gameNearbyTransfer.bindNearbyGame(bindInfo).then(() => {
     8. hilog.info(0x0000, 'nearby', `bindNearbyGame success`);
     9. }).catch((err: BusinessError) => {
     10. hilog.error(0x0000, 'nearby', `bindNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
     11. });
     12. } catch (error) {
     13. let err = error as BusinessError;
     14. hilog.error(0x0000, 'nearby', `bindNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
     15. }
     16. }
     ```

### 接收端发送自身文件信息

收到建链成功回调后，接收端调用[sendPackageInfo](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfersendpackageinfo>)接口发送自身文件，如版本信息、包信息。

```
1. function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
2. if (callback.connectState == gameNearbyTransfer.ConnectState.CONNECTED) {
3. // 连接成功回调，判断当前是否为接收端。若当前设备为接收端，请设置为true，否则请设置为false。
4. let isReceive = true;
5. if (!isReceive) {
6. return;
7. }
8. // 接收端收到连接回调后需要处理，发送资源包信息给发送端
9. let packageInfo: gameNearbyTransfer.PackageInfo = {
10. name: 'com.huawei.xxxx',
11. files: [],
12. version: '1.1.0',
13. extraData: 'extraData'
14. };
15. let fileInfo: gameNearbyTransfer.FileInfo = {
16. path: '/xxx/xxxx/files/data.zip', // 建议使用沙箱路径
17. hash: 'fileHash' // 可选
18. };
19. packageInfo.files?.push(fileInfo);
20. try {
21. gameNearbyTransfer.sendPackageInfo(packageInfo).then(() => {
22. hilog.info(0x0000, 'nearby', `sendPackageInfo success`);
23. }).catch((err: BusinessError) => {
24. hilog.error(0x0000, 'nearby', `sendPackageInfo failed. Code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (error) {
27. let err = error as BusinessError;
28. hilog.error(0x0000, 'nearby', `sendPackageInfo exception. Code: ${err.code}, message: ${err.message}`);
29. }
30. }
31. }
```

### 发送端对比后传输资源包

发送端收到接收端发送的版本信息后进行对比，调用[replyPackageInfoResult](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferreplypackageinforesult>)上报对比结果，根据对比结果决定是否需要调用[transferPackageData](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransfertransferpackagedata>)接口发送资源包数据。

```
1. function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
2. const version = callback.version;
3. hilog.info(0x0000, 'nearby', `remote version: ${version}`);
4. // 比较版本，决定是否需要发送资源包，也可以比较文件hash
5. let packageInfoResult: gameNearbyTransfer.PackageInfoResult = {
6. packageInfoResultCode: gameNearbyTransfer.PackageInfoResultCode.PACKAGE_AVAILABLE_COMPARED
7. };
8. try {
9. // 上报对比结果
10. gameNearbyTransfer.replyPackageInfoResult(packageInfoResult).then(() => {
11. let packageData: gameNearbyTransfer.PackageData = {
12. name: 'com.huawei.gamenearbydemo',
13. version: '1.0.0',
14. files: [{
15. srcPath: '/data/xxxx/a.zip',
16. destPath: 'xxxx/a.zip'
17. }] // srcPath是需要发送文件的路径，详情请参见沙箱路径。destPath为接收文件的路径，完整路径是fileStoragePath+destPath。
18. };
19. try {
20. // 发送资源包
21. gameNearbyTransfer.transferPackageData(packageData).then(() => {
22. // 发送成功
23. }).catch((err: BusinessError) => {
24. hilog.error(0x0000, 'nearby', `transferPackageData error Code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (err) {
27. let error = err as BusinessError;
28. hilog.error(0x0000, 'nearby', `transferPackageData exception Code: ${error.code}, message: ${error.message}`);
29. }
30. }).catch((err: BusinessError) => {
31. hilog.error(0x0000, 'nearby', `replyPackageInfoResult error Code: ${err.code}, message: ${err.message}`);
32. });
33. } catch (error) {
34. let err = error as BusinessError;
35. hilog.error(0x0000, 'nearby', `replyPackageInfoResult exception Code: ${err.code}, message: ${err.message}`);
36. }
37. }
```

### 处理资源包传输进度信息

发送端和接收端在传输回调中处理传输进度信息。

```
1. function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
2. if (callback.transferState == gameNearbyTransfer.TransferState.SEND_PROCESS) {
3. // 处理发送进度，如显示进度条和速率
4. }
5. if (callback.transferState == gameNearbyTransfer.TransferState.SEND_FINISH) {
6. // 发送完成
7. }
8. if (callback.transferState == gameNearbyTransfer.TransferState.RECEIVE_PROCESS) {
9. // 处理接收进度，如显示进度条和速率
10. }
11. if (callback.transferState == gameNearbyTransfer.TransferState.RECEIVE_FINISH) {
12. // 接收完成，获取到资源包存储的沙箱路径
13. let fileStoragePath = callback.fileStoragePath;
14. hilog.info(0x0000, 'nearby', `get transfer path: ${fileStoragePath}`);
15. // 对fileStoragePath下的文件做处理
16. }
17. }
```

### 处理已接收资源包后销毁服务

对已接收数据做好处理或转移后，调用[destroy](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gameNearbyTransfer(游戏近场快传)/gameservice-nearbytransfer.md#gamenearbytransferdestroy>)接口销毁服务。若服务销毁后再次使用近场快传服务，需重新[创建游戏近场快传服务并注册相关回调](gameservice-nearbytransfer-resource-package.md#创建游戏近场快传服务并注册相关回调)。

```
1. public destroy() {
2. // 取消回调注册
3. this.unregisterCallback();
4. // 销毁服务
5. try {
6. gameNearbyTransfer.destroy().then(() => {
7. hilog.info(0x0000, 'nearby', `destroy success`);
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'nearby', `destroy failed. Code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (error) {
12. let err = error as BusinessError;
13. hilog.error(0x0000, 'nearby', `destroy exception. Code: ${err.code}, message: ${err.message}`);
14. }
15. }

17. public unregisterCallback() {
18. try {
19. gameNearbyTransfer.off('connectNotify', connectNotifyCallBack);
20. gameNearbyTransfer.off('receivePackageInfo', receivePackageInfoCallBack);
21. gameNearbyTransfer.off('transferNotify', transferNotifyCallBack);
22. gameNearbyTransfer.off('error', errorCallBack);
23. // 发送端选择手动绑定接收端且已订阅discovery事件
24. gameNearbyTransfer.off('discovery', discoveryCallBack);
25. } catch (error) {
26. let err = error as BusinessError;
27. hilog.error(0x0000, 'nearby', `unregisterCallback error. Code: ${err.code}, message: ${err.message}`);
28. }
29. }

31. function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
32. // 连接状态回调，接收端收到建链成功回调后，在此处调用sendPackageInfo接口发送自身文件信息，如版本信息、包信息
33. hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
34. }

36. function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
37. // 接收包信息回调，发送端收到接收端发送的版本信息后进行对比，根据对比结果决定是否需要传输资源包数据。
38. hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
39. }

41. function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
42. // 传输回调，处理传输进度信息
43. hilog.info(0x0000, 'nearby', `get transfer state: ${callback.transferState}`);
44. }

46. function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
47. // 异常信息回调，处理相关异常信息
48. hilog.error(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
49. }

51. function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
52. // 获取到发现的设备 展示设备列表
53. callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
54. hilog.info(0x0000, 'nearby', `device info. name: ${device.deviceName}, index: ${index}`);
55. });
56. }
```
