---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-device-info
title: deviceInfo错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > deviceInfo错误码
category: harmonyos-references
scraped_at: 2026-06-11T16:19:12+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:ee3c084ce370df9bd9a303706f15acddfec79162710c29522857220eecd7dc8e
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 14700103 操作权限被拒绝

PhonePC/2in1TabletTVWearable

**错误信息**

The operation on the system permission is denied.

**错误描述**

应用没有对应字段的权限时，系统会报此错误码。比如ohos.permission.sec.ACCESS\_UDID权限。

**可能原因**

应用没有配置需要的权限，比如ohos.permission.sec.ACCESS\_UDID。

**处理步骤**

添加相应的权限。
