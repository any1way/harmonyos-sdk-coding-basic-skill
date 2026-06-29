---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-params
title: UsbSerial_Params
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbSerial_Params
category: harmonyos-references
scraped_at: 2026-06-11T16:23:33+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:f165028ea850b5efa57271fae3e539d0901288f121f508dfc5aa0011c40c2f25
---
```
1. typedef struct UsbSerial_Params {...} __attribute__((aligned(8))) UsbSerial_Params
```

## 概述

PC/2in1

定义USB Serial DDK使用的USB串口参数。

**起始版本：** 18

**相关模块：** [USBSerialDDK](../../模块/USBSerialDDK/capi-serialddk.md)

**所在头文件：** [usb\_serial\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/usb_serial_types.h/capi-usb-serial-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t baudRate | 波特率，单位为波特。 |
| uint8\_t nDataBits | 数据位比特数。 |
| uint8\_t nStopBits | 停止位比特数。 |
| uint8\_t parity | 校验参数设置（0：无校验；1：奇校验；2：偶校验；）。 |
