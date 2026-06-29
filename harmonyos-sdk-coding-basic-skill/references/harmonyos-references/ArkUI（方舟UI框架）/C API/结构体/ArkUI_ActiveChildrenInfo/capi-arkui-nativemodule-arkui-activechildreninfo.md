---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo
title: ArkUI_ActiveChildrenInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ActiveChildrenInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:51:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:061df2361229b061b158170e4668454ec9be835399288410ab4424ceb67b7864
---
```
1. typedef struct ArkUI_ActiveChildrenInfo ArkUI_ActiveChildrenInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义ActiveChildrenInfo类信息。

**起始版本：** 14

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](../../头文件/native_type.h/capi-native-type-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo](../../头文件/native_node.h/capi-native-node-h.md#oh_arkui_nodeutils_getactivechildreninfo) | 获取某个节点所有活跃的子节点。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_activechildreninfo_getnodebyindex) | 获取ActiveChildrenInfo结构体的下标为index的子节点。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_GetCount](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_activechildreninfo_getcount) | 获取ActiveChildrenInfo结构体内的节点数量。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_Destroy](../../头文件/native_type.h/capi-native-type-h.md#oh_arkui_activechildreninfo_destroy) | 销毁ActiveChildrenInfo实例。 |
