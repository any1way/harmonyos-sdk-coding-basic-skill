---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-instant-shape
title: 接入一笔成形
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入一笔成形
category: harmonyos-guides
scraped_at: 2026-06-11T14:51:25+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:0563939cba98710a6556f5a9d999027489dfba59ff256d557c71eb572dfc2581
---
接入一笔成形功能，可以传入手写笔迹的点位信息、通过手写笔/手指在屏幕上停顿一定的时间后触发此功能，触发功能后将自动识别当前绘制的图形，并生成对应的图像信息。

## 场景介绍

在应用中实现一笔成形，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/tF7DIxzPTmqjbR_JNTv6ig/zh-cn_image_0000002622858345.gif?HW-CC-KV=V1&HW-CC-Date=20260611T065124Z&HW-CC-Expire=86400&HW-CC-Sign=8DE2150977627BD2A6B40DA29A81273F0181769AEA5C942B30D991AF28520E17)

1. 支持获取识别的图像信息，图像信息支持存储。
2. 支持从存储的图像信息中读取信息。

## 接口说明

| 类名 | 接口名 | 说明 |
| --- | --- | --- |
| [InstantShapeGenerator](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md>) | [processTouchEvent](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md#processtouchevent>) | 传递触摸事件。 |
| [InstantShapeGenerator](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md>) | [getPathFromString](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md#getpathfromstring>) | 从给定的形状字符串中提取形状信息。 |
| [InstantShapeGenerator](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md>) | [notifyAreaChange](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md#notifyareachange>) | 通知组件大小变化。 |
| [InstantShapeGenerator](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md>) | [setPauseTime](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md#setpausetime>) | 设置触发识别的暂停时间，单位：ms。 |
| [InstantShapeGenerator](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md>) | [release](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md#release>) | 销毁识别工具。 |
| [InstantShapeGenerator](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md>) | [onShapeRecognized](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/InstantShapeGenerator（一笔成形功能）/pen-instantsshapegenerator.md#onshaperecognized>) | 注册识别完成时的回调方法。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { InstantShapeGenerator, ShapeInfo } from '@kit.Penkit';
   ```
2. 构造包含一笔成形能力，下面以控件为例：

   ```
   1. @Entry
   2. @Component
   3. struct InstantShapeDemo {
   4. private instantShapeGenerator: InstantShapeGenerator = new InstantShapeGenerator();
   5. private points: DrawPathPointModel[] = [];
   6. // 绘制路径
   7. private drawPath = new Path2D();
   8. private shapePath = new Path2D();
   9. private mShapeSuccess = false;
   10. private settings: RenderingContextSettings = new RenderingContextSettings(true);
   11. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   12. // 通过回调方法获取识别结果
   13. private shapeInfoCallback = (shapeInfo: ShapeInfo) => {
   14. this.shapePath = shapeInfo.shapePath;
   15. this.mShapeSuccess = true;
   16. this.context.beginPath();
   17. this.context.reset();
   18. this.drawCurrentPathModel(this.shapePath);
   19. }

   21. aboutToAppear() {
   22. console.info('InstantShapeGenerator aboutToAppear');
   23. // 设置触发识别的暂停时间
   24. try {
   25. this.instantShapeGenerator?.setPauseTime(280);
   26. } catch (error) {
   27. console.error('setPauseTime failed: ', error);
   28. }
   29. // 注册完成时的回调方法
   30. this.instantShapeGenerator?.onShapeRecognized(this.shapeInfoCallback);
   31. }

   33. aboutToDisappear() {
   34. console.info('InstantShapeGenerator aboutToDisappear');
   35. this.instantShapeGenerator?.release();
   36. }

   38. build() {
   39. Stack({ alignContent: Alignment.TopEnd }) {
   40. Canvas(this.context)
   41. .width('100%')
   42. .height('100%')
   43. .onAreaChange((oldValue: Area, newValue: Area) => {
   44. // 通知组件大小变化。形状的大小（例如圆的半径）根据组件尺寸而变化
   45. this.instantShapeGenerator?.notifyAreaChange(Number(newValue.width), Number(newValue.height));
   46. }).onTouch((event: TouchEvent) => {
   47. // 传递触摸事件
   48. this.instantShapeGenerator?.processTouchEvent(event);
   49. switch (event.type) {
   50. case TouchType.Down:
   51. this.moveStart(event.touches[0]?.x, event.touches[0]?.y);
   52. break;
   53. case TouchType.Move:
   54. this.moveUpdate(event.touches[0]?.x, event.touches[0]?.y);
   55. break;
   56. case TouchType.Up:
   57. this.moveEnd();
   58. break;
   59. }
   60. })
   61. }.height('100%').width('100%')
   62. }

   64. moveStart(x: number, y: number) {
   65. this.points.push({ x: x, y: y });
   66. this.drawPath.moveTo(x, y);
   67. this.drawCurrentPathModel(this.drawPath);
   68. this.mShapeSuccess = false;
   69. }

   71. moveUpdate(x: number, y: number) {
   72. let lastPoint = this.points[this.points.length - 1];
   73. this.points.push({ x: x, y: y });
   74. this.drawPath.quadraticCurveTo((x + lastPoint?.x) / 2, (y + lastPoint?.y) / 2, x, y);
   75. if (!this.mShapeSuccess) {
   76. this.drawCurrentPathModel(this.drawPath);
   77. }
   78. }

   80. moveEnd() {
   81. this.points = [];
   82. this.drawPath = new Path2D();
   83. this.shapePath = new Path2D();
   84. }

   86. private drawCurrentPathModel(path: Path2D) {
   87. this.context.globalCompositeOperation = 'source-over';
   88. this.context.lineWidth = 8;
   89. this.context.strokeStyle = '#ED1B1B';
   90. this.context.lineJoin = 'round';
   91. this.context.stroke(path);
   92. }
   93. }

   95. export class DrawPathPointModel {
   96. x: number = 0;
   97. y: number = 0;
   98. }
   ```
