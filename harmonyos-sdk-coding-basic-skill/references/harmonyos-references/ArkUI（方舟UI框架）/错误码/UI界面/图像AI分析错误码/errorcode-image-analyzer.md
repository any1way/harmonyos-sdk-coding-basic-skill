---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer
title: 图像AI分析错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 图像AI分析错误码
category: harmonyos-references
scraped_at: 2026-06-01T15:53:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a20284c2273b06670f0ecd30eae4ef03b44824a3f6562b0ccb1aff6c73213e1e
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 110001 AI图像分析功能不支持

**错误信息**

Image analysis feature is unsupported.

**错误描述**

当开发者调用startImageAnalyzer()接口时，若当前不支持AI分析功能，会抛出此错误码。

**可能原因**

调用不支持的功能接口。

**处理步骤**

NA

## 110002 AI图像分析正在进行中

**错误信息**

Image analysis is currently being executed.

**错误描述**

当开发者调用startImageAnalyzer()接口时，若上一次的分析还没有结束，会抛出此错误码。

**可能原因**

调用接口时机错误。

**处理步骤**

NA

## 110003 AI图像分析已停止

**错误信息**

Image analysis is stopped.

**错误描述**

当开发者调用startImageAnalyzer()接口，当前分析未完成时调用了stopImageAnalyzer()接口，会抛出此错误码。

**可能原因**

调用接口时机错误。

**处理步骤**

NA
