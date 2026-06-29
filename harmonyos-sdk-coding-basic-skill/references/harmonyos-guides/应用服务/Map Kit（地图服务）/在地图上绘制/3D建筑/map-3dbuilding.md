---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-3dbuilding
title: 3D建筑
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 3D建筑
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:15+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:55c4dbb8717491ed1530db45b9e26ec2fe0b7081ba4f7c9a87c89b98fe54dc05
---
## 场景介绍

本章节将向您介绍如何在地图上绘制3D建筑。

3D建筑主要用于展示城市建筑外观，帮助用户直观了解城市面貌，同时还可应用于楼盘、小区等三维模型的呈现，辅助用户全面了解周边环境。此外，在导航定位、旅游导览以及商业选址分析等场景中也有广泛应用，能够为用户提供更加真实、直观的地图体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/SwABwySiToyacDZ7R2lzyw/zh-cn_image_0000002592379410.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071013Z&HW-CC-Expire=86400&HW-CC-Sign=E5F25D1904554886ADD682E21ACA179ADB2ADCB345B9F55F23A275D7ADEBF530 "点击放大")

## 接口说明

添加3D建筑功能主要由[BuildingOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#buildingoverlayparams>)、[addBuildingOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addbuildingoverlay>)和[BuildingOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (BuildingOverlay)/map-map-buildingoverlay.md>)提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (BuildingOverlay)/map-map-buildingoverlay.md>)。

| 接口名 | 描述 |
| --- | --- |
| [BuildingOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#buildingoverlayparams>) | 3D建筑参数。 |
| [addBuildingOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addbuildingoverlay>)(params: [mapCommon.BuildingOverlayParams](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#buildingoverlayparams>)): Promise<[BuildingOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (BuildingOverlay)/map-map-buildingoverlay.md>)> | 在地图上添加3D建筑。 |
| [BuildingOverlay](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (BuildingOverlay)/map-map-buildingoverlay.md>) | 3D建筑，支持更新和查询相关属性。 |

## 开发步骤

### 添加3D建筑

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加3D建筑。

   ```
   1. @Entry
   2. @Component
   3. struct BuildingOverlayDemo {
   4. private TAG = "OHMapSDK_BuildingOverlayDemo";
   5. private mapOptions?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. private buildingOverlay?: map.BuildingOverlay;

   10. aboutToAppear(): void {
   11. // 初始化地图参数
   12. this.mapOptions = {
   13. position: {
   14. target: {
   15. latitude: 31.984794,
   16. longitude: 118.765865
   17. },
   18. zoom: 18
   19. },
   20. scaleControlsEnabled: true
   21. }

   23. this.callback = async (err, mapController) => {
   24. console.info(this.TAG, "addBuildingOverlay");
   25. if (!err) {
   26. this.mapController = mapController;
   27. // 3D建筑底面坐标集合
   28. let points: Array<mapCommon.LatLng> = [
   29. {
   30. latitude: 31.984794,
   31. longitude: 118.765865
   32. },
   33. {
   34. latitude: 31.98468,
   35. longitude: 118.766076
   36. },
   37. {
   38. latitude: 31.98472,
   39. longitude: 118.766116
   40. },
   41. {
   42. latitude: 31.98463,
   43. longitude: 118.766292
   44. },
   45. {
   46. latitude: 31.984586,
   47. longitude: 118.766251
   48. },
   49. {
   50. latitude: 31.984536,
   51. longitude: 118.766344
   52. },
   53. {
   54. latitude: 31.984633,
   55. longitude: 118.766446
   56. },
   57. {
   58. latitude: 31.9848,
   59. longitude: 118.766285
   60. },
   61. {
   62. latitude: 31.984925,
   63. longitude: 118.766312
   64. },
   65. {
   66. latitude: 31.985282,
   67. longitude: 118.766661
   68. },
   69. {
   70. latitude: 31.985438,
   71. longitude: 118.766419
   72. },
   73. {
   74. latitude: 31.985801,
   75. longitude: 118.766755
   76. },
   77. {
   78. latitude: 31.985856,
   79. longitude: 118.766504
   80. },
   81. {
   82. latitude: 31.985785,
   83. longitude: 118.766434
   84. },
   85. {
   86. latitude: 31.985821,
   87. longitude: 118.766278
   88. },
   89. {
   90. latitude: 31.985897,
   91. longitude: 118.766311
   92. },
   93. {
   94. latitude: 31.985944,
   95. longitude: 118.766095
   96. },
   97. {
   98. latitude: 31.985909,
   99. longitude: 118.766069
   100. },
   101. {
   102. latitude: 31.985794,
   103. longitude: 118.765989
   104. },
   105. {
   106. latitude: 31.9857,
   107. longitude: 118.766029
   108. },
   109. {
   110. latitude: 31.985658,
   111. longitude: 118.766164
   112. },
   113. {
   114. latitude: 31.985647,
   115. longitude: 118.766271
   116. },
   117. {
   118. latitude: 31.985574,
   119. longitude: 118.766297
   120. },
   121. {
   122. latitude: 31.985458,
   123. longitude: 118.766285
   124. },
   125. {
   126. latitude: 31.985271,
   127. longitude: 118.766002
   128. },
   129. {
   130. latitude: 31.985219,
   131. longitude: 118.766002
   132. },
   133. {
   134. latitude: 31.985135,
   135. longitude: 118.766029
   136. },
   137. {
   138. latitude: 31.985093,
   139. longitude: 118.766083
   140. },
   141. {
   142. latitude: 31.985019,
   143. longitude: 118.766109
   144. },
   145. {
   146. latitude: 31.984978,
   147. longitude: 118.766083
   148. },
   149. {
   150. latitude: 31.984794,
   151. longitude: 118.765865
   152. }
   153. ];
   154. points.reverse();
   155. // 3D建筑参数
   156. let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
   157. {
   158. // 3D建筑的范围参数（点为顺时针绘制）
   159. points: points,
   160. // 3D建筑的高度
   161. totalHeight: 51,
   162. // 3D建筑的选中楼层高度
   163. floorBottomHeight: 33,
   164. // 3D建筑的顶部颜色
   165. topFaceColor: 0xffa4b8f7,
   166. // 3D建筑的侧面颜色
   167. sideFaceColor: 0x44a4b8f7,
   168. // 3D建筑的选中楼层颜色
   169. floorColor: 0xff000000,
   170. // 3D建筑的展示层级
   171. showLevel: 14,
   172. // 3D建筑选中楼层从底部升起的动画时长
   173. animationDuration: 5000,
   174. // 3D建筑侧面的纹理，需要替换您自己的资源图片，存放在resources/base/media目录下
   175. sideTexture: { image: $r("app.media.side_tex"), height: 3, width: 3 },
   176. // 3D建筑选中楼层的纹理，需要替换您自己的资源图片，存放在resources/base/media目录下
   177. floorTexture: { image: $r("app.media.floor_tex"), height: 3, width: 3 }
   178. };
   179. let cameraUpdate = map.newCameraPosition({
   180. target: {
   181. latitude: 31.984794,
   182. longitude: 118.765865
   183. },
   184. zoom: 18,
   185. tilt: 70
   186. });
   187. // 将地图镜头移动到3D建筑区域
   188. this.mapController?.moveCamera(cameraUpdate);
   189. // 新建3D建筑
   190. try {
   191. this.buildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
   192. } catch (e) {
   193. console.error(`Failed to create the buildingOverlay, code is：${e.code}, message is ${e.message}`);
   194. }
   195. } else {
   196. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   197. }
   198. }
   199. }

   201. build() {
   202. Stack() {
   203. Column() {
   204. MapComponent({
   205. mapOptions: this.mapOptions,
   206. mapCallback: this.callback,
   207. }).width('100%').height('100%');
   208. }.width('100%')
   209. }.height('100%')
   210. }
   211. }
   ```
