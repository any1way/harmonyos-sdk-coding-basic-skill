---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-preparations
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-01T11:16:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7969673388dcfa2d693bf151a9c879f5e63791aefad16d295074e44ac8522493
---
## 环境准备

* HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。
* DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上。
* HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta1 SDK及以上。

## 申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

* [注册账号](https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148)和[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。
* [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)和[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
* [申请企业MDM应用发布证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-cert-0000002283256801)和[申请企业MDM应用发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-profile-0000002248341094)。

## 申请权限

在申请权限前，请确保符合[权限使用的基本原则](../../程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md#权限使用的基本原则)。然后在工程模块对应的[module.json5配置文件](../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中"requestPermissions"标签下申请实际所需的开发权限。

| 应用能力 | 需要权限 |
| --- | --- |
| 文件分级管控 | ohos.permission.FILE\_GUARD\_MANAGER  ohos.permission.SET\_FILE\_GUARD\_POLICY |
| 企业恢复密钥 | ohos.permission.ENTERPRISE\_RECOVERY\_KEY |

例如：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.FILE_GUARD_MANAGER"
4. },
5. {
6. "name": "ohos.permission.SET_FILE_GUARD_POLICY"
7. },
8. {
9. "name": "ohos.permission.ENTERPRISE_RECOVERY_KEY"
10. }
11. ]
```
