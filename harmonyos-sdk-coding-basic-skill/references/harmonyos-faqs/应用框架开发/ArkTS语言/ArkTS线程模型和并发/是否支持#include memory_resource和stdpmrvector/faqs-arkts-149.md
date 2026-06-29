---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149
title: 是否支持#include <memory_resource>和std::pmr::vector
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 是否支持#include <memory_resource>和std::pmr::vector
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0790869b6fa43957d628756162fb36a5be4cdbcf91fc294e9bff09d5a5b08b92
---

暂时不支持。

C++从C++17标准开始正式支持 <memory\_resource> 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。

Windows：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/TLmIBJgvSi-GaiM9tmfT4w/zh-cn_image_0000002335841501.png?HW-CC-KV=V1&HW-CC-Date=20260612T022436Z&HW-CC-Expire=86400&HW-CC-Sign=D3B3C0BC934905DFA0CE88BB95122CDC32ED14D9D487EB6CEE6ACB42DC8FFC15)

Mac：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/FHrV1A51SE2nhdxCPVtNrQ/zh-cn_image_0000002301915320.png?HW-CC-KV=V1&HW-CC-Date=20260612T022436Z&HW-CC-Expire=86400&HW-CC-Sign=6F786D918B64DA5008A2D41EB21B6F169CCFB91A1C5AD57D863960D735D19A13 "点击放大")
