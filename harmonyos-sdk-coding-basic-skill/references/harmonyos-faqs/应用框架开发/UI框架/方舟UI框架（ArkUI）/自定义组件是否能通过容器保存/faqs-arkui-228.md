---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-228
title: 自定义组件是否能通过容器保存
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义组件是否能通过容器保存
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:17f1cdd1dff3d7b489f0bba0b8658045cdfe5dc39ef0a9119f5d5c0a1f6a3fc5
---
自定义组件是 struct 而非 class，因此无法直接存储在容器中。可以通过将自定义组件封装在 Builder 函数中，利用 Builder 的封装来实现存储。

参考代码如下：

```
1. @Component
2. struct ComA {
3. build() {
4. Text('ComA').fontSize(50).fontWeight(FontWeight.Bold)
5. }
6. }

8. @Component
9. struct ComB {
10. build() {
11. Text('ComB').fontSize(50).fontWeight(FontWeight.Bold)
12. }
13. }

15. @Component
16. struct ComC {
17. build() {
18. Text('ComC').fontSize(50).fontWeight(FontWeight.Bold)
19. }
20. }

22. //if else logical branch writing
23. @Builder
24. function buildCom(param: string) {
25. if (param == 'ComA') {
26. ComA()
27. } else if (param == 'ComB') {
28. ComB()
29. } else if (param == 'ComC') {
30. ComC()
31. }
32. }

34. @Builder
35. function buildComA() {
36. ComA()
37. }

39. @Builder
40. function buildComB() {
41. ComB()
42. }

44. @Builder
45. function buildComC() {
46. ComC()
47. }

49. //Encapsulate in container through map
50. let map: Map<string, WrappedBuilder<[]>> = new Map();
51. map.set('ComA', wrapBuilder(buildComA));
52. map.set('ComB', wrapBuilder(buildComB));
53. map.set('ComC', wrapBuilder(buildComC));

55. @Component
56. struct Page12 {
57. @State message: string = 'Hello World';
58. @State arr: string[] = ['ComA', 'ComB', 'ComC'];

60. build() {
61. Column() {
62. ForEach(this.arr, (item: string) => {
63. //Retrieve based on the key during use
64. map.get(item)?.builder()
65. })
66. }
67. .justifyContent(FlexAlign.Center)
68. .width('100%')
69. .height('100%')
70. }
71. }
```

[CanCustomComponentsBeSavedInContainers.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CanCustomComponentsBeSavedInContainers.ets#L21-L92)

**参考链接：**

[@BuilderParam装饰器：引用@Builder函数](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@BuilderParam装饰器：引用@Builder函数/arkts-builderparam.md>)
