---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-coastingaxisevent
title: ArkUI_CoastingAxisEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_CoastingAxisEvent
category: harmonyos-references
scraped_at: 2026-06-01T15:53:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1661553059f609ae801975235da8d0e7fdea4f2d9e9eafa5b1b361e3b4145861
---
```
1. typedef struct ArkUI_CoastingAxisEvent ArkUI_CoastingAxisEvent
```

## 概述

PhonePC/2in1TabletTVWearable

定义惯性滚动轴事件。

当用户在触控板上用双指滑动时，系统会根据手指抬起时的速度，按照一定的衰减曲线构造滑动事件。可以监听此类事件，以便在常规轴事件之后立即处理抛滑效果。

仅当用户在触控板上双指抛滑，且指针位置下存在通过[registerNodeEvent](../ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册了[NODE\_ON\_COASTING\_AXIS\_EVENT](../../头文件/native_node.h/capi-native-node-h.md#arkui_nodeeventtype)事件的组件时，才能接收到此事件。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](../../模块/ArkUI_EventModule/capi-arkui-eventmodule.md)

**所在头文件：** [ui\_input\_event.h](../../头文件/ui_input_event.h/capi-ui-input-event-h.md)
