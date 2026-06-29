---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-11
title: 应用申请位置信息权限为什么没有弹窗
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 应用申请位置信息权限为什么没有弹窗
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:45+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:e5d558987809ff6b3312480a99b31d00e0064e4314a646ff32d217d66355b84d
---
**可能原因**

未申请ohos.permission.LOCATION权限。

**解决措施**

开发应用时，需要先申请权限ohos.permission.LOCATION，才能获取位置信息。

**参考链接**

[开放权限（用户授权）](../../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/应用权限列表/开放权限（用户授权）/permissions-for-all-user.md)
