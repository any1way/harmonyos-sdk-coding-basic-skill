---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-touchevent
title: OH_NativeXComponent_TouchEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_TouchEvent
category: harmonyos-references
scraped_at: 2026-06-11T15:56:09+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:9c45b0b354d921ae350687cb3751cb565a8c9cc1405c0d529c1a67f7c37c9ad1
---
```
1. typedef struct {...} OH_NativeXComponent_TouchEvent
```

## 概述

PhonePC/2in1TabletTVWearable

触摸事件。

**起始版本：** 8

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
| int64\_t deviceId | 产生当前触摸事件的设备的ID。 |
| int64\_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| [OH\_NativeXComponent\_TouchPoint](../OH_NativeXComponent_TouchPoint/capi-nxcomp-touchpoint.md) touchPoints[OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER] | 当前触摸点的数组。OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER的介绍请参考[宏定义](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md#宏定义)。 |
| uint32\_t numPoints | 当前接触点的数量，值为1时为单指触摸，大于1时为多指触摸。 |
