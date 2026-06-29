---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-319
title: 如何设置禁止分屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置禁止分屏
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:667deb988ebe20cc9465f4db2556d1e17df946aed5d3c2c4385d7d6add116422
---
在应用开发阶段设置时，通过在module.json5配置文件中[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)下的supportWindowMode属性设置fullscreen字段，设置后应用将强制全屏运行，无法进入分屏模式。
