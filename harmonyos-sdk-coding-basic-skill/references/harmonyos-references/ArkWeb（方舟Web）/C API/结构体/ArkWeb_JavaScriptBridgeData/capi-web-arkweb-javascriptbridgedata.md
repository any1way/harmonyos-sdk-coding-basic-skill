---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptbridgedata
title: ArkWeb_JavaScriptBridgeData
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptBridgeData
category: harmonyos-references
scraped_at: 2026-06-01T15:56:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fdda7e3529ee0e77cc5136c80ea33e30e7306fee3d5eaa0c301dd417adcf779f
---
```
1. typedef struct {...} ArkWeb_JavaScriptBridgeData
```

## 概述

PhonePC/2in1TabletTVWearable

定义JavaScript Bridge数据的基础结构。

**起始版本：** 12

**相关模块：** [Web](../../模块/Web/capi-web.md)

**所在头文件：** [arkweb\_type.h](../../头文件/arkweb_type.h/capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const uint8\_t\* buffer | 指向传输数据的指针。仅支持前端传入String和ArrayBuffer类型，其余类型会被json序列化后，以String类型传递。 |
| size\_t size | 传输数据的长度。 |
