---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-extendederrorinfo
title: JSVM_ExtendedErrorInfo
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_ExtendedErrorInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:53:10+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:361fe703f0dc988d0f6a98ae08ddf01f715dc8bbb5ff512b26c18be9f36dba6a
---
```
1. typedef struct {...} JSVM_ExtendedErrorInfo
```

## 概述

PhonePC/2in1TabletWearable

扩展的异常信息。

**使用场景：** 在JSVM API调用失败时获取详细的异常信息，调试和排查JavaScript运行时错误，日志记录和错误上报。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| const char\* errorMessage | UTF-8编码的字符串，包含异常信息。 |
| void\* engineReserved | 特定于VM的详细异常信息。目前尚未为任何VM实现此功能。 |
| uint32\_t engineErrorCode | 特定于VM的异常代码。目前尚未为任何VM实现此功能。 |
| [JSVM\_Status](../../头文件/jsvm_types.h/capi-jsvm-types-h.md#jsvm_status) errorCode | 源自最后一个异常的JSVM-API状态码。 |
