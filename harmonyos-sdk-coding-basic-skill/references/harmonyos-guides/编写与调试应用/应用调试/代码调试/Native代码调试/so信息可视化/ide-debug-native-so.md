---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-so
title: so信息可视化
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > so信息可视化
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:13+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:8a87f8b14e4fd3f6d9c4ae8a3a28e8045feaac8094f9319bb2468a4124a112b0
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/vdwthpqxRNKP54CJLyvooQ/zh-cn_image_0000002571546866.png?HW-CC-KV=V1&HW-CC-Date=20260611T072912Z&HW-CC-Expire=86400&HW-CC-Sign=DF168EDE378A7D21FCFDB3E5AD53C3A3378374EF92F6F1E45348BCA1EB04538F)，勾选**Modules**，打开模块视图。

在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持字符串匹配搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/vKYWuJQXQm6309kOnMbiOQ/zh-cn_image_0000002602066347.png?HW-CC-KV=V1&HW-CC-Date=20260611T072912Z&HW-CC-Expire=86400&HW-CC-Sign=CFCB22294DB3CD99A7BEF9FCE041C46E0C62D8C4A99B0BA60A51707DE9452B5F)

* 加载符号表文件

  如果符号未加载，可右键点击模块，选择**Load Modules**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。

  如需将符号恢复为初始状态，可右键点击模块，选择**Reset** **Modules**。
* 添加源码地址映射

  加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。

  如需恢复为默认路径，可右键点击模块，选择**Reset** **Source Mapping****s**。
