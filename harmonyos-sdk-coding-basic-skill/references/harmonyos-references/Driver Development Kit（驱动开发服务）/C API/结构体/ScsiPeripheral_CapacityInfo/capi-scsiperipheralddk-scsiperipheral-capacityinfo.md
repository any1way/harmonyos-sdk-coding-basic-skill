---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-capacityinfo
title: ScsiPeripheral_CapacityInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > ScsiPeripheral_CapacityInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:23:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:06e23e1bdbf607ca6062cf1314bc64ca7f7b1ea7298a65696f149618d039a00d
---
```
1. typedef struct ScsiPeripheral_CapacityInfo {...} ScsiPeripheral_CapacityInfo
```

## 概述

PC/2in1

SCSI read capacity 数据。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](../../模块/ScsiPeripheralDDK/capi-scsiperipheralddk.md)

**所在头文件：** [scsi\_peripheral\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/scsi_peripheral_types.h/capi-scsi-peripheral-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t lbAddress | 返回的逻辑单元地址。 |
| uint32\_t lbLength | 单个逻辑单元长度，单位：字节。 |
