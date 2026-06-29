---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewucreatesessionresult
title: OH_QoS_GewuCreateSessionResult
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 结构体 > OH_QoS_GewuCreateSessionResult
category: harmonyos-references
scraped_at: 2026-06-11T16:22:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fccff196e551030e6906b60cb381dd99255a0820dc6c999ebd3449dd283b33ea
---
```
1. typedef struct { ... } OH_QoS_GewuCreateSessionResult
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_QoS\_GewuCreateSession()接口的返回结果，成功时返回创建的 session，失败时 error 会置为对应的错误码 。

**起始版本：** 20

**相关模块：** [QoS](../../模块/QoS/capi-qos.md)

**所在头文件：** [qos.h](../../头文件/qos.h/capi-qos-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](../../头文件/qos.h/capi-qos-h.md#变量) session | 创建出来的会话句柄 |
| [OH\_QoS\_GewuErrorCode](../../头文件/qos.h/capi-qos-h.md#oh_qos_gewuerrorcode) error | 错误码- 创建会话成功返回OH\_QOS\_GEWU\_OK。- 由于没有足够的内存而创建会话失败返回OH\_QOS\_GEWU\_NOMEM。 |
