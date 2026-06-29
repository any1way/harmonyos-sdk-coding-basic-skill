---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-functions
title: Functions
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Functions
category: harmonyos-references
scraped_at: 2026-06-01T16:36:17+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:aba42549eeb3782a0764be59b8bdb75899647674357de4bac975d5b3d752d647
---
## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## newCameraPosition

PhonePC/2in1TabletWearable

newCameraPosition(cameraPosition: mapCommon.CameraPosition): CameraUpdate

创建CameraUpdate对象，更新地图状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| cameraPosition | [mapCommon.CameraPosition](../../mapCommon（地图属性模型）/map-common.md#cameraposition) | 是 | 更新后的地图状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化，例如平移、缩放。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
```

## newLatLng

PhonePC/2in1TabletWearable

newLatLng(latLng: mapCommon.LatLng, zoom?: number): CameraUpdate

设置地图的中心点和缩放层级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| latLng | [mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng) | 是 | 经纬度。 |
| zoom | number | 否 | 缩放层级，取值范围：[2, 20]，超出按边界值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let latLng: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraUpdate: map.CameraUpdate = map.newLatLng(latLng);
```

## newLatLngBounds

PhonePC/2in1TabletWearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding?: number): CameraUpdate

设置地图经纬度范围、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](../../mapCommon（地图属性模型）/map-common.md#latlngbounds) | 是 | 地图显示经纬度范围。 |
| padding | number | 否 | 地图区域和边界之间的距离，默认值：0，单位：px，异常值返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 33,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 32,
8. longitude: 119
9. }
10. };
11. let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 5);
```

## newLatLngBounds

PhonePC/2in1TabletWearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, width: number, height: number, padding: number): CameraUpdate

设置地图经纬度范围、经纬度矩形范围的高和宽、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](../../mapCommon（地图属性模型）/map-common.md#latlngbounds) | 是 | 地图显示经纬度范围。 |
| width | number | 是 | 经纬度矩形范围的屏幕宽，单位：px，取值范围：大于等于0。 |
| height | number | 是 | 经纬度矩形范围的屏幕高，单位：px，取值范围：大于等于0。 |
| padding | number | 是 | 地图区域和边界之间的距离，单位：px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 31,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 30.5,
8. longitude: 123
9. }
10. };
11. // 设置地图显示经纬度范围，设置经纬度矩形范围的宽为1000像素，设置经纬度矩形范围的高为1000像素，设置地图区域和边界之间的距离为100像素
12. let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 1000, 1000, 100);
```

## newLatLngBounds

PhonePC/2in1TabletWearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding: mapCommon.Padding): CameraUpdate

设置地图经纬度范围和4个方向与边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.1(13)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](../../mapCommon（地图属性模型）/map-common.md#latlngbounds) | 是 | 地图显示经纬度范围，异常值返回401错误码。 |
| padding | [mapCommon.Padding](../../mapCommon（地图属性模型）/map-common.md#padding) | 是 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。  **说明：**  - 地图组件高度减去padding的top值和bottom值，结果需要大于等于100px。  - 地图组件宽度减去padding的left值和right值，结果需要大于等于100px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 31,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 30.5,
8. longitude: 123
9. }
10. };
11. // 初始化参数，左边距0，底边距50
12. let padding: mapCommon.Padding = {
13. left: 0,
14. bottom: 50
15. };
16. let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, padding);
```

## scrollBy

PhonePC/2in1TabletWearable

scrollBy(x: number, y: number): CameraUpdate

按像素移动地图中心点。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| x | number | 是 | 水平移动的像素数。正值代表可视区域向右移动，负值代表可视区域向左移动。单位：px。 |
| y | number | 是 | 竖直移动的像素数。正值代表可视区域向下移动，负值代表可视区域向上移动。单位：px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let cameraUpdate: map.CameraUpdate = map.scrollBy(100, 200);
```

## zoomBy

PhonePC/2in1TabletWearable

zoomBy(amount: number, focus?: mapCommon.MapPoint): CameraUpdate

根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。

以屏幕左顶点为（0, 0）点，focus.positionX正值代表可视区域向右移动，负值代表可视区域向左移动。focus.positionY正值代表可视区域向下移动，负值代表可视区域向上移动。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| amount | number | 是 | 地图缩放级别增量。 |
| focus | [mapCommon.MapPoint](../../mapCommon（地图属性模型）/map-common.md#mappoint) | 否 | 地图缩放中心点对应的屏幕坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let focus: mapCommon.MapPoint = {
2. positionX: 100,
3. positionY: 200
4. };
5. let cameraUpdate: map.CameraUpdate = map.zoomBy(10, focus);
```

## zoomIn

PhonePC/2in1TabletWearable

zoomIn(): CameraUpdate

放大地图缩放级别，在当前地图显示的级别基础上加1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**示例：**

```
1. let cameraUpdate: map.CameraUpdate = map.zoomIn();
```

## zoomOut

PhonePC/2in1TabletWearable

zoomOut(): CameraUpdate

缩小地图缩放级别，在当前地图显示的级别基础上减1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**示例：**

```
1. let cameraUpdate: map.CameraUpdate = map.zoomOut();
```

## zoomTo

PhonePC/2in1TabletWearable

zoomTo(zoom: number): CameraUpdate

设置地图缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| zoom | number | 是 | 地图缩放级别，取值范围为[2, 20]，超出按边界值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](<../Interface (CameraUpdate)/map-map-cameraupdate.md>) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let cameraUpdate: map.CameraUpdate = map.zoomTo(10);
```

