---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-123
title: Color支持哪些格式，使用color: 'rgba(0, 0, 255, .5)'格式不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Color支持哪些格式，使用color: 'rgba(0, 0, 255, .5)'格式不生效
category: harmonyos-faqs
scraped_at: 2026-06-12T10:27:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a68674df668b5d60821f64ff5d6a6e779b1e4f6173d8fe4a50f83707a5842f4b
---
系统规格要求rgba格式必须完整书写，如rgba(0, 0, 255, 0.5)中透明度值前导0不可省略。

**参考链接**

[ResourceColor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor)
