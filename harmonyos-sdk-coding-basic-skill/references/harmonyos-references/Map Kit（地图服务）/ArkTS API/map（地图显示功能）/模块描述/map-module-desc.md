---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-module-desc
title: 模块描述
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > 模块描述
category: harmonyos-references
scraped_at: 2026-06-01T16:35:33+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:cd31bb3d6ae0103a398a4978fe9ac88b72b3e86cac883b75eb271c6e214d3afe
---
map（地图显示功能）为开发者提供易于上手的接口，开发者可以通过相关接口便捷地在HarmonyOS应用/元服务中加入地图相关的功能，包括显示地图、在地图上绘制（覆盖物）、添加动画、与地图交互、更新地图状态、常用工具函数等功能。

该模块提供以下地图常用功能：

* [MapComponentController](<../Class (MapComponentController)/map-map-mapcomponentcontroller.md>)：显示地图，与地图有关的所有方法从此处接入。

地图覆盖物：

* [Marker](<../Interface (Marker)/map-map-marker.md>)：标记。
* [MapPolyline](<../Interface (MapPolyline)/map-map-mappolyline.md>)：折线。
* [MapArc](<../Interface (MapArc)/map-map-maparc.md>)：弧线。
* [MapPolygon](<../Interface (MapPolygon)/map-map-mappolygon.md>)：多边形。
* [MapCircle](<../Interface (MapCircle)/map-map-mapcircle.md>)：圆形。
* [PointAnnotation](<../Interface (PointAnnotation)/map-map-pointannotation.md>)：点注释。
* [Bubble](<../Interface (Bubble)/map-map-bubble.md>)：气泡。
* [ClusterOverlay](<../Interface (ClusterOverlay)/map-map-clusteroverlay.md>)：点聚合。
* [ImageOverlay](<../Interface (ImageOverlay)/map-map-imageoverlay.md>)：图片覆盖物。
* [BuildingOverlay](<../Interface (BuildingOverlay)/map-map-buildingoverlay.md>)：3D建筑。
* [TraceOverlay](<../Interface (TraceOverlay)/map-map-traceoverlay.md>)：动态轨迹。
* [TileOverlay](<../Interface (TileOverlay)/map-map-tileoverlay.md>)：瓦片图层。
* [Heatmap](<../Interface (Heatmap)/map-map-heatmap.md>)：热力图。
* [MvtOverlay](<../Interface (MvtOverlay)/map-map-mvtoverlay.md>)：矢量图层。
* [FlowFieldOverlay](<../Interface (FlowFieldOverlay)/map-map-flowfieldoverlay.md>)：流场图层。
* [MassPointOverlay](<../Interface (MassPointOverlay)/map-map-masspointoverlay.md>)：海量点图层。

添加动画：

* [Animation](<../Class (Animation)/map-map-animation.md>)：动画抽象类。
* [AlphaAnimation](<../Class (AlphaAnimation)/map-map-alphaanimation.md>)：控制透明度的动画类。
* [RotateAnimation](<../Class (RotateAnimation)/map-map-rotateanimation.md>)：控制旋转的动画类。
* [ScaleAnimation](<../Class (ScaleAnimation)/map-map-scaleanimation.md>)：控制缩放的动画类。
* [TranslateAnimation](<../Class (TranslateAnimation)/map-map-translateanimation.md>)：控制移动的动画类。
* [FontSizeAnimation](<../Class (FontSizeAnimation)/map-map-fontsizeanimation.md>)：控制字体大小的动画类。
* [PlayImageAnimation](<../Class (PlayImageAnimation)/map-map-playimageanimation.md>)：控制多张图片的帧动画类。
* [AnimationSet](<../Class (AnimationSet)/map-map-animationset.md>)：动画类集合。

与地图交互：

* [MapEventManager](<../Interface (MapEventManager)/map-map-mapeventmanager.md>)：地图监听事件管理器。

更新地图状态：

* [newLatLng](../Functions/map-map-functions.md#newlatlng)：设置地图的中心点和缩放层级。
* [newLatLngBounds](../Functions/map-map-functions.md#newlatlngbounds)：设置地图经纬度范围、地图区域和边界之间的距离。
* [scrollBy](../Functions/map-map-functions.md#scrollby)：按像素移动地图中心点。
* [zoomBy](../Functions/map-map-functions.md#zoomby)：根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。
* [zoomIn](../Functions/map-map-functions.md#zoomin)：放大地图缩放级别，在当前地图显示的级别基础上加1。
* [zoomOut](../Functions/map-map-functions.md#zoomout)：缩小地图缩放级别，在当前地图显示的级别基础上减1。
* [zoomTo](../Functions/map-map-functions.md#zoomto)：设置地图缩放级别。

常用工具函数：

* [calculateDistance](../Functions/map-map-functions.md#calculatedistance)：计算坐标点之间的距离。
* [convertCoordinate](../Functions/map-map-functions.md#convertcoordinate)：坐标系转换，使用Promise异步回调。
* [convertCoordinateSync](../Functions/map-map-functions.md#convertcoordinatesync)：坐标系转换。
* [rectifyCoordinate](../Functions/map-map-functions.md#rectifycoordinate)：根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```
