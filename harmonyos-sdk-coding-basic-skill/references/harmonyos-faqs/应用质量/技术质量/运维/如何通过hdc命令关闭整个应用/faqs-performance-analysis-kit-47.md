---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-47
title: 如何通过hdc命令关闭整个应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令关闭整个应用
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:46+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:6ed4843000228cbf069c968c5baec0942378e44fabba0318d7cc8e6b3ab4abbf
---
可以通过以下命令结束应用：

```
1. hdc shell aa force-stop <bundleName>
```

返回“force stop process successfully”，表示应用已成功结束。

示例如下：

```
1. hdc shell aa force-stop com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/81IA_tsCRTyh4hR_vP1qMQ/zh-cn_image_0000002194158796.png?HW-CC-KV=V1&HW-CC-Date=20260612T021945Z&HW-CC-Expire=86400&HW-CC-Sign=588BA3C4D4B748BC513D47C31DDFB9EC8DF9C5B8C8242BA01C188DCA5834F893 "点击放大")

**参考链接**

[aa工具](../../../../../harmonyos-guides/系统/调测调优/调试命令/aa工具/aa-tool.md)
