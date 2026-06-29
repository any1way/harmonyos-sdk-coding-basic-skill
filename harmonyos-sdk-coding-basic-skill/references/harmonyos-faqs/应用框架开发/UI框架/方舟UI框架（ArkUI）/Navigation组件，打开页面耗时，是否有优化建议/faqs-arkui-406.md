---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-406
title: Navigation组件，打开页面耗时，是否有优化建议
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件，打开页面耗时，是否有优化建议
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:35+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:3d01f0f18efa9d2b72a18741e80742b52ddd7c9410d2c18fdabf8da412c93938
---
**问题描述**

在业务场景中，使用Navigation打开子页面，其中父容器布局为Row容器下套一个Navigation，子页面就是一个普通的Component，整体测试下来发现从父容器aboutToAppear到子页面aboutToAppear耗时10~15ms，这段时间是否能优化。

**解决措施**

Navigation组件跳转后父容器aboutToAppear到子页面aboutToAppear耗时10~15ms属于正常耗时。

**参考链接**

[页面生命周期](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation子页面/arkts-navigation-navdestination.md#页面生命周期>)
