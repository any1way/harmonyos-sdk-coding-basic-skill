---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hw-guide
title: 硬件兼容性简介
breadcrumb: 指南 > NDK开发 > 硬件兼容性 > 硬件兼容性简介
category: harmonyos-guides
scraped_at: 2026-06-01T15:16:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7e2f3226e46a8a39683cfd6f8df9ce0a4ddc075d61c225e5ba2ccbf421ea08d0
---
使用C/C++开发HarmonyOS应用原生库时，需要感知到硬件特性；HarmonyOS系统会运行在多种架构、多厂商的设备上，对于使用了HarmonyOS原生库的应用，如何保证其在不同设备上的兼容性以及体验的一致性是一个很大的挑战。

本章节将介绍HarmonyOS应用二进制接口（Application Binary Interface，简称ABI），定义了当前HarmonyOS系统支持的[ABI标准](<../HarmonyOS ABI/ohos-abi.md>)；同时也提供了如何使用[CPU扩展特性](../CPU特性/cpu-features.md)的指导，方便应用在不破坏兼容性的基础上更好的利用CPU硬件特性。最后通过一些简单的示例演示如何更好的使用[ARM Neon特性](../使用Neon指令扩展/neon-guide.md)。
