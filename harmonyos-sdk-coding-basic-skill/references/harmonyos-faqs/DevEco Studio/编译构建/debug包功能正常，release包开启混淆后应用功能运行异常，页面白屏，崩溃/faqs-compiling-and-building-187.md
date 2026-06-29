---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-187
title: debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
breadcrumb: FAQ > DevEco Studio > 编译构建 > debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:740767aab67915092be54be92203f2f33f0ecda0fd347c08a61ee3a7ec432389
---
**解决措施**

在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/1z_3-7VnQq60PA7MbHtUvA/zh-cn_image_0000002372892821.png?HW-CC-KV=V1&HW-CC-Date=20260612T024338Z&HW-CC-Expire=86400&HW-CC-Sign=B0DB8427EAC9329331A944CE76CC8D56ACE4E99F325900FD61D7AA8BABB9D5AE)

如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。

**参考链接**

[通过混淆助手配置保留选项](../../../../harmonyos-guides/构建应用/混淆加固/ide-build-obfuscation.md#section19439175917123)
