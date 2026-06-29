---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-2
title: 预览功能使用过程中，可能无法使用帮助菜单压缩日志按钮收集日志
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览功能使用过程中，可能无法使用帮助菜单压缩日志按钮收集日志
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dff082eec6d860e47af017c5128b6f88e9603ca0a33a47bb34b6f7883794c603
---

**问题现象**

当同时预览多个工程时，点击帮助菜单中的“压缩日志”按钮，可能会因日志文件被占用而无法压缩。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/XareXeQaTgixKXLUWh_k-g/zh-cn_image_0000002229603945.png?HW-CC-KV=V1&HW-CC-Date=20260612T024050Z&HW-CC-Expire=86400&HW-CC-Sign=9122494EE516023B132B297D6CCB126F51CB9EC5433C76CB553121A7C2792133)

此时右下角会出现压缩失败的提示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/dmOS00paSASblsiyHgwkvQ/zh-cn_image_0000002229758417.png?HW-CC-KV=V1&HW-CC-Date=20260612T024050Z&HW-CC-Expire=86400&HW-CC-Sign=6DADB6E5AC35E783C384C5F62FA9D38489AD5A974B3CA50E9668F5718FD42149)

**解决措施**

请关闭预览过的工程，或者重启DevEco Studio后不要打开预览器，即可再次压缩收集日志。
