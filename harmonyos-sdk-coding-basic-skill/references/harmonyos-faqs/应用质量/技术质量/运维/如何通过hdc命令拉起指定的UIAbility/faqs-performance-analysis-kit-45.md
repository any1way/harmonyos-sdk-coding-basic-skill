---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-45
title: 如何通过hdc命令拉起指定的UIAbility
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令拉起指定的UIAbility
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:44+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:584aebd2860b6a0a18a67785e211a63f460c331691f5088dcb36d2f95fbf1f25
---
使用命令拉起指定UIAbility：

```
1. hdc shell aa start -a <UIAbility Name> -b <Bundle Name>
```

启动成功时，返回"start ability successfully."，启动失败时，返回"error: failed to start ability"，同时会包含相应的失败信息。

示例如下：

```
1. hdc shell aa start -a EntryAbility -b com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/BuaiR0IVS9Ow4FCLUBJV9Q/zh-cn_image_0000002229758597.png?HW-CC-KV=V1&HW-CC-Date=20260612T021943Z&HW-CC-Expire=86400&HW-CC-Sign=ABD6C0797E7AD54942A13FFAB47563EC8B28427895FB3D2D5014806D1F2D3DA8 "点击放大")

**参考链接**

[aa工具](../../../../../harmonyos-guides/系统/调测调优/调试命令/aa工具/aa-tool.md)
