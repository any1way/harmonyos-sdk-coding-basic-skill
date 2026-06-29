---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-calculate-distance
title: 距离计算
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图计算工具 > 距离计算
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:45+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:d1c5b1938be99e649e9e2235d578a629acdf9188ffbb8cd69f1bfa26e678e27f
---
## 场景介绍

根据用户指定的两个经纬度坐标点，计算这两个点间的直线距离，单位为米。

## 接口说明

以下是距离计算功能相关接口，主要由[map](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/模块描述/map-module-desc.md>)命名空间下的[calculateDistance](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Functions/map-map-functions.md#calculatedistance>)方法提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Functions/map-map-functions.md#calculatedistance>)。

| 接口名 | 描述 |
| --- | --- |
| [mapCommon.LatLng](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#latlng>) | 经纬度对象。 |
| [calculateDistance](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Functions/map-map-functions.md#calculatedistance>)(from: [mapCommon.LatLng](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#latlng>), to: [mapCommon.LatLng](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#latlng>)): number | 计算坐标点之间的距离。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { map, mapCommon } from '@kit.MapKit';
   ```
2. 初始化需要计算的坐标，调用[calculateDistance](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Functions/map-map-functions.md#calculatedistance>)方法计算距离。

   ```
   1. let fromLatLng: mapCommon.LatLng = {
   2. latitude: 38,
   3. longitude: 118
   4. };
   5. let toLatLng: mapCommon.LatLng = {
   6. latitude: 39,
   7. longitude: 119
   8. };
   9. // 计算坐标点之间的距离
   10. let distance = map.calculateDistance(fromLatLng, toLatLng);
   ```
