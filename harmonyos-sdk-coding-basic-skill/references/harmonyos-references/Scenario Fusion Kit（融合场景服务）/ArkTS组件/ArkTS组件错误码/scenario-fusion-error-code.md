---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-error-code
title: ArkTS组件错误码
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS组件 > ArkTS组件错误码
category: harmonyos-references
scraped_at: 2026-06-01T16:39:31+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:08d400cc5ca280b7166960e3106b7e3ceedc33bb03175c4eee8564727af8450b
---
说明

本模块错误码请参考以下链接。

[通用错误码](../../../通用错误码/errorcode-universal.md)

[Map Kit错误码](<../../../Map Kit（地图服务）/ArkTS API/ArkTS API错误码/errorcode-map.md>)

[Ability Kit错误码](<../../../Ability Kit（程序框架服务）/错误码/ability-arkts-errcode.md>)

[Account Kit错误码](<../../../Account Kit（华为账号服务）/ArkTS错误码/account-api-error-code.md>)

[Live View Kit错误码](<../../../Live View Kit（实况窗服务）/ArkTS API/ArkTS API错误码/liveview-error-code.md>)

[Push Kit错误码](<../../../Push Kit（推送服务）/ArkTS API/ArkTS API错误码/push-error-code.md>)

[ArkTS API错误码](../../../ArkTS（方舟编程语言）/错误码/语言基础类库错误码/errorcode-utils.md)

[REST API错误码](<../../../Account Kit（华为账号服务）/REST API/REST API错误码/account-server-error-code.md>)

## 10004 系统内部异常

PhonePC/2in1TabletTV

**错误信息**

Internal error.

**错误描述**

系统内部异常。

**可能原因**

系统内部异常。

**处理步骤**

检查是否是网络问题，如果是服务动态授权码Button报错，查看是否对子场景进行了邮件申请，详见[参考文档](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-timeline#section18702113217305)。

## 10006 获取分享数据失败

PhonePC/2in1TabletTV

**错误信息**

Failed to get data.

**错误描述**

获取分享数据失败。

**可能原因**

系统内部异常。

**处理步骤**

检查网络环境，如非网络环境影响需要结合具体日志分析。

## 10008 调用方非元服务

PhonePC/2in1TabletTV

**错误信息**

Not atomic service.

**错误描述**

调用方非元服务。

**可能原因**

非元服务调用了此接口。

**处理步骤**

通过元服务应用调用此接口。
