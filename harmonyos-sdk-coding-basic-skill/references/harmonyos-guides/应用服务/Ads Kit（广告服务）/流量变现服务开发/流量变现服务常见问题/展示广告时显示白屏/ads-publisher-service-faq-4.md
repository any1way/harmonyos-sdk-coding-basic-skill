---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-faq-4
title: 展示广告时显示白屏
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 流量变现服务常见问题 > 展示广告时显示白屏
category: harmonyos-guides
scraped_at: 2026-06-01T15:00:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:644c438b707833b22fdc0cff3228b2e2df9f12b5db8e2f301141aec9fc74e71c
---
展示广告时出现白屏可能原因为展示的广告样式与UI展示页面不匹配，横幅广告使用[AutoAdComponent](<../../../../../../harmonyos-references/Ads Kit（广告服务）/ArkTS组件/@ohos.advertising.AutoAdComponent (轮播广告展示组件)/js-apis-autoadcomponent.md>)组件展示；原生广告、开屏广告、贴片广告使用[AdComponent](<../../../../../../harmonyos-references/Ads Kit（广告服务）/ArkTS组件/@ohos.advertising.AdComponent (广告展示组件)/js-apis-adcomponent.md>)组件展示；激励广告、插屏广告调用[showAd](<../../../../../../harmonyos-references/Ads Kit（广告服务）/ArkTS API/@ohos.advertising (广告服务框架)/js-apis-advertising.md#advertisingshowad>)方法展示。

建议排查步骤：

1. 获取请求广告时返回的广告数据并记录。
2. 打印展示广告时入参的广告数据，对比两者是否一致。
3. 检查请求的广告类型与使用的展示组件是否匹配。
