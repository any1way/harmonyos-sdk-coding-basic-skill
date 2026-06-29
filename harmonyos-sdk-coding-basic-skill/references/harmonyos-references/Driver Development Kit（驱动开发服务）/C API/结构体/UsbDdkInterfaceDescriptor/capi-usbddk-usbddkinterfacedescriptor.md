---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterfacedescriptor
title: UsbDdkInterfaceDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkInterfaceDescriptor
category: harmonyos-references
scraped_at: 2026-06-11T16:23:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a7fe41356db7232b36fcdab3a9b0f5f01729bdeeb2c8cc1e65761d8c080f6b7c
---
```
1. typedef struct UsbDdkInterfaceDescriptor {...} UsbDdkInterfaceDescriptor
```

## 概述

PC/2in1

接口描述符。

**起始版本：** 10

**相关模块：** [UsbDdk](../../模块/UsbDdk/capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/usb_ddk_types.h/capi-usb-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [struct UsbInterfaceDescriptor](../UsbInterfaceDescriptor/capi-usbddk-usbinterfacedescriptor.md) interfaceDescriptor | 标准接口描述符。 |
| [struct UsbDdkEndpointDescriptor](../UsbDdkEndpointDescriptor/capi-usbddk-usbddkendpointdescriptor.md)\* endPoint | 该接口所包含的端点描述符。 |
| const uint8\_t\* extra | 未做解析的描述符，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |
