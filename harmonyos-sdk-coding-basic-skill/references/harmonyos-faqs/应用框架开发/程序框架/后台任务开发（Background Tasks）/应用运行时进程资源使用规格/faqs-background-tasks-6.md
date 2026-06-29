---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-6
title: 应用运行时进程资源使用规格
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 应用运行时进程资源使用规格
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:22+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:5535735980bb0ea70577035df56a3c50208cca42cf72803e84a24eb9a0f1b7aa
---
内存资源配额为2GB。当内存使用量连续1分钟超过2GB时，前台触发告警，后台终止进程。

* 后台10分钟单核平均使用率超过10%时，结束进程。
* 后台20分钟单核平均使用率超过7.5%时，结束进程。
* 后台单核平均使用率在60分钟内高于2.5%时，结束进程。
* 后台120分钟内单核平均使用率超过1.3%，结束进程。

  IO：资源配额1GB，进程重启后配额清零。

**参考链接**

[Stage模型开发概述](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型开发概述/stage-model-development-overview.md>)

[Background Tasks Kit](<../../../../../harmonyos-references/Background Tasks Kit（后台任务开发服务）/background-tasks-api.md>)
