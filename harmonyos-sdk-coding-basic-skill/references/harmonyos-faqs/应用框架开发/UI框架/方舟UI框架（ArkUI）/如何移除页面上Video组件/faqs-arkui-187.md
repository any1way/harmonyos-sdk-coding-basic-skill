---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-187
title: 如何移除页面上Video组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何移除页面上Video组件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b31e0da9587c05388e224ed7b8bc80320762a85909c798276fbee864aa1030b1
---
**问题现象**

ForEach刷新UI，数组中的Video组件移除了，但屏幕上还有之前的Video组件占着屏幕。

**解决措施**

采用规避的方式，在移除Video前调用[exitFullscreen()](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Video/ts-media-components-video.md#exitfullscreen)方法退出全屏播放，这样才能正常的移除掉Video组件。

**参考链接**

[Video](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Video/ts-media-components-video.md)
