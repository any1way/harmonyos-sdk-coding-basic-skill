---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-decorationstyle
title: OH_ArkUI_DecorationStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_DecorationStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:30+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a4ec08f5194fc505a3c6c0e26223963acdc1099fe9b78fd9e2267f8949d5a65f
---
```
1. typedef struct OH_ArkUI_DecorationStyle OH_ArkUI_DecorationStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义文本装饰线样式。

可以通过[OH\_ArkUI\_DecorationStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_decorationstyle_create)接口创建对应的文本装饰线样式对象。

可以通过[OH\_ArkUI\_DecorationStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_decorationstyle_destroy)接口销毁文本装饰线样式对象。

对象创建后通过OH\_ArkUI\_DecorationStyle\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_DecorationStyle\_SetTextDecorationType](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_decorationstyle_settextdecorationtype)设置装饰线类型。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
