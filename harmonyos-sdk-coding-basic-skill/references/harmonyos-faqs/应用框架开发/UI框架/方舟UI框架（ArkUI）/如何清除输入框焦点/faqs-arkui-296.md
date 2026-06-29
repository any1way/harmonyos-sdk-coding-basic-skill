---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-296
title: 如何清除输入框焦点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何清除输入框焦点
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:60682c66d11454959e6d6ebf30fe47f2ec3d0050c86755fc11aa49e3ca1e9eba
---
可以使用FocusController的[clearFocus](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (FocusController)/arkts-apis-uicontext-focuscontroller.md#clearfocus12>)方法来清除焦点并关闭软键盘，示例代码如下：

```
1. this.getUIContext().getFocusController().clearFocus()
```

[ClearFocus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ClearFocus.ets#L10-L10)
