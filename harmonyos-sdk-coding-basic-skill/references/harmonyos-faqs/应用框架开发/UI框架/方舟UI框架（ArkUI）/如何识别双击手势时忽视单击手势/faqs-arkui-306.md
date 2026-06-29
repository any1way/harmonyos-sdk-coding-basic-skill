---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-306
title: 如何识别双击手势时忽视单击手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何识别双击手势时忽视单击手势
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b4a2da42a8a72f3a1c263eb3b545ebeef3ef207d1c1ef59e256ff3737439fd8e
---
使用组合手势GestureGroup的互斥识别。双击事件应置于单击事件之前，互斥识别按排列顺序进行。如果单击事件在前，则只会识别单击事件。参考代码如下：

```
1. @Entry
2. @Component
3. struct TapGestureExample {
4. build() {
5. Column() {
6. Text('Click twice')
7. .fontSize(28)
8. .gesture(GestureGroup(GestureMode.Exclusive,
9. TapGesture({ count: 2 })
10. .onAction(() => {
11. console.info('TapGesture 2');
12. }),
13. TapGesture({ count: 1 })
14. .onAction(() => {
15. console.info('TapGesture 1');
16. })
17. ))
18. }
19. .width('100%')
20. .height('100%')
21. .justifyContent(FlexAlign.Center)
22. .alignSelf(ItemAlign.Center)
23. }
24. }
```

[IgnoreSingleClickGestures.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/IgnoreSingleClickGestures.ets#L21-L44)

**参考链接**

[互斥识别](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/添加手势响应/组合手势/arkts-gesture-events-combined-gestures.md#互斥识别>)
