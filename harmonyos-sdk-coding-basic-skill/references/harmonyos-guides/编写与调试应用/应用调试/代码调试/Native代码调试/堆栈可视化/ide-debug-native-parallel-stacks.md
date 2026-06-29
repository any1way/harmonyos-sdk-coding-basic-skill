---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-parallel-stacks
title: 堆栈可视化
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 堆栈可视化
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bd9b80cb8de6c8696a7e91d159fa88abc926c2bb52619b9728a6bc78919ec6c9
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/QOUgQHGDTSielcA7rmTEgg/zh-cn_image_0000002571546762.png?HW-CC-KV=V1&HW-CC-Date=20260611T072912Z&HW-CC-Expire=86400&HW-CC-Sign=01CA435D9C0F85CF593B976BBBD0D9BE6CCD8871C320A97761891A3E975ED045)，勾选**Parallel Stacks**，打开并行栈视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/iZ0b2FItTXGTHx9jJiSKqw/zh-cn_image_0000002571546760.png?HW-CC-KV=V1&HW-CC-Date=20260611T072912Z&HW-CC-Expire=86400&HW-CC-Sign=0A9497B6650C9537071DA22284DEDAEA1B0FEE01B08142016E88D74020BB8DA7)

在程序停下时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/5jspI5lJRC23WKP_OcELKA/zh-cn_image_0000002602186293.png?HW-CC-KV=V1&HW-CC-Date=20260611T072912Z&HW-CC-Expire=86400&HW-CC-Sign=21F359B09D691C94533B601A0695E7814632BDC60FC3037F1E6554E2675A7887)

## 调用栈跳转

您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。

## 线程信息查看

在多个线程合并的位置处悬停鼠标，可以显示这些线程的具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/edUWqYTLQO6S8xkrmBPzkg/zh-cn_image_0000002602186295.png?HW-CC-KV=V1&HW-CC-Date=20260611T072912Z&HW-CC-Expire=86400&HW-CC-Sign=273C23EA4F60C59B2CAA610A0B450E3D16D8DCDB8DE9E5B4D1AE50C49F86BBFF)
