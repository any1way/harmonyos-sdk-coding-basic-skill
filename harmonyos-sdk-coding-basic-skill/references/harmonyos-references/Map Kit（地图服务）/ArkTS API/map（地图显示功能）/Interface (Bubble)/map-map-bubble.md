---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-bubble
title: Interface (Bubble)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (Bubble)
category: harmonyos-references
scraped_at: 2026-06-01T16:35:45+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:3c8d72a4aece083d390e4aa4db0542de9e16b9ebcbfe97d82f94df618075d211
---
## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
2. import { image } from '@kit.ImageKit';
```

## Bubble

PhonePC/2in1TabletWearable

气泡，继承[BasePriorityOverlay](<../Interface (BasePriorityOverlay)/map-map-basepriorityoverlay.md>)。在调用map.[MapComponentController](<../Class (MapComponentController)/map-map-mapcomponentcontroller.md>)类的[addBubble](<../Class (MapComponentController)/map-map-mapcomponentcontroller.md#addbubble>)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let bubbleOptions: mapCommon.BubbleParams = {
2. positions: [[{
3. latitude: 31.98,
4. longitude: 118.766
5. }]],
6. // 图标需存放在resources/rawfile目录下
7. icons: [
8. 'icon.png',
9. 'icon.png',
10. 'icon.png',
11. 'icon.png'
12. ],
13. forceVisible: true,
14. priority: 3,
15. minZoom: 2,
16. maxZoom: 20,
17. visible: true,
18. zIndex: 1
19. };
20. let bubble: map.Bubble = await this.mapController.addBubble(bubbleOptions);
```

### setIcons

PhonePC/2in1TabletWearable

setIcons(icons: Array<string | image.PixelMap | Resource>): Promise<void>

设置气泡的图标。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| icons | Array<string | [image.PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | [Resource](../../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#resource)> | 是 | 气泡的图标，异常值不处理。  - 必须提供4个方向的图标，传入的图标宽高需要相同。  - 图片格式支持jpg、jpeg、png、gif、webp、svg。  - string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。  **说明：**  从5.0.0(12)版本开始，icon属性支持[Resource](../../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#resource)和[image.PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // 图标需存放在resources/rawfile目录下
2. let icons: Array<string | image.PixelMap | Resource> = [
3. 'test1.png',
4. 'test2.png',
5. 'test3.png',
6. 'test4.png'
7. ];
8. await bubble.setIcons(icons);
```

### setPositions

PhonePC/2in1TabletWearable

setPositions(positions: Array<Array<mapCommon.LatLng>>): void

设置气泡的候选位置坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| positions | Array<Array<[mapCommon.LatLng](../../mapCommon（地图属性模型）/map-common.md#latlng)>> | 是 | 气泡的候选位置坐标，异常值不处理。 |

**示例：**

```
1. let positions: Array<Array<mapCommon.LatLng>> = [[
2. {
3. latitude: 31.9844,
4. longitude: 118.7112
5. }, {
6. latitude: 31.9844,
7. longitude: 118.7262
8. }, {
9. latitude: 31.9844,
10. longitude: 118.7362
11. }, {
12. latitude: 31.9844,
13. longitude: 118.7462
14. }, {
15. latitude: 31.9844,
16. longitude: 118.7562
17. }, {
18. latitude: 31.9844,
19. longitude: 118.7662
20. }, {
21. latitude: 31.9844,
22. longitude: 118.7762
23. }
24. ]];
25. bubble.setPositions(positions);
```
