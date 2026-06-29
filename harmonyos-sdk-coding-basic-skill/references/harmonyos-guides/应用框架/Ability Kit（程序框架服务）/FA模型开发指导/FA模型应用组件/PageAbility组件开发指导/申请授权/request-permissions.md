---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-permissions
title: 申请授权
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > 申请授权
category: harmonyos-guides
scraped_at: 2026-06-01T10:58:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8103b83cba2152b7992550f77da1b064b6920fe0fac8fdeaf53eb4e8379932cc
---
应用需要获取用户的隐私信息或使用系统能力时，例如获取位置信息、使用相机拍摄照片或录制视频等，需要向用户申请授权。

在开发过程中，开发者首先需要明确涉及的敏感权限，并在config.json中声明这些权限。然后在运行时通过requestPermissionsFromUser接口，以动态弹窗的方式向用户申请授权。

在config.json声明需要的权限，在module下添加"reqPermissions"，并写入对应权限。

例如申请访问日历权限：

1. 需要申请ohos.permission.DISTRIBUTED\_DATASYNC权限，配置方式请参见[声明权限](../../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。
2. 同时需要在应用首次启动时弹窗向用户申请授权，使用方式请参见[向用户申请授权](../../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)。
