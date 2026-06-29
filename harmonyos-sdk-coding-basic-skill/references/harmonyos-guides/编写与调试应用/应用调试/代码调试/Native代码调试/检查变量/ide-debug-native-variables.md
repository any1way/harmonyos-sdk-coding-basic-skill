---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-variables
title: 检查变量
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:08+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:563d42504f48fc64604bdc4df66833aa8954cea41b9fb68656b0f51b473f909a
---

调试时，在“Variables”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击“Edit Configurations...”打开调试配置，在 native 调试配置界面中勾选“Show static/global variables in the Variables Pane”，调试过程中变量列表会展示全局/静态变量。

## Simplify STL

在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Debugger > C++ Debugger”，通过勾选“Display STL variables as visualization in the Variables Pane”在变量列表中展示简化后的 STL 变量值，或去掉勾选以展示其原始结构。

## 变量监视

在"Watches"列表中输入表达式，然后点击Add to Watches 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/_P4OaJxlRKSvJQ8IQgUEIw/zh-cn_image_0000002571547210.png?HW-CC-KV=V1&HW-CC-Date=20260611T072907Z&HW-CC-Expire=86400&HW-CC-Sign=D1866B8105427C21BE737739679119F469E2B99107197070899B50F824C73608)，或在某个变量右键菜单中的“Add to Watches”添加监视的表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/FWkp_27GR3OV1yrGsjitGA/zh-cn_image_0000002602186745.png?HW-CC-KV=V1&HW-CC-Date=20260611T072907Z&HW-CC-Expire=86400&HW-CC-Sign=51C7FC6DF866ECCB9013C2E79CD77B44D69934EEAADA8FFD8C4886CF8BAB7778)

## 表达式求值

通过点击“Evaluate Expression...”按钮，或Watches 页面中的输入行中，输入表达式进行计算。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/eEv5S-TYRreNEBb9wfUUBA/zh-cn_image_0000002602066687.png?HW-CC-KV=V1&HW-CC-Date=20260611T072907Z&HW-CC-Expire=86400&HW-CC-Sign=9F57729DE26256F1E695B738FBEAB8899DDEDC6F4B1725E0E9A26333B500FA7F)

## 查看十六进制视图

在“Variables”页面点击鼠标右键，弹出框中选择“Show As Hex Values”，此时页面中的整型变量会以十六进制进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/rF4blp-OQRi7Jp_mEvUedA/zh-cn_image_0000002602066689.png?HW-CC-KV=V1&HW-CC-Date=20260611T072907Z&HW-CC-Expire=86400&HW-CC-Sign=8BFDAA9DF747A9DAD2AFE7E3050943DD8BCFD0EDC75DEC306F1DAEA1F546B530)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uM0U5rveQwGKPS0qsUaVNg/zh-cn_image_0000002602186743.png?HW-CC-KV=V1&HW-CC-Date=20260611T072907Z&HW-CC-Expire=86400&HW-CC-Sign=18E198572ECA0FA501B6DF98D251696A7D9780CB2BCC7AB546184FB7027BF102)

说明

* 无法查看长度超过64位的数据结构。
* 无法查看引用类型返回值。
* Step Out返回的位置存在断点时，无法查看函数返回值。

## 其他说明

对于特定类型的变量，还支持查看bitmap预览、查看较长的字符串等功能。

* ...View Bitmap：支持在调试时查看bitmap预览。

* ...View：支持展开查看较长的字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/TnQYDXf3S52PFfaOZlTaxA/zh-cn_image_0000002571387574.png?HW-CC-KV=V1&HW-CC-Date=20260611T072907Z&HW-CC-Expire=86400&HW-CC-Sign=91D48ED2ABD79445C064AC9BCCA6367C799B6350A26D68AE7E09374121ADA2F9)
