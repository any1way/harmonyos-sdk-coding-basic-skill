---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/debug-asan
title: C/C++内存错误检测
breadcrumb: 指南 > NDK开发 > 调试和性能分析 > C/C++内存错误检测
category: harmonyos-guides
scraped_at: 2026-06-01T15:16:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:224809f174dfd883ef90ac6e27c7c7c9d2e965b8136aa53759179712ff09b0d0
---
为追求C/C++的更优性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。

关于ASan的使用说明请参见[C/C++内存错误检测](../../../编写与调试应用/日志与故障分析/故障分析/使用ASan检测内存错误/ide-asan.md)。
