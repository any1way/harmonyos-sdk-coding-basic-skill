---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log
title: FaultLog
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:37+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:e8753367b532b884fab84960ee93a9037f44a57627fb9ba198db536d30ca7ce6
---
当应用运行发生错误导致应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

FaultLog由系统自动从设备进行收集，包括如下几类故障信息：

* [AppFreeze](../查看AppFreeze（应用冻屏）日志/ide-faultlog-appfreeze.md)
* CPP Crash
* JS Crash
* System Freeze
* [ASan](../使用ASan检测内存错误/ide-asan.md)
* [HWASan](../使用HWASan检测内存错误/ide-hwasan.md)
* [TSan](../使用TSan检测线程错误/ide-tsan.md)
* [UBSan](../使用UBSan检测未定义行为/ide-ubsan.md)

说明

调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的App Freeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。

当前支持屏蔽的App Freeze故障类型：

* THREAD\_BLOCK\_3S/THREAD\_BLOCK\_6S：应用主线程卡死检测，卡住3秒/6秒。
* APP\_INPUT\_BLOCK：输入响应超时。

当前支持屏蔽的System Freeze故障类型：

* LIFECYCLE\_TIMEOUT：app、ability生命周期切换超时。

## 查看FaultLog日志

### 查看设备历史抛出的FaultLog日志

打开FaultLog窗口，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/aquluHvBTtGVt1GVRnXQQg/zh-cn_image_0000002571387388.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=3C74434CFEDDD76E2C0606FB71891D568676580694653D2AB357F789719BCE0B)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，开发者点击**Jump to Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/3EvHVH6fSi6iFxj5tE2tuQ/zh-cn_image_0000002571547030.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=08784EDA1AEBBE1D8CF96FBE10C33DA7E4F55F2AD2C7ED3A54F210EAE4FF8856)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ku9L4DuaTQyfTWwxIV3eJw/zh-cn_image_0000002571547026.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=9B28836B22D2A2C25007CA0BAB6551CB662811B701A7D3CD0D6789830E65CA7E)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便后续的进一步分析。开发者可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**Export FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/lhQT1derRP2gBA6y3K0U1A/zh-cn_image_0000002571387396.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=DC2003CE2E20E9CAD4A7C03C256A477EB4C4EDBBE97D5EE268064CEFDDE7C607)
  + 点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/1bUYAkqnTu-IN1pE7aHb-A/zh-cn_image_0000002602186565.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=0A153E79D9736E3C462C77E5F2CD8F1E5D654A1F4E2167B52B55B46BE33167C0)，弹出子选项后进一步点击**Export Selected FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/MAU2OiBETWCLaEVJtzle9A/zh-cn_image_0000002602066507.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=56563FFB4503433F3C0AA9C11FD3BB7D47DD0E86D659DC6DBA49801EE843D679)
* 保存所有日志：点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/eX5GVXj9TVOgiYcaCqR5jw/zh-cn_image_0000002602186557.png?HW-CC-KV=V1&HW-CC-Date=20260611T072936Z&HW-CC-Expire=86400&HW-CC-Sign=58804C27C435F24BFC714A533C0D0CDEFA7BA1E6CF467FB752B6502BBC5EAF28)，弹出子选项后进一步点击**Export All FaultLog**。
