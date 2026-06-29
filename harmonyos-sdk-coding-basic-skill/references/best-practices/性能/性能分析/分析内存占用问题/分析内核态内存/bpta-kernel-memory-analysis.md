---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-06-12T10:15:19+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:5baaec3fcc4edd39c8f59e1a2bf2690114b777e1b449e0170cb24474e7dc6967
---
**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/N1OXADCJT9CTBsd6j0GdlQ/zh-cn_image_0000002370565340.png?HW-CC-KV=V1&HW-CC-Date=20260612T021518Z&HW-CC-Expire=86400&HW-CC-Sign=5A4B2FBA6F48066EB2C970FD8C6B7CFC84A7886B6E8BABAFAC9CC36B970E9333 "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/YS-I-rN3SqCXonvQjKfraA/zh-cn_image_0000002404125005.png?HW-CC-KV=V1&HW-CC-Date=20260612T021518Z&HW-CC-Expire=86400&HW-CC-Sign=FF9522B18595528FD543C1A255775EB065E9A38FB9955BC37F496FBCF8C15CFE)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/fC_kvhMUTdao5XutRwMbAA/zh-cn_image_0000002370405452.png?HW-CC-KV=V1&HW-CC-Date=20260612T021518Z&HW-CC-Expire=86400&HW-CC-Sign=6CBC70C8AAEBD3B7579E4B1E41F7FCA43BCFC652E0128143164E8B85A90A7AEF)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/ib7cNlSOS8qx6qA22i4m5Q/zh-cn_image_0000002404045177.png?HW-CC-KV=V1&HW-CC-Date=20260612T021518Z&HW-CC-Expire=86400&HW-CC-Sign=C166EC3CBAEBE6C6D0471AE44B270D6D7A3820EAD139C562E157AB491E6AC5B4 "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem内存；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION内存。

如果这类内存发生膨胀，往往会导致卡死、花屏等较严重的整机问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](../../../../稳定性/稳定性分析/资源泄漏类问题分析方法/bpta-stability-leak-way.md#section2825227501)中的ashmem、ION内存泄漏分析方法。
