---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-imageattachment
title: OH_ArkUI_ImageAttachment
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_ImageAttachment
category: harmonyos-references
scraped_at: 2026-06-01T15:52:22+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9f3ef2149a47af326a19dc4702437c2630b4eb590a736d77c028cf99d0a2e324
---
```
1. typedef struct OH_ArkUI_ImageAttachment OH_ArkUI_ImageAttachment
```

## 概述

PhonePC/2in1TabletTVWearable

定义图片样式对象。

可以通过[OH\_ArkUI\_ImageAttachment\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_imageattachment_create)接口创建对应的图片样式对象。

可以通过[OH\_ArkUI\_ImageAttachment\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_imageattachment_destroy)接口销毁图片样式对象。

对象创建后通过OH\_ArkUI\_ImageAttachment\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_ImageAttachment\_SetPixelMap](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_imageattachment_setpixelmap)设置图片源。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
