---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-displaynameinfo
title: CloudDisk_DisplayNameInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_DisplayNameInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:57:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ba5ce90e0beea031a36cf74785df970d8720db5ac437e61fc92db690f7b1bb0d
---
```
1. typedef struct CloudDisk_DisplayNameInfo {...} CloudDisk_DisplayNameInfo
```

## 概述

PC/2in1Tablet

定义同步根路径的显示名称信息。

**起始版本：** 21

**相关模块：** [CloudDisk](../../模块/CloudDisk/capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](../../头文件/oh_cloud_disk_manager.h/capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t displayNameResId | 应用同步根路径显示名称对应的静态资源ID。 |
| char \*customAlias | 自定义的别名，不能包含字符：\/\*?<>|:"，以及不能以"."、".."和纯空格作为完整名称。 |
| size\_t customAliasLength | 自定义别名的长度，范围：[0, 255]。 |
