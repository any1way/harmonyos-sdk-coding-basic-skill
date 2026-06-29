---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-tensorhandlearray
title: OH_AI_TensorHandleArray
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 结构体 > OH_AI_TensorHandleArray
category: harmonyos-references
scraped_at: 2026-06-01T16:40:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:31edb857c1c1c6f23407f0419b69325ef87613c662cb9360d265229dfe2ada83
---
```
1. typedef struct OH_AI_TensorHandleArray {...} OH_AI_TensorHandleArray
```

## 概述

PhonePC/2in1TabletTVWearable

张量数组结构体，用于存储张量数组指针和张量数组长度。

**起始版本：** 9

**相关模块：** [MindSpore](../../模块/MindSpore/capi-mindspore.md)

**所在头文件：** [model.h](../../头文件/model.h/capi-model-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| size\_t handle\_num | 张量数组长度。 |
| [OH\_AI\_TensorHandle](../OH_AI_TensorHandle/capi-mindspore-oh-ai-tensorhandle.md)\* handle\_list | 指向张量数组的指针。 |
