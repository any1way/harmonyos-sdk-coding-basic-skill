---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-60
title: DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: no such file or directory”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: no such file or directory”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f783f72875fd6e9ce0aebc577fe672364c77f4e7cdc32724d5eee09b29dccfcd
---
**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: no such file or directory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/6Wx-U4_jS3SAEiMjEr_XZQ/zh-cn_image_0000002356774736.png?HW-CC-KV=V1&HW-CC-Date=20260612T024459Z&HW-CC-Expire=86400&HW-CC-Sign=E675091E93BAEAB492506FEA65AE5BF9E442AC2FB05923F3D206A663100A6FB4)

**解决措施**

出现该问题的原因是path路径的安装包不存在，可以检查签名HAP包是否没打包成功，修改签名，正常打出签名HAP包后再运行。

**参考链接**

[对HAP/APP进行签名](../../../../harmonyos-guides/命令行工具/搭建流水线/ide-command-line-building-app.md#section103321051433)
