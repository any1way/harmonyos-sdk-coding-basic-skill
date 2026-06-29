---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-14
title: PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8b544c472291f0a94dca29e341197201534810fe5309dce972e4fc89d7e65227
---

**问题现象**

在使用PC设备时，通过FP回栈模式录制Allocation模板，Graphic Memory泳道中的OpenGL ES子泳道无数据。

**可能原因**

GPU底层库不支持FP回栈模式。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/2nVfFZdASQi7SCpTMYCKfw/zh-cn_image_0000002538356035.png?HW-CC-KV=V1&HW-CC-Date=20260612T024524Z&HW-CC-Expire=86400&HW-CC-Sign=0B6F621842FA77270CDEF7960580FA16BCD69824C6FABDA20FC2DE68FADD5718)按钮，设置内存分配栈回栈模式为DWARF。使用DWARF回栈模式采集数据时，性能开销较大，因此在录制Graphic Memory泳道时，建议不同时录制Native Allocation泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/0oEKrZYZTxSMLEqTaMFTCQ/zh-cn_image_0000002506636162.png?HW-CC-KV=V1&HW-CC-Date=20260612T024524Z&HW-CC-Expire=86400&HW-CC-Sign=DBBDC34F0F78271F41F9261504499CA529E8EF2EA12000BD50475849C61413FE "点击放大")
