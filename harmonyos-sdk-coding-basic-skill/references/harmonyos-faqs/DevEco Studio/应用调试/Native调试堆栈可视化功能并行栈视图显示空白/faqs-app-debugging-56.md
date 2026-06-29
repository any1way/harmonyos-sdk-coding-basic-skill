---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-56
title: Native调试堆栈可视化功能并行栈视图显示空白
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试堆栈可视化功能并行栈视图显示空白
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e17d647c7f4c705cd1e82f8f999a74b136020666ef88a765e1a5eeb1842b7149
---

**问题现象**

使用Native调试堆栈可视化功能时，如果在任意两个页签之间来回切换，可能会遇到并行栈视图界面显示为空白的情况。

**解决措施**

导致该问题的原因可能是电脑GPU不兼容，或在云桌面的场景下使用DevEco Studio。

在DevEco Studio中**双击Shift**，在弹出的窗口中搜索**Registry**，**在Registry**页面中勾选**ide.browser.jcef.gpu.disable**项，关闭窗口并重启DevEco Studio即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/PAXpsIR9TtGiV28IV2mkkg/zh-cn_image_0000002521308425.png?HW-CC-KV=V1&HW-CC-Date=20260612T024503Z&HW-CC-Expire=86400&HW-CC-Sign=F6F74D13B11D2FDF179DE81A240AD50F689F2A22575ABD8B600DF5576D05106F)
