---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-resultlist
title: CloudDisk_ResultList
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_ResultList
category: harmonyos-references
scraped_at: 2026-06-01T15:57:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ee3e597c09a4d9fb003f37f65af8dc2ccf4115f9c47dc5bcbe742f83704d34b3
---
```
1. typedef struct CloudDisk_ResultList {...} CloudDisk_ResultList
```

## 概述

PC/2in1Tablet

表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。

**起始版本：** 21

**相关模块：** [CloudDisk](../../模块/CloudDisk/capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](../CloudDisk_PathInfo/capi-clouddisk-clouddisk-pathinfo.md) pathInfo | 文件的绝对路径信息。 |
| bool isSuccess{false} | 表示操作是否成功。true：表示操作成功；false：表示操作失败。默认值为false。 |
| [CloudDisk\_SyncState](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md#clouddisk_syncstate) syncState | 文件的同步状态。当isSuccess为true时才生效。 |
| [CloudDisk\_ErrorReason](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md#clouddisk_errorreason) errorReason | 文件同步状态获取失败的原因。当isSuccess为false时才生效。 |
