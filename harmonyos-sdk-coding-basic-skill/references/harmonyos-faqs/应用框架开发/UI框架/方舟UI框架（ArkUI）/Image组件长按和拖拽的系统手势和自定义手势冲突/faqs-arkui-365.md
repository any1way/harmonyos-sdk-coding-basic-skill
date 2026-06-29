---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-365
title: Image组件长按和拖拽的系统手势和自定义手势冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Image组件长按和拖拽的系统手势和自定义手势冲突
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9995496558503176002b5870535784d40f3dc62e779bc98ea4973c6ef8f5897a
---
开发者可根据业务逻辑，使用parallelGesture或者priorityGesture绑定，解决自定义手势与系统手势之间的冲突。

系统默认手势效果保留，自定义的LongPressGesture和panGesture手势也能响应，使用parallelGesture绑定。

**参考代码****：**

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Image($r('app.media.app_icon'))
7. .width('80%')
8. .parallelGesture(GestureGroup(GestureMode.Exclusive,
9. TapGesture({ count: 2, fingers: 1 })
10. // Double click
11. .onAction(() => {
12. console.log('TapGesture--double click');
13. }),
14. TapGesture({ count: 1, fingers: 1 })
15. // TapGesture single
16. .onAction(() => {
17. console.log('TapGesture--single click');
18. }),
19. LongPressGesture({ repeat: true })
20. // LongPressGesture Long
21. .onAction(() => {
22. console.log('LongPressGesture--Long press');
23. }),
24. PanGesture()
25. // PanGesture drag
26. .onActionStart((gestureEvent: GestureEvent | undefined) => {
27. console.info('PanGesture--drag');
28. })
29. ))
30. }
31. .height('100%')
32. .width('100%')
33. }
34. }
```

[ImageComponentGestureConflict.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageComponentGestureConflict.ets#L21-L55)

**参考链接**

[绑定手势方法](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/添加手势响应/绑定手势方法/arkts-gesture-events-binding.md>)
