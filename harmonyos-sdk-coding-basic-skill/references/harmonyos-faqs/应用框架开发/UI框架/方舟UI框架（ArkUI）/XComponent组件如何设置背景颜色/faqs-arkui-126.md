---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-126
title: XComponent组件如何设置背景颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > XComponent组件如何设置背景颜色
category: harmonyos-faqs
scraped_at: 2026-06-12T10:27:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a8d2b7151380a1ac03f87f1af21f156bd17bc014001f4b49a636ab46193bf779
---
XComponent组件仅在XComponentType为TEXTURE时支持设置，XComponentType为SURFACE类型时不支持通用属性包括背景颜色设置，需采用EGL/OpenGLES或子组件内容设置。

**参考链接**

[XComponent](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/渲染绘制/XComponent/ts-basic-components-xcomponent.md)
