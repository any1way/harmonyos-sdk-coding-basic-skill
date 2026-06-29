---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-478
title: Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:51+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:9b5391bb5025f0f4bd683c252f3b0839c1757ff8fc3be7e377f71a5576f3fadc
---

**问题描述**

在Tabs刚启动的时候创建四个TabContent ，当this.isShowMessageTab为true会再加一个TabContent，

当前有遇到一个问题，当this.isShowMessageTab从false变到true后（即TabContent从4个变成5个后）。 点击最后一个tabBar后，再点击前面的tabBar就无法响应Tabs下的onChange，用左右滑动可以切换Tabs且触发onChange。

**解决方案**

定义一个selectedIndex变量，在onChange函数中将当前Tabs的index赋值给selectedIndex。此时selectedIndex的值等于当前被选中Tab的索引值。在tabBuilder中，对选中的Tab进行样式的修改即可。

完整示例代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. private currentIndex: number = 0;
5. private controller: TabsController = new TabsController();
6. @State selectedIndex: number = 0;
7. @State change: boolean = false;

9. @Builder
10. tabBuilder(index: number, name: string) {
11. RelativeContainer() {
12. Text(name)
13. .fontColor(this.selectedIndex === index ? '#007DFF' : '#182431')
14. .fontSize(16)
15. .fontWeight(this.selectedIndex === index ? 500 : 400)
16. .height('auto')
17. .padding({
18. left: 8,
19. right: 8,
20. top: 6,
21. bottom: 6
22. })
23. .id('textTitle')
24. .alignRules({
25. middle: { anchor: '__container__', align: HorizontalAlign.Center },
26. center: { anchor: '__container__', align: VerticalAlign.Center }
27. })
28. Divider()
29. .strokeWidth(1)
30. .color('#C3C3C3')
31. .width(100)
32. .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
33. Divider()
34. .strokeWidth(2)
35. .color('#007DFF')
36. .opacity(this.selectedIndex === index ? 1 : 0)
37. .width(100)
38. .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
39. }
40. .width(100)
41. .backgroundColor('#F0F1F3')
42. }

44. build() {
45. RelativeContainer() {
46. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
47. TabContent() {
48. Text('Page One')
49. }
50. .tabBar(this.tabBuilder(0, 'Page One'))
51. .backgroundColor('#ffa2051d')

53. TabContent() {
54. Text('Page Two, Click on Page Three to show or hide')
55. .onClick(() => {
56. this.change = !this.change;
57. })
58. }
59. .tabBar(this.tabBuilder(1, 'Page Two'))
60. .backgroundColor('#ffefd005')

62. if (this.change) {
63. TabContent() {
64. Text('Page Three')
65. }
66. .tabBar(this.tabBuilder(2, 'Page Three'))
67. .backgroundColor('#ff061ef8')

69. TabContent() {
70. Text('Page Four')
71. }
72. .tabBar(this.tabBuilder(3, 'Page Four'))
73. .backgroundColor('#ff039105')

75. TabContent() {
76. Text('Page Five')
77. }
78. .tabBar(this.tabBuilder(4, 'Page Five'))
79. .backgroundColor('#ff02e7c4')
80. }
81. // When the page is hidden, it is necessary to ensure that the first parameter Index of the TabContent page is continuous
82. else {
83. TabContent() {
84. Text('Page Four')
85. }
86. .tabBar(this.tabBuilder(2, 'Page Four'))
87. .backgroundColor('#ff039105')

89. TabContent() {
90. Text('Page Five')
91. }
92. .tabBar(this.tabBuilder(3, 'Page Five'))
93. .backgroundColor('#ff02e7c4')
94. }
95. }
96. .barMode(BarMode.Scrollable)
97. .barBackgroundColor('#fff3f3f3')
98. .onChange((index) => {
99. this.selectedIndex = index;
100. })
101. .animationDuration(400)
102. .scrollable(true)
103. .vertical(false)
104. .width('100%')
105. .fadingEdge(false)
106. }
107. }
108. }
```

[TabsLinkageAbnormal.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsLinkageAbnormal.ets#L21-L129)
