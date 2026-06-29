---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/siperipheralddk-scsiperipheral-readcapacityrequest
title: ScsiPeripheral_ReadCapacityRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_ReadCapacityRequest
category: harmonyos-references
scraped_at: 2026-06-01T16:13:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f86cb3c4b8b03af3b5c4add2d9b2527ddf740ce99943fc3c46d2b0a2ff504f87
---
```
1. typedef struct ScsiPeripheral_ReadCapacityRequest {...} ScsiPeripheral_ReadCapacityRequest
```

## 概述

PC/2in1

SCSI命令（read capacity）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](../../模块/ScsiPeripheralDDK/capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](../../头文件/scsi_peripheral_types.h/capi-scsi-peripheral-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 逻辑单元地址。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte8 | CDB的第八个字节。 |
| uint32\_t timeout | 超时时间（单位: 毫秒）。 |
