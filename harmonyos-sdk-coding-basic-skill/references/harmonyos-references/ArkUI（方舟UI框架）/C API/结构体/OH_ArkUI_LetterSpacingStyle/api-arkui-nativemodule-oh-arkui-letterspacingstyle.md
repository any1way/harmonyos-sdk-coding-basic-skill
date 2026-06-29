---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-oh-arkui-letterspacingstyle
title: OH_ArkUI_LetterSpacingStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LetterSpacingStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:32+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:291aaa1be9efacae79b4c9308aeb072cbe28e67a1645760e7c029446156c6c58
---
```
1. typedef struct OH_ArkUI_LetterSpacingStyle OH_ArkUI_LetterSpacingStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义字符间距样式。

可以通过[OH\_ArkUI\_LetterSpacingStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_letterspacingstyle_create)接口创建对应的字符间距样式对象。

可以通过[OH\_ArkUI\_LetterSpacingStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_letterspacingstyle_destroy)接口销毁字符间距样式对象。

对象创建后通过[OH\_ArkUI\_LetterSpacingStyle\_SetLetterSpacing](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_letterspacingstyle_setletterspacing)接口设置具体的字符间距值。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
