---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-55
title: 应用运行报错：hap path error
breadcrumb: FAQ > DevEco Studio > 应用调试 > 应用运行报错：hap path error
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9883a9c58889c03bbbc3774680fc4f244c598c109c0cb116423f31d689cb010a
---

**问题现象**

启动调试或运行应用/服务时，应用运行崩溃，提示错误信息“errorMsg: hap path error”。

**解决措施**

如果依赖的应用包未安装，建议进入**Run/Debug Configurations > Deploy Multi Hap****/Hsp**页签，勾选**Deploy Multi Hap/Hsp Packages**，选择所需依赖的应用包，然后重新运行应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/pRi1ye84TeWpCH1j10GHKA/zh-cn_image_0000002487797922.png?HW-CC-KV=V1&HW-CC-Date=20260612T024502Z&HW-CC-Expire=86400&HW-CC-Sign=F32E504C4270164BD85811C5795D8DCAAFB0BDB6E65E33D35DDAABC8DC7D8352)
