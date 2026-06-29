---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-rawdevinfo
title: Hid_RawDevInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_RawDevInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:23:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb7a32b1ff6048a91c65ad46c8e2ea24abc2a3d14431fa117c118f5488bdca5d
---
```
1. typedef struct Hid_RawDevInfo {...} Hid_RawDevInfo
```

## 概述

PC/2in1

原始设备信息定义。

**起始版本：** 18

**相关模块：** [HidDdk](../../模块/HidDdk/capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/hid_ddk_types.h/capi-hid-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t busType | 总线类型 |
| uint16\_t vendor | 供应商ID |
| uint16\_t product | 产品ID |
