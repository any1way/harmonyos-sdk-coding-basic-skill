---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render-monitor
title: 注册节点渲染状态监听错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 注册节点渲染状态监听错误码
category: harmonyos-references
scraped_at: 2026-06-01T15:53:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:10ae9f87ed8b7d4b07c7efbc9347597b2aa7d29c516b59c04be2c84dab129b84
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](../../../../通用错误码/errorcode-universal.md)。

## 161001 监视渲染状态的节点数超过限制

PhonePC/2in1TabletTVWearable

**错误信息**

The count of nodes monitoring render state is over the limitation.

**错误描述**

当注册的监视渲染状态的节点数超过限制时，系统会产生此错误码。

**可能原因**

监视渲染状态的节点数超过限制。

**处理步骤**

请确保注册的监视渲染状态的节点数小于64。
