---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-screenshots
title: 地图截图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 地图截图
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:55+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:1c84a79e1a41ed7c14a98cbd8b837bc912a7580762ff7ef3603624e7e5051907
---
本章节将向您介绍如何实现地图截图功能。

地图截图指对当前屏幕显示区域进行截屏，支持对地图、覆盖物、Logo进行屏幕截图。地图截图功能适用于需要将当前地图状态保存为图片的场景，如分享当前位置、生成导航路线图、记录特定视角的地图内容等。该功能可以帮助开发者快速实现地图内容的可视化输出，提升用户体验

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/jl22j0F3QiWNO25FnbYVHA/zh-cn_image_0000002592379394.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070954Z&HW-CC-Expire=86400&HW-CC-Sign=72C36E683E880DF24E28AE57668865436EFC6D5BBCB472831ADB8EF91C1C6E87 "点击放大")

## 接口说明

以下是地图截图相关接口，以下功能主要由[snapshot](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#snapshot>)提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#snapshot>)。

| 接口名 | 描述 |
| --- | --- |
| [snapshot](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#snapshot>)(): Promise<[image.PixelMap](<../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)> | 地图截图。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   3. import { image } from '@kit.ImageKit';
   ```
2. 调用[snapshot](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#snapshot>)方法对当前屏幕进行截图。

   ```
   1. @Entry
   2. @Component
   3. struct HuaweiMapDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private callback?: AsyncCallback<map.MapComponentController>;
   6. private mapController?: map.MapComponentController;
   7. @State image?: image.PixelMap = undefined;

   9. aboutToAppear(): void {
   10. // 地图初始化参数，设置地图中心点坐标及层级
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 39.9,
   15. longitude: 116.4
   16. },
   17. zoom: 10
   18. }
   19. };

   21. // 地图初始化的回调
   22. this.callback = async (err, mapController) => {
   23. if (!err) {
   24. // 获取地图的控制器类，用来操作地图
   25. this.mapController = mapController;
   26. } else {
   27. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   28. }
   29. };
   30. }

   32. build() {
   33. Stack() {
   34. Column() {
   35. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
   36. .width('100%')
   37. .height('50%');

   39. Scroll(new Scroller()) {
   40. Column() {
   41. Image(this.image)
   42. .objectFit(ImageFit.Auto)
   43. .border({ width: 1, color: Color.Red }).width("100%")
   44. Button("获取截图")
   45. .margin({ left: 10 })
   46. .fontSize(12)
   47. .onClick(async () => {
   48. if (this.mapController) {
   49. // 获取截图
   50. let pixelMap = await this.mapController.snapshot();
   51. this.image = pixelMap;
   52. }
   53. });
   54. }
   55. }.width('70%').height("50%")
   56. }.width('100%')
   57. }.height('100%')
   58. }
   59. }
   ```
