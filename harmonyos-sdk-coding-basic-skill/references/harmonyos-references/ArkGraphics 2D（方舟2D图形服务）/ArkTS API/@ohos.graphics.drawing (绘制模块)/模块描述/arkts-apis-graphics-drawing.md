---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing
title: 模块描述
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > 模块描述
category: harmonyos-references
scraped_at: 2026-06-01T16:26:53+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:cf56336056e30800628a730b15c1b7ac38fed66658337cbfabfe5a81604edb0b
---

应用在开发中，经常需要针对不同的元素内容进行绘制，开发者通常可以选择直接使用ArkUI组件来绘制想要的元素或效果，但有些自定义图形或效果无法满足，此时可以选择使用Drawing来实现灵活的自定义绘制效果。Drawing模块提供基本的绘制能力，如绘制矩形、圆形、点、直线、自定义Path和字体等。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```
