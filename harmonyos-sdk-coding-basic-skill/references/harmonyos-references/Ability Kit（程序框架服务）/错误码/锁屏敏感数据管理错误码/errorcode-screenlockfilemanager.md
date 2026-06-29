---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screenlockfilemanager
title: 锁屏敏感数据管理错误码
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > 错误码 > 锁屏敏感数据管理错误码
category: harmonyos-references
scraped_at: 2026-06-01T15:32:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:828c07c325e699dc7606a35e9cb364135dce36c0ba20281ef32e3c4e2cb14985
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../通用错误码/errorcode-universal.md)。

## 29300002 系统服务工作异常

PhonePC/2in1Tablet

**错误信息**

The system ability work abnormally.

**可能原因**

该错误码表示系统服务工作异常。

1. 锁屏敏感数据管理服务无法正常启动。
2. IPC数据读取写入失败。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备。

## 29300003 应用未开启锁屏敏感数据保护功能

PhonePC/2in1Tablet

**错误信息**

The application has not enabled the data protection under lock screen.

**可能原因**

1. 应用未在[requestpermissions](../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md#在配置文件中声明权限)配置权限ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA开启应用锁屏敏感数据保护功能。
2. 当前硬件不支持锁屏敏感数据保护功能。

**处理步骤**

在[requestpermissions](../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md#在配置文件中声明权限)中配置权限ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA开启应用锁屏敏感数据保护功能。

## 29300004 锁屏敏感数据访问权限已释放

PhonePC/2in1Tablet

**错误信息**

File access is denied.

**可能原因**

锁屏敏感数据访问权限已释放。

**处理步骤**

锁屏下无法访问敏感数据，如有需要，请提示用户重新解锁屏幕，解锁后敏感数据恢复方可使用。

## 29300005 未申请锁屏敏感数据访问权限

PhonePC/2in1Tablet

**错误信息**

File access was not acquired.

**可能原因**

该错误码表示释放前，未申请锁屏敏感数据访问权限。

**处理步骤**

检查当前接口是否有配套使用，请在释放前先申请锁屏敏感数据访问权限。
