---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-provider-management-overview
title: Provider管理介绍及规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > Provider管理 > Provider管理介绍及规格
category: harmonyos-guides
scraped_at: 2026-06-01T11:18:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bcfe2306b25e33313b98cf794f5650ae694853acd9f0dc4264717ed58f57fb46
---
HUKS提供外部密钥管理扩展能力（简称Ukey Extension）注册和注销接口。三方驱动HAP检测到Ukey存在时，调用Provider注册接口，将驱动HAP应用提供的外部密钥管理能力注册到系统中来。当检测到所有Ukey被拔出时，通过调用Provider注销接口，将其提供的外部密钥管理能力从系统中注销。

说明

1. Provider名称建议包含厂商信息，全局唯一。
2. Provider名称长度最大为128字节。
3. Provider注册和注销有权限管控，需申请[ohos.permission.CRYPTO\_EXTENSION\_REGISTER](../../../../程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md#ohospermissioncrypto_extension_register)权限。
4. 一个Provider可以关联到多个Ability。一般来说，Provider是厂商驱动名称，Ability是厂商针对其名下的各个业务定制扩展能力的名称，也可以由厂商自行决定Provider和Ability的名称。

**支持功能规格：**

| 功能 | 说明 | API级别 |
| --- | --- | --- |
| Provider注册 | 注册外部密钥管理扩展能力提供者到系统。 | 22+ |
| Provider注销 | 从系统中注销外部密钥管理扩展能力提供者。 | 22+ |
