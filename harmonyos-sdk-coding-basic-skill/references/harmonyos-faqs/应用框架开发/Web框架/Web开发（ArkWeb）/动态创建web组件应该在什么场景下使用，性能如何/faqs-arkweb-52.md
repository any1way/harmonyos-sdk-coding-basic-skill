---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-52
title: 动态创建web组件应该在什么场景下使用，性能如何
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 动态创建web组件应该在什么场景下使用，性能如何
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:699e9d7f651e5efa13ec9b2fe5f49fabacdd103e32f84237d5bd7f475a263508
---
使用场景：动态创建Web组件旨在解决页面切换时的加载白屏问题，典型场景是在多页面应用中。例如，当需要在三个页面之间来回切换时，每个页面都是一个Web组件。如果每次页面切换都重新初始化Web组件，会消耗大量资源，导致加载缓慢，从而出现白屏现象，影响用户体验。通过动态创建Web组件，可以有效减少资源消耗；提高加载速度；避免白屏问题，提升用户体验。

性能：动态加载在非UI线程中执行，数量较多时会对现有WebView加载产生一定影响。建议后台启动的Web实例不超过200个。

**参考链接**

[使用Web组件加载页面](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/管理网页加载与浏览记录/使用Web组件加载页面/web-page-loading-with-web-components.md)
