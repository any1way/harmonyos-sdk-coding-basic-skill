---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-urlstyle
title: OH_ArkUI_UrlStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_UrlStyle
category: harmonyos-references
scraped_at: 2026-06-01T15:52:34+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:dc3554c2fd75723c19429fe580500860f160b8dd6fbd1d82a93a19dd29894e09
---
```
1. typedef struct OH_ArkUI_UrlStyle OH_ArkUI_UrlStyle
```

## 概述

PhonePC/2in1TabletTVWearable

定义超链接样式。

可以通过[OH\_ArkUI\_UrlStyle\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_urlstyle_create)接口创建对应的超链接样式对象。

可以通过[OH\_ArkUI\_UrlStyle\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_urlstyle_destroy)接口销毁超链接样式对象。

对象创建后通过[OH\_ArkUI\_UrlStyle\_SetUrl](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_urlstyle_seturl)接口设置链接地址。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
