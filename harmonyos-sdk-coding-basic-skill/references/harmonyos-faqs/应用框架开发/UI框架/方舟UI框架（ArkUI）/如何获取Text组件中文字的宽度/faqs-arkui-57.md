---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-57
title: 如何获取Text组件中文字的宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取Text组件中文字的宽度
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6b986f781d8ffe9670128064936c1722214c6dad730ed03a22e36036a268f7f2
---
使用@ohos.measure中的measureText()方法计算指定文本单行布局下的宽度。具体可参考如下代码：

```
1. @Entry
2. @Component
3. struct IndexTest {
4. @State textWidth: number = this.getUIContext().getMeasureUtils().measureText({
5. textContent: "Hello World",
6. fontSize: '50px'
7. })

9. build() {
10. Row() {
11. Column() {
12. Text(`The width of 'Hello World': ${this.textWidth}`)
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }
```

[GetTextWidth.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTextWidth.ets#L21-L38)

**参考链接**

[@ohos.measure (文本计算)](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.measure (文本计算)/js-apis-measure.md>)
