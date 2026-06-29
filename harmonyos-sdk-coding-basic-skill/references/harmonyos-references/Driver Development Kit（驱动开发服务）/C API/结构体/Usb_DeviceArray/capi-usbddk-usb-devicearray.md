---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usb-devicearray
title: Usb_DeviceArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Usb_DeviceArray
category: harmonyos-references
scraped_at: 2026-06-11T16:23:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c64d5c2909dfbdc42285d1149c80a8c9f4e3ad009a08d5f198e4c7c61659b863
---
```
1. typedef struct Usb_DeviceArray {...} Usb_DeviceArray
```

## 概述

PC/2in1

设备ID清单，用于存放[OH\_Usb\_GetDevices](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/usb_ddk_api.h/capi-usb-ddk-api-h.md#oh_usb_getdevices>)接口获取到的设备ID列表和设备数量。

**起始版本：** 18

**相关模块：** [UsbDdk](../../模块/UsbDdk/capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/usb_ddk_types.h/capi-usb-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint64\_t\* deviceIds | 开发者申请好的设备ID数组首地址，申请的数组大小建议一般不超过128，以避免过度占用内存。 |
| uint32\_t num | 实际返回的设备数量，根据数量遍历deviceIds获得设备ID。当该值为0时，表示不存在USB设备。 |
