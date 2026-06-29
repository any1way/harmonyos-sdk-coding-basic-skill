---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-446
title: pc上，bindPopup设置了showInSubWindow:true时，气泡无法再弹出菜单
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > pc上，bindPopup设置了showInSubWindow:true时，气泡无法再弹出菜单
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:15+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:a0c4dffdedc85b382aa527607fcae36b0b47d5cb086d38ce90e0f143f3d8593a
---
**问题背景**

在PC端使用bindPopup组件时，当设置了showInSubWindow: true属性后，如果气泡内的组件再次绑定子窗口弹窗，会导致内层弹窗无法正常弹出，如何修改？

**解决措施**

在PC设备上，使用[bindMenu方法](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md#bindmenu)弹出的菜单默认会以子窗口形式显示。由于系统限制，子窗口类型的弹窗无法嵌套绑定同类型弹窗，因此当尝试在子窗口弹窗内再弹出子窗口菜单时，操作将不被支持。若需要弹出bindMenu，可设置bindMenu的参数[showInSubWindow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md#menuoptions10)为false。

**参考链接**

[bindPopup](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/Popup控制/ts-universal-attributes-popup.md#bindpopup)
