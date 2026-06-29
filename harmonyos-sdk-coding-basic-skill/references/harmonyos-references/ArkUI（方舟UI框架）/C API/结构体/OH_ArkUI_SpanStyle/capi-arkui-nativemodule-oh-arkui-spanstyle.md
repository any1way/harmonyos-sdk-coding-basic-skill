---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-spanstyle
title: OH_ArkUI_SpanStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_SpanStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:21+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:e1dbf291cb6e536be289d6aac0372663d48c580e5340821a512d95d051ab1e8e
---
```
1. typedef struct OH_ArkUI_SpanStyle OH_ArkUI_SpanStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义属性字符串样式对象。

可以通过[OH\_ArkUI\_SpanStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_spanstyle_create)接口创建对应的属性字符串样式对象。

可以通过[OH\_ArkUI\_SpanStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_spanstyle_destroy)接口销毁属性字符串样式对象。

对象创建后通过[OH\_ArkUI\_SpanStyle\_SetStart](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_spanstyle_setstart)和[OH\_ArkUI\_SpanStyle\_SetLength](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_spanstyle_setlength)指定样式作用的范围。

对象创建后通过OH\_ArkUI\_SpanStyle\_SetXXXStyle系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_SpanStyle\_SetTextStyle](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_spanstyle_settextstyle)设置字体样式效果。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
