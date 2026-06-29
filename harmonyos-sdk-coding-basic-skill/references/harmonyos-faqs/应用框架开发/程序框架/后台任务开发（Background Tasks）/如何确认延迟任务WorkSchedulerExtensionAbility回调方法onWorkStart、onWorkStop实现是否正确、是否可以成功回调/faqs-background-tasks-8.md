---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-8
title: 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3ffb8beac4c608f34de485b1fca7cc11136c98ad53afd23065789188433b17d6
---

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下hidumper命令手动触发延迟任务执行回调。

```
1. hdc shell hidumper -s 1904 -a '-t com.hmos.workschedulerdemo MyWorkSchedulerExtensionAbility'
```

com.hmos.workschedulerdemo、MyWorkSchedulerExtensionAbility需要替换为需要查询应用的bundleName和abilityName。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/n9ckJk7-SjO6AOqvDPaBlA/zh-cn_image_0000002194317960.png?HW-CC-KV=V1&HW-CC-Date=20260612T022221Z&HW-CC-Expire=86400&HW-CC-Sign=97FA577CE5C8B7C4D4217ACD15E6D7FCC0CEB0DB9F3B4BC1DACF23FECC355AFD "点击放大")
