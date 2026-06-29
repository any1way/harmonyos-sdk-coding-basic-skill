---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-8
title: Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9e35d7ae5587ffe61b16287a5753acbb00a42333403baf0af76aa6223fecb7c7
---

**问题现象**

Profiler录制Launch，将ETS文件监控时长配置为20000，录制成功后，详情中Load ETS Files和TOP Redundant页签无数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/FKc0-lOcRgWgHarW7K7IHA/zh-cn_image_0000002314311052.png?HW-CC-KV=V1&HW-CC-Date=20260612T024517Z&HW-CC-Expire=86400&HW-CC-Sign=CF45B903038805D7D82F9C9154CE95C08B9BE821DF9CDB1542869BA661E061A0 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/eY7CzE7wSzWNdTrJLTzicg/zh-cn_image_0000002314151220.png?HW-CC-KV=V1&HW-CC-Date=20260612T024517Z&HW-CC-Expire=86400&HW-CC-Sign=9476E3DC27FEFB25074C926C42176D8AD96927E123C6C040A445E5D8CB12DABA "点击放大")

**问题原因**

ETS文件监控时长配置为20000，需要在拉起应用20000ms之后，才能生成对应的ETS冗余打点文件。

**解决措施**

将ETS文件监控时长配置为20000后，录制时长一定要大于配置时长。
