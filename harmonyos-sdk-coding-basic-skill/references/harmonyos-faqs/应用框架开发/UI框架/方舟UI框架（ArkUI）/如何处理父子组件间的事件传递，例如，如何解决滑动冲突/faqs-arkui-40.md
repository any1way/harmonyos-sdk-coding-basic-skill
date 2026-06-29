---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-40
title: 如何处理父子组件间的事件传递，例如，如何解决滑动冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何处理父子组件间的事件传递，例如，如何解决滑动冲突
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:37+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:0a05719469e8ef83cbf710861df6f484f5684000507611b8a1c99dcf958f29d2
---
1. 系统基于触摸测试收集需响应事件的控件，测试顺序从父组件到子组件。后续手势识别和竞争基于hitTest结果。

2. 应用可改变组件上 hitTestBehavior 的值，以修改系统对其的 hitTest 结果。

3. 通过自定义事件和手势判定能力，可细化手势识别与竞争结果的干预。

**参考链接**

[触摸测试控制](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸测试控制/ts-universal-attributes-hit-test-behavior.md)、[自定义事件分发](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互事件分发控制/自定义事件分发/ts-universal-attributes-on-child-touch-test.md)、[自定义手势判定](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/手势控制/自定义手势判定/ts-gesture-customize-judge.md)
