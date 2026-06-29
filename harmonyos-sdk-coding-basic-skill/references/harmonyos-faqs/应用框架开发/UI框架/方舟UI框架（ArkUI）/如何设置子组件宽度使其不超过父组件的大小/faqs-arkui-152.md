---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-152
title: 如何设置子组件宽度使其不超过父组件的大小
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置子组件宽度使其不超过父组件的大小
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b1d08a20c9b789e4f0dd13f84379bb6810186d18738912482d2ae06dcda2c0f3
---
使用calc()函数计算并动态设置子组件宽度。参考代码如下：

```
1. @Entry
2. @Component
3. struct SizeExample {
4. @State flag:boolean = true;

6. build() {
7. Row() {
8. Text(this.flag ? 'Followed by' : 'Not following')
9. .fontSize(20)
10. .fontWeight(FontWeight.Bold)
11. .backgroundColor(0xFFFAF0)
12. .textAlign(TextAlign.Center)
13. .margin(10)
14. .size({ width: this.flag ? 60 : 80 })
15. .onClick(()=>{
16. this.flag = !this.flag
17. })
18. Text('HarmonyOS Developer Community')
19. .fontSize(20)
20. .fontWeight(FontWeight.Bold)
21. .backgroundColor(0xFFFAF0)
22. .size({width: this.flag ? 'calc(100% - 60vp)' : 'calc(100% - 80vp)'})
23. }
24. .width(500)
25. .margin({ top: 5 })
26. }
27. }
```

[WidthNotExceedingTheParentComponent.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/WidthNotExceedingTheParentComponent.ets#L21-L47)

**参考链接**

[尺寸设置](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md)
