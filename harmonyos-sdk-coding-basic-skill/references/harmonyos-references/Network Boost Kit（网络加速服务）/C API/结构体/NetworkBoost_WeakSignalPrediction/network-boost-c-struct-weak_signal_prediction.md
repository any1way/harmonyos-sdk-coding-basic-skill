---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-weak_signal_prediction
title: NetworkBoost_WeakSignalPrediction
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_WeakSignalPrediction
category: harmonyos-references
scraped_at: 2026-06-11T16:15:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2562fcc5855b87d087c9ae275ed669c1f0704bf914f798ec00d09eba6780b519
---
## 概述

PhonePC/2in1Tablet

弱信号预测相关信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](../../头文件/network_boost_quality.h/network-boost-c-files-quality.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| bool [isLastPredictionValid](network-boost-c-struct-weak_signal_prediction.md#islastpredictionvalid) | 最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。 |
| uint32\_t [startTime](network-boost-c-struct-weak_signal_prediction.md#starttime) | 预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。 |
| uint32\_t [duration](network-boost-c-struct-weak_signal_prediction.md#duration) | 预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### duration

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_WeakSignalPrediction::duration
```

**描述**

预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。

### isLastPredictionValid

PhonePC/2in1Tablet

```
1. bool NetworkBoost_WeakSignalPrediction::isLastPredictionValid
```

**描述**

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。

### startTime

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_WeakSignalPrediction::startTime
```

**描述**

预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。
