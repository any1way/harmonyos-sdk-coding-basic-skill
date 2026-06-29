---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-477
title: 组件内转场(transition)新增内容动画生效，但删除内容动画不生效的可能原因是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 组件内转场(transition)新增内容动画生效，但删除内容动画不生效的可能原因是什么
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b7013bb09054de37cba4e4753aa5a77aa50bb027bcb06961f287de77482532bc
---
**问题描述**

当为List等组件设置组件内转场动画时，data数组size变化时展示对应的新增或删除动画，但删除动画未生效，可能是什么原因？

**解决措施**

检查组件是否设置了clip裁剪属性为true且未设置高度。例如给ListItem设置transition动画时，List组件默认的clip裁剪属性为true，若List未设置高度，则会根据子组件自动调整，删除item后，List的高度会减小，但未给List设置动画，由于未对List高度变化设置动画过渡，且clip裁剪区域同步缩小，即List的clip为true且有裁剪效果，因此被裁剪的删除动画不可见。

**参考链接**

[clip](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/形状裁剪/ts-universal-attributes-sharp-clipping.md#clip12)
