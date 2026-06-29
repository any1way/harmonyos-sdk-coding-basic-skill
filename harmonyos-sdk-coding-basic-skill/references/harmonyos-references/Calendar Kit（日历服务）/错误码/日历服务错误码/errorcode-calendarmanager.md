---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-calendarmanager
title: 日历服务错误码
breadcrumb: API参考 > 应用服务 > Calendar Kit（日历服务） > 错误码 > 日历服务错误码
category: harmonyos-references
scraped_at: 2026-06-11T16:43:27+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:9a391d25a81322daf80051776a948e4ee95258791aeaaf6be11ea44975c935cc
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../通用错误码/errorcode-universal.md)。

## 23900001 参数值错误

PhonePC/2in1TabletTVWearable

**错误信息**

Parameter value error.

**错误描述**

参数值错误。

**可能原因**

1. 参数为字符串时，长度超范围。
2. 参数值超范围。

**处理步骤**

1. 检查参数字串长度是否超范围。
2. 检查参数值是否超范围。

## 23900003 未找到指定的账户

PhonePC/2in1TabletTVWearable

**错误信息**

The specified account was not found.

**错误描述**

未找到指定的账户。

**可能原因**

输入账号与创建的账户不一致，导致查询的账户不存在。

**处理步骤**

确保使用已创建的账户，不要使用未创建的账户。

## 23900004 内部程序错误

PhonePC/2in1TabletTVWearable

**错误信息**

Internal program error.

**错误描述**

内部程序错误。

**可能原因**

1. dataShare数据库执行错误。
2. 空指针错误。
3. 数据解析错误。

**处理步骤**

内部异常，请稍后重试。
