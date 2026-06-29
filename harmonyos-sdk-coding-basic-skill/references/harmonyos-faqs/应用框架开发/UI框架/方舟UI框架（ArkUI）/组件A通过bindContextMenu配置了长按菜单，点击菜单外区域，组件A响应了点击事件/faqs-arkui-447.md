---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-447
title: 组件A通过bindContextMenu配置了长按菜单，点击菜单外区域，组件A响应了点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 组件A通过bindContextMenu配置了长按菜单，点击菜单外区域，组件A响应了点击事件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fa35262f9aa8ee243e1286d2e96fea326f9ad0877afd83c5b909e2520de65f24
---
**问题背景**

在组件A上通过bindContextMenu配置了长按菜单后，当用户点击菜单外区域时，会出现事件透传现象——组件A会响应点击事件。这种交互行为不符合某些场景下的设计需求，需要实现菜单弹出时完全阻断对下层组件的事件传递。

**解决措施**

当前菜单默认的模态行为是仅菜单自身区域可交互，菜单外区域保持事件穿透（点击会穿透到下层组件），默认模态模式对应的枚举值（如ModalMode.NONE）。从API 20版本开始，HarmonyOS开放了菜单模态模式的配置能力。通过将ModalMode参数设置为TARGET\_WINDOW即可实现。

**参考示例：**

```
1. @Entry
2. @Component
3. struct ModalModeDemo {
4. @State btnMessage: string = "Click To Trigger, longPress To Pop Up Menu"
5. @State toastMessage: string = "The Click event was triggered."
6. @Builder
7. MyMenu() {
8. Menu() {
9. MenuItem({ content: "MenuOptionOne" })
10. MenuItem({ content: "MenuOptionTwo" })
11. }
12. }

14. build() {
15. Stack({ alignContent: Alignment.Center }) {
16. Column() {
17. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
18. Column() {
19. Button(this.btnMessage)
20. .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
21. modalMode: ModalMode.TARGET_WINDOW,
22. placement: Placement.BottomLeft
23. })
24. .onClick(() => {
25. this.getUIContext().getPromptAction().showToast({
26. message: this.toastMessage
27. })
28. })
29. }
30. }
31. }
32. }.width('100%').height('100%')
33. }
34. }
```

[ModalModeDemo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ModalModeDemo.ets#L21-L54)

**参考链接**

[菜单控制](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md)
