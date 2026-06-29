---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-42
title: 在使用Canvas的场景中，如何主动控制组件刷新UI
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在使用Canvas的场景中，如何主动控制组件刷新UI
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a467bd8a0e90c8d02c1681927df2839df296e39f0b3b7aa736ef0313230fb44c
---
Canvas组件最终的显示内容分两种：

一是组件的通用属性包括背景色、边框等渲染属性，这些属性可以通过状态变量驱动更新。

二是通过CanvasRenderingContext2D绘制接口由应用自行绘制的内容。该接口在调用时不会响应状态变量，会在下一帧自动刷新绘制内容，无需开发者主动控制刷新。

**参考链接**

[CanvasRenderingContext2D](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/画布绘制/CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md)
