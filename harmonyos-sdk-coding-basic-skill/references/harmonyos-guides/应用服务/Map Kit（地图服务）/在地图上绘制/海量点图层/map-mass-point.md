---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-mass-point
title: 海量点图层
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 海量点图层
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9a03bb9ca78cc53d2b8ad0e296da0add717e3014e9cfe92ad8759f37747cb9b3
---
## 场景介绍

新增海量点图层，用于批量展示坐标点数据。海量点图层支持处理的点数量级跨度较大，从几十个点至十万个点都可以应用海量点图层进行处理，本章节将向您介绍如何在地图上绘制海量点图层。

6.0.0(20)开始，支持海量点图层功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/JMWI1wrYSEuWOKng_iwdnw/zh-cn_image_0000002592219480.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071027Z&HW-CC-Expire=86400&HW-CC-Sign=3BD5E4673C5604A87C0DA0D2D8050CE103ADC9C7A5FDF1C1056EC9C945D43683 "点击放大")

## 接口说明

海量点图层功能主要由[MassPointOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#masspointoverlayparams>)、[addMassPointOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addmasspointoverlay>)、[MassPointOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MassPointOverlay)/map-map-masspointoverlay.md>)提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MassPointOverlay)/map-map-masspointoverlay.md>)。

| 接口名 | 描述 |
| --- | --- |
| [MassPointOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#masspointoverlayparams>) | 海量点参数。 |
| [addMassPointOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addmasspointoverlay>)(params: mapCommon.[MassPointOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#masspointoverlayparams>)): Promise<[MassPointOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MassPointOverlay)/map-map-masspointoverlay.md>)> | 新增海量点。 |
| [MassPointOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MassPointOverlay)/map-map-masspointoverlay.md>) | 海量点管理对象。 |

## 开发步骤

### 添加海量点图层

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 绘制海量点图层。

   ```
   1. @Entry
   2. @Component
   3. struct MassPointOverlayDemo {
   4. private TAG = 'OHMapSDK_MassPointOverlayDemo';
   5. private mapOption?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. private massPointOverlay?: map.MassPointOverlay;
   9. @State currentTimestamp: number = 0;
   10. @State mapHeight: string = '65%'
   11. @State mapWidth: string = '100%'
   12. aboutToAppear(): void {
   13. this.mapOption = {
   14. position: {
   15. target: {
   16. latitude: 32.11111,
   17. longitude: 118.11111
   18. },
   19. zoom: 9
   20. },
   21. scaleControlsEnabled: true
   22. }
   23. this.callback = async (err, mapController) => {
   24. if (!err) {
   25. this.mapController = mapController;
   26. let items: mapCommon.MassPointItem[] = [];
   27. for (let i = 0; i < 1000; i++) {
   28. // 将海量点存入items
   29. items.push({
   30. itemId: 'test' + i,
   31. position: {
   32. longitude: 118.11111 + Math.random() * 1 - 0.5,
   33. latitude: 32.11111 + Math.random() * 1 - 0.5
   34. },
   35. snippet: 'test' + i,
   36. title: 'test' + i
   37. })
   38. }
   39. let params: mapCommon.MassPointOverlayParams = {
   40. id: 'test',
   41. items: items,
   42. // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
   43. icon: 'icon/maps_blue_dot.png'
   44. }
   45. try {
   46. this.massPointOverlay = await this.mapController?.addMassPointOverlay(params);
   47. } catch (e) {
   48. console.error(this.TAG, `code:${e.code}, message:${e.message}`);
   49. }
   50. } else {
   51. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   52. }
   53. }
   54. }
   55. build() {
   56. Stack() {
   57. Column() {
   58. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback, })
   59. .width(this.mapWidth)
   60. .height(this.mapHeight);
   61. }.width('100%')
   62. }.height('100%')
   63. }
   64. }
   ```

### 海量点点击事件

```
1. // 初始化地图组件的监听事件管理接口
2. let mapEventManager = this.mapController?.getEventManager();
3. let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
4. console.info(`overlayId:${overlay.getId()},item :${JSON.stringify(item)}`);
5. }
6. // 启动海量点点击事件监听
7. mapEventManager.on('massPointOverlayClick', massCallback);
8. // 停止海量点点击事件监听,传入指定callback
9. mapEventManager.off('massPointOverlayClick', massCallback);
10. // 停止所有海量点点击事件监听，无需传入callback
11. mapEventManager.off('massPointOverlayClick');
```
