---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-dyntrajectories
title: 动态轨迹
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 动态轨迹
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:19+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:b4116f2027bf2e887eb2e056836b347345ffecb28f026369b7cec847be10df73
---
## 场景介绍

本章节将向您介绍如何在地图上绘制动态轨迹。

动态轨迹功能可用于实时展示车辆行驶路径、用户运动轨迹等，帮助用户直观了解行程信息，并支持轨迹回放、暂停、删除等操作，广泛应用于物流跟踪、出行导航、运动监测等领域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ERo4cCr4TF-aV5zbbDiESg/zh-cn_image_0000002622858919.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071014Z&HW-CC-Expire=86400&HW-CC-Sign=53B984EE80E7226FDAE760D780C58A471E3AEC7586F295A15372982F65B0707A "点击放大")

## 接口说明

绘制动态轨迹功能主要由[TraceOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#traceoverlayparams>)、[addTraceOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addtraceoverlay>)、[Marker](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (Marker)/map-map-marker.md>)和[TraceOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (TraceOverlay)/map-map-traceoverlay.md>)提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (TraceOverlay)/map-map-traceoverlay.md>)。

| 接口名 | 描述 |
| --- | --- |
| [TraceOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#traceoverlayparams>) | 动态轨迹参数。 |
| [addTraceOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addtraceoverlay>)(params: [mapCommon.TraceOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#traceoverlayparams>), markers?: Array<[Marker](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (Marker)/map-map-marker.md>)>): Promise<[TraceOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (TraceOverlay)/map-map-traceoverlay.md>)> | 绘制动态轨迹。 |
| [Marker](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (Marker)/map-map-marker.md>) | 动态轨迹的一组标记。 |
| [TraceOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (TraceOverlay)/map-map-traceoverlay.md>) | 动态轨迹，支持暂停和删除等功能。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 绘制动态轨迹。

   ```
   1. @Entry
   2. @Component
   3. struct TraceOverlayDemo {
   4. private TAG = "OHMapSDK_TraceOverlayDemo";
   5. private mapOptions?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;

   9. aboutToAppear(): void {
   10. // 初始化地图参数
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 31.99227173519985,
   15. longitude: 118.7622219990476
   16. },
   17. zoom: 16
   18. },
   19. scaleControlsEnabled: true
   20. }

   22. this.callback = async (err, mapController) => {
   23. console.info(this.TAG, "mapCallback err=" + JSON.stringify(err) +
   24. "; mapController=" + JSON.stringify(mapController));
   25. if (!err) {
   26. this.mapController = mapController;
   27. // marker1的参数
   28. let markerOptions1: mapCommon.MarkerOptions = {
   29. position: {
   30. latitude: 31.99227173519985,
   31. longitude: 118.7622219990476
   32. },
   33. // 存放在resources/base/media目录下
   34. icon: $r("app.media.track_setting_sport_map_marker_22"),
   35. anchorU: 0.5,
   36. anchorV: 1,
   37. visible: true
   38. };
   39. // 新增marker1
   40. let markerBoy1 = await this.mapController.addMarker(markerOptions1);
   41. let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
   42. boyImages1.setDuration(1000);
   43. let resourceArray: Array<Resource> = new Array();
   44. // 每一帧展示的图片，需要替换您自己的资源图片，存放在resources/base/media目录下
   45. resourceArray.push($r("app.media.side_0"));
   46. resourceArray.push($r("app.media.side_1"));
   47. resourceArray.push($r("app.media.side_2"));
   48. resourceArray.push($r("app.media.side_3"));
   49. resourceArray.push($r("app.media.side_4"));
   50. resourceArray.push($r("app.media.side_5"));
   51. resourceArray.push($r("app.media.side_6"));
   52. resourceArray.push($r("app.media.side_7"));
   53. resourceArray.push($r("app.media.side_8"));
   54. resourceArray.push($r("app.media.side_9"));
   55. resourceArray.push($r("app.media.side_10"));
   56. resourceArray.push($r("app.media.side_11"));
   57. resourceArray.push($r("app.media.side_12"));
   58. resourceArray.push($r("app.media.side_13"));
   59. resourceArray.push($r("app.media.side_14"));
   60. resourceArray.push($r("app.media.side_15"));
   61. resourceArray.push($r("app.media.side_16"));
   62. resourceArray.push($r("app.media.side_17"));
   63. resourceArray.push($r("app.media.side_18"));
   64. resourceArray.push($r("app.media.side_19"));
   65. resourceArray.push($r("app.media.side_20"));
   66. await boyImages1.addImages(resourceArray);
   67. boyImages1.setRepeatCount(-1);

   69. // marker1添加动画
   70. markerBoy1.setAnimation(boyImages1);
   71. markerBoy1.startAnimation();

   73. // marker2的参数
   74. let markerOptions2: mapCommon.MarkerOptions = {
   75. position: {
   76. latitude: 31.99227173519985,
   77. longitude: 118.7622219990476
   78. },
   79. icon: $r("app.media.track_setting_sport_map_marker_22"),
   80. anchorU: 0.5,
   81. anchorV: 1,
   82. visible: false
   83. };
   84. // 新增marker2
   85. let markerBoy2 = await this.mapController.addMarker(markerOptions2);
   86. let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
   87. boyImages2.setDuration(1000);
   88. let resourceArray2: Array<Resource> = new Array();
   89. // 需要替换您自己的资源图片，存放在resources/base/media目录下
   90. resourceArray2.push($r("app.media.behavior_front_cycling_boy_000"));
   91. resourceArray2.push($r("app.media.behavior_front_cycling_boy_001"));
   92. resourceArray2.push($r("app.media.behavior_front_cycling_boy_002"));
   93. resourceArray2.push($r("app.media.behavior_front_cycling_boy_003"));
   94. resourceArray2.push($r("app.media.behavior_front_cycling_boy_004"));
   95. resourceArray2.push($r("app.media.behavior_front_cycling_boy_005"));
   96. resourceArray2.push($r("app.media.behavior_front_cycling_boy_006"));
   97. resourceArray2.push($r("app.media.behavior_front_cycling_boy_007"));
   98. resourceArray2.push($r("app.media.behavior_front_cycling_boy_008"));
   99. resourceArray2.push($r("app.media.behavior_front_cycling_boy_009"));
   100. resourceArray2.push($r("app.media.behavior_front_cycling_boy_010"));
   101. resourceArray2.push($r("app.media.behavior_front_cycling_boy_011"));
   102. resourceArray2.push($r("app.media.behavior_front_cycling_boy_012"));
   103. resourceArray2.push($r("app.media.behavior_front_cycling_boy_013"));
   104. resourceArray2.push($r("app.media.behavior_front_cycling_boy_014"));
   105. resourceArray2.push($r("app.media.behavior_front_cycling_boy_015"));
   106. resourceArray2.push($r("app.media.behavior_front_cycling_boy_016"));
   107. resourceArray2.push($r("app.media.behavior_front_cycling_boy_017"));
   108. resourceArray2.push($r("app.media.behavior_front_cycling_boy_018"));
   109. await boyImages2.addImages(resourceArray2);
   110. boyImages2.setRepeatCount(-1);
   111. // marker2添加动画
   112. markerBoy2.setAnimation(boyImages2);
   113. markerBoy2.startAnimation();

   115. let points: Array<mapCommon.LatLng> = new Array();
   116. points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
   117. points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
   118. points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
   119. points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
   120. points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
   121. points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
   122. points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
   123. points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
   124. points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
   125. points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
   126. points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
   127. points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
   128. points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
   129. points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
   130. points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
   131. points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
   132. points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
   133. points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
   134. points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
   135. points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
   136. points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
   137. points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
   138. points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
   139. points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
   140. points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

   142. // 动态轨迹的入参
   143. let traceOptions: mapCommon.TraceOverlayParams = {
   144. // 轨迹点
   145. points: points,
   146. // 轨迹的动画时长
   147. animationDuration: 5000,
   148. // 相机是否跟随动画移动
   149. isMapMoving: true,
   150. // 轨迹的颜色
   151. color: 0xAAFFAA00,
   152. // 轨迹的宽度
   153. width: 20,
   154. // 轨迹的动画回调（回调轨迹点的index）
   155. animationCallback: (pointIndex) => {
   156. // 换成骑行
   157. if (pointIndex === 10) {
   158. markerBoy1.setVisible(false);
   159. markerBoy2.setVisible(true);
   160. }
   161. }
   162. }
   163. let markers: Array<map.Marker> = new Array();
   164. markers.push(markerBoy1, markerBoy2);
   165. // 新增轨迹点动画
   166. try {
   167. let traceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);
   168. } catch (e) {
   169. console.error(`Failed to create the traceOverlay, code is：${e.code}, message is ${e.message}`);
   170. }
   171. } else {
   172. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   173. }
   174. }
   175. }

   177. build() {
   178. Stack() {
   179. Column() {
   180. MapComponent({
   181. mapOptions: this.mapOptions,
   182. mapCallback: this.callback,
   183. }).width('100%').height('100%');
   184. }.width('100%')
   185. }.height('100%')
   186. }
   187. }
   ```
