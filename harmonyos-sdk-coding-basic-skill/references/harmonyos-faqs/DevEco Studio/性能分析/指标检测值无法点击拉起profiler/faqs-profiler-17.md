---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-17
title: 指标检测值无法点击拉起profiler
breadcrumb: FAQ > DevEco Studio > 性能分析 > 指标检测值无法点击拉起profiler
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:29+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:cef70ab97f044729e484b2393da810b6ce1aad28ed84ffb7a9678a548fd5a779
---

**问题现象**

报告详情页，指标检测值无法点击，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/H1AgZdImRne4gejaMUjpJg/zh-cn_image_0000002527522192.png?HW-CC-KV=V1&HW-CC-Date=20260612T024528Z&HW-CC-Expire=86400&HW-CC-Sign=8422F4210CB108C4418D5047624C3D2D37F5578B0953FAD10E74929D70A115D8)

预期是可以点击指标检测值并拉起profiler，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/WOMvMz_MTSGbeU2J6vh0Ew/zh-cn_image_0000002558681913.png?HW-CC-KV=V1&HW-CC-Date=20260612T024528Z&HW-CC-Expire=86400&HW-CC-Sign=B291595D97C9CFC09B357C282CDC9599D8E52DFDCFC3BFD0C7160A83426E70DD)

**问题原因**

体检卡片勾选冷启动场景，但在录制开始时未重启应用，导致堆栈抓取失败。

**解决措施**

1、建议冷启动场景，使用“手动性能冷启动体检”卡片进行检测。

2、如果是自定义卡片场景勾选“冷启动”场景，需要在录制开始时，强制重启应用，之后再进行体检。
