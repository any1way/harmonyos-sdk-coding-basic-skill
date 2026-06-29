---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview
title: 群组密钥介绍
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 群组密钥 > 群组密钥介绍
category: harmonyos-guides
scraped_at: 2026-06-01T11:18:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:05fa38133b28f843edd086660f245ad111ff7d324b6c912296b8f85f8e9de731
---
从API 23开始，HUKS支持群组密钥功能，该功能是针对同一开发者开发的多个HAP应用，提供的跨应用密钥共享能力。

当多个HAP在配置中指定相同的组标识时，可共享同一组密钥资源，实现密钥在开发者自有应用生态内的安全复用，无需重复生成或手动传递密钥，简化跨应用加密场景的密钥管理流程。

说明

* 仅在手机、平板、PC/2in1、智能穿戴上支持群组密钥功能。
* 群组密钥严格限定在同一开发者相同组的HAP范围内。不同开发者的相同组或者相同开发者的不同组，都无法相互访问对方的群组密钥，从而保障密钥的隔离性与安全性。

## 规格说明

| 支持的本地密钥操作 | API级别 | 说明 |
| --- | --- | --- |
| [密钥生成](../../../密钥生成导入/密钥生成/密钥生成介绍及算法规格/huks-key-generation-overview.md) | 23+ | 支持生成群组密钥。 |
| [密钥导入](../../../密钥生成导入/密钥导入/密钥导入介绍及算法规格/huks-key-import-overview.md) | 23+ | 支持导入群组密钥。 |
| [加密/解密](../../../密钥使用/加密解密/加密解密介绍及算法规格/huks-encryption-decryption-overview.md) | 23+ | 支持使用群组密钥进行加密/解密。 |
| [签名/验签](../../../密钥使用/签名验签/签名验签介绍及算法规格/huks-signing-signature-verification-overview.md) | 23+ | 支持使用群组密钥进行签名/验签。 |
| [密钥协商](../../../密钥使用/密钥协商/密钥协商介绍及算法规格/huks-key-agreement-overview.md) | 23+ | 支持使用群组密钥进行密钥协商。 |
| [密钥派生](../../../密钥使用/密钥派生/密钥派生介绍及算法规格/huks-key-derivation-overview.md) | 23+ | 支持使用群组密钥进行密钥派生。 |
| [访问控制](../../../密钥使用/访问控制/用户身份认证访问控制简介/huks-identity-authentication-overview.md) | 23+ | 支持使用群组密钥进行二次访问控制。 |
| [HMAC](../../../密钥使用/HMAC/HMAC介绍及算法规格/huks-hmac-overview.md) | 23+ | 支持使用群组密钥进行HMAC。 |
| [密钥删除](../../../密钥删除/密钥删除(ArkTS)/huks-delete-key-arkts.md) | 23+ | 支持删除群组密钥。 |
| [密钥证明](../../../密钥证明/密钥证明介绍及算法规格/huks-key-attestation-overview.md) | 23+ | 支持群组密钥的合法性证明。 |
| [查询密钥是否存在](../../查询密钥是否存在/查询密钥是否存在(ArkTS)/huks-check-key-arkts.md) | 23+ | 支持查询群组密钥是否存在。 |
| [获取密钥属性](../../获取密钥属性/获取密钥属性(ArkTS)/huks-obtain-key-properties-arkts.md) | 23+ | 支持查询群组密钥的属性。支持获取DeveloperID和GroupID信息。 |
| [密钥导出](../../密钥导出/密钥导出(ArkTS)/huks-export-key-arkts.md) | 23+ | 支持导出群组密钥。 |
| [查询密钥别名集](../../查询密钥别名集/查询密钥别名集(ArkTS)/huks-list-aliases-arkts.md) | 23+ | 支持查询群组密钥别名集。 |
