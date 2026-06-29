---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-193
title: 应用如何设置隐藏顶部的状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 应用如何设置隐藏顶部的状态栏
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4c839019da29308f0c526fd9cbc731efe170dbda30913532bef7f6928a31d0eb
---
在UIAbility的onWindowStageCreate生命周期中，设置setWindowSystemBarEnable接口。

```
1. onWindowStageCreate(windowStage: window.WindowStage): void {
2. windowStage.getMainWindowSync().setWindowSystemBarEnable([])
3. // ...
4. }
```

[EntryAbilityForHideBar.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityForHideBar.ets#L21-L37)

**参考链接**

[体验窗口沉浸式能力](../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/窗口管理/管理应用窗口（Stage模型）/application-window-stage.md#体验窗口沉浸式能力)
