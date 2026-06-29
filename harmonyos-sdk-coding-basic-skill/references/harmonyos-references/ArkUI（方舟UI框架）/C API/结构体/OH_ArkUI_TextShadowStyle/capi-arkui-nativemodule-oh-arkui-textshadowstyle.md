---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textshadowstyle
title: OH_ArkUI_TextShadowStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextShadowStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:28+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:60faa457c7c65089e0649d90d53d1ef3aaa65d9e83cad2e177bfc56495332ea8
---
```
1. typedef struct OH_ArkUI_TextShadowStyle OH_ArkUI_TextShadowStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义文本阴影样式。

可以通过[OH\_ArkUI\_TextShadowStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textshadowstyle_create)接口创建对应的文本阴影样式对象。

可以通过[OH\_ArkUI\_TextShadowStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textshadowstyle_destroy)接口销毁文本阴影样式对象。

对象创建后通过[OH\_ArkUI\_TextShadowStyle\_SetTextShadow](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textshadowstyle_settextshadow)接口设置生效的具体样式。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
