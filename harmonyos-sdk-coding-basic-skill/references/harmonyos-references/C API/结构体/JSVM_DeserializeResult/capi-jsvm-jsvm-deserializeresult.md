---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deserializeresult
title: JSVM_DeserializeResult
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_DeserializeResult
category: harmonyos-references
scraped_at: 2026-06-11T16:53:33+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:f0d7822461524976f1d39d00616d6bd6f5eb7a43f425b24bc30a3c6834067623
---
```
1. typedef struct JSVM_DeserializeResult__* JSVM_DeserializeResult
```

## 概述

PhonePC/2in1TabletWearable

与JSVM\_COMPILE\_BACKGROUND\_DESERIALIZE\_RESULT一起传递的后台反序列化结果。

**使用场景：** 用于在JSVM后台编译场景中，传递和存储后台反序列化的结果数据。

**特点：** 轻量级的类型定义，与JSVM\_COMPILE\_BACKGROUND\_DESERIALIZE\_RESULT配合使用。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 24

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)
