---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-215
title: 如何动态控制键盘绑定在不同的TextInput上
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何动态控制键盘绑定在不同的TextInput上
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d1f57cf2f027b79d28268c1fd345fa9952155c95a4f7dfa3779244028295029f
---
软键盘的收起和弹出与输入框的获焦和失焦相关。可以通过 focusControl 动态控制输入框焦点的转移，从而控制软键盘的显示和隐藏。将焦点转移到目标输入框可以实现键盘的动态切换。参考代码如下：

```
1. @Entry
2. @Component
3. struct DynamicControlKeyboard {
4. // Whether focus is on "key1" TextInput
5. private flag: boolean = true;
6. @Builder
7. customKeyboardBuilder() {
8. Row() {
9. Text('Customize keyboard')
10. }
11. .justifyContent(FlexAlign.Center)
12. .width('1260px')
13. .height('1161px')
14. .backgroundColor(Color.Brown)
15. }
16. build() {
17. Column({space: 10}) {
18. TextInput()
19. .key('key1')
20. .onAppear(() => {
21. focusControl.requestFocus('key1');
22. })
23. .defaultFocus(true)
24. TextInput()
25. .key('key2')
26. .customKeyboard(this.customKeyboardBuilder())
27. Button('Switch TextInput')
28. .onClick(() => {
29. if (this.flag) {
30. console.info('TextInput2 ==> ' + focusControl.requestFocus('key2'));
31. } else {
32. console.info('TextInput1 ==> ' + focusControl.requestFocus('key1'));
33. }
34. this.flag = !this.flag;
35. })
36. Button()
37. .width(0)
38. .height(0)
39. .key('key3')
40. }
41. .padding({ top: 20 })
42. .width('100%')
43. .height('100%')
44. .onClick(() => {
45. focusControl.requestFocus('key3');
46. })
47. }
48. }
```

[DynamicallyControlKeyboardBinding.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DynamicallyControlKeyboardBinding.ets#L21-L68)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cd8fCwixQDqzsZkr6H7nEg/zh-cn_image_0000002426207326.png?HW-CC-KV=V1&HW-CC-Date=20260612T022914Z&HW-CC-Expire=86400&HW-CC-Sign=78B25FB12FB97851BC2B9FAC3913CA7CF5B29C5DC34F23ED5DC5DA6550E500FD)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/s7A__2nwToqfxOddEt5Jrg/zh-cn_image_0000002426218940.png?HW-CC-KV=V1&HW-CC-Date=20260612T022914Z&HW-CC-Expire=86400&HW-CC-Sign=C54DCCDD19127BF6254962B3B2609927EB46263DC6E2885CB3840B4FF495F8DD)

**参考链接**

[focusControl](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/焦点控制/ts-universal-attributes-focus.md#focuscontrol9)
