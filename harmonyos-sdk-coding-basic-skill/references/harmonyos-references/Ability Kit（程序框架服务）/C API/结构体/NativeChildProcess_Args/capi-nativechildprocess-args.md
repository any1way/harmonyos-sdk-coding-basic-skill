---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-args
title: NativeChildProcess_Args
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_Args
category: harmonyos-references
scraped_at: 2026-06-01T15:32:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:815518dfa0e5e28612c489f97c750baaf75c339b064e03a7dcfe5616b19a20a7
---
```
1. typedef struct {...} NativeChildProcess_Args
```

## 概述

PhonePC/2in1TabletTVWearable

传递给子进程的参数。

**起始版本：** 13

**相关模块：** [ChildProcess](../../模块/ChildProcess/capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](../../头文件/native_child_process.h/capi-native-child-process-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* entryParams | 入口参数，大小不能超过150KB。 |
| struct [NativeChildProcess\_FdList](../NativeChildProcess_FdList/capi-nativechildprocess-fdlist.md) fdList | 传递给子进程的文件描述符信息列表。 |
