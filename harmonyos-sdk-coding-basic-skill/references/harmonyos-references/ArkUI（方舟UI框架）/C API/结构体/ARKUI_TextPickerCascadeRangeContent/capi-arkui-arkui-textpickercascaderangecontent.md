---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textpickercascaderangecontent
title: ARKUI_TextPickerCascadeRangeContent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ARKUI_TextPickerCascadeRangeContent
category: harmonyos-references
scraped_at: 2026-06-11T15:56:44+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:a68fa80010b65ad53af2ee2bd123aaf034ceaff1a8cf36e2a38f7d5baaf9e5cc
---
```
1. typedef struct {...} ARKUI_TextPickerCascadeRangeContent
```

## 概述

PhonePC/2in1TabletTVWearable

定义多列联动滑动数据选择器的结构体。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](../../头文件/native_type.h/capi-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* text | 文本信息。 |
| const [ARKUI\_TextPickerRangeContent](../ARKUI_TextPickerRangeContent/capi-arkui-arkui-textpickerrangecontent.md)\* children | 联动数据。 |
| int32\_t size | 联动数据数组大小。 |
