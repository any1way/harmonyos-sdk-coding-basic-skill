---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbrequestpipe
title: UsbRequestPipe
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbRequestPipe
category: harmonyos-references
scraped_at: 2026-06-11T16:23:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d182d0ad29fe9b574cb477bd755d7192da219922327375a9751218c99010aa49
---
```
1. typedef struct UsbRequestPipe {...} __attribute__((aligned(8))) UsbRequestPipe
```

## 概述

PC/2in1

请求管道。

**起始版本：** 10

**相关模块：** [UsbDdk](../../模块/UsbDdk/capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/usb_ddk_types.h/capi-usb-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint64\_t interfaceHandle | 接口操作句柄。 |
| uint8\_t endpoint | 要通信的端点的地址。 |
| uint32\_t timeout | 超时时间，单位是毫秒。 |
