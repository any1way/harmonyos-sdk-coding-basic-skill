---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps
title: 通过地图应用实现导航等能力
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 通过地图应用实现导航等能力
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:42+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:bbf9fc304c33a2432512b1720826824d058dc287a7b9ca0bd3439271751ec76c
---
## 场景介绍

从5.0.3(15)开始，支持地图应用首页、搜索地点、查看地点详情、规划路线和进行导航功能；从6.0.1(21)开始，支持地图应用发起打车功能；从6.1.1(24)开始，打开地图应用查看地点详情支持终点描述，支持拉起地图应用离线地图管理页面。

本章节将向您介绍如何打开地图应用实现如下能力：

* 打开地图应用首页
* 打开地图应用搜索地点
* 打开地图应用查看地点详情
* 打开地图应用规划路线
* 打开地图应用进行导航
* 打开地图应用发起打车
* 打开地图应用离线地图管理页面

## 接口说明

调用地图应用的功能主要通过[petalMaps](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md>)命名空间下的[openMapHomePage](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaphomepage>)、[openMapTextSearch](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaptextsearch>)、[openMapPoiDetail](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmappoidetail>)、[openMapRoutePlan](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaprouteplan>)、[openMapNavi](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapnavi>)、[openMapTaxi](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaptaxi>)、[openMapOfflineDataManagement](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapofflinedatamanagement>)等接口实现，更多接口及使用方法请参见[接口文档](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md>)。

