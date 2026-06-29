---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-2
title: 游戏上划退出后，场景切换阶段存在振动，应该如何避免
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏上划退出后，场景切换阶段存在振动，应该如何避免
category: harmonyos-guides
scraped_at: 2026-06-01T14:58:23+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:075d3fa554a2fe89d056c4608c913d7b52819d520789bb5258dddd24d584edc6
---
开发步骤如下：

1. 通过globalThis定义全局作用域的变量isCacheStatus，在onCreate生命周期函数中赋值false，[isLaunchMirrorEnabled](<../../../../../../harmonyos-references/Graphics Accelerate Kit（图形加速服务）/ArkTS API/launchAcceleration（游戏启动加速）/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled>)接口返回true时赋值true。
2. 在函数[startVibration](<../../../../../../harmonyos-references/硬件/Sensor Service Kit（传感器服务）/ArkTS API/@ohos.vibrator (振动)/js-apis-vibrator.md#vibratorstartvibration9>)前增加isCacheStatus校验，若当前处于缓存态，则不进行振动操作。

以团结工程为例，修改如下：

```
1. // TuanjiePlayerAbilityBase.ets
2. import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
3. onCreate(): void {
4. globalThis.isCacheStatus = false;
5. // ......
6. }
7. onWindowStageWillDestroy(): void {
8. if (launchAcceleration.isLaunchMirrorEnabled()) {
9. globalThis.isCacheStatus = true;
10. // ......
11. }
12. }

14. // TuanjieVibrate.ets
15. static vibrate(vibrateMs: number) {
16. if (globalThis.isCacheStatus) {
17. console.info('globalThis.isCacheStatus true, vibration returned.');
18. return;
19. }
20. // ......
21. }
```
