---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-masspointoverlay
title: Interface (MassPointOverlay)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MassPointOverlay)
category: harmonyos-references
scraped_at: 2026-06-01T16:36:13+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:478357b1554e01e9c7708c87df1737cc2c3df3415ce76959c0ec57e92b97c217
---
## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MassPointOverlay

PhonePC/2in1TabletWearable

海量点的管理对象。在调用map.[MapComponentController](<../Class (MapComponentController)/map-map-mapcomponentcontroller.md>)类的[addMassPointOverlay](<../Class (MapComponentController)/map-map-mapcomponentcontroller.md#addmasspointoverlay>)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**示例：**

```
1. let items: mapCommon.MassPointItem[] = [];
2. for (let i = 0; i < 1000; i++) {
3. // 将海量点存入items
4. items.push({
5. // itemId为开发者自定义标识符
6. itemId: 'test' + i,
7. // 经纬度坐标
8. position: {
9. longitude: 118.11111 + Math.random() * 1 - 0.5,
10. latitude: 32.11111 + Math.random() * 1 - 0.5
11. },
12. snippet: 'test' + i,
13. title: 'test' + i
14. })
15. }
16. let params: mapCommon.MassPointOverlayParams = {
17. id: 'test',
18. items: items,
19. // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
20. icon: 'icon/maps_blue_dot.png'
21. }
22. let massPointOverlay = await this.mapController?.addMassPointOverlay(params);
```

### getId

PhonePC/2in1TabletWearable

getId(): string

获取海量点的ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 海量点的ID。 |

**示例：**

```
1. let Id = massPointOverlay.getId();
```

### setItems

PhonePC/2in1TabletWearable

setItems(items: mapCommon.MassPointItem[]): void

更新海量点列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| items | [mapCommon.MassPointItem](../../mapCommon（地图属性模型）/map-common.md#masspointitem)[] | 是 | 海量点列表（建议数据量小于100000条）。 |

**示例：**

```
1. let items: mapCommon.MassPointItem[] = [
2. {
3. itemId: '1',
4. position: { latitude: 32.11111, longitude: 118.11111 }
5. },
6. {
7. itemId: '2',
8. position: { latitude: 32.22222, longitude: 118.22222 }
9. }
10. ];
11. massPointOverlay.setItems(items);
```

### getItems

PhonePC/2in1TabletWearable

getItems(): mapCommon.MassPointItem[]

获取海量点列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.MassPointItem](../../mapCommon（地图属性模型）/map-common.md#masspointitem)[] | 海量点列表。 |

**示例：**

```
1. let MassPointItem: mapCommon.MassPointItem[] = this.massPointOverlay.getItems();
```

### setAnchorU

PhonePC/2in1TabletWearable

setAnchorU(anchorU: number): void

更新图标锚点在水平方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchorU | number | 是 | 更新图标锚点在水平方向上的位置，取值范围：[0, 1]。 |

**示例：**

```
1. massPointOverlay.setAnchorU(0.6);
```

### getAnchorU

PhonePC/2in1TabletWearable

getAnchorU(): number

获取图标锚点在水平方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图标锚点在水平方向上的位置。 |

**示例：**

```
1. let AnchorU: number = this.massPointOverlay.getAnchorU();
```

### setAnchorV

PhonePC/2in1TabletWearable

setAnchorV(anchorV: number): void

更新图标锚点在垂直方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchorV | number | 是 | 更新图标锚点在垂直方向上的位置，取值范围：[0, 1]。 |

**示例：**

```
1. massPointOverlay.setAnchorV(0.6);
```

### getAnchorV

PhonePC/2in1TabletWearable

getAnchorV(): number

获取图标锚点在垂直方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图标锚点在垂直方向上的位置。 |

**示例：**

```
1. let AnchorV: number = this.massPointOverlay.getAnchorV();
```

### setVisible

PhonePC/2in1TabletWearable

setVisible(visible: boolean): void

设置海量点是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 海量点是否可见。  - true：可见。  - false：不可见。 |

**示例：**

```
1. massPointOverlay.setVisible(true);
```

### isVisible

PhonePC/2in1TabletWearable

isVisible(): boolean

获取海量点是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 海量点是否可见。  - true：可见。  - false：不可见。 |

**示例：**

```
1. let isVisible: boolean = massPointOverlay.isVisible();
```

### remove

PhonePC/2in1TabletWearable

remove(): void

删除海量点。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**示例：**

```
1. massPointOverlay.remove();
```
