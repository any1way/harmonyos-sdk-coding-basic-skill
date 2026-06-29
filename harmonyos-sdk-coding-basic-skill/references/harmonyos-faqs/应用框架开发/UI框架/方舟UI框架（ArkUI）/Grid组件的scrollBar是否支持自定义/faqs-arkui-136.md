---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-136
title: Grid组件的scrollBar是否支持自定义
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Grid组件的scrollBar是否支持自定义
category: harmonyos-faqs
scraped_at: 2026-06-12T10:27:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e2eeb413a45e5a1a1b8fb99c09205637f68d74f21669891d14ab5cb31922a74a
---
Grid组件的默认滑动条scrollBar不支持自定义样式。

可以通过隐藏默认滑动条并绑定ScrollBar组件来满足该场景。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. private scroller: Scroller = new Scroller()
5. private arr: number[] = [];

7. build() {
8. Column() {
9. Stack({ alignContent: Alignment.End }) {
10. Grid(this.scroller) {
11. ForEach(this.arr, (item: number) => {
12. GridItem() {
13. Text(item.toString())
14. .width(100)
15. .height(50)
16. .backgroundColor('#3366CC')
17. .borderRadius(15)
18. .fontSize(16)
19. .textAlign(TextAlign.Center)
20. }
21. })
22. }
23. .width('100%')
24. .columnsTemplate("1fr 1fr 1fr")
25. .columnsGap(5)
26. .rowsGap(5)
27. // Hide native scrollBar
28. .scrollBar(BarState.Off)

30. ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
31. Text("A")
32. .width(20)
33. .height(50)
34. .borderRadius(10)
35. .backgroundColor('#C0C0C0')
36. }
37. .width(20)
38. .backgroundColor('#ededed')
39. }
40. }
41. }

43. aboutToAppear() {
44. for (let i = 0; i < 100; i++) {
45. this.arr.push(i)
46. }
47. }
48. }
```

[DoesGridSupportCustomization.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DoesGridSupportCustomization.ets#L21-L68)

**参考链接**

[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)，[ScrollBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ScrollBar/ts-basic-components-scrollbar.md)
