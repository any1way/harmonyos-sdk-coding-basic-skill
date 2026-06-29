---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-controls-and-interaction
title: 控件交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 控件交互
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:51+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c55e4d439518541ec9326c11323b7347202c64be611e3b48265c2cd0536e8b1c
---
## 场景介绍

从6.1.0(23)开始，支持在地图左下角设置审图号。

本章节将向您介绍如何使用地图的控件。

控件是指浮在地图组件上的一系列用于操作地图的组件，例如缩放按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/wo22wXPfTa-ZgMPouCPf5Q/zh-cn_image_0000002592379386.png?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=8316A71D06D391A2973FBB0E9DB44565C3846887E216B9F7D1932B71CA6D627F)、定位按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/8ZkJfvD_QVWBiUucqe10AA/zh-cn_image_0000002622858895.png?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=4CF13E39FB98C73BBA3E8BEB25CA9346D8A385DD080C1246D61CE6E27F83664F)、比例尺![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/V1EHL4MuR9ujTNzEFqrcUA/zh-cn_image_0000002622699015.png?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=74059D1E1C9EC7864DA7C12CBF5ACDDF809E5C57A088DC80AF0FEDB8F7C7EF32)等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/0HmfoxcwTLq4NhGTILnlMg/zh-cn_image_0000002592219454.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=9857A6335840B6E6675385B1036E49F4BAABB38DEB8B5EE97128F867C95E51C0 "点击放大")

## 接口说明

以下是地图的控件相关接口，该功能有2种实现方式：

* 地图初始化时，可在初始化参数[MapOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mapoptions>)中设置是否启用控件功能，详细讲解见[显示地图](../../创建地图/显示地图/map-presenting.md)章节。
* 通过调用[MapComponentController](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md>)提供的set方法实现相关控件的开启或关闭。

| 接口名 | 描述 |
| --- | --- |
| [setZoomControlsEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setzoomcontrolsenabled>)(enabled: boolean): void | 设置是否启用缩放控制器。 |
| [setMyLocationEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationenabled>)(myLocationEnabled: boolean): void | 设置是否启用我的位置图层。 |
| [setMyLocationControlsEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled>)(enabled: boolean): void | 设置是否启用我的位置按钮。 |
| [setScaleControlsEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setscalecontrolsenabled>)(enabled: boolean): void | 设置是否启用比例尺。 |
| [setScalePosition](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setscaleposition>)(point: [mapCommon.MapPoint](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mappoint>)): void | 设置比例尺控件的位置。 |
| [setAlwaysShowScaleEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setalwaysshowscaleenabled>)(enabled: boolean): void | 设置是否始终显示比例尺。 |
| [setCompassControlsEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setcompasscontrolsenabled>)(enabled: boolean): void | 设置是否启用指南针。 |
| [setLogoAlignment](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setlogoalignment>)(alignment: [mapCommon.LogoAlignment](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#logoalignment>)): void | 设置地图Logo的对齐方式。 |
| [setApproveNumberEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setapprovenumberenabled>)(enabled: boolean): void | 设置是否显示审图号，只有路由地在中国才会显示。 |

## 开发步骤

mapController对象在初始化地图时获取，初始化地图功能在[显示地图](../../创建地图/显示地图/map-presenting.md)章节中有详细讲解。

### 缩放控件

Map Kit提供了内置的缩放控件，默认情况下是开启的。

```
1. // 开启缩放控件
2. this.mapController.setZoomControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/76PQqkx7RUy8FGPHjXUykw/zh-cn_image_0000002592379388.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=BF16993437809DA72C5BD59E68124B84F2E841F4E3E98710DA7F17513D46E907 "点击放大")

### 比例尺

Map Kit提供了内置的比例尺控件，默认情况下是关闭的。

```
1. // 开启比例尺控件
2. this.mapController.setScaleControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/_peuGjnfSTyY95n3dRudmQ/zh-cn_image_0000002622858897.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=4C63F376E3C5862BC9B7F385F2DEECBC50EE2C1E2A50CE675EDF4AD8DEB1B44C "点击放大")

**调整比例尺位置：**

可通过[setScalePosition](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setscaleposition>)方法设置比例尺控件的位置。

```
1. let point: mapCommon.MapPoint = {
2. // 以当前地图组件左上角为原点，向右移动1000px
3. positionX: 1000,
4. // 以当前地图组件左上角为原点，向下移动1000px
5. positionY: 1000
6. };
7. this.mapController.setScalePosition(point);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/aMGgfUfmQNCBkGqKJID6ow/zh-cn_image_0000002622699017.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=ECE5FB8ABF0A295DB255217CBFD8C24AFFAE296E2C531701ED580284357E36F3 "点击放大")

**获取当前层级的比例尺大小：**

可通过[getScaleLevel](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#getscalelevel>)方法获取当前层级比例尺大小。

```
1. let level = this.mapController.getScaleLevel();
```

**获取比例尺控件宽高：**

可通过[getScaleControlsHeight](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#getscalecontrolsheight>)和[getScaleControlsWidth](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#getscalecontrolswidth>)方法获取当前比例尺控件宽高。

```
1. // 获取比例尺控件的高度
2. let height = this.mapController.getScaleControlsHeight();
3. // 获取比例尺控件的宽度
4. let width = this.mapController.getScaleControlsWidth();
```

**设置比例尺控件常显：**

可通过[setAlwaysShowScaleEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setalwaysshowscaleenabled>)方法设置比例尺控件常显，通过[isAlwaysShowScaleEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#isalwaysshowscaleenabled>)方法查询比例尺控件是否常显。

```
1. // 设置比例尺控件常显
2. this.mapController.setAlwaysShowScaleEnabled(true);
3. // 查询比例尺控件是否常显
4. let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();
```

### 指南针

Map Kit提供了内置的指南针控件，默认情况下是开启的，控件位置默认显示在地图的右上角。如果是启用状态，当地图不是指向正北方向或者发生倾斜时，地图右上角会显示一个指南针图标，点击指南针可使地图旋转为正北方向并且取消倾斜；当地图为正北方向且未发生倾斜时，指南针图标隐藏。如果是禁用状态，将不会显示指南针图标。

```
1. // 开启指南针控件
2. this.mapController.setCompassControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/LdwgNzbpQXWFGWb2mYQkQQ/zh-cn_image_0000002592219456.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=780727A1758B3ED2CD78CAD8BD00282F266001CEB9229AECDFE6F25214BA84D9 "点击放大")

