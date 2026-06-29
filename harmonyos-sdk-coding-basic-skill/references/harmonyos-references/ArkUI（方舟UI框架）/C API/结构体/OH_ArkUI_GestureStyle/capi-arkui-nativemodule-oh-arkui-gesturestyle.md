---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-gesturestyle
title: OH_ArkUI_GestureStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_GestureStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:28+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:945587e90794419194902ddf8d60fa406e734beba436f1c1ef8e5b058aef887b
---
```
1. typedef struct OH_ArkUI_GestureStyle OH_ArkUI_GestureStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义事件手势样式。

可以通过[OH\_ArkUI\_GestureStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_gesturestyle_create)接口创建对应的事件手势样式对象。

可以通过[OH\_ArkUI\_GestureStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_gesturestyle_destroy)接口销毁事件手势样式对象。

对象创建后通过OH\_ArkUI\_GestureStyle\_RegisterOnXXXCallback系列接口注册具体的事件回调，例如通过[OH\_ArkUI\_GestureStyle\_RegisterOnClickCallback](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_gesturestyle_registeronclickcallback)注册点击事件回调。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
