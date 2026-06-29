---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-13
title: 测试报告中，用例执行详情为红色，且无数据是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 测试报告中，用例执行详情为红色，且无数据是什么原因
category: harmonyos-faqs
scraped_at: 2026-06-12T10:46:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3d939e94928d4b1ee0a4e84f365f953e2f5a00a48e816e3948ff2fc38d679c21
---

报告中用例详情表头为红色，表示用例未能成功执行。可以点击报告右上角的执行日志查看具体的错误信息。常见的失败原因包括：用例抛出未捕获的异常、待测应用未安装、设备断开连接等。建议先在PyCharm中运行和调试脚本，确保脚本能够顺利执行，然后再使用DevEco Testing进行正式测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/sc3Igb2-S9-wlPbEjCGG9A/zh-cn_image_0000002229758345.png?HW-CC-KV=V1&HW-CC-Date=20260612T024653Z&HW-CC-Expire=86400&HW-CC-Sign=7B138EC06B1E0AB9A63A0D74EACACDFBA8FD1A3F48F9DA0D8AF0BD597D39B98F "点击放大")
