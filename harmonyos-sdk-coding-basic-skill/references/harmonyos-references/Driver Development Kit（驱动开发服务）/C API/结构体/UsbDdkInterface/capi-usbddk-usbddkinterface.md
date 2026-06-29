---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterface
title: UsbDdkInterface
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkInterface
category: harmonyos-references
scraped_at: 2026-06-11T16:23:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:383af23755131659c5b67b2ddad8f5a5bfed3a3d6aa1f133b3fb2e3d47158597
---
```
1. typedef struct UsbDdkInterface {...} UsbDdkInterface
```

## 概述

PC/2in1

USB接口，是特定接口下备用设置的集合。

**起始版本：** 10

**相关模块：** [UsbDdk](../../模块/UsbDdk/capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/usb_ddk_types.h/capi-usb-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t numAltsetting | 接口的备用设置数量。 |
| [struct UsbDdkInterfaceDescriptor](../UsbDdkInterfaceDescriptor/capi-usbddk-usbddkinterfacedescriptor.md)\* altsetting | 接口的备用设置。 |
