---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b4c2bba5fe5607eb973e70695359c062b57c4e0a3a23d85612641ae3b343c589
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DtU-Vj-FTFiZnsXdt8jlYA/zh-cn_image_0000002571546578.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=171E84AC5EB241A6DB4BD3B0754CE47FC3344B8F5229386690D1134723C4B446)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/PNzESzvESPyzRTMdIZI5Tg/zh-cn_image_0000002602186105.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=AD73CA12656BE5F0B393069E99AAC23265F279E4E5CF7E86DC6A08F1D8690C27)

## 条件断点

在某个断点的配置中，勾选 Condition ，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

说明

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/6YMR3KIZTxmRfrLh7R5Dkw/zh-cn_image_0000002602066059.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=A58DFBD70C0470ED6FEAB8A3533768A11B3D1B09F1083155DBDD49DED31B1EF0)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/iQIwqht5QL2YD07zIT4a5g/zh-cn_image_0000002571546576.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=13AA7C9CA9AB17CF49148BEF0A76ACC2F2E7506B4A3C2FCDDAC53AEC3A8E44DC)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

说明

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/-p3OUWGbTWCSsyhgvghuDg/zh-cn_image_0000002571386938.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=B628C1BEB17771B77A8F60A22E6A9C0830DFB1D99A117A0C2A89BCF69817A27F)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/aKbP2sNGQ16bL4WJsDY4YQ/zh-cn_image_0000002602186111.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=E12C642D97ED1A8E93B60A83954C3194B298A03A1F8F61F2EFC0D7C75A4ED3AB)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/ECYepTBOS-mvqjGE5GLeHA/zh-cn_image_0000002602186107.png?HW-CC-KV=V1&HW-CC-Date=20260611T072906Z&HW-CC-Expire=86400&HW-CC-Sign=9BC8CC418DD52ABA301036D7DF3D2EFE6F716AD92A1BD9140C6D438F8F261A90)

说明

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
