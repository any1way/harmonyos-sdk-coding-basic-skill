---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-10
title: 卡顿率指标是怎么定义的
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 卡顿率指标是怎么定义的
category: harmonyos-faqs
scraped_at: 2026-06-12T10:46:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:20c2794015c02490208c2bd9a336bcfe54910b96179ce3e56d1dcce085012ab6
---

卡顿率是指在一段动效区间内累计的丢帧时长，用于评估整个动效时段的画面流畅度。卡顿率的值是累计丢帧时长与动效时长的比值，单位为ms/s。

单帧丢帧时长等于实际上屏时间减去期望上屏时间。上屏时间可在trace图形子系统的present线程中查看，取泳道结束点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/_rlZhxsPTOKR8UGi4sWNMQ/zh-cn_image_0000002194318020.png?HW-CC-KV=V1&HW-CC-Date=20260612T024651Z&HW-CC-Expire=86400&HW-CC-Sign=20F4EC0039A0DA5020589B4AFE8C1AC97FF005C4268A01263AC3D7F0BC30AF92 "点击放大")
