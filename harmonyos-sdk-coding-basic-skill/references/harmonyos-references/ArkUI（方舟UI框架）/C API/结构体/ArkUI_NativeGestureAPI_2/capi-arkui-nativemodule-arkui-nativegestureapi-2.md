---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2
title: ArkUI_NativeGestureAPI_2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeGestureAPI_2
category: harmonyos-references
scraped_at: 2026-06-01T15:50:28+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:b8d21fa38c58e4b7794d3ef9a438b3b78badcd843d37064fe6ac11717fb65450
---
```
1. typedef struct {...} ArkUI_NativeGestureAPI_2
```

## 概述

PhonePC/2in1TabletTVWearable

定义手势模块接口集合。

**起始版本：** 18

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](../../头文件/native_gesture.h/capi-native-gesture-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NativeGestureAPI\_1](../ArkUI_NativeGestureAPI_1/capi-arkui-nativemodule-arkui-nativegestureapi-1.md)\* gestureApi1 | 指向ArkUI\_NativeGestureAPI\_1结构体的指针。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, void\* userData,ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))](capi-arkui-nativemodule-arkui-nativegestureapi-2.md#setgestureinterruptertonode) | 设置手势打断事件的回调函数。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### setGestureInterrupterToNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

**描述：**

设置手势打断事件的回调函数。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](../ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md) node | 需要被设置手势打断回调的ArkUI节点指针。 |
| void\* userData | 用户自定义数据。 |
| [ArkUI\_GestureInterruptResult](../../头文件/native_gesture.h/capi-native-gesture-h.md#arkui_gestureinterruptresult) (\*interrupter)([ArkUI\_GestureInterruptInfo](../ArkUI_GestureInterruptInfo/capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* info) | 打断回调，info返回手势打断数据。interrupter返回GESTURE\_INTERRUPT\_RESULT\_CONTINUE，手势正常进行；返回GESTURE\_INTERRUPT\_RESULT\_REJECT，手势打断。设置此参数为nullptr时将取消注册回调函数。  **说明：** 该事件打断回调注册后，后续在单次手势处理流程中都会存在。即使在单次事件处理流程中使用setGestureInterrupterToNode接口将手势打断回调重置为undefined，或者使用[dispose](../ArkUI_NativeGestureAPI_1/capi-arkui-nativemodule-arkui-nativegestureapi-1.md#dispose)接口使即将被触发的手势销毁，该回调在满足触发条件后仍会响应。如果在该回调中使用到的对象，在回调触发前已被释放，需要对该对象进行保护。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../头文件/native_type.h/capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../头文件/native_type.h/capi-native-type-h.md#arkui_errorcode) 参数错误。 |
