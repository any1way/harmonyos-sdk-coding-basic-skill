---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-fontconfigs
title: OH_ArkUI_FontConfigs
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_FontConfigs
category: harmonyos-references
scraped_at: 2026-06-01T15:50:04+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c2466be0f6ee7a954d4ac493cba505e59233d64547cad824cb2078bfdc646bf5
---
```
1. typedef struct OH_ArkUI_FontConfigs OH_ArkUI_FontConfigs
```

## 概述

PhonePC/2in1TabletTVWearable

定义文本的字体配置。可以通过[OH\_ArkUI\_FontConfigs\_Create](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_fontconfigs_create) 接口创建文本字体配置对象。可以通过[OH\_ArkUI\_FontConfigs\_Destroy](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_fontconfigs_destroy) 接口销毁文本字体配置对象。配置创建后通过[OH\_ArkUI\_FontConfigs\_SetFontWeightConfigs](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_fontconfigs_setfontweightconfigs) 接口设置文本的字体粗细配置。配置创建后通过[OH\_ArkUI\_FontConfigs\_GetFontWeightConfigs](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_fontconfigs_getfontweightconfigs) 接口查看文本的字体粗细配置。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](../../头文件/native_type.h/capi-native-type-h.md)
