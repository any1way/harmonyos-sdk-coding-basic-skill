---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-devecostudio-glossary
title: DevEco Profiler术语
breadcrumb: 指南 > 优化应用性能 > 附录 > DevEco Profiler术语
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:52+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:65f1d48c81327a706015266a13bdbcc75ad383c7a28d340984fa4d486c5b6ecc
---

## 异步栈缝合

在异步回栈时，该功能支持多回一层异步栈帧。如下图中的start\_malloc\_xxx\_work异步调用malloc\_xxx\_work，当开关未开启时，仅能回malloc\_xxx\_work栈帧；当开关开启后，支持回malloc\_xxx\_work栈帧和start\_malloc\_xxx\_work栈帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/8ePZuKMOQICH3wAE4pOE1w/zh-cn_image_0000002602066371.png?HW-CC-KV=V1&HW-CC-Date=20260611T073151Z&HW-CC-Expire=86400&HW-CC-Sign=334A22D8DF3E8CE83F20CDB664F77C547229343E522BA71B8AF241879B82B9F8 "点击放大")
