---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location
title: 显示我的位置
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 显示我的位置
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:47+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:cd3127264e1b98c5d0d0d60d7403770b68f324885581c31de124d51a22984564
---
## 场景介绍

从6.0.1(21)开始，支持更改我的位置相对覆盖物的顺序。

本章节将向您介绍如何开启和展示“我的位置”功能，“我的位置”指的是进入地图后点击“我的位置”显示当前位置点的功能。效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Wc8v1GRJRGKBgOPitR_R2w/zh-cn_image_0000002592379378.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070749Z&HW-CC-Expire=86400&HW-CC-Sign=613B58286753AC43390E1A5A8B0079128D7FC675F1EFE11728BCAB809D714950 "点击放大")

## 接口说明

“我的位置”功能主要由[MapComponentController](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md>)的方法实现，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationenabled>)。

| 方法名 | 描述 |
| --- | --- |
| [setMyLocationEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationenabled>)(myLocationEnabled: boolean): void | “我的位置”图层功能开关，默认使用系统的连续定位能力显示用户位置。开关打开后，“我的位置”按钮默认显示在地图的右下角。点击“我的位置”按钮，将会在屏幕中心显示当前定位，以蓝色圆点的形式呈现。 |
| [setMyLocationControlsEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled>)(enabled: boolean): void | 设置是否启用“我的位置”按钮。只显示按钮，在不开启“我的位置”图层功能的情况下，点击按钮没反应。 |
| [setMyLocation](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocation>)(location: [geoLocationManager.Location](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.geoLocationManager (位置服务)/js-apis-geolocationmanager.md#location>)): void | 设置“我的位置”坐标。  如果不使用Map Kit提供的默认定位行为，可以通过[Location Kit](<../../../../../harmonyos-references/Location Kit（位置服务）/location-api.md>)获取用户位置后，传给Map Kit。 |
| [setMyLocationStyle](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationstyle>)(style: [mapCommon.MyLocationStyle](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mylocationstyle>)): Promise<void> | 设置“我的位置”样式。 |
| [on](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapEventManager)/map-map-mapeventmanager.md#onmylocationbuttonclick>)(type: 'myLocationButtonClick', callback: Callback<void>): void | 监听“我的位置”按钮点击事件。 |
| [off](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapEventManager)/map-map-mapeventmanager.md#offmylocationbuttonclick>)(type: 'myLocationButtonClick', callback?: Callback<void>): void | 取消监听“我的位置”按钮点击事件。 |

## 开发步骤

### 开启“我的位置”按钮

1. 在启用“我的位置”功能前，开发者应确保应用已申请并获得用户定位权限，以便正确显示用户当前位置。

   申请ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限，您需要在module.json5配置文件中声明所需要的权限，具体可参考[声明权限](../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

   ```
   1. {
   2. "module" : {
   3. // ...
   4. "requestPermissions":[
   5. {
   6. // 允许应用在前台运行时获取位置信息
   7. "name" : "ohos.permission.LOCATION",
   8. // reason需要在/resources/base/element/string.json中新建
   9. "reason": "$string:location_permission",
   10. "usedScene": {
   11. "abilities": [
   12. "EntryAbility"
   13. ],
   14. "when":"inuse"
   15. }
   16. },
   17. {
   18. // 允许应用获取设备模糊位置信息
   19. "name" : "ohos.permission.APPROXIMATELY_LOCATION",
   20. // reason需要在/resources/base/element/string.json中新建
   21. "reason": "$string:approximately_location_permission",
   22. "usedScene": {
   23. "abilities": [
   24. "EntryAbility"
   25. ],
   26. "when":"inuse"
   27. }
   28. }
   29. ]
   30. }
   31. }
   ```
2. 初始化地图并获取[MapComponentController](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md>)地图操作类对象。调用mapController对象的[setMyLocationEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationenabled>)方法启用“我的位置”功能。

   建议在获得用户授权后开启“我的位置”功能。

   ```
   1. import { abilityAccessCtrl, bundleManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
   2. import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
   3. import { MapComponent, mapCommon, map } from '@kit.MapKit';

   5. @Entry
   6. @Component
   7. struct LocationDemo {
   8. private mapOptions?: mapCommon.MapOptions;
   9. private callback?: AsyncCallback<map.MapComponentController>;
   10. private mapController?: map.MapComponentController;
   11. private mapEventManager?: map.MapEventManager;

   13. aboutToAppear(): void {
   14. // 地图初始化参数，设置地图中心点坐标及层级
   15. this.mapOptions = {
   16. position: {
   17. target: {
   18. latitude: 39.9,
   19. longitude: 116.4
   20. },
   21. zoom: 10
   22. }
   23. };

   25. // 地图初始化的回调
   26. this.callback = async (err, mapController) => {
   27. if (!err) {
   28. // 获取地图的控制器类，用来操作地图
   29. this.mapController = mapController;
   30. this.mapEventManager = this.mapController.getEventManager();
   31. let permission = await this.checkPermissions();
   32. if (!permission) {
   33. this.requestPermissions();
   34. // 启用我的位置按钮
   35. this.mapController?.setMyLocationControlsEnabled(true);
   36. }
   37. } else {
   38. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   39. }
   40. };
   41. }

   43. // 校验应用是否被授予定位权限，可以通过调用checkAccessToken()方法来校验当前是否已经授权。
   44. async checkPermissions(): Promise<boolean> {
   45. const permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
   46. for (let permission of permissions) {
   47. let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
   48. if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
   49. // 启用我的位置图层，mapController为地图操作类对象
   50. this.mapController?.setMyLocationEnabled(true);
   51. // 启用我的位置按钮
   52. this.mapController?.setMyLocationControlsEnabled(true);
   53. return true;
   54. }
   55. }
   56. return false;
   57. }

   59. // 如果没有被授予定位权限，动态向用户申请授权
   60. requestPermissions(): void {
   61. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   62. atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
   63. ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'])
   64. .then((data: PermissionRequestResult) => {
   65. // 启用我的位置图层
   66. this.mapController?.setMyLocationEnabled(true);
   67. })
   68. .catch((err: BusinessError) => {
   69. console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
   70. })
   71. }

   73. async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
   74. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   75. let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

   77. // 获取应用程序的accessTokenID
   78. let tokenId: number = 0;
   79. let bundleInfo: bundleManager.BundleInfo =
   80. await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
   81. console.info('Succeeded in getting Bundle.');
   82. let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
   83. tokenId = appInfo.accessTokenId;

   85. // 校验应用是否被授予权限
   86. grantStatus = await atManager.checkAccessToken(tokenId, permission);
   87. console.info('Succeeded in checking access token.');
   88. return grantStatus;
   89. }

   91. build() {
   92. Stack() {
   93. // 调用MapComponent组件初始化地图
   94. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%');
   95. }.height('100%')
   96. }
   97. }
   ```
3. 检查“我的位置”功能是否成功启用。

   “我的位置”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/cvlUkuxaQHeK1h6Wo4zXrQ/zh-cn_image_0000002622858887.png?HW-CC-KV=V1&HW-CC-Date=20260611T070749Z&HW-CC-Expire=86400&HW-CC-Sign=758AE03BD293BD5B5E40C4395F87800820F6E1863E900CB6F123D8121200A219)默认显示在地图的右下角。点击“我的位置”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/QBi6X1xSQT2u0jjIeTkGLw/zh-cn_image_0000002622699007.png?HW-CC-KV=V1&HW-CC-Date=20260611T070749Z&HW-CC-Expire=86400&HW-CC-Sign=D98CC6729301845D82CED5058791EC76245F901CD964DEDB7DA5EE87031D5BC2)，将会在屏幕中心显示当前定位，以蓝色圆点的形式呈现，效果如下图所示，效果根据获取到的用户位置会有变化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/rNA6fSZgQ-66uuelMF7ALQ/zh-cn_image_0000002592219446.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070749Z&HW-CC-Expire=86400&HW-CC-Sign=6BBB2C1509CCF6234629D7690A1E853835069C726CB0211708ADE967F636F4E5 "点击放大")
