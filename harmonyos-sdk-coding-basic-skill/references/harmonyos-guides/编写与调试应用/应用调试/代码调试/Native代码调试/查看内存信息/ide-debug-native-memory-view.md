---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ed949feae5bba7a54c820ea7baed9579c45ab8b464b881b1a1337dd5c7f65958
---

在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址，点击“View”按钮，查看对应地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/7yy4bKYMS_i5gSxGuCzcwQ/zh-cn_image_0000002571546980.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=BE9BE1E9F76F9E4160C6DC2D86FADE85646363C6D8731B0C99AE9B21762A78AF)

点击“Settings”按钮，设置进制、偏移量和内存数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/aSvXZtiDRrmkA-TiDi6MiA/zh-cn_image_0000002602066461.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=EF6B6003157CAE71CB1F419FF5069A6433F5B4F1099FED1873B4AA5EC85923AB)

## 内存转换

通过点击某一个内存格子，右侧会自动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。

## 查看变量内存

在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/fjWJ9iZXTDO4N067tXCzJg/zh-cn_image_0000002571387342.png?HW-CC-KV=V1&HW-CC-Date=20260611T072908Z&HW-CC-Expire=86400&HW-CC-Sign=505FAE0708301778FBA55BE5BEA0CCE3AA13FA2E48FD6B0EE52E225A13CE794C)

## 内存修改

您可以在内存格上双击，键入您想要修改的内存来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。
