---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-2
title: siteId参数如何获取
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > siteId参数如何获取
category: harmonyos-guides
scraped_at: 2026-06-01T15:07:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee342fdcbd654cd16f1b31f34f8a4dd0c91947b0df40ffc320476e98943e7d6c
---
siteId有多种获取方式，这里提供其中的3种作为参考：

1. 可通过[on('poiClick')](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapEventManager)/map-map-mapeventmanager.md#onpoiclick>)方法获取。
2. 可通过[位置搜索](../../位置搜索/POI搜索/map-site-search.md)相关接口（关键字搜索、周边搜索、地点详情、自动补全、正地理编码）的返回结果中获取。
3. 可通过[chooseLocation](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#chooselocation>)接口的返回结果中获取。
