---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-nativemodule-oh-arkui-leadingmarginspandrawinfo
title: OH_ArkUI_LeadingMarginSpanDrawInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LeadingMarginSpanDrawInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:52:37+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:f414f3aed5c41f5dae2591f6af50b25a224bd2375dcd877bfc9298b469cf34d9
---
```
1. typedef struct OH_ArkUI_LeadingMarginSpanDrawInfo OH_ArkUI_LeadingMarginSpanDrawInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义段落缩进的自定义绘制信息。

可以通过[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_create)接口创建对应的段落缩进的自定义绘制信息对象。

可以通过[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_destroy)接口销毁段落缩进的自定义绘制信息对象。

对象用于在[OH\_ArkUI\_ParagraphStyle\_RegisterOnDrawLeadingMarginCallback](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_paragraphstyle_registerondrawleadingmargincallback)注册的回调函数中，提供当前行的绘制上下文信息。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
