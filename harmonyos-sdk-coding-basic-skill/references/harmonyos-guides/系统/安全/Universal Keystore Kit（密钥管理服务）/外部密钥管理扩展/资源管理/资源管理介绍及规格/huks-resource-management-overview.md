---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-resource-management-overview
title: 资源管理介绍及规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 资源管理 > 资源管理介绍及规格
category: harmonyos-guides
scraped_at: 2026-06-01T11:18:49+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:60a8e2b73ddec1c7ce1b47f81b6a0b56b3272e8b28343f76cb91bdfe5fbee1fd
---
约定外部密钥管理扩展（例如Ukey）中使用resourceId唯一标识资源。该resourceId目前支持通过[查询证书操作](<../../../../../../../harmonyos-references/安全/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.certManagerDialog (证书管理对话框模块)/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22>)返回。每个证书链对应1个resourceId。应用拿到resourceId后，需要[打开资源](../打开资源关闭资源(CC++)/huks-open-close-resource-ndk.md#打开资源)，然后才可以进行后续密钥操作。操作完成后需要[关闭资源](../打开资源关闭资源(CC++)/huks-open-close-resource-ndk.md#关闭资源)。

说明

1. 操作密钥之前，必须先打开资源。如果涉及私钥签名等高权限操作，需要验证完PIN码后，才能继续执行，否则会导致资源状态异常。
2. 用户操作之后，必须手动关闭资源，避免资源泄漏。
