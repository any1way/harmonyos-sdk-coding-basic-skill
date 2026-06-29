---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textstyle
title: OH_ArkUI_TextStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:25+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9201c66986c43d93e7393fb5145863e43e9bf9cd32279c25b625d0e6e0d3c6a7
---
```
1. typedef struct OH_ArkUI_TextStyle OH_ArkUI_TextStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义文本字体样式。

可以通过[OH\_ArkUI\_TextStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textstyle_create)接口创建对应的文本字体样式对象。

可以通过[OH\_ArkUI\_TextStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textstyle_destroy)接口销毁文本字体样式对象。

对象创建后通过OH\_ArkUI\_TextStyle\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_TextStyle\_SetFontColor](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textstyle_setfontcolor)设置字体颜色。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
