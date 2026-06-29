---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:09+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:83c6e9e7959b29d07f217805e899588737de7b1e512b0f5c904a05fe55f6bdaa
---

DevEco Studio支持查看汇编和汇编代码调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编代码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择“**Disassemble Frame**”，可以查看该栈帧对应的汇编代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/3bJudvQxQm6G7LKzEOhlZw/zh-cn_image_0000002571547182.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=1DF985D3BB57451619C198A8AF4AF64F221D91274C81E59353F18B936E55C12C)

支持在汇编视图中展示源码、函数名，可以跳转到对应源代码，汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/b0NYAIXvQSiqeNTlKijE3Q/zh-cn_image_0000002602066663.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=88EC59E947FFEDC51FA7071CF1FE86F76615FD1B4A599A0E962F2F6F6BD75AA9)

## 汇编断点

可以在汇编视图设置断点，程序运行到对应地址时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/K2-4csbrR_qpueGQwTTESw/zh-cn_image_0000002571547184.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=EB9526C7B06EF4CEDEB70D474BAD779A96D7C6CD49F41C4D64696837F82FBFA5)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/mBWqeSQtTnmAzwYtT1eMVg/zh-cn_image_0000002602186715.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=6E6801E3C4E625DF5217A5A06E456CD2FD96D235E81480160F38289D7E2A7622)
