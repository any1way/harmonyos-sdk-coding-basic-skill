---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-weaksignaljudge
title: 弱网感知判决
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 > 弱网感知判决
category: harmonyos-guides
scraped_at: 2026-06-01T11:20:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6f002f7662e3516d678a2aa11092745ced55dc30e74d66b16805f0eff6dc128f
---
通过[网络质量评估](../网络质量评估/networkboost-qoscallback.md)和[网络场景识别](../网络场景识别/networkboost-scenecallback.md)章节，弱网感知判决可归纳为3种方式获取：

**监听系统实时判决**：

根据网络场景识别信息，如NetworkScene.scene(weakSignal/congestion)，系统直接判决为弱网。

**监听系统预测判决：**

根据网络场景识别中的弱信号预测信息，如NetworkScene.weakSignalPrediction，系统预测即将进入弱网区域。

**应用自定义判决：**

根据网络质量评估信息，如NetworkQos(linkUpBandwidth/linkDownBandwidth/rttMs/linkUpBufferDelayMs/linkUpBufferCongestionPercent)，应用自定义门限来判决为弱网。

应用可根据自身业务特点，选择其中一种或多种使用。
