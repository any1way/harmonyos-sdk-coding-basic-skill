---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/development-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-01T14:59:59+08:00
doc_updated_at: 2026-05-13
content_hash: sha256:e7cde62fa3aa18bf7d6277434b3e1ed25b9a21e980e52928ae7623710b100c4c
---
## 申请权限

应用在使用Ads Kit能力前，需要检查是否已经获取对应权限。如未获得授权，需要声明对应权限。

Ads Kit所需的权限有：

* ohos.permission.INTERNET：用于请求和展示广告、回传竞价结果。
* ohos.permission.APP\_TRACKING\_CONSENT：用于获取开放匿名设备标识符。

在模块的module.json5中配置所需申请的权限，其中跨应用关联权限[ohos.permission.APP\_TRACKING\_CONSENT](../../../系统/安全/程序访问控制/应用权限管控/应用权限列表/开放权限（用户授权）/permissions-for-all-user.md#ohospermissionapp_tracking_consent)为user\_grant权限，reason和abilities标签必填，配置方式参见[requestPermissions标签说明](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md#在配置文件中声明权限)。

示例代码如下所示：

```
1. {
2. "module": {
3. "requestPermissions": [
4. {
5. "name": "ohos.permission.APP_TRACKING_CONSENT",
6. "reason": "$string:reason",
7. "usedScene": {
8. "abilities": [
9. "EntryAbility"
10. ],
11. "when": "inuse"
12. }
13. },
14. {
15. "name": "ohos.permission.INTERNET"
16. }
17. ]
18. }
19. }
```
