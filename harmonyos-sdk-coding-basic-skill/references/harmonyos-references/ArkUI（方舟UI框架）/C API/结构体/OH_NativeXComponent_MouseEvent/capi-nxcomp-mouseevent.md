---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent
title: OH_NativeXComponent_MouseEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_MouseEvent
category: harmonyos-references
scraped_at: 2026-06-11T15:56:10+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:533589012ade6c04f15729a45736658fbc9d2e6183bc21215aa9ba2bfcc4d1cb
---
```
1. typedef struct {...} OH_NativeXComponent_MouseEvent
```

## 概述

PhonePC/2in1TabletTVWearable

鼠标事件。

**起始版本：** 9

**相关模块：** [OH\_NativeXComponent Native XComponent](<../../模块/OH_NativeXComponent Native XComponent/capi-oh-nativexcomponent-native-xcomponent.md>)

**所在头文件：** [native\_interface\_xcomponent.h](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| float x | 点击触点相对于当前组件左上角的x轴坐标。单位：vp。 |
| float y | 点击触点相对于当前组件左上角的y轴坐标。单位：vp。 |
| float screenX | 点击触点相对于XComponent所在应用屏幕左上角的x轴坐标。单位：vp。 |
| float screenY | 点击触点相对于XComponent所在应用屏幕左上角的y轴坐标。单位：vp。 |
| int64\_t timestamp | 当前鼠标事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| [OH\_NativeXComponent\_MouseEventAction](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventaction) action | 当前鼠标事件动作。 |
| [OH\_NativeXComponent\_MouseEventButton](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventbutton) button | 鼠标事件按键。 |