## calculateDistance

PhonePC/2in1TabletWearable

calculateDistance(from: mapCommon.LatLng, to: mapCommon.LatLng): number

计算坐标点之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| from | [mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng) | 是 | 起点坐标。 |
| to | [mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng) | 是 | 终点坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 两个坐标点之间的距离，单位：m。  入参为空返回0。 |

**示例：**

```
1. let fromLatLng: mapCommon.LatLng = {
2. latitude: 38,
3. longitude: 118
4. };
5. let toLatLng: mapCommon.LatLng = {
6. latitude: 39,
7. longitude: 119
8. };

10. let distance = map.calculateDistance(fromLatLng, toLatLng);
```

## convertCoordinate

PhonePC/2in1TabletWearable

convertCoordinate(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): Promise<mapCommon.LatLng>

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。使用Promise异步回调。

同步函数建议使用[convertCoordinateSync](map-map-functions.md#convertcoordinatesync)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromType | [mapCommon.CoordinateType](../../mapCommon（地图属性模型）/map-common.md#coordinatetype) | 是 | 转换前坐标类型，当前仅支持WGS84。 |
| toType | [mapCommon.CoordinateType](../../mapCommon（地图属性模型）/map-common.md#coordinatetype) | 是 | 转换后坐标类型，当前仅支持GCJ02。 |
| location | [mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng) | 是 | 待转换坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng)> | Promise对象，返回[mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let wgs84Position: mapCommon.LatLng = {
2. latitude: 30,
3. longitude: 118
4. };
5. let gcj02Position: mapCommon.LatLng = await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02,wgs84Position);
```

## convertCoordinateSync

PhonePC/2in1TabletWearable

convertCoordinateSync(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): mapCommon.LatLng

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromType | [mapCommon.CoordinateType](../../mapCommon（地图属性模型）/map-common.md#coordinatetype) | 是 | 转换前坐标类型，当前仅支持WGS84。 |
| toType | [mapCommon.CoordinateType](../../mapCommon（地图属性模型）/map-common.md#coordinatetype) | 是 | 转换后坐标类型，当前仅支持GCJ02。 |
| location | [mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng) | 是 | 待转换坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng) | 经纬度对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let wgs84Position: mapCommon.LatLng = {
2. latitude: 30,
3. longitude: 118
4. };
5. // 转换经纬度坐标
6. let gcj02Position: mapCommon.LatLng =
7. map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```

## rectifyCoordinate

PhonePC/2in1TabletWearable

rectifyCoordinate(context: common.Context, locations: Array<mapCommon.CoordinateLatLng>): Promise<Array<mapCommon.CoordinateLatLng>>

根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。如果需要修正，则返回修正后的坐标系和坐标。使用Promise异步回调。

说明

* rectifyCoordinate接口仅为解决原始坐标与华为地图展示偏转的问题。
* rectifyCoordinate接口仅支持WGS84坐标系转为GCJ02坐标系。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](<../../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>) | 是 | Context上下文。 |
| locations | Array<[mapCommon.CoordinateLatLng](../../mapCommon（地图属性模型）/map-common.md#coordinatelatlng)> | 是 | 输入坐标系和坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[mapCommon.CoordinateLatLng](../../mapCommon（地图属性模型）/map-common.md#coordinatelatlng)>> | Promise对象，返回修正后的坐标系和坐标。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../../ArkTS API错误码/errorcode-map.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600013 | The current routing location is unknown. Try again later. |

**示例：**

```
1. let locations: Array<mapCommon.CoordinateLatLng> = [
2. {
3. // 输入香港坐标和WGS84坐标系，若当前地图站点使用GCJ02坐标系，返回GCJ02坐标系和转换后的香港坐标（输入的坐标转换为GCJ02坐标系）
4. coordinateType: mapCommon.CoordinateType.WGS84,
5. location: { latitude: 22.280556, longitude: 114.984000 }
6. }
7. ];
8. // 包含await的外层方法需要添加async关键字
9. let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(this.getUIContext().getHostContext(), locations);
```
