---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoreventcallback
title: Input_InterceptorEventCallback
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_InterceptorEventCallback
category: harmonyos-references
scraped_at: 2026-06-11T16:20:23+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:5e5779f4e78ecaf11c46bb13f2e05b1aceae25ce7be6200553da8ca3a9cdd9d6
---
```
1. typedef struct Input_InterceptorEventCallback {...} Input_InterceptorEventCallback
```

## 概述

PhonePC/2in1TabletTVWearable

拦截回调事件结构体，拦截鼠标事件、触屏输入事件和轴事件。

**起始版本：** 12

**相关模块：** [input](../../模块/input/capi-input.md)

**所在头文件：** [oh\_input\_manager.h](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| Input\_MouseEventCallback mouseCallback | 鼠标事件的回调函数。  **起始版本：** 12。 |
| Input\_TouchEventCallback touchCallback | 触屏输入事件的回调函数。  **起始版本：** 12。 |
| Input\_AxisEventCallback axisCallback | 轴事件的回调函数。  **起始版本：** 12。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)](capi-input-input-interceptoreventcallback.md#input_keyeventcallback) | Input\_KeyEventCallback() | 按键事件的回调函数，keyEvent的生命周期为回调函数内。  **起始版本：** 12。 |
| [typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)](capi-input-input-interceptoreventcallback.md#input_mouseeventcallback) | Input\_MouseEventCallback() | 鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。  **起始版本：** 12。 |
| [typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)](capi-input-input-interceptoreventcallback.md#input_toucheventcallback) | Input\_TouchEventCallback() | 触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。  **起始版本：** 12。 |
| [typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)](capi-input-input-interceptoreventcallback.md#input_axiseventcallback) | Input\_AxisEventCallback() | 轴事件的回调函数，axisEvent的生命周期为回调函数内。  **起始版本：** 12。 |
| [typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)](capi-input-input-interceptoreventcallback.md#input_deviceaddedcallback) | Input\_DeviceAddedCallback() | 回调函数，用于回调输入设备的热插事件。  **起始版本：** 13。 |
| [typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)](capi-input-input-interceptoreventcallback.md#input_deviceremovedcallback) | Input\_DeviceRemovedCallback() | 回调函数，用于回调输入设备的热拔事件。  **起始版本：** 13。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### Input\_KeyEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)
```

**描述**

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_KeyEvent](../Input_KeyEvent/capi-input-input-keyevent.md)\* keyEvent | 按键事件对象。 |

### Input\_MouseEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)
```

**描述**

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_MouseEvent](../Input_MouseEvent/capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象。 |

### Input\_TouchEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)
```

**描述**

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_TouchEvent](../Input_TouchEvent/capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象。 |

### Input\_AxisEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)
```

**描述**

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](../Input_AxisEvent/capi-input-input-axisevent.md)\* axisEvent | 轴事件对象。 |

### Input\_DeviceAddedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热插事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

### Input\_DeviceRemovedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热拔事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