**调整指南针位置：**

可通过[setCompassPosition](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setcompassposition>)方法设置指南针控件的位置。

```
1. let point: mapCommon.MapPoint = {
2. // 以当前地图组件左上角为原点，向右移动1000px
3. positionX: 1000,
4. // 以当前地图组件左上角为原点，向下移动1000px
5. positionY: 1000
6. };
7. this.mapController.setCompassPosition(point);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/zBNMbte2TuypxWTA1VnnNg/zh-cn_image_0000002592379390.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=7F4B4F92F6DABD802B6B7D9BF6974DA28DEBF86E73D8E461FF72AF222D6616FC "点击放大")

### 地图Logo

Map Kit提供了调整地图Logo对齐方式的方法[setLogoAlignment](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setlogoalignment>)和调整地图边界与Logo之间的间距的方法[setLogoPadding](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setlogopadding>)。需注意，地图Logo不允许被遮挡，可通过[setLogoPadding](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setlogopadding>)方法设置地图边界区域，来避免logo被遮挡。

```
1. // 将Logo放置在右下角位置
2. this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM_END);
3. // 设置地图边界与Logo之间的间距，单位：px
4. let padding: mapCommon.Padding = {
5. right: 50,
6. bottom: 50
7. };
8. this.mapController.setLogoPadding(padding);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/h9zjwbdDRbOhh8Oeuy0rZw/zh-cn_image_0000002622858899.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=1B3B0090A58E0A1B4262CA212479A2CB26D51514122D03E6536A3E58B6DCEAE6 "点击放大")

### 审图号

审图号是指国家对地图产品进行审核并颁发的编号，用于标识地图已通过国家测绘地理信息局的审查。

Map Kit通过方法[setApproveNumberEnabled](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setapprovenumberenabled>)展示审图号。如图左下角：

```
1. // 显示审图号
2. this.mapController?.setApproveNumberEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/WKDfOHhLSBmdW4eHWUl00w/zh-cn_image_0000002622699019.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070949Z&HW-CC-Expire=86400&HW-CC-Sign=4BB843D89D87D9BC193B23CB564D851FF9903043E72742554C80C955F9174F81 "点击放大")
