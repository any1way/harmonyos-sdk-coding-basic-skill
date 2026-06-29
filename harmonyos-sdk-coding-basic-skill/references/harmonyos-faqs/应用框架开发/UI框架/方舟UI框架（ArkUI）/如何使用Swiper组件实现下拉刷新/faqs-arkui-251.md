---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-251
title: 如何使用Swiper组件实现下拉刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何使用Swiper组件实现下拉刷新
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:67a3a32f31d3680d95e8f86241ac95ee03eab29d102a52f65a6efa0c11df3bd4
---
Swiper组件用于创建滑块视图容器，可以使用Refresh组件实现下拉刷新效果。

```
1. @Entry
2. @Component
3. struct SwiperItemLeak {
4. @State isStopSwiperSlide: boolean = false;
5. @State positionY: number = 0;
6. private swiperController: SwiperController = new SwiperController();
7. @State curSwiperIndex: number = 0;
8. private list: number[] = [];

10. aboutToAppear(): void {
11. for (let i = 1; i <= 10; i++) {
12. this.list.push(i);
13. }
14. }

16. build() {
17. Refresh({ refreshing: $$this.isStopSwiperSlide}) {
18. Swiper(this.swiperController) {
19. ForEach(this.list, (item: number) => {
20. Text(item.toString())
21. .width('100%')
22. .height('100%')
23. .backgroundColor(0xAFEEEE * ((item + 1) / 0x0f))
24. .textAlign(TextAlign.Center)
25. .fontSize(30)
26. },(item: number) => JSON.stringify(item))
27. }
28. .vertical(true)
29. .width('100%')
30. .height('100%')
31. .cachedCount(3)
32. .index(0)
33. .autoPlay(false)
34. .indicator(false)
35. .effectMode(EdgeEffect.None)
36. .loop(false)
37. .duration(100)
38. .disableSwipe(this.isStopSwiperSlide)
39. .displayCount(1)
40. .itemSpace(0)
41. .curve(Curve.Linear)
42. .backgroundColor(Color.Red)
43. .position({ y: this.positionY })
44. .onChange((index: number) => {
45. this.curSwiperIndex = index;
46. })
47. }
48. .onRefreshing(() => {
49. setTimeout(() => {
50. this.isStopSwiperSlide = false
51. }, 2000)
52. })
53. .backgroundColor(0x89CFF0)
54. .refreshOffset(64)
55. .pullToRefresh(true)
56. .width('100%')
57. .height('100%')
58. }
59. }
```

[UseSwiperDropdownToRefresh.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/UseSwiperDropdownToRefresh.ets#L21-L79)

**参考链接**

[Refresh](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Refresh/ts-container-refresh.md)
