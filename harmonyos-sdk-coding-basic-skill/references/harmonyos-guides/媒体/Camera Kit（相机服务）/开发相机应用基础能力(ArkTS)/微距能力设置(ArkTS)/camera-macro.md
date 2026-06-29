---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-macro
title: 微距能力设置(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 微距能力设置(ArkTS)
category: harmonyos-guides
scraped_at: 2026-06-01T11:28:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d412cdda3e7fb6716935cab2eebbbd309e4b4211ed62b9a60a79e37c7ed70e92
---
从API version 19开始，支持设置微距能力。微距能力是指通过光学设计与算法优化，实现近距离对焦并清晰捕捉微小物体细节的相机功能。

## 开发步骤

详细的API说明请参考[Camera](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/模块描述/arkts-apis-camera.md>)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[isMacroSupported](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (MacroQuery)/arkts-apis-camera-macroquery.md#ismacrosupported19>)接口，查询当前设备是否支持微距能力。

   ```
   1. let isSupported: boolean = photoSession.isMacroSupported();
   ```
3. 通过[enableMacro](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (Macro)/arkts-apis-camera-macro.md#enablemacro19>)接口，开启或关闭微距能力。

   ```
   1. function EnableMacro(photoSession: camera.PhotoSession): void {
   2. let isSupported: boolean = photoSession.isMacroSupported();
   3. if (isSupported) {
   4. photoSession.enableMacro(true);
   5. }
   6. }
   ```

## 状态监听

从API version 20开始，支持监听微距能力是否发生改变。

注册macroStatusChanged事件监听微距能力变化，事件监听可参考[on('macroStatusChanged')](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (PhotoSession)/arkts-apis-camera-photosession.md#onmacrostatuschanged20>)。

```
1. function callback(err: BusinessError, macroStatus: boolean): void {
2. if (err !== undefined && err.code !== 0) {
3. console.error(`Callback Error, errorCode: ${err.code}`);
4. return;
5. }
6. console.info(`Macro state: ${macroStatus}`);
7. }

9. // 注册回调函数。
10. function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
11. photoSession.on('macroStatusChanged', callback);
12. }

14. // 解注册。
15. function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
16. photoSession.off('macroStatusChanged');
17. }
```
