---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-publish-test-3
title: 测试报告中，为什么会批量出现待检测项
breadcrumb: FAQ > DevEco Testing > 上架预检 > 测试报告中，为什么会批量出现待检测项
category: harmonyos-faqs
scraped_at: 2026-06-12T10:47:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ec09c0c0d3742aedddd782625a384d78f784dccd5f528d6ae7f556019a776148
---

由于测试任务内部异常，偶现任务终止的情况。请查看【测试报告-执行日志】，如果应用信息为空，请重新创建任务并执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/KcipPtpeSlelCJair7NYRw/zh-cn_image_0000002229758645.png?HW-CC-KV=V1&HW-CC-Date=20260612T024700Z&HW-CC-Expire=86400&HW-CC-Sign=D5F93E0A392998394640D14A5C4998523B782E3C55D081AC849307595838C7F2)

该问题由应用信息未完全解析导致。再次创建任务时，请等待右侧应用信息加载完成，再进行创建，即可解决该问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/cTOjRYWaTuiX4ikFwscwKw/zh-cn_image_0000002194318380.png?HW-CC-KV=V1&HW-CC-Date=20260612T024700Z&HW-CC-Expire=86400&HW-CC-Sign=1EB500AAAD22EF81118C5CDDB9037A1B0EAD506DCEE0815BF1D87CF84666793B "点击放大")
