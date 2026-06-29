---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-59
title: 弹窗组件无法进入onPageShow方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 弹窗组件无法进入onPageShow方法
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee0b42b0bc57ef68f49ad0659a806692a8927dd7989dafe75395b8ecd48655d5
---
自定义弹窗作为自定义组件的一种，拥有自定义组件生命周期aboutToAppear和aboutToDisappear。

onPageShow和onPageHide仅作为页面生命周期提供，@Entry修饰的自定义组件定义为页面，不适用于自定义弹窗。

**参考链接**

[自定义组件生命周期](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/自定义组件生命周期/arkts-page-custom-components-lifecycle.md>)
