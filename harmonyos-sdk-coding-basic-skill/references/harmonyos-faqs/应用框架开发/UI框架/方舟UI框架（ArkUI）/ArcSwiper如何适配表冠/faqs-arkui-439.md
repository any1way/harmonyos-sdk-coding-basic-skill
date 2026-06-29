---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-439
title: ArcSwiper如何适配表冠
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ArcSwiper如何适配表冠
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:08+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:6e2b7c6f7e7cfd65db187b90bd289a479989a7fc961a8db987ed2fd453a926f4
---
可以滑动的组件需要适配旋转表冠，默认支持的组件在获焦时即可响应表冠事件。

1. 默认支持表冠事件的组件: Slider、DatePicker、TextPicker、 TimePicker、Scroll、List、Grid、WaterFlow、ArcList、Refresh和ArcSwiper。

   默认支持组件只需要添加.focusable(true)、 .focusOnTouch(true)、.defaultFocus(true)属性获焦即可响应。
2. 通过onDigitalCrown监听表冠事件。

   示例代码如下：

   ```
   1. import {
   2. ArcSwiper,
   3. ArcSwiperAttribute,
   4. ArcDotIndicator,
   5. ArcDirection,
   6. ArcSwiperController
   7. } from '@kit.ArkUI';

   9. @Entry
   10. @Component
   11. struct ArcSwiperDemo {
   12. @State currentIndex: number = 0;
   13. private swiperController: ArcSwiperController = new ArcSwiperController();

   15. build() {
   16. ArcSwiper(this.swiperController) {
   17. Text('page 1')
   18. .width('100%').height('100%').backgroundColor(Color.Red)
   19. Text('page 2')
   20. .width('100%').height('100%').backgroundColor(Color.Green)
   21. Text('page 3')
   22. .width('100%').height('100%').backgroundColor(Color.Blue)
   23. }
   24. .focusable(true)
   25. .focusOnTouch(true)
   26. .defaultFocus(true)
   27. .onDigitalCrown((event: CrownEvent) => {
   28. if (event.degree > 0) {
   29. this.swiperController.showNext();
   30. } else if (event.degree < 0) {
   31. this.swiperController.showPrevious();
   32. }
   33. })
   34. }
   35. }
   ```

**参考链接**

[表冠事件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/表冠事件/ts-universal-events-crown.md)

[焦点控制](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/焦点控制/ts-universal-attributes-focus.md)

[ArcSwiper示例](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcSwiper/ts-container-arcswiper.md#示例)
