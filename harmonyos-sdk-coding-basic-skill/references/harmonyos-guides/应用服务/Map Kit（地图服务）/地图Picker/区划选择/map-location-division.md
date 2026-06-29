---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:41+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:3a9f8a173a6cbe23c5dc4edad1c799be2c71a43f920cb5621fed0daabcb67674
---
## 场景介绍

从6.1.1(24)开始，支持区划选择控件最大显示层级。

本章节将介绍如何集成区划选择控件。该控件不支持在Wearable设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Ekh8s0dXSB2GhAvivjoIJg/zh-cn_image_0000002622858925.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071040Z&HW-CC-Expire=86400&HW-CC-Sign=4907C8AF609037741CAB3925B15AF7AF388FFDC9475695717B260A6CD9CA182D "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/bpLwxsAHQKay9WG2KtvLFA/zh-cn_image_0000002622699045.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071040Z&HW-CC-Expire=86400&HW-CC-Sign=5D3478D9C1EFE8001EACC75834036BB5C74BAEF0FFF6B16699958AB958898B71 "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/WIfCEmIPQuGKaLflZrhV_A/zh-cn_image_0000002592219484.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071040Z&HW-CC-Expire=86400&HW-CC-Sign=BBDAFB7DBA8F21DDD7B4589FA3F3E4DE45180B0D8CB12B2D5B1969A1E8ACF66A "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Ed-i7iatQ2-EhtFmwNWobw/zh-cn_image_0000002592379418.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071040Z&HW-CC-Expire=86400&HW-CC-Sign=33C2187ABD513E2B34EE693B106B534D8D8F2930C68D0013EFBFA6F07DDEB20F "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 仅支持手机、平板和2in1设备。

## 接口说明

区划选择控件功能主要由[sceneMap](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md>)命名空间下的[selectDistrict](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#selectdistrict>)方法提供，更多接口及使用方法请参见[接口文档](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md>)。

| 接口名 | 描述 |
| --- | --- |
| [DistrictSelectOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#districtselectoptions>) | 区划选择页面初始选项。 |
| [selectDistrict](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#selectdistrict>)(context: [common.Context](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>), options: [DistrictSelectOptions](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#districtselectoptions>)): Promise<[DistrictSelectResult](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#districtselectresult>)> | 调出区划选择页面。 |
| [DistrictSelectResult](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#districtselectresult>) | 区划选择结果。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { sceneMap } from '@kit.MapKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建区划选择请求参数，调用[selectDistrict](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#selectdistrict>)方法拉起区划选择页。

   ```
   1. let districtSelectOptions: sceneMap.DistrictSelectOptions = {
   2. countryCode: "CN",
   3. // 使用子窗拉起方式
   4. subWindowEnabled: true,
   5. // 区划选择控件的最大显示层级
   6. maxAdminLevel: 3
   7. };
   8. // 拉起区划选择页
   9. sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
   10. console.info("SelectDistrict", "Succeeded in selecting district.");
   11. }).catch((err: BusinessError) => {
   12. console.error("SelectDistrict", `Failed to select district, code: ${err.code}, message: ${err.message}`);
   13. });
   ```
