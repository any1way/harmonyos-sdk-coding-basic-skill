---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-point-prediction
title: 接入报点预测
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入报点预测
category: harmonyos-guides
scraped_at: 2026-06-11T14:51:24+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:f0d7b8b8ef3d01f3bc1546ce0ea37dbf416fd5802cdb865cb599cd21c1c20a58
---
接入报点预测功能，可以优化应用中手写效果的绘制跟手性，提升应用中手写笔书写场景的跟手体验。

## 场景介绍

在应用的自定义界面中，获取到界面的触摸事件，通过调用报点预测的接口，可以得到预测的下一个报点的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/REU648ueRq-AT8k2YyuH4w/zh-cn_image_0000002622858347.png?HW-CC-KV=V1&HW-CC-Date=20260611T065123Z&HW-CC-Expire=86400&HW-CC-Sign=64D8913CD92E15FA607AF690ED75BBE330B34A7E99C79FD46CC799D35FD26D9D)

## 接口说明

| 类名 | 接口名 | 描述 |
| --- | --- | --- |
| [PointPredictor](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/PointPredictor（报点预测功能）/pen-pointpredictor.md>) | [getPredictionPoint](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/PointPredictor（报点预测功能）/pen-pointpredictor.md#getpredictionpoint>)(event: [TouchEvent](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/触摸事件/ts-universal-events-touch.md#touchevent对象说明)): [TouchPoint](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#touchpoint11) | 获取预测点 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { PointPredictor } from '@kit.Penkit';
   ```
2. 获取当前界面的触摸事件信息，调用接口计算预测点信息。

   ```
   1. @Entry
   2. @Component
   3. struct PointPredictorDemo {
   4. @State actualXCoordinate: number = 0;
   5. @State actualYCoordinate: number = 0;
   6. @State predictorXCoordinate: Dimension = 0;
   7. @State predictorYCoordinate: Dimension = 0;
   8. pointPredictor: PointPredictor = new PointPredictor();

   10. aboutToAppear() {
   11. console.info('getPredictionPoint aboutToAppear');
   12. }

   14. aboutToDisappear() {
   15. console.info('getPredictionPoint aboutToDisappear');
   16. }

   18. build() {
   19. Stack({ alignContent: Alignment.TopEnd }) {
   20. this.canvas(); // 画布
   21. }.height('100%').width('100%')
   22. }

   24. // 画布
   25. @Builder
   26. canvas() {
   27. Column() {
   28. Text('实际点坐标： X: ' + this.actualXCoordinate + ' Y: ' + this.actualYCoordinate).textAlign(TextAlign.Start)
   29. Text('预测点坐标： X: ' + this.predictorXCoordinate + ' Y: ' + this.predictorYCoordinate)
   30. .textAlign(TextAlign.Start)
   31. }.position({ x: 0, y: 0 })
   32. .alignItems(HorizontalAlign.Start)

   34. Stack()
   35. .width('100%')
   36. .height('100%')
   37. .onTouch((event: TouchEvent) => {
   38. switch (event.type) {
   39. case TouchType.Down: // 按下时，新建一条画图路径
   40. break;
   41. case TouchType.Move: // 使用预测算法进行预测,获得预测点
   42. let point = this.pointPredictor?.getPredictionPoint(event);
   43. this.actualXCoordinate = event.touches[0]?.x;
   44. this.actualYCoordinate = event.touches[0]?.y;
   45. this.predictorXCoordinate = point?.x;
   46. this.predictorYCoordinate = point?.y;
   47. console.info('pointPredictor 实际点坐标 x:' + event.touches[0]?.x + ' y:' + event.touches[0]?.y);
   48. console.info('pointPredictor 预测点坐标 x:' + point?.x + '  y:' + point?.y);
   49. break;
   50. case TouchType.Up:
   51. break;
   52. }
   53. })
   54. }
   55. }
   ```
