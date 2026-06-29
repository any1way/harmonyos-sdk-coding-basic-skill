---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-preparations
title: 开发准备
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-01T15:10:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e5347e27ce9df45ba2e2fb50076deda2b5bb152558e61665215fb5fbdd4be12
---
请先参考“[应用开发准备](../../../应用开发准备/应用开发准备/application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

## 申请权限

开发者需要根据实际场景申请对应权限，请保证符合[权限使用的基本原则](../../../系统/安全/程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[声明权限](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)声明对应权限。

| 权限 | 使用场景 |
| --- | --- |
| ohos.permission.GET\_WIFI\_INFO | 使用场景化API获取Wi-Fi信息需要申请该权限（使用5.0.1(13)及以上版本时不需要设置该权限）。 |
| ohos.permission.ACCESS\_BLUETOOTH | 使用场景化API获取蓝牙信息需要申请该权限（使用5.0.1(13)及以上版本时不需要设置该权限）。 |

说明

获取用户程序访问控制权限可参考[程序访问控制管理](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.abilityAccessCtrl (程序访问控制管理)/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9>)。
