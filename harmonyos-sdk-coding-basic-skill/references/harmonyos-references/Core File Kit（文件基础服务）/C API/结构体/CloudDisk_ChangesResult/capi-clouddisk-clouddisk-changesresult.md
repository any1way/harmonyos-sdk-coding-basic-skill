---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-changesresult
title: CloudDisk_ChangesResult
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_ChangesResult
category: harmonyos-references
scraped_at: 2026-06-01T15:57:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eb2be8356c64e443ebd40d11e3c8c9b4db417ef418e14372932f51874b929495
---
```
1. typedef struct CloudDisk_ChangesResult {...} CloudDisk_ChangesResult
```

## 概述

PC/2in1Tablet

查询同步根路径中文件变更的结果。该结构体包含同步根路径中文件的变更数据，包括下一个更新序列号、结尾标志以及变更数据项数组。

**起始版本：** 21

**相关模块：** [CloudDisk](../../模块/CloudDisk/capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint64\_t nextUsn{0} | 下一次可查询的有效起始变更序列号。 |
| bool isEof{false} | 本次变更是否为同步根路径中记录的最后的修改记录。true：表示是最后的修改记录；false：表示不是最后的修改记录。 |
| size\_t bufferLength{0} | 历史变更记录数组中的元素数量。 |
| [CloudDisk\_ChangeData](../CloudDisk_ChangeData/capi-clouddisk-clouddisk-changedata.md) changeDatas[] | 历史变更记录数组。 |
