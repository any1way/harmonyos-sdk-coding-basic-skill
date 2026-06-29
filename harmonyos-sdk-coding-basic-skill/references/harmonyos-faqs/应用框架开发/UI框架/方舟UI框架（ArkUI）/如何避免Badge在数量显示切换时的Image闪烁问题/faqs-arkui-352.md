---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-352
title: 如何避免Badge在数量显示切换时的Image闪烁问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何避免Badge在数量显示切换时的Image闪烁问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:29+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:c17cc63c77992015ce8a4a617470d84b3fbb3ee1673abafdffcdf5d0057f20f7
---

通过@Stage装饰器修饰变量，动态设置badgeSize以控制Badge状态，当值设为0时Badge自动隐藏。

```
1. @Entry
2. @Component
3. struct BadgeDemo {
4. @State message: string = 'Hello World';
5. @State badgeSize: number = 15;

7. build() {
8. Row() {
9. Text(this.message)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. .onClick(() => {
13. // change the Badge size
14. this.badgeSize = this.badgeSize === 0 ? 15 : 0;
15. })
16. Badge({
17. value: '1',
18. position: {
19. x: 40,
20. y: 0
21. },
22. style: {
23. badgeSize: this.badgeSize,
24. badgeColor: Color.Red
25. }
26. }) {
27. Image($r('app.media.startIcon'))
28. .width(50)
29. .height(50)
30. }
31. }
32. .height('100%')
33. }
34. }
```

[BadgeDoesNotFlash.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BadgeDoesNotFlash.ets#L21-L54)
