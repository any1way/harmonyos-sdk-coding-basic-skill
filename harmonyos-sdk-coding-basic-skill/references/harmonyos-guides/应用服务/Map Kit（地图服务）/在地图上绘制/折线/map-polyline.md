---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-polyline
title: 折线
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 折线
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:05+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:a908089f78b98450794bbc752d90902a4b0304f80996bdf6866ddcdcfc1ff129
---
## 场景介绍

本章节将向您介绍如何在地图上绘制折线、设置折线分段颜色、设置折线可渐变、绘制纹理。

折线主要用于展示步行、驾车、骑行等各类导航路线，同时可记录并呈现用户的运动轨迹及历史行程信息。此外，在区域边界标注、距离测量、管网线路布局以及活动路径可视化等场景中也有广泛应用。

5.0.3(15)开始，支持折线绘制纹理功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/gOI7CcR4RgqMXIGLc4ESnA/zh-cn_image_0000002592379400.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071003Z&HW-CC-Expire=86400&HW-CC-Sign=7F298740BD343CB55EB9F1B969E103CD19BCDE129D16A8964E9434B9ED5301BC "点击放大")

## 接口说明

添加折线功能主要由[MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>)、[addPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addpolyline>)和[MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)。

| 接口名 | 描述 |
| --- | --- |
| [MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>) | 折线参数。 |
| [addPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#addpolyline>)(options: [mapCommon.MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>)): Promise<[MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)> | 在地图上添加一条折线。 |
| [MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>) | 折线，支持更新和查询相关属性。 |

## 开发步骤

### 添加折线

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加折线，在callback方法中创建初始化参数并新建[MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)。

   ```
   1. @Entry
   2. @Component
   3. struct MapPolylineDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapPolyline?: map.MapPolyline;

   9. aboutToAppear(): void {
   10. // 地图初始化参数
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 31.98,
   15. longitude: 118.78
   16. },
   17. zoom: 14
   18. }
   19. };
   20. this.callback = async (err, mapController) => {
   21. if (!err) {
   22. this.mapController = mapController;

   24. // polyline初始化参数
   25. let polylineOption: mapCommon.MapPolylineOptions = {
   26. points: [
   27. { longitude: 118.78, latitude: 31.975 },
   28. { longitude: 118.78, latitude: 31.982 },
   29. { longitude: 118.79, latitude: 31.985 }
   30. ],
   31. clickable: true,
   32. startCap: mapCommon.CapStyle.BUTT,
   33. endCap: mapCommon.CapStyle.BUTT,
   34. geodesic: false,
   35. jointType: mapCommon.JointType.BEVEL,
   36. visible: true,
   37. width: 10,
   38. zIndex: 10,
   39. gradient: false
   40. }
   41. // 创建polyline
   42. try {
   43. this.mapPolyline = await this.mapController.addPolyline(polylineOption);
   44. } catch (e) {
   45. console.error(`Failed to create the mapPolyline, code is：${e.code}, message is ${e.message}`);
   46. }
   47. } else {
   48. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   49. }
   50. };
   51. }

   53. build() {
   54. Stack() {
   55. Column() {
   56. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   57. }.width('100%')
   58. }.height('100%')
   59. }
   60. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/EYinSbj8TrKdY2-HxGrR6Q/zh-cn_image_0000002622858909.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071003Z&HW-CC-Expire=86400&HW-CC-Sign=F92952921CFEADC8D0C0EB2A8E6B142F780A87A6BF4B6BAF783CBBFE90FA0D43 "点击放大")

### 设置折线分段颜色

方法一：新建折线时在[MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>)的colors属性中设置折线分段颜色值。

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { longitude:118.78, latitude:31.975 },
4. { longitude:118.78, latitude:31.982 },
5. { longitude:118.79, latitude:31.985 }
6. ],
7. clickable: true,
8. startCap: mapCommon.CapStyle.BUTT,
9. endCap: mapCommon.CapStyle.BUTT,
10. geodesic: false,
11. jointType: mapCommon.JointType.BEVEL,
12. visible: true,
13. width: 10,
14. zIndex: 10,
15. // 设置颜色
16. colors: [0xffffff00, 0xff000000],
17. gradient: false
18. };
```

方法二：调用[MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)的[setColors](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md#setcolors>)()方法。

```
1. let colors = [0xffffff00, 0xff000000];
2. this.mapPolyline.setColors(colors);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/iQVaTX1wQvGv33i-UrWmAw/zh-cn_image_0000002622699029.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071003Z&HW-CC-Expire=86400&HW-CC-Sign=B29A53DA8C8D8FA5AAFEA0D20D4F87D30B95D66C9BCEC79B5E829CE748811242 "点击放大")

### 设置折线可渐变

方法一：[MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>)的gradient属性设置为true。

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { longitude:118.78, latitude:31.975 },
4. { longitude:118.78, latitude:31.982 },
5. { longitude:118.79, latitude:31.985 }
6. ],
7. clickable: true,
8. startCap: mapCommon.CapStyle.BUTT,
9. endCap: mapCommon.CapStyle.BUTT,
10. geodesic: false,
11. jointType: mapCommon.JointType.BEVEL,
12. visible: true,
13. width: 10,
14. zIndex: 10,
15. colors: [0xffffff00, 0xff000000],
16. // 设置颜色折线可渐变
17. gradient: true
18. };
```

方法二：调用[MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)的[setGradient](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md#setgradient>)()方法。

```
1. this.mapPolyline.setGradient(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/NDHOSfefTF2bxBFFSndQ0Q/zh-cn_image_0000002592219468.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071003Z&HW-CC-Expire=86400&HW-CC-Sign=0ED860010D508113B9B08743573A47A8869D34622388F32BE3A86B9A26DF474E "点击放大")

### 绘制纹理

方法一：新建折线时在[MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>)的customTexture属性设置折线纹理。

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { latitude: 32.220750, longitude: 118.788765 },
4. { latitude: 32.120750, longitude: 118.788765 },
5. { latitude: 32.020750, longitude: 118.788765 },
6. { latitude: 31.920750, longitude: 118.788765 },
7. { latitude: 31.820750, longitude: 118.788765 }
8. ],
9. clickable: true,
10. jointType: mapCommon.JointType.DEFAULT,
11. width: 20,
12. // 图标需存放在resources/rawfile目录下
13. customTexture: "icon/naviline_arrow.png"
14. }
```

方法二：调用[MapPolyline](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md>)的[setCustomTexture](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapPolyline)/map-map-mappolyline.md#setcustomtexture>)方法。

```
1. await this.mapPolyline.setCustomTexture("icon/naviline_arrow.png");
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/5LuR6n1KTqy8mIQrU6w4ZQ/zh-cn_image_0000002592379402.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071003Z&HW-CC-Expire=86400&HW-CC-Sign=ADDDBEA1A54307BFAE95A98343EAF9EC22DC6A7004472C79C371E40FEB12E200 "点击放大")

### 折线设置分段纹理

新建折线时利用在[MapPolylineOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappolylineoptions>)的customTextures和customTextureIndexes属性设置折线分段纹理。

```
1. import { image } from '@kit.ImageKit';

3. // 数组存放图片内容
4. let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
5. // 图标存放在resources/rawfile，'icon/img.png'参数值传入rawfile文件夹下的相对路径
6. customTextures.push('icon/img.png');
7. customTextures.push('icon/img_1.png');
8. let cusIndexNumber: Array<number> = new Array();
9. // cusIndexNumber数组长度与折线点数量必须相同，数组元素内容与customTextures下标相对应，图片从数组第二个元素开始选择
10. cusIndexNumber.push(0, 0, 1);
11. // polyline初始化参数
12. let polylineOption: mapCommon.MapPolylineOptions = {
13. points: [
14. { longitude: 118.78, latitude: 31.975 },
15. { longitude: 118.78, latitude: 31.982 },
16. { longitude: 118.79, latitude: 31.985 }
17. ],
18. clickable: true,
19. startCap: mapCommon.CapStyle.BUTT,
20. endCap: mapCommon.CapStyle.BUTT,
21. jointType: mapCommon.JointType.BEVEL,
22. width: 30,
23. // 图标需存放在resources/rawfile目录下
24. customTextures: customTextures,
25. customTextureIndexes: cusIndexNumber
26. };
27. let mapPolyline = await this.mapController.addPolyline(polylineOption);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WOI6HZRpRIy_uf_dtW2C_g/zh-cn_image_0000002622858911.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071003Z&HW-CC-Expire=86400&HW-CC-Sign=27996FE695D3639A21AA46F3DEA54E0A9CAB7FA145515D414C1792DF895058FB "点击放大")