| 接口说明 | 描述 |
| --- | --- |
| [TextSearchParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#textsearchparams>) | 文本搜索的参数。 |
| [PoiDetailParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#poidetailparams>) | POI详情的参数。 |
| [RoutePlanParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#routeplanparams>) | 路线规划的参数。 |
| [NaviParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#naviparams>) | 导航的参数。 |
| [TaxiParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#taxiparams>) | 打车的参数。 |
| [OfflineDataParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#offlinedataparams>) | 离线地图管理参数。 |
| [openMapHomePage](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaphomepage>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>)): Promise<void> | 打开地图应用首页。 |
| [openMapTextSearch](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaptextsearch>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), textSearchParams: [TextSearchParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#textsearchparams>)): Promise<void> | 打开地图应用搜索地点。 |
| [openMapPoiDetail](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmappoidetail>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), poiDetailParams: [PoiDetailParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#poidetailparams>)): Promise<void> | 打开地图应用查看地点详情。 |
| [openMapRoutePlan](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaprouteplan>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), routePlanParams: [RoutePlanParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#routeplanparams>)): Promise<void> | 打开地图应用规划路线。 |
| [openMapNavi](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapnavi>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), naviParams: [NaviParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#naviparams>)): Promise<void> | 打开地图应用进行导航。 |
| [openMapTaxi](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaptaxi>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), taxiParams: [TaxiParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#taxiparams>)): Promise<void> | 打开地图应用打车页面。 |
| [openMapOfflineDataManagement](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapofflinedatamanagement>)(context: [common.Context](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), offlineDataParams: [OfflineDataParams](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#offlinedataparams>)): Promise<void> | 打开地图应用的离线地图管理页面。 |

## 地图应用使用的坐标类型

在国内站点，中国大陆使用GCJ02坐标系，中国台湾使用WGS84坐标系。

在海外站点，统一使用WGS84坐标系。坐标系转换参考：[坐标纠偏](../地图计算工具/坐标纠偏/map-convert-coordinate.md)。

## 开发步骤

导入相关模块

```
1. import { petalMaps } from '@kit.MapKit'
```

### 打开地图应用首页

通过[openMapHomePage](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaphomepage>)，打开地图应用首页。

```
1. try {
2. await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
3. } catch (e) {
4. console.error(`code:${e.code}, message:${e.message}`);
5. }
```

**图1** 打开地图应用首页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/v61vz3NvTeOmZ72uGUMxrQ/zh-cn_image_0000002622858927.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=A74D0390E509D4063F765EAA69F0403FFB57E9AD7112D5CD1056605E69023BF8 "点击放大")

### 打开地图应用进行地点搜索

通过[openMapTextSearch](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaptextsearch>)，传入搜索目标名称，打开地图应用进行地点搜索。

```
1. try {
2. let params: petalMaps.TextSearchParams = {
3. destinationName: '云谷'
4. };
5. await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
6. } catch (e) {
7. console.error(`code:${e.code}, message:${e.message}`);
8. }
```

**图2** 打开地图应用进行地点搜索

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/xkWVVeqXTFuWHSwsPHj4ag/zh-cn_image_0000002622699047.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=7A59A1E059847AC990C53AEE7745F36018569490CD05B92BC6BF9E13D67D7A85 "点击放大")

### 打开地图应用查看地点详情

通过[openMapPoiDetail](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmappoidetail>)，传入地点的经纬度，打开地图应用查看地点详情。

```
1. try {
2. let params: petalMaps.PoiDetailParams = {
3. destinationPosition: {
4. latitude: 31.968789,
5. longitude: 118.798537
6. },
7. destinationName: '标记点',
8. zoom: 17,
9. coordinateType: mapCommon.CoordinateType.GCJ02,
10. destinationAddress: '这是我选择的演示名称'
11. };
12. await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
13. } catch (e) {
14. console.error(`code:${e.code}, message:${e.message}`);
15. }
```

**图3** 打开地图应用查看地点详情

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/62FxAR0dRKuw_iVe5nvF4g/zh-cn_image_0000002592219486.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=3A7B4C9C2F46EDA8E77CBDE3FC79E47BCBCAA3F178710084CA4D589AD92B7437 "点击放大")

### 打开地图应用规划路线

通过[openMapRoutePlan](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaprouteplan>)，传入终点经纬度，打开地图应用规划路线。

```
1. try {
2. let params: petalMaps.RoutePlanParams = {
3. destinationPosition: {
4. latitude: 31.983015468224288,
5. longitude: 118.78058590757131
6. }
7. };
8. await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }
```

**图4** 打开地图应用规划路线

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/eZdDry7yQ9C30zbaQwsnCA/zh-cn_image_0000002592379420.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=5CDF3A01B0A0852F19F08469EB33C4B008270246EB29FCC2175F480A8C1D6B67 "点击放大")

### 打开地图应用进行导航

通过[openMapNavi](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapnavi>)，传入终点经纬度，打开地图应用发起导航。

```
1. try {
2. let params: petalMaps.NaviParams = {
3. destinationPosition: {
4. latitude: 31.983015468224288,
5. longitude: 118.78058590757131
6. }
7. };
8. await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }
```

**图5** 打开地图应用进行导航

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/HNcUzIIFQm2_ZT28UTse5A/zh-cn_image_0000002622858929.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=BECF08F84E74714A74161C7D986FCBB175DFB2BE6457409D2308D920738277F5 "点击放大")

### 打开地图应用打车页面

通过[openMapTaxi](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmaptaxi>)，传入终点经纬度，打开地图应用发起打车。

```
1. try {
2. let params: petalMaps.TaxiParams = {
3. destinationPosition: {
4. latitude: 31.983015468224288,
5. longitude: 118.78058590757131
6. }
7. };
8. await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }
```

**图6** 打开地图应用进行打车

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/qXpv312qSlyda5w9yVg53g/zh-cn_image_0000002622699049.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=7E1C17A60E4FB00A22FC5D85BF14950B108769745FE05C8A20955D261E524508 "点击放大")

### 打开地图应用离线地图管理页面

通过[openMapOfflineDataManagement](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapofflinedatamanagement>)，传入离线地图管理参数，打开地图应用离线地图管理页面。

```
1. try {
2. // 打开地图应用手表离线地图管理页面
3. let params: petalMaps.OfflineDataParams = {
4. scenarios: 'WATCH',
5. // 推荐下载离线地图的地区集合
6. recommendedRegionIds: ['1026355368865976081']
7. };
8. await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }

13. try {
14. // 打开地图应用地图资源（手机离线地图）管理页面
15. let params: petalMaps.OfflineDataParams = {
16. scenarios: 'PHONE',
17. // 推荐下载离线地图的地区集合
18. recommendedRegionIds: ['1026355368865976081']
19. };
20. await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
21. } catch (e) {
22. console.error(`code:${e.code}, message:${e.message}`);
23. }

25. try {
26. // 打开地图应用导航语音管理页面
27. let params: petalMaps.OfflineDataParams = {
28. scenarios: 'VOICE'
29. };
30. await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
31. } catch (e) {
32. console.error(`code:${e.code}, message:${e.message}`);
33. }
```

**图7** 打开地图应用手表离线地图管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JFULLEj-RoGg5ouDnWd5IA/zh-cn_image_0000002592219488.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=1F7852D7F1C1891D31B682CD35B92A130C0D45A68E161A62A1428F6D2C9B27A2 "点击放大")

**图8** 打开地图应用地图资源（手机离线地图）管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/1a6LYewyQX-iqfGwpfCOdg/zh-cn_image_0000002592379422.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=8221D54225DEBC5C7FBA69B9DE184C60A781A39EB1BDDF3137DC47906809C570 "点击放大")

**图9** 打开地图应用导航语音管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/tJRLYksxQ5STtSLJRBBp9Q/zh-cn_image_0000002622858931.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071041Z&HW-CC-Expire=86400&HW-CC-Sign=D87C4B1D552AF720F003AC366F81F4E330538B5DE0FAFDD7D09EE920CE3AA142 "点击放大")
