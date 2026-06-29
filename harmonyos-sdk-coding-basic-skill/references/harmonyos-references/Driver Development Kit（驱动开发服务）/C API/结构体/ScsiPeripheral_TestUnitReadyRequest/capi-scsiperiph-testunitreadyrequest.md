---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-testunitreadyrequest
title: ScsiPeripheral_TestUnitReadyRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_TestUnitReadyRequest
category: harmonyos-references
scraped_at: 2026-06-11T16:23:12+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:4f792e6056b2f67ec2177a6be6d01d38eca3b65b0c5b8d0d061476646d865272
---
```
1. typedef struct ScsiPeripheral_TestUnitReadyRequest {...} ScsiPeripheral_TestUnitReadyRequest
```

## 概述

PC/2in1

命令（test unit ready）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](../../模块/ScsiPeripheralDDK/capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/scsi_peripheral_types.h/capi-scsi-peripheral-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint32\_t timeout | 超时时间(单位: 毫秒)。 |
