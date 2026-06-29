---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-105
title: 滑动的页面软键盘挡住内容不能向上滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 滑动的页面软键盘挡住内容不能向上滑动
category: harmonyos-faqs
scraped_at: 2026-06-12T10:27:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a10988de874ae68080425b90f3e9a1361dac034d8efac2da28d6c7aac67b2f11
---
计算软键盘的高度，然后将整体的margin-bottom设置为软键盘的高度。软键盘消失时，将margin-bottom设置为 0。软键盘高度可通过监听软键盘的显示事件获取。

**参考链接**

[输入法框架](<../../../../../harmonyos-references/IME Kit（输入法开发服务）/ArkTS API/@ohos.inputMethod (输入法框架)/js-apis-inputmethod.md>)
