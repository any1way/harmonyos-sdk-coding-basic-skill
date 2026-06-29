---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemrect
title: ArkUI_GridItemRect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_GridItemRect
category: harmonyos-references
scraped_at: 2026-06-01T15:53:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6a2547eb60ecb44d5f874d3561838125de25ca0b8df706615ed01130766e2177
---
```
1. typedef struct {...} ArkUI_GridItemRect
```

## 概述

PhonePC/2in1TabletTVWearable

定义Grid布局选项onGetRectByIndex回调返回值结构体。

**起始版本：** 22

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](../../头文件/native_type.h/capi-native-type-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t rowStart | GridItem行起始位置。 |
| uint32\_t columnStart | GridItem列起始位置。 |
| uint32\_t rowSpan | GridItem占用的行数。 |
| uint32\_t columnSpan | GridItem占用的列数。 |
