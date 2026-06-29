---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4
title: 出现“container is not running”错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 出现“container is not running”错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:839b978081c9d8144b5d930383c84e9a6b1e35009ba0fd33a8636a6d8e68066f
---

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/26zDvHghQa-KDNFBfG3U7w/zh-cn_image_0000002194318268.png?HW-CC-KV=V1&HW-CC-Date=20260612T024533Z&HW-CC-Expire=86400&HW-CC-Sign=643F935A40723AE5E14E9C6F2028D2942A0A98F8C4F7BE24FDCF1DA7D6243CA4)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/jpIR3fLwSLy8mAC9FVSzbw/zh-cn_image_0000002194158644.png?HW-CC-KV=V1&HW-CC-Date=20260612T024533Z&HW-CC-Expire=86400&HW-CC-Sign=20AEFD781936F2C60C6FA46FD7CA0440A8CCD4DBAD6BE96C5EDD92B8531999E8)
