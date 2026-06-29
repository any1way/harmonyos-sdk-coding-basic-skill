---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-06-11T15:18:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:37bcf9ac80cc02da5aaed388b66eca3932438c2aa55a8193b43b2e972fff2142
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/CMhG9_3bR8G8_Yn5S3lIfA/zh-cn_image_0000002592379686.png?HW-CC-KV=V1&HW-CC-Date=20260611T071817Z&HW-CC-Expire=86400&HW-CC-Sign=EFF9598E9DE6BAE9F410A2341B691CCE6A38DD75EA2456CA75D3F23DB1BCB3E4)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/0EE3ZbyURM-AXPDffEX6kQ/zh-cn_image_0000002622859195.png?HW-CC-KV=V1&HW-CC-Date=20260611T071817Z&HW-CC-Expire=86400&HW-CC-Sign=6FC374E0B3E50AA3715E837A0CC1A5833356002F7FAD4DFB6894A6EDAC134C13)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/AwV2TBMJQ169KmRsKBS8_w/zh-cn_image_0000002622699315.png?HW-CC-KV=V1&HW-CC-Date=20260611T071817Z&HW-CC-Expire=86400&HW-CC-Sign=1E629B7C746DF5AD760C0DC08D26F841ACA67DD18E996105A0C360AB6C0D2331)
