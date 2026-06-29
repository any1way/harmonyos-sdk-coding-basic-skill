---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/debug-performance-profiling-overview
title: 调试和性能分析概述
breadcrumb: 指南 > NDK开发 > 调试和性能分析 > 调试和性能分析概述
category: harmonyos-guides
scraped_at: 2026-06-01T15:16:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c05dc1d1c4f1b00d73a6896235288b7a4da689f3c59857af2f4bdd8198011410
---
通过NDK开发C/C++程序不可避免会遇到Native程序常见的异常、性能等问题，NDK随包提供了常用的调试调优工具，方便开发者定位问题。

* 已提供如下方式进行调试和性能分析：

  + [C/C++内存错误检测](../../../编写与调试应用/日志与故障分析/故障分析/使用ASan检测内存错误/ide-asan.md)
  + 通过DevEco Studio调试
    - [1.C/C++反向调试](../../../编写与调试应用/应用调试/代码调试/Native代码调试/反向调试/ide-debug-native-reverse.md)
    - [2.使用真机进行调试](../../../编写与调试应用/应用调试/调试概述/ide-debug-device.md)

      注意

      在[使用真机进行调试](../../../编写与调试应用/应用调试/调试概述/ide-debug-device.md)中，如果本地编译设备so文件的源码路径和当前配置的C++源码路径不一致，可以参考[三方源码调试](../../../编写与调试应用/应用调试/代码调试/三方库源码调试/ide-source-code-debugging.md)
