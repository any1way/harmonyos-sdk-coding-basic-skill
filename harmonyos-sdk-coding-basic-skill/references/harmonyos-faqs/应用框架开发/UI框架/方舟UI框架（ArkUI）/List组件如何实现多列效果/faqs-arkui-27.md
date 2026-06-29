---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-27
title: List组件如何实现多列效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > List组件如何实现多列效果
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0cfff7fd75747fe8bc728f253e6913bd1568d3230a2dcd403b98d1eb2a7b5fbf
---
设置[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)组件的lanes属性，以实现交叉轴上的多列布局。示例代码如下：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListExample {
5. @State arr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

7. build() {
8. Column() {
9. List() {
10. ForEach(this.arr, (item: string) => {
11. ListItem() {
12. Row() {
13. Text(item)
14. .fontColor(Color.Red)
15. .fontSize(40)
16. }
17. }
18. .width('100%')
19. .border({
20. width: 1,
21. color: Color.Black,
22. radius: 5
23. })
24. })
25. }
26. .lanes(3)
27. .alignListItem(ListItemAlign.Center)
28. }
29. .padding({ top: 30 })
30. }
31. }
```

[ListImplementsMultiColumnEffect.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListImplementsMultiColumnEffect.ets#L21-L51)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QmKWWD9GSBeMHlF9XHz8yw/zh-cn_image_0000002194158740.png?HW-CC-KV=V1&HW-CC-Date=20260612T022627Z&HW-CC-Expire=86400&HW-CC-Sign=F0D759B0B3AC417F3C26359184DF4E8B5708A79D79FAEEF54BEBECC9872AEBD4 "点击放大")
