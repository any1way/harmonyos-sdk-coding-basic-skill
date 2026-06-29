---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-464
title: 半模态打开的页面被半模态覆盖了，怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 半模态打开的页面被半模态覆盖了，怎么解决
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:393a765913af084697da67334d281447575e28ec0b91c23b8dfdd3f8b1d4e5a5
---
**问题描述**

在路由框架使用NavPathStack+NavDestination的组合方案时。在页面A通过bindSheet打开了一个半模态窗口W，然后在窗口W里，点击按钮打开页面B，此时发现页面B在窗口W下面打开。希望新页面打开不要被半模态窗口覆盖住。

**解决措施**

半模态面板默认是在当前UIContext内顶层显示，在所有页面之上。可以通过设置半模态的[SheetOptions](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#sheetoptions)中[mode](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#sheetmode12枚举说明)属性来实现打开的页面覆盖在半模态上方。
