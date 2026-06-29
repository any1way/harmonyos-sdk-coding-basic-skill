---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:44+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:40787bf2de35353ca25e846b8b3bcff7ce40b7b95980ee19904304fbd308ab85
---
## 场景介绍

从6.0.0(20)开始，支持卫星图和混合地图功能。

Map Kit支持以下地图类型：

* STANDARD：标准地图，展示道路、建筑物以及河流等重要的自然特征。
* NONE：空地图，没有加载任何数据的地图。
* TERRAIN：地形图，在保留了行政区划边界、POI、楼块等地图要素的基础上，呈现完整清晰描绘地形走势的标准地图。
* SATELLITE：卫星图，显示卫星照片的地图，只支持中国。
* HYBRID：混合地图，在显示卫星照片的同时也显示路网信息。

**图1** 标准地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/QH_lA0_SS9mGujlyArWdpQ/zh-cn_image_0000002622858883.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=AEAAAE8EC678DBADB813624A2AFB322CE4984A0CC2183F0B27520A3DB66CB2BD "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/tVnLVgwPRBiialSvmsYfkQ/zh-cn_image_0000002622699003.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=FDDD3C4E601C861D7D9029559278D876C4B1319FB7A300FB4C0DB350E98B43E8 "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/CWCUiaIIRt6-qZW6e985ow/zh-cn_image_0000002592219442.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=4B56FCFDA9DAA0A41156EF218A60BD259523972BF27A4FE9F3C69D2036472768 "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/l1ym4STGS3yQzBS3C6UK2Q/zh-cn_image_0000002592379376.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=101943446A57E8D9EDE181FCE7BAABE69E1E6CF8FE975308BCB00EA54C2E27E7 "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/zLk0rUswRk-cWJskCoWbvw/zh-cn_image_0000002622858885.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=7899A2576F230C3B45F32FC864E0DD5B20BC49CC2CAC1D3C61CC6FAD2FD59390 "点击放大")

## 接口说明

Map Kit提供2种方式设置地图类型：

方式一：在初始化的时候，通过设置[MapOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#mapoptions>)中的mapType属性来控制展示不同地图类型。

| 属性名 | 描述 |
| --- | --- |
| mapCommon.MapOptions.mapType | 地图初始化参数中的MapType地图类型。 |

方式二：地图创建后，可通过[setMapType](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmaptype>)方法动态设置地图类型。

| 方法名 | 描述 |
| --- | --- |
| [setMapType](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmaptype>)(mapType: [mapCommon.MapType](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#maptype>)): void | 设置地图类型。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { mapCommon } from '@kit.MapKit';
   ```
2. 设置地图类型。

   方式一：

   在地图初始化的时候，在mapOptions参数中新增mapType属性：[mapCommon.MapType](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#maptype>).STANDARD（标准地图）。

   ```
   1. this.mapOptions = {
   2. position: {
   3. target: {
   4. latitude: 31.984410259206815,
   5. longitude: 118.76625379397866
   6. },
   7. zoom: 15
   8. },
   9. mapType: mapCommon.MapType.STANDARD
   10. };
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/E2vur4gpRB6NceVGu48Vnw/zh-cn_image_0000002622699005.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=7987C967D8BFB789CA4211E1AC5D675F4F737DA82EC4EBB0DD1C79B76774E4CC "点击放大")

   方式二：地图创建后，调用[setMapType](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setmaptype>)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```
   1. this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/cLqkJsusSiWHbRSv1GRkcw/zh-cn_image_0000002592219444.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070807Z&HW-CC-Expire=86400&HW-CC-Sign=F8572E90B2381967AD7EA94F74EDCA9462518996A0440F6C8F57B29B7C27330C "点击放大")
