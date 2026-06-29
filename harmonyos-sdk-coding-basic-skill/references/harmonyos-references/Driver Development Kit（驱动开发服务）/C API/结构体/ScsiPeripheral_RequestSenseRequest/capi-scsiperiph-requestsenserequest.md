---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-requestsenserequest
title: ScsiPeripheral_RequestSenseRequest
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_RequestSenseRequest
category: harmonyos-references
scraped_at: 2026-06-11T16:23:16+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:8f520f797156d63325672ec5cd2764fa35bec7451937c1e7b3ec297d39e4a87c
---
```
1. typedef struct ScsiPeripheral_RequestSenseRequest {...} ScsiPeripheral_RequestSenseRequest
```

## 概述

PC/2in1

SCSI命令（Request Sense）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](../../模块/ScsiPeripheralDDK/capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/scsi_peripheral_types.h/capi-scsi-peripheral-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t allocationLength | Allocation length字段，指定了请求方向发起者（通常是主机）为响应数据准备的缓冲区大小。 |
| uint8\_t control | Control字段，用于指定一些控制信息。 |
| uint8\_t byte1 | CDB的第一个字节。 |
| uint32\_t timeout | 超时时间(单位: 毫秒)。 |
