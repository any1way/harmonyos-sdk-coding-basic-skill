---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-414
title: 如何监听Navigation页面栈变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听Navigation页面栈变化
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:11f235635a38809b6f1df71d280af2fea90172512541fbf6c639a8b6b0d68ace
---
通过[uiObserver.on('navDestinationSwitch')](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.observer (无感监听)/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12-1>)方法，可以监听Navigation的页面切换事件，当Navigation组件发生页面跳转时触发该事件，典型场景包括页面访问统计、页面生命周期管理等。
