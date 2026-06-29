---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan
title: 使用ASan检测内存错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用ASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6d1303df8e95870324dae56a13fe32989e0718a0dd469dfdd8fbdef6d71b2079
---
为追求C/C++的极致性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于ASan的检测原理请参考[ASan检测原理](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/地址越界检测工具原理/bpta-stability-address-sanitizer-principle.md#section159561141247)。

## 使用约束

* 如果应用内的任一模块开启ASan，那么entry模块需同时开启ASan。如果entry模块未开启ASan，该应用在启动时将闪退，出现CPP Crash报错。
* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

## 开启ASan

可通过以下两种方式开启ASan。

### 方式一

1. 点击**Run > Edit Configurations >** **Diagnostics**，勾选**Address Sanitizer**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/KUZMfo8iTPCypjykJYMtrw/zh-cn_image_0000002602186261.png?HW-CC-KV=V1&HW-CC-Date=20260611T072942Z&HW-CC-Expire=86400&HW-CC-Sign=E6CCFD6391119C91023D605A418FDBD2639D9C1EA50CF82217EC15370750B901)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/F3vblOoESauVMDctjajAGQ/zh-cn_image_0000002571546728.png?HW-CC-KV=V1&HW-CC-Date=20260611T072942Z&HW-CC-Expire=86400&HW-CC-Sign=39B9FD13D5E4D3FA365BCDA50A7F126D9F8121554C7C02EDB5F9EF4BE1EAAB68)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加ASan配置开关。

   ```
   1. "asanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/E8S84LNISAGzzENIKJsFIQ/zh-cn_image_0000002602066209.png?HW-CC-KV=V1&HW-CC-Date=20260611T072942Z&HW-CC-Expire=86400&HW-CC-Sign=FAEF703B748ACE6FD36F090B5AD2778711FC0B289D2364ABD02D35AB6FCB6E6E)
2. 设置模块级构建ASan插桩。

   在需要开启ASan的模块中，通过添加构建参数开启ASan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```
   1. "arguments": "-DOHOS_ENABLE_ASAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/RTPJxnDkQKiY43GpXxPSNg/zh-cn_image_0000002571387092.png?HW-CC-KV=V1&HW-CC-Date=20260611T072942Z&HW-CC-Expire=86400&HW-CC-Sign=034A7857D8412C9104AE7C57BA54555E03617A5A3EC9E7BA599EFACAF67B711A)

   说明

   该参数未配置不会报错，但是除包含malloc和free函数等少数内存错误外，出现其他需要插桩检测的内存错误时，ASan无法检测到错误。

## 配置参数（可选）

ASAN\_OPTIONS用于在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等。ASAN\_OPTIONS支持在app.json5中配置，也支持在Run/Debug Configurations中配置。app.json5的优先级更高，即两种方式都配置后，以app.json5中的配置为准。关于ASAN\_OPTIONS的配置方式和常用参数请参考[配置参数](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/使用ASan检测内存错误/bpta-stability-asan-detection.md#section1496994494018)。

## 使用ASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[ASan日志规格](<../../../../系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/AddrSanitizer（地址越界）检测/address-sanitizer-guidelines.md#asan日志规格>)，异常检测类型请参考[ASan异常检测类型](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/使用ASan检测内存错误/bpta-stability-asan-detection.md#section12508111110451)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/UyHOBqg8T6GKOnSXtvC_yg/zh-cn_image_0000002602066207.png?HW-CC-KV=V1&HW-CC-Date=20260611T072942Z&HW-CC-Expire=86400&HW-CC-Sign=0434D61F2B2F45D2F53DAB01A16DC9BE34EBB40ABB0CE9B4BD668428D02A0FB6)
