---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderpositionparams
title: OH_AudioSuite_SpaceRenderPositionParams
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_SpaceRenderPositionParams
category: harmonyos-references
scraped_at: 2026-06-11T16:27:04+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:b1d9c8adc55576cfd89f2501e0fad76940d87bdeedf82c5e84e097221268b206
---
```
1. typedef struct {...} OH_AudioSuite_SpaceRenderPositionParams
```

## 概述

PhonePC/2in1Tablet

定义3D空间渲染效果节点固定摆位模式的配置参数。

左手坐标系：伸出左手，用拇指和食指形成一个“L”形。拇指指向右侧，食指向上，其余手指指向前。此时形成了一个3D的左手坐标系。在这个坐标系中，拇指、食指和其他手指分别代表x轴、y轴和z轴的正方向。

**起始版本：** 23

**相关模块：** [OHAudioSuite](../../模块/OHAudioSuite/capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](../../头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| float x | 空间中的X坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float y | 空间中的Y坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float z | 空间中的Z坐标。取值范围为[-5.0, 5.0]，单位为米。 |
