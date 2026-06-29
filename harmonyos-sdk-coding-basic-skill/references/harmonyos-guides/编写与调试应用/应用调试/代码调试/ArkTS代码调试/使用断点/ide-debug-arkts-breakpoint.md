---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:59+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fb98d687f9535ddf1f9134dd96624aaf9b3baf1e99adc6ab46b5a76561687646
---
DevEco Studio ArkTS支持行断点、日志断点等多种不同类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，您可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到您要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当您设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/AJpXeq_MSSSmetsIl6v5lg/zh-cn_image_0000002602186373.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=FFCDE43C88A5D3DDFD0B7ABD074D5E184C0BA61F97ACECB5ADED5040A39F0217)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅会在满足特定条件时才会暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/xU1DQ80qTgKwmaSrO7htIg/zh-cn_image_0000002571387208.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=77381D4790CC058DC651BED1D9ADE020B47D4BD23025034AF16DBCEDD159AFA7)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/pCg6d3vmTIe8dpn5-1Z3wg/zh-cn_image_0000002571387202.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=EC0C6EC2D6805C72D1AE7CBF1BEE46B5476ADE3712B43B986751C3929BF6CE61)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/D22lxJ9eS_u1NRYlhzYdoA/zh-cn_image_0000002602186371.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=7040973A0A45B7C0843B7C1FF34E2B4E95CE9CADAEEB6D1FC09A57951BA76765)。

   当应用运行到代码处，会在代码处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/cx99syS8RVKadUdR6N5WPw/zh-cn_image_0000002602066321.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=F1078837AB6D885EBC6C69FFC707E6B3B12C4021DA8991A02B3009713D7D25EA)

## 日志断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选以下类型的Log，可以使进程运行到断点时在Console窗口打印相应日志。

* 勾选**"Breakpoint hit"message**，程序运行到断点时，打印“Breakpoint reached”。
* 勾选**Stack trace**，程序运行到断点时，打印当前线程的堆栈。
* 勾选**Evaluate and log**，并添加表达式，程序运行到断点时，打印表达式的值。

说明

未勾选Enable的断点不会打印日志，未勾选Suspend execution的断点会打印日志，不满足所设置的Condition的断点不会打印日志。

## 临时断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选**Remove once hit**，该断点只生效一次，生效后该断点会被删除。

## 函数断点

从DevEco Studio 6.0.0 Beta2版本开始，支持在ArkTS代码中设置函数断点。

函数断点也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，点击**+ > ArkTS Symbolic Breakpoints**，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/HVQ8v7I3QS2yT2Gcky0B2g/zh-cn_image_0000002571546836.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=9AC8D8C1E8DCEF75DB149D3C1041355ED9F45173703E916D4BC7D4F42E5AC0A2) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/QTbYWVotSi28idNd3HZxAA/zh-cn_image_0000002571546832.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=0AB4999D4716E22F88A9DB0BF389512D5697FE884D0143F46EA4B5282697209E)

说明

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/Js Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/UJp5x4d3QEyvJIKqswIgxw/zh-cn_image_0000002571546830.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=943795D8E7475A79395D598336FAEB2AADC95116EA39B3BCF3FEB6EB68AD3B26)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/xDla-VZvQCiWehezfGDCsQ/zh-cn_image_0000002602186377.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=D637DD0DAB3EE1415B5FF9362A50C0273ECA49F20B5E9BE61B17B50F9F63E29E)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/gK_whpBESkuaP0YHR_lswQ/zh-cn_image_0000002602186367.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=02A550BFFEE7EF291D3702ABD0286BA420D4959DB7C222FDA9A5E1B38847DA30)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/8CG-ahBkRyiSaSs6-5RKag/zh-cn_image_0000002571387198.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=E51EB21879A49DD2ABE861D92AED2A060966B1A3BC8014008BBAC113450AB055)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/RyDDKNs2RP-f_nOPHBqkQw/zh-cn_image_0000002571546840.png?HW-CC-KV=V1&HW-CC-Date=20260611T072858Z&HW-CC-Expire=86400&HW-CC-Sign=3591C23B9E872F0248FA5EA0BB86B44FD3418A757C044A39547A95C1C2071958)
