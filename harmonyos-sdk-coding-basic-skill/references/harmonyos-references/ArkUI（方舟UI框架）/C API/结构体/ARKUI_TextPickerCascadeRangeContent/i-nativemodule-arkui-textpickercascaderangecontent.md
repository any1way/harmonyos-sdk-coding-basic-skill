---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-nativemodule-arkui-textpickercascaderangecontent
title: ARKUI_TextPickerCascadeRangeContent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ARKUI_TextPickerCascadeRangeContent
category: harmonyos-references
scraped_at: 2026-06-01T15:51:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1c4f817c6526bfdf326544e2d420006fd6d8e9e6ff454d18d1f633983f50871f
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
| const [ARKUI\_TextPickerRangeContent](../ARKUI_TextPickerRangeContent/pi-arkui-nativemodule-arkui-textpickerrangecontent.md)\* children | 联动数据。 |
| int32\_t size | 联动数据数组大小。 |
