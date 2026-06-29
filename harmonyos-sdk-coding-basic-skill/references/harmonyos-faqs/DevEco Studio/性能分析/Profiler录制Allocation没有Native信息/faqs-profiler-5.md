---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-5
title: Profiler录制Allocation没有Native信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Allocation没有Native信息
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3d849cf492cdfba607bca4334a494ff7e7e3f913fbc86aa1d73417d1b83112c0
---

**解决措施**

取消勾选Run > Edit Configurations > Diagnostics 内的Address Sanitizer、Thread Sanitizer、Hardware-Assisted Address Sanitizer选项重新运行应用录制即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/_RS2bRGjTT6HW0w48Z7IIg/zh-cn_image_0000002269366576.png?HW-CC-KV=V1&HW-CC-Date=20260612T024515Z&HW-CC-Expire=86400&HW-CC-Sign=6E3554710E5ACC375A2DFB3127D24E1E338769C16BC0FBF6D91E456A3B15C5C0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/z2IrM5ZHTbGnfYexI7u2AQ/zh-cn_image_0000002304120341.png?HW-CC-KV=V1&HW-CC-Date=20260612T024515Z&HW-CC-Expire=86400&HW-CC-Sign=7F4B317639D84FC38C0C6067F9CF2DB41EF55C4F1ADA71CB1859940919D67B38)
