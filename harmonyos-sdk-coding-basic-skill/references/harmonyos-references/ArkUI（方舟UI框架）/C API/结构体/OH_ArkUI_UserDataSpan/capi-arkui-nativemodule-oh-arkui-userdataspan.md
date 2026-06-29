---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-userdataspan
title: OH_ArkUI_UserDataSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_UserDataSpan
category: harmonyos-references
scraped_at: 2026-06-01T15:52:37+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:f72b77905c927377666ee3a42605c6b52c02a7074934159002cef5307e2d2731
---
```
1. typedef struct OH_ArkUI_UserDataSpan OH_ArkUI_UserDataSpan
```

## 概述

PhonePC/2in1TabletTVWearable

定义用户数据Span样式。

可以通过[OH\_ArkUI\_UserDataSpan\_Create](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_userdataspan_create)接口创建对应的用户数据Span样式对象。

可以通过[OH\_ArkUI\_UserDataSpan\_Destroy](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_userdataspan_destroy)接口销毁用户数据Span样式对象。

对象创建后通过[OH\_ArkUI\_UserDataSpan\_SetUserData](../../头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_userdataspan_setuserdata)接口绑定用户数据。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md)
