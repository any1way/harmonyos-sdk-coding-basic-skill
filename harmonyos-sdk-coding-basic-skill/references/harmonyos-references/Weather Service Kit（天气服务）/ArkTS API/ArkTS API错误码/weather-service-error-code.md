---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/weather-service-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Weather Service Kit（天气服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-06-01T16:39:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d07b4a45ec8a51a194dd8b09db894dab9cda3294968df0fd1cecbf9ba92a5f6
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](../../../通用错误码/errorcode-universal.md)说明文档。

## 1011900001 未开通天气服务

PhonePC/2in1TabletTVWearable

**错误信息**

Capability is not configured.

**错误描述**

未开通天气服务。

**可能原因**

1、未开通天气服务。

2、应用签名配置不正确。

**处理步骤**

1、确认用户已开通天气服务。

2、参考[配置签名信息](../../../../harmonyos-guides/应用开发准备/应用开发准备/application-dev-overview.md#配置签名信息)的流程，确认应用签名配置正确。

3、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1011900002 天气数据缺失

PhonePC/2in1TabletTVWearable

**错误信息**

The requested longitude and latitude grid point lacks data.

**错误描述**

天气数据缺失。

**可能原因**

提供的经纬度位置非陆地区域。

**处理步骤**

1、可以利用搜索引擎检查经纬度数据是否是陆地区域。

2、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1011900003 网络错误

PhonePC/2in1TabletTVWearable

**错误信息**

Network error.

**错误描述**

网络错误。

**可能原因**

网络未连接。

**处理步骤**

1、检查网络配置。

2、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1011900004 系统内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

System error.

**错误描述**

系统内部错误。

**可能原因**

连接服务失败或其他内部错误。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
