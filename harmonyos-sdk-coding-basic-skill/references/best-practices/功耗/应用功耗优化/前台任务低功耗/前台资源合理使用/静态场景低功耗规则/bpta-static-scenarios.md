---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-static-scenarios
title: 静态场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 静态场景低功耗规则
category: best-practices
scraped_at: 2026-06-12T10:16:41+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:215a643ec4f13052befa9951e9e1e492e2d797f9558e9dc4f9899069bf43388a
---

## 规则

在界面完全静止且无音频输出、资源下载的场景下，三方应用应停止频繁请求显示和sensor等无关资源，不随vsync信号每帧周期性运行，不持续请求sensor等资源。三方应用进程的CPU负载率应低于10%（单核负载）。

## 开发步骤

静置场景下，三方应用进程不会随着vsync信号每帧周期性运行。以下“案例分析”对此进行详细说明。

在静置场景下，未使用的资源应及时释放。以sensor为例：

1. 按需使用sensor资源，并按需注册SensorId。

   注册监听，通过on()接口实现对传感器的持续监听。设置传感器上报周期interval为200000000纳秒（最小采样周期为5000000纳秒，最大采样周期为200000000纳秒）。

   ```
   1. import { sensor } from '@kit.SensorServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
   5. hilog.info(0x0000, 'Sample', 'Succeeded in obtaining data. x: ' + data.x + ' y: ' + data.y + ' z: ' + data.z);
   6. }, { interval: 200000000 });
   ```

   [StaticScenesRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/StaticScenesRule.ets#L21-L26)

2. 在sensor频次需求较低的场景中，根据需要调整sensor.on()的interval属性，以改变上报频次。

   ```
   1. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
   2. hilog.info(0x0000, 'Sample', 'Succeeded in obtaining data. x: ' + data.x + ' y: ' + data.y + ' z: ' + data.z);
   3. }, { interval: 200000000 });
   ```

   [StaticScenesRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/StaticScenesRule.ets#L30-L32)
3. 不使用sensor资源时，使用以下接口进行解注册。

   ```
   1. sensor.off(sensor.SensorId.ACCELEROMETER);
   ```

   [StaticScenesRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/StaticScenesRule.ets#L36-L36)

## 案例分析

* 开机后，桌面静置。连接Wi-Fi后，lottie动效异常，导致UI和RS空跑。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/o2SG_t39Qh6emtaiJLIXoQ/zh-cn_image_0000002194011528.png?HW-CC-KV=V1&HW-CC-Date=20260612T021640Z&HW-CC-Expire=86400&HW-CC-Sign=DAFA01F35547A4F11E5684176FA0F879DFB01BB7B1E060A3FFA34CEEDA04172B "点击放大")
* 应用静置界面时，应用以120 fps响应vsync事件但无实际显示，导致应用进程和RS负载较高。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/pX6cfmukRBS5Y25Qxm086w/zh-cn_image_0000002229451821.png?HW-CC-KV=V1&HW-CC-Date=20260612T021640Z&HW-CC-Expire=86400&HW-CC-Sign=2415B6F679601FAE4595A116EDD9A846C00DC630A05B46D73A2993F72D44C30C "点击放大")

## 调测验证

* 查看日志：在控制台输入top指令，可直接获取进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/1_Sfsg0xRNSb162WgXW8lQ/zh-cn_image_0000002193851952.png?HW-CC-KV=V1&HW-CC-Date=20260612T021640Z&HW-CC-Expire=86400&HW-CC-Sign=7AF3BB39C27BF49532064C0F7AD79F3CDC346B74EF4F4F45B8D6C2C364C9757A "点击放大")
* 抓取trace：通过trace中的进程耗时和绝对耗时，计算进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/A5GZcFX0T5mIJKHLnLx0ew/zh-cn_image_0000002229337329.png?HW-CC-KV=V1&HW-CC-Date=20260612T021640Z&HW-CC-Expire=86400&HW-CC-Sign=8ADB645F94BF96D06291BCC0ABEB3C87D11ACAD80BACABD65807D56D6D0D4D83 "点击放大")
