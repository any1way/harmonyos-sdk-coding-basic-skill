---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-6
title: 游戏出现卡死后，应该如何避免下一次秒启后还是卡死场景
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏出现卡死后，应该如何避免下一次秒启后还是卡死场景
category: harmonyos-guides
scraped_at: 2026-06-01T14:58:26+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:6ada807b4289597acae2cbe21c192f97e8e6723135fccfb74ea535e455134e43
---

建议游戏上划退出后进行场景切换操作，若场景切换失败或场景切换超时（5s）则设置游戏不支持缓存后快速启动。

以团结工程为例，修改如下：

```
1. import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { preferences } from '@kit.ArkData';
4. import Tuanjie from 'libtuanjie.so';
5. import sleepNapi from 'libentry.so'; // 通过napi封装的std::this_thread::sleep_for

7. let dataPreferences: preferences.Preferences | null = null;

9. onWindowStageWillDestroy(): void {
10. let enable = launchAcceleration.isLaunchMirrorEnabled();
11. if (enable) {
12. this.onResume(); // 团结工程中恢复引擎方法
13. Tuanjie.TuanjieSendMessage("GlobalObjectForArkTSCall", "OnMessageCall", "SwitchToLoginPage");
14. let waitTime = 0; // 等待时长，单位：ms
15. while(true) {
16. let sceneChangeResult = dataPreferences?.getSync('sceneChangeResult', undefined);
17. if (sceneChangeResult != undefined) {
18. if (sceneChangeResult) {
19. break; // 场景切换成功，跳出while循环
20. }
21. this.setSupportedProcessCache(false); // 场景切换失败，设置游戏不支持缓存后快速启动
22. break;
23. }
24. if (waitTime >= 5000) {
25. this.setSupportedProcessCache(false); // 场景切换超时，设置游戏不支持缓存后快速启动
26. break;
27. }
28. sleepNapi.sleep(500);
29. waitTime += 500;
30. }
31. sleepNapi.sleep(500);
32. this.onPause(); // 团结工程中暂停引擎方法
33. }
34. }

36. setSupportedProcessCache(isSupported : boolean): void {
37. try {
38. this.context.getApplicationContext().setSupportedProcessCache(isSupported);
39. } catch (error) {
40. let code = (error as BusinessError).code;
41. let message = (error as BusinessError).message;
42. console.error(`setSupportedProcessCache fail, code: ${code}, msg: ${message}`);
43. }
44. }
```
