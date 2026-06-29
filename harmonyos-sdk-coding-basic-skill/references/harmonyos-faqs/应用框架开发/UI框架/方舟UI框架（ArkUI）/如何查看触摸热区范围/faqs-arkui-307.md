---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-307
title: 如何查看触摸热区范围
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何查看触摸热区范围
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:44+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:6c282585f1d59c1f02693349acab6e159bcfd21fcc971eabc8ce2fa03e2143b1
---
通过自定义方式设置responseRegion属性值并结合日志打印的方式，来明确和验证组件的触摸热区范围。

默认情况下，组件的触摸热区即为其自身的位置和大小，与用户看到的视觉范围一致。当开发者显示调用responseRegion()时，系统会以所绑定的热区范围为准，替代默认的布局区域。

通过为组件绑定包含x、y、width、height参数的responseRegion属性来自定义热区，并在点击回调中打印出具体的坐标与尺寸参数，从而确认热区的生效范围。例如，在下面示例代码中，按钮的触摸热区被设置为宽度50%、高度100%。这意味着只有按钮的左半部分（热区内）响应点击事件，右半部分（热区外）点击无效。

参考代码如下：

```
1. @Entry
2. @Component
3. struct TouchTargetExample {
4. @State text: string = '';
5. @State x: number = 0;
6. @State y: number = 0;
7. @State regWidth: string = '50%';
8. @State regHeight: string = '100%';

10. build() {
11. Column({ space: 20 }) {
12. Text(`{x:0,y:0,width:'50%',height:'100%'}`)
13. // The width of the hot zone is half of the button, and there is no response when clicking on the right side
14. Button('button1')
15. .responseRegion({
16. x: this.x,
17. y: this.y,
18. width: this.regWidth,
19. height: this.regHeight
20. })
21. .onClick(() => {
22. this.text = 'button1 clicked';
23. console.info('button1 clicked: ' + this.x + ' ' + this.y + ' ' + this.regWidth + ' ' + this.regHeight);
24. })

26. Text(this.text)
27. .margin({ top: 10 })
28. }
29. .width('100%')
30. .margin({ top: 100 })
31. }
32. }
```

[ViewRangeOfTouchHotspots.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ViewRangeOfTouchHotspots.ets#L21-L53)

**参考链接**

[responseRegion](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸热区设置/ts-universal-attributes-touch-target.md#responseregion)
