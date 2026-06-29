---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-264
title: Navigation中pushPathByName与pushDestinationByName的区别
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation中pushPathByName与pushDestinationByName的区别
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:434a4b4c1f782fcd75c53a5e9ab9ab802c12aafead59d9f593bf276a4429c38f
---
[pushDestinationByName](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#pushdestinationbyname11)绑定上下文对象，调用时验证上下文是否一致，而[pushPathByName](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#pushpathbyname10)不进行验证。

不同的窗口，运行的UIContext不同。在单窗口场景下使用时，两者仅返回值存在差异；跨窗口使用时需注意UIContext的匹配性。
