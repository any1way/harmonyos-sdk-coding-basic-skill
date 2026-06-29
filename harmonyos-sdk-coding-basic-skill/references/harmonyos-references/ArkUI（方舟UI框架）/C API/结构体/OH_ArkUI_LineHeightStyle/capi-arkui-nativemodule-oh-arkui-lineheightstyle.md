---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-lineheightstyle
title: OH_ArkUI_LineHeightStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LineHeightStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:32+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:fb8518b8e49a34e1d5ce8393397554af6026f86c49f407029c712a4d07419a8f
---
```
1. typedef struct OH_ArkUI_LineHeightStyle OH_ArkUI_LineHeightStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义行高样式。

可以通过[OH\_ArkUI\_LineHeightStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_lineheightstyle_create)接口创建对应的行高样式对象。

可以通过[OH\_ArkUI\_LineHeightStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_lineheightstyle_destroy)接口销毁行高样式对象。

对象创建后通过[OH\_ArkUI\_LineHeightStyle\_SetLineHeight](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheight)接口设置具体的固定行高值。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
