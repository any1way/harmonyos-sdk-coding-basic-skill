---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-416
title: Watch开发，ArcSwiper实现右滑退出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Watch开发，ArcSwiper实现右滑退出
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:95f70ca0bd64be4786d294e8ac28af5386c3be7b608929123361474a71696572
---
通过[onGestureRecognizerJudgeBegin()](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/手势控制/手势拦截增强/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)函数识别滑动位置，该函数通过比较触摸起始坐标与移动坐标的差值来判断滑动方向，示例代码参考：[示例](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcSwiper/ts-container-arcswiper.md#示例)。
