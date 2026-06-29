---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-transienttaskinfo
title: TransientTask_TransientTaskInfo
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > C API > 结构体 > TransientTask_TransientTaskInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:56:42+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:b0e8697fae1e3cab14af37c931891bd15afe92e978b2428d6fea51b3cd6289e4
---
```
1. typedef struct TransientTask_TransientTaskInfo {...} TransientTask_TransientTaskInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义所有短时任务信息结构体。用于返回当日剩余总配额和已申请的所有短时任务信息。

**起始版本：** 20

**相关模块：** [TransientTask](../../模块/TransientTask/capi-transienttask.md)

**所在头文件：** [transient\_task\_type.h](../../头文件/transient_task_type.h/capi-transient-task-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t remainingQuota | 当日剩余总配额。单位：毫秒。 |
| [TransientTask\_DelaySuspendInfo](../TransientTask_DelaySuspendInfo/capi-transienttask-transienttask-delaysuspendinfo.md) transientTasks[[TRANSIENT\_TASK\_MAX\_NUM](../../头文件/transient_task_type.h/capi-transient-task-type-h.md#宏定义)] | 已申请的所有短时任务信息。包括短时任务请求ID、剩余时间（单位：毫秒）。 |
