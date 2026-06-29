---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-79
title: web组件访问过程中的illegal、fraud、risk和warning这4个风险等级区别是什么？是否可以自定义
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > web组件访问过程中的illegal、fraud、risk和warning这4个风险等级区别是什么？是否可以自定义
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:37afab0d7229257ffb6e34deb89169a025959ebf36d4c9cc0a315efe17fbd1c5
---
* illegal、fraud 禁止访问，没有继续浏览的按钮。
* risk 禁止访问，有继续浏览的按钮。
* warning web内核不会主动拦截，仅展示警告提示，不提供继续访问的按钮。

目前不允许自定义风险访问控制的流程，也没有提供相关回调。

**参考链接**

[ThreatType](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/Enums/arkts-basic-components-web-e.md#threattype11>)
