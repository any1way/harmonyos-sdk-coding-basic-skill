---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-exploration-test-7
title: 应用为什么无法进行应用探索测试
breadcrumb: FAQ > DevEco Testing > 探索测试 > 应用探索测试 > 应用为什么无法进行应用探索测试
category: harmonyos-faqs
scraped_at: 2026-06-12T10:47:23+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:74641387a7efba9a92f4d30a82c35905a561d35966081a00b6b99f8fa1026759
---

若发现应用界面控件无法点击，请使用 DevEco Testing 实用工具中的 UIViewer 打开该应用界面，逐层检查控件树以排查问题。

1. 查看页面控件树，如果仅存在一个节点且最底层组件为XComponent，则不支持进一步遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/nPtYUImzRQijUBW3xByxGg/zh-cn_image_0000002429905500.png?HW-CC-KV=V1&HW-CC-Date=20260612T024722Z&HW-CC-Expire=86400&HW-CC-Sign=F863F809D67BB0D7E259E9BA37B784BA8F75378CC83056DBCADA0107A215F7ED "点击放大")
2. 查看该页面的控件树。如果页面中大部分控件的clickable属性为false，则表示这些控件不支持点击或点击无效。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/7fw7SoCpTM6p4lmcmHMAFA/zh-cn_image_0000002430065352.png?HW-CC-KV=V1&HW-CC-Date=20260612T024722Z&HW-CC-Expire=86400&HW-CC-Sign=793EA2796D114014700CF90A9F5A6756419572A6BA169E3309AAE571B188D6C4 "点击放大")
3. 当前页面的遍历层级限制为8层。如果测试场景的页面层级超过8层，将无法继续遍历。