4. 获取用户位置坐标并设置用户的位置。

   Map Kit默认使用系统的连续定位能力，如果您希望定制显示频率或者精准度，可以调用[geoLocationManager](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.geoLocationManager (位置服务)/js-apis-geolocationmanager.md>)相关接口获取用户位置坐标（WGS84坐标系）。注意访问设备的位置信息必须申请权限，并且获得用户授权，详情见[geoLocationManager](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.geoLocationManager (位置服务)/js-apis-geolocationmanager.md>)。

   下面的示例仅显示一次定位结果，在获取到用户坐标后，调用mapController对象的[setMyLocation](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocation>)设置用户的位置，[setMyLocation](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocation>)接口使用的是WGS84坐标系。

   ```
   1. // 需要引入@kit.LocationKit模块
   2. import { geoLocationManager } from '@kit.LocationKit';
   3. // ...

   5. // 获取用户位置坐标
   6. let location = await geoLocationManager.getCurrentLocation();

   8. // 设置用户的位置
   9. this.mapController.setMyLocation(location);
   ```

### 监听“我的位置”按钮点击事件

通过调用[on('myLocationButtonClick')](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapEventManager)/map-map-mapeventmanager.md#onmylocationbuttonclick>)方法，设置'myLocationButtonClick'事件监听。设置监听后“我的位置按钮”点击事件自定义，反之不设置则由Map Kit执行点击后默认事件，即地图移动到当前用户位置。

```
1. let callback = () => {
2. console.info("myLocationButtonClick", `myLocationButtonClick`);
3. };
4. this.mapEventManager.on("myLocationButtonClick", callback);
```

### 隐藏“我的位置”按钮

控制是否显示“我的位置”按钮。

```
1. this.mapController.setMyLocationControlsEnabled(false);
```

### 自定义位置图标样式

通过调用mapController.[setMyLocationStyle](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationstyle>)方法，设置用户位置图标样式。效果如下：

```
1. let style: mapCommon.MyLocationStyle = {
2. anchorU: 0.5,
3. anchorV: 0.5,
4. radiusFillColor: 0xffff0000,
5. // icon为自定义图标资源，使用时需要替换
6. // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
7. icon: 'test.png'
8. };
9. await this.mapController.setMyLocationStyle(style);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0gV5xEMPRVqy6mUf6v-6Tg/zh-cn_image_0000002592379380.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070749Z&HW-CC-Expire=86400&HW-CC-Sign=7BDB52F25DAFF84CEBC3A60E2FDF78299EEC3469F110C0401FB3EF2D93CCC107 "点击放大")

### 更改我的位置图层相对于覆盖物的压盖顺序

通过调用mapController.[changeMyLocationLayerOrder](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#changemylocationlayerorder>)方法，更改我的位置图层相对于覆盖物的压盖顺序。效果如下：

```
1. // true：我的位置图层位于覆盖物之下
2. this.mapController?.changeMyLocationLayerOrder(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aRDjnS4OSCyeKKqJNSO4hw/zh-cn_image_0000002622858889.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070749Z&HW-CC-Expire=86400&HW-CC-Sign=A52D627089BE6B53B01E09CE675604FEBBA312658B19A1E9D4BFB47704E2A5DB "点击放大")
