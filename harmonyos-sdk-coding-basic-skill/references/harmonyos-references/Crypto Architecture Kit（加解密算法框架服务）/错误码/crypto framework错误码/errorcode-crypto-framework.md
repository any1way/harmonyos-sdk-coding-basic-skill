---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-crypto-framework
title: crypto framework错误码
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 错误码 > crypto framework错误码
category: harmonyos-references
scraped_at: 2026-06-01T16:02:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2f674905b0b3e4935a8193d6c5ca67ce546785d94ca1f05ecdc88e2850431793
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 17620001 内存操作失败

PhonePC/2in1TabletTVWearableLite Wearable

**错误信息**

Memory operation failed.

**错误描述**

内存操作失败。

**可能原因**

当前系统内存分配失败。

**处理步骤**

1. 检查当前系统功能是否正常。
2. 业务检查数据是否超长，导致系统无法分配内存。

## 17620002 ArkTS和C之间转换参数失败

PhonePC/2in1TabletTVWearableLite Wearable

**错误信息**

Failed to convert parameters between arkts and c.

**错误描述**

ArkTS和C之间转换参数失败。

**可能原因**

系统出现的不可预期的错误。

**处理步骤**

检查当前系统功能是否正常。

## 17620003 参数校验失败

PhonePC/2in1TabletTVWearable

**错误信息**

Parameter check failed.

**错误描述**

参数校验失败。

**可能原因**

输入的参数超出了规格范围，如长度、值等。

**处理步骤**

检查当前输入的参数是否在支持的范围内。

## 17630001 算法相关的操作错误，调用三方算法库API出错

PhonePC/2in1TabletTVWearableLite Wearable

**错误信息**

Crypto operation error.

**错误描述**

调用三方算法库API出错。

**可能原因**

加解密算法框架与三方算法库交互时，出现错误。

**处理步骤**

检查该接口或相关联接口输入参数的正确性。

AES解密失败可参考[AES解密失败返回错误码17630001](<../../../../../harmonyos-guides/系统/安全/Crypto Architecture Kit（加解密算法框架服务）/Crypto Architecture Kit常见问题/AES解密失败返回错误码17630001/crypto-aes-decryption-error-faq.md>)。
