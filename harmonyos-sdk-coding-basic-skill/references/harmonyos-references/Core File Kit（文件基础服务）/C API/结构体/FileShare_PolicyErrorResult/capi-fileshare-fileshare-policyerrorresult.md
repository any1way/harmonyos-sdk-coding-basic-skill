---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyerrorresult
title: FileShare_PolicyErrorResult
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > FileShare_PolicyErrorResult
category: harmonyos-references
scraped_at: 2026-06-01T15:57:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ea75fa6b749a256aec9b839a88ebdc9597db925569b3ed1581ef6458258f8c5
---
```
1. typedef struct FileShare_PolicyErrorResult {...} FileShare_PolicyErrorResult
```

## 概述

PhonePC/2in1Tablet

授予或使能权限失败的URI策略结果。

**起始版本：** 12

**相关模块：** [fileShare](../../模块/fileShare/capi-fileshare.md)

**所在头文件：** [oh\_file\_share.h](../../头文件/oh_file_share.h/capi-oh-file-share-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char \*uri | 授予或使能策略失败的URI。 |
| [FileShare\_PolicyErrorCode](../../头文件/oh_file_share.h/capi-oh-file-share-h.md#fileshare_policyerrorcode) code | 授予或使能策略失败的URI对应的错误码。 |
| char \*message | 授予或使能策略失败的URI对应的原因。 |
