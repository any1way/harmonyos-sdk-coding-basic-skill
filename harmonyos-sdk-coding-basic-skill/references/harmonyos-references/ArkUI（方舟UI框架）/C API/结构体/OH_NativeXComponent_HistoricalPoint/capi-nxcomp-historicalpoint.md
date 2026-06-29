---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-historicalpoint
title: OH_NativeXComponent_HistoricalPoint
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_HistoricalPoint
category: harmonyos-references
scraped_at: 2026-06-11T15:56:07+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:0a23fb3faae02eb6276116c4f17716c6fc7e2367d5bcdffc09cb31a58fc7cf73
---
```
1. typedef struct {...} OH_NativeXComponent_HistoricalPoint
```

## 概述

PhonePC/2in1TabletTVWearable

历史接触点

**起始版本：** 10

**相关模块：** [OH\_NativeXComponent Native XComponent](<../../模块/OH_NativeXComponent Native XComponent/capi-oh-nativexcomponent-native-xcomponent.md>)

**所在头文件：** [native\_interface\_xcomponent.h](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t id | 手指的唯一标识符。 |
| float screenX | 触摸点相对于XComponent所在应用窗口左上角的x坐标。 |
| float screenY | 触摸点相对于XComponent所在应用窗口左上角的y坐标。 |
| float x | 触摸点相对于XComponent组件左边缘的x坐标。 |
| float y | 触摸点相对于XComponent组件上边缘的y坐标。 |
| [OH\_NativeXComponent\_TouchEventType](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_toucheventtype) type | 触摸事件的触摸类型。 |
| double size | 指垫和屏幕之间的接触面积。 |
| float force | 当前触摸事件的压力。 |
| int64\_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| float titlX | 平面X-Y上的投影与当前触摸事件的Z轴之间的角度。 |
| float titlY | 当前触摸事件在平面Y-Z和轴Z上的投影之间的角度。 |
| [OH\_NativeXComponent\_TouchEvent\_SourceTool](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_touchevent_sourcetool) sourceTool | 当前触摸事件的源工具。 |
