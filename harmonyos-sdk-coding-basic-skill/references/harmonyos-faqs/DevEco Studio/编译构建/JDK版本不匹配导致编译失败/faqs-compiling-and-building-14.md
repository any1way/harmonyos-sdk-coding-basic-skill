---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-14
title: JDK版本不匹配导致编译失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > JDK版本不匹配导致编译失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3084ed82b6ae13b8aad8377a2098c071430706e0f469ec427344394a58974e15
---
**问题现象**

通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/wZVor4lLSmelHPejhWTkrA/zh-cn_image_0000002229604033.png?HW-CC-KV=V1&HW-CC-Date=20260612T024107Z&HW-CC-Expire=86400&HW-CC-Sign=A4DA836B14EBE4B48F96DD70556E5C292B83D1E974C6A069EBA77EE18DBC5266)

**解决措施**

该问题需使用配套的JDK 17版本解决，请根据如下方法进行修正：

1. 下载并安装JDK 17版本。
2. 修改JAVA\_HOME环境变量，取值为JDK 17。如果是Linux系统，可参考命令行方式构建服务或应用的[配置JDK](../../../../harmonyos-guides/命令行工具/搭建流水线/ide-command-line-building-app.md#section195447475220)。
