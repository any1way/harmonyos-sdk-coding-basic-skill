---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-1
title: 如何解决振动模块接口调用报错，错误码201的问题
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何解决振动模块接口调用报错，错误码201的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c48c7d9d7be605f2abc84d0f5b14e30b7ec48ae2ec09d56dffa7171216dad767
---
**问题现象**

振动模块接口调用出现错误，错误码为201。

错误信息：“振动失败，错误代码：201，错误消息：NaN”。

**解决措施**

权限校验失败。请申请ohos.permission.VIBRATE权限。

**参考链接**

[应用权限管控概述](../../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md)
