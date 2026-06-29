---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-customspan
title: OH_ArkUI_CustomSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_CustomSpan
category: harmonyos-references
scraped_at: 2026-06-01T15:52:23+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:63819db521a3465c6e6f175443fff88cd59c9a301d7d188c27a720cdc064f116
---
```
1. typedef struct OH_ArkUI_CustomSpan OH_ArkUI_CustomSpan
```

## 概述

PhonePC/2in1TabletTVWearable

定义自定义绘制Span。

可以通过[OH\_ArkUI\_CustomSpan\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_customspan_create)接口创建对应的自定义绘制Span对象。

可以通过[OH\_ArkUI\_CustomSpan\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_customspan_destroy)接口销毁自定义绘制Span对象。

对象创建后通过[OH\_ArkUI\_CustomSpan\_RegisterOnMeasureCallback](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_customspan_registeronmeasurecallback)和[OH\_ArkUI\_CustomSpan\_RegisterOnDrawCallback](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_customspan_registerondrawcallback)接口注册绘制回调函数。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
