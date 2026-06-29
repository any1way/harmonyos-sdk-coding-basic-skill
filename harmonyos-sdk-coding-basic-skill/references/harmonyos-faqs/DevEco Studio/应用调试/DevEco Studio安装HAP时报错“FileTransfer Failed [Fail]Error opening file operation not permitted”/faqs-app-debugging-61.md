---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-61
title: DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:06f258e640cc386e02d78ab254438ea82b36ace599de1d168942719abdcbef1f
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/FPaBcvfkRbqqfi4jztUjOQ/zh-cn_image_0000002557334391.png?HW-CC-KV=V1&HW-CC-Date=20260612T024500Z&HW-CC-Expire=86400&HW-CC-Sign=188ED5AE4981BB05BF1A687F674744E3C075E1FBC6A2E7844139265A9CC68B79)

**解决措施**

出现该问题的原因是安装包HAP所在路径没有权限。

1、Windows系统建议将工程移出C盘，然后重新运行。

2、MAC系统为DevEco Studio获取完全磁盘访问权，请进入**“系统设置”>“隐私与安全性”>“完全磁盘访问权限”**，在列表中勾选DevEco Studio软件并重启。
