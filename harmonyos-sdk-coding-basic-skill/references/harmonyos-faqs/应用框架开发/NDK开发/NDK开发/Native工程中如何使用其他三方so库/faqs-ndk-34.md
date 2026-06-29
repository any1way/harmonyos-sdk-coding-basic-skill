---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-34
title: Native工程中如何使用其他三方so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native工程中如何使用其他三方so库
category: harmonyos-faqs
scraped_at: 2026-06-12T10:25:06+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:f7339a120eb986cc51e7f66fb77149383dcf794c2f1d35536f446e245d5e6f0f
---
1.将编译好的so库放到Native工程的entry/libs/arm64-v8a/目录下，并将so库对应的头文件放到entry/src/main/cpp目录层级下（可以在cpp目录下增加一个文件夹专门存放三方so库的头文件）。

2.在CMakeLists.txt文件中链入so库。

3.在Native侧 .cpp文件中引入头文件使用so库的相关能力。

示例如下：

在Native侧集成三方库Curl

1. 将移植后的Curl的so库放到Native工程的entry/libs/目录下，并将移植后生成的、包含头文件的include目录放到entry/src/main/cpp目录下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/68RTP_xWROCICe895cOU2A/zh-cn_image_0000002194158760.png?HW-CC-KV=V1&HW-CC-Date=20260612T022505Z&HW-CC-Expire=86400&HW-CC-Sign=981E673FC917530F757288FC931BFA575F0A37C13F6123B7E6299D8F52990A77 "点击放大")

2. 在CMakeLists.txt文件中链接Curl对应的so库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/RM5hC3gGSjCyU257q9_JMg/zh-cn_image_0000002194158764.png?HW-CC-KV=V1&HW-CC-Date=20260612T022505Z&HW-CC-Expire=86400&HW-CC-Sign=673088179A171A8DFF39F224767F6030D151955E50CE02F5685EA8B10BFDD8F4 "点击放大")

3. 在Native侧.cpp文件中通过引入头文件curl.h来使用Curl的相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ZWbL2Gm2RhCutz3DcPx4cQ/zh-cn_image_0000002229758629.png?HW-CC-KV=V1&HW-CC-Date=20260612T022505Z&HW-CC-Expire=86400&HW-CC-Sign=6CAD36E977173536BD1E17D8E593F3E71D29A0E86F6A3FBED903B37408497682 "点击放大")

**参考链接：**

[在NDK工程中使用预构建库](../../../../../harmonyos-guides/NDK开发/构建NDK工程/在NDK工程中使用预构建库/build-with-ndk-prebuilts.md)
