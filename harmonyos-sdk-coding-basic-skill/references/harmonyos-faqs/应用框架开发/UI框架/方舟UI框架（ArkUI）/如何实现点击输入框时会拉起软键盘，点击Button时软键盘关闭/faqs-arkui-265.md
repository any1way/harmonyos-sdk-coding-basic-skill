---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-265
title: 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:04+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:ddc069ea42264d52fc1ea4bf991969705dc46f025d2e2b49ea28a2743315350f
---
可以通过全局的焦点控制对象FocusController的[clearFocus()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (FocusController)/arkts-apis-uicontext-focuscontroller.md#clearfocus12>)方法收起软键盘，示例代码如下：

```
1. @Entry
2. @Component
3. struct ClickBlankHideKeyboard {
4. build() {
5. Column({ space: 12 }) {
6. TextInput({ placeholder: 'Please enter your account' })
7. .height(40)
8. TextInput({ placeholder: 'Please input a password' })
9. .height(40)
10. Button('log on').width('100%')
11. .onClick(() => {
12. this.getUIContext().getFocusController().clearFocus();
13. })
14. }
15. }
16. }
```

[ClickButtonSoftwareKeyboardToClose.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ClickButtonSoftwareKeyboardToClose.ets#L21-L36)

参考链接：

[代码控制收起软键盘](../../../../../best-practices/应用框架/输入法/软键盘布局适配/bpta-keyboard-layout-adapt.md#section19809195110316)
