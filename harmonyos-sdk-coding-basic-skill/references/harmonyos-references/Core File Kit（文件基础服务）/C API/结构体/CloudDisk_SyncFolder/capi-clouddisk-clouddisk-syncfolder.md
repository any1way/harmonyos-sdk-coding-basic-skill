---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-syncfolder
title: CloudDisk_SyncFolder
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_SyncFolder
category: harmonyos-references
scraped_at: 2026-06-01T15:57:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6c0fdea118d6e6f2939a826a8e0c8e027e5e5f909c736879af3dda7eb6820d5d
---
```
1. typedef struct CloudDisk_SyncFolder {...} CloudDisk_SyncFolder
```

## 概述

PC/2in1Tablet

同步根属性信息。

**起始版本：** 21

**相关模块：** [CloudDisk](../../模块/CloudDisk/capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| CloudDisk\_SyncFolderPath path | 同步根路径。 |
| [CloudDisk\_SyncFolderState](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md#clouddisk_syncfolderstate) state | 同步根路径状态。 |
| [CloudDisk\_DisplayNameInfo](../CloudDisk_DisplayNameInfo/capi-clouddisk-clouddisk-displaynameinfo.md) displayNameInfo | 同步根路径别名信息。 |
