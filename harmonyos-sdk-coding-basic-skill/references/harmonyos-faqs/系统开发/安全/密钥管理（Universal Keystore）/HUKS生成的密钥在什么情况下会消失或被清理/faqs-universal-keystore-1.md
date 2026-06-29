---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-1
title: HUKS生成的密钥在什么情况下会消失或被清理
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > HUKS生成的密钥在什么情况下会消失或被清理
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:05b02e02303c44aac600ca594a865c3b9b8ab1d36d7d3ba3bbf603567e187fa2
---
应用中调用 `huks.deleteKeyItem` 接口可以删除指定别名的密钥。应用卸载后，存储在设备安全环境中的密钥将自动销毁。

**参考链接**

[huks.deleteKeyItem](<../../../../../harmonyos-references/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huks (通用密钥库系统)/js-apis-huks.md#huksdeletekeyitem9>)
