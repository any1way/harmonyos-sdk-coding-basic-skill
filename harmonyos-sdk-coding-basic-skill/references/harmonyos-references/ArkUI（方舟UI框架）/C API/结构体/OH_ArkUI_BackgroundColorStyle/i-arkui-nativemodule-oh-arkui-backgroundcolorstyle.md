---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-oh-arkui-backgroundcolorstyle
title: OH_ArkUI_BackgroundColorStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_BackgroundColorStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:35+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:1e1fb4d45866496cf3b0b1c3154d9ff1b0ad6e1e729cf722217bfa419dd0c273
---
```
1. typedef struct OH_ArkUI_BackgroundColorStyle OH_ArkUI_BackgroundColorStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义背景颜色样式。

可以通过[OH\_ArkUI\_BackgroundColorStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_create)接口创建对应的背景颜色样式对象。

可以通过[OH\_ArkUI\_BackgroundColorStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_destroy)接口销毁背景颜色样式对象。

对象创建后通过[OH\_ArkUI\_BackgroundColorStyle\_SetColor](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setcolor)和[OH\_ArkUI\_BackgroundColorStyle\_SetRadius](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setradius)接口设置背景颜色和圆角。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
