---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-prepare
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:20+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:bb32c9e1c2f37e91e4e58f584e350d8189b8a5836b1ced568c7b36dbff33bf58
---
## 申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

* [注册账号](https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148)和[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。
* [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)和[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
* [申请企业应用发布证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-cert-0000002248177978)和[申请企业应用发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-profile-0000002248181282)。

## 申请权限

在申请权限前，请保证符合[权限使用的基本原则](../../程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md#权限使用的基本原则)。随后在工程模块对应的[module.json5配置文件](../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中"requestPermissions"标签下声明实际所需的开发权限。使用文件访问与处置能力，则应申请[ohos.permission.SCAN\_REMEDIATE\_VIRUS](../../程序访问控制/应用权限管控/应用权限列表/企业类应用可用权限/permissions-for-enterprise-apps.md#ohospermissionscan_remediate_virus)权限，此权限仅面向企业杀毒软件开放申请。权限申请代码示例如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.SCAN_REMEDIATE_VIRUS"
4. }
5. ]
```
