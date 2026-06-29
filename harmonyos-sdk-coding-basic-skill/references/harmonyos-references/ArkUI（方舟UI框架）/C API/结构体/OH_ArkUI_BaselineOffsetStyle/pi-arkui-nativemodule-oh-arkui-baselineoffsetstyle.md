---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-oh-arkui-baselineoffsetstyle
title: OH_ArkUI_BaselineOffsetStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_BaselineOffsetStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:30+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c16a4ebc14a2de172c5f903badec284ed8b0811e30b523b132130f386c766248
---
```
1. typedef struct OH_ArkUI_BaselineOffsetStyle OH_ArkUI_BaselineOffsetStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义基线偏移量样式。

可以通过[OH\_ArkUI\_BaselineOffsetStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_create)接口创建对应的基线偏移量样式对象。

可以通过[OH\_ArkUI\_BaselineOffsetStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_destroy)接口销毁基线偏移量样式对象。

对象创建后通过[OH\_ArkUI\_BaselineOffsetStyle\_SetBaselineOffset](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_setbaselineoffset)接口设置具体的基线偏移量值。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
