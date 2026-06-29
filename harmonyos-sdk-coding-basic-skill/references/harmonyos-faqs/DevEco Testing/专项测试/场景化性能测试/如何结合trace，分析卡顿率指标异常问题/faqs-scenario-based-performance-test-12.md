---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-12
title: 如何结合trace，分析卡顿率指标异常问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 如何结合trace，分析卡顿率指标异常问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:46:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5cfefd32a83214411feb5f9e4468c43d2264659eac85925b69406058f5d6ce9
---

下载并打开trace后，通过上报的Present ID字段搜索，可快速定位问题点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/zjga1-EKR-megF2r_6g9rA/zh-cn_image_0000002229758405.png?HW-CC-KV=V1&HW-CC-Date=20260612T024653Z&HW-CC-Expire=86400&HW-CC-Sign=B20576E4BB87BC2D7015010457DD3E041B082751E6D8F30D8F1943E8DC7450A2 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/O2vR8AXwQqK_cSDL_lhs1A/zh-cn_image_0000002194318144.png?HW-CC-KV=V1&HW-CC-Date=20260612T024653Z&HW-CC-Expire=86400&HW-CC-Sign=630523DB0C4C0AEDD8CBE3181426EE15EC307CEC54992A4708DB0BF5E88C6ACB "点击放大")

上图中，99009这一帧在屏幕上持续了33ms，超出应持续的16.6ms，被统计为丢1帧。
