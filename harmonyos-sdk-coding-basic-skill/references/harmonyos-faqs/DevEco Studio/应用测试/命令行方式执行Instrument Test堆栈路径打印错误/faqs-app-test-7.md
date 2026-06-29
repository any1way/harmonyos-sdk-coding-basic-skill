---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-7
title: 命令行方式执行Instrument Test堆栈路径打印错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 命令行方式执行Instrument Test堆栈路径打印错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f1fac7b48b4982cd21f670fe47c80afb89e0fa7697517cfe5393744b13cd1ff6
---

**问题现象**

在5.0.3.400版本下，通过命令行执行Instrument Test，堆栈信息中的文件路径和位置有误，出现“|”而不是“/”，升级到5.0.3.401及以上版本仍然有误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/-uw2MuaZQtGYnlYx4KP7Rw/zh-cn_image_0000002194158620.png?HW-CC-KV=V1&HW-CC-Date=20260612T024538Z&HW-CC-Expire=86400&HW-CC-Sign=BBBD66E72C97F266F17307DCF94AE32C7C14D1F07606B36BE7E497991F96D5AF "点击放大")

**原因**

在5.0.3.400版本下生成的.test文件和build文件夹未被同时删除，需要手动删除。

**解决措施**

删除5.0.3.400版本下生成的.test文件和build文件夹，然后重新执行测试用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/cQ8vwP2kTZSEKdQXKkTOSA/zh-cn_image_0000002194318232.png?HW-CC-KV=V1&HW-CC-Date=20260612T024538Z&HW-CC-Expire=86400&HW-CC-Sign=CFA1BAFB7BF6D43900C6808B4E9CB5A0EC827D595BBE389463DF532B66AB92D2 "点击放大")
