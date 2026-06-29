---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-image-feature-picker
title: 接入全局取色
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入全局取色
category: harmonyos-guides
scraped_at: 2026-06-11T14:51:25+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:568cd497dfad78d50fa01b959f4e98952b2dd93bb5bccb5cc55a0257c957a90e
---
接入全局取色功能，用户可以使用手指或者手写笔操作取色器在屏幕上移动，在目标位置抬起手指/抬起手写笔，会生成该位置色值对应的图像信息。

## 场景介绍

在应用中拉起全局取色，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/HGN9AJVKSA-KmD9U38WHTA/zh-cn_image_0000002622698467.png?HW-CC-KV=V1&HW-CC-Date=20260611T065125Z&HW-CC-Expire=86400&HW-CC-Sign=7E56E3E83888002641B968F144F9A82783F5FF1F75529F20013C4C357575F042)

支持获取当前屏幕上选中位置的色值和色域空间。

## 限制与约束

* 全局取色能力支持设备：Tablet、PC/2in1，并且从5.1.1(19)版本开始，新增支持设备：Phone。
* 设备不支持连接手写笔的话，无法使用全局取色能力。

## 接口说明

| 类名 | 接口名 | 说明 |
| --- | --- | --- |
| [imageFeaturePicker](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/imageFeaturePicker (全局取色功能)/pen-imagefeaturepicker.md>) | [pickForResult](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/ArkTS API/imageFeaturePicker (全局取色功能)/pen-imagefeaturepicker.md#pickforresult>) | 启动取色器。此API用于启动取色器，在取色器移动时不显示色值。该接口要求设备支持手写笔功能，若设备不支持手写笔，则无法启动取色器。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { imageFeaturePicker } from '@kit.Penkit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造全局取色能力。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State message: string = 'Hello World';

   6. build() {
   7. Stack({ alignContent: Alignment.Center }) {
   8. Column() {
   9. Row() {
   10. Button() {
   11. Text('Call GlobalColorPicker from ets side')
   12. .fontSize(18)
   13. .fontWeight(FontWeight.Normal)
   14. }
   15. .width('50%')
   16. .height('60vp')
   17. .align(Alignment.Center)
   18. .onClick((event) => {
   19. // 此处的 displayX 和 displayY 为触摸事件触发时屏幕上的坐标位置
   20. imageFeaturePicker.pickForResult(event.displayX, event.displayY)
   21. .then((colorInfo: imageFeaturePicker.PickedColorInfo) => {
   22. if (colorInfo) {
   23. console.info('colorInfo=' + JSON.stringify(colorInfo));
   24. }
   25. }).catch((err: BusinessError) => {
   26. console.error(`pickForResult failed. Code is ${err.code}, message is ${err.message}`);
   27. })
   28. })
   29. }
   30. }
   31. .align(Alignment.Center)
   32. }
   33. .width('100%')
   34. .height('100%')
   35. }
   36. }
   ```
