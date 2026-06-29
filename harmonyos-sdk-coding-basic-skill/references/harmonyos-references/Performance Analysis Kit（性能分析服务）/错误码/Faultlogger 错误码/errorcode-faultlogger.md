---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-faultlogger
title: Faultlogger 错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > Faultlogger 错误码
category: harmonyos-references
scraped_at: 2026-06-11T16:25:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fde77a13b1c991f17812ef0296df05673378a7dd92fb77b55227914e57376f7e
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../通用错误码/errorcode-universal.md)。

## 10600001 服务未启动或故障

PhonePC/2in1TabletTVWearable

**错误信息**

The service is not started or is faulty.

**错误描述**

服务未启动或者遇到未知错误。

**可能原因**

hiview服务未启动。

**处理步骤**

不应该发生的场景，考虑重试。
