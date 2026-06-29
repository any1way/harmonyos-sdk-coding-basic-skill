---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-18
title: 如何解决Web与List的嵌套滑动冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决Web与List的嵌套滑动冲突
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e287a0f62d5c87bccc209b6a1bdfe56a4aab43a21aee0573482ff1ae58729d32
---
可以设置组件的hitTestBehavior来避免这种情况，参考代码如下：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct SlidingConflictBetweenWebAndList {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. List() {
10. ListItem() {
11. Web({
12. src: $rawfile('index.html'),
13. controller: this.webviewController
14. })
15. .width('100%')
16. .height(220)
17. }.hitTestBehavior(HitTestMode.Block)
18. ListItem() {
19. Web({
20. src: $rawfile('index.html'),
21. controller: this.webviewController
22. })
23. .width('100%')
24. .height(220)
25. }
26. ListItem() {
27. Text('1')
28. }
29. .height(220)
30. ListItem() {
31. Text('2')
32. }
33. .height(220)
34. }
35. .backgroundColor(Color.Blue)
36. .width('100%')
37. .height('100%')
38. }
39. }
```

[ResolveTheNestingOfWebAndList.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveTheNestingOfWebAndList.ets#L21-L59)

**参考链接**

[触摸测试控制](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸测试控制/ts-universal-attributes-hit-test-behavior.md)
