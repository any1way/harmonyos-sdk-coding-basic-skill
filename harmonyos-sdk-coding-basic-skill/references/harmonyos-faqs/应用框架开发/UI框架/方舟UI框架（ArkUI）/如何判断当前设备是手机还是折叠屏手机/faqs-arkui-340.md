---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-340
title: 如何判断当前设备是手机还是折叠屏手机
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何判断当前设备是手机还是折叠屏手机
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:17+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:c6375e3d1813454e9f62690044fd7b80a8816d4c5bd48eff993a4a2f1df5d84a
---
* 页面布局类问题：

  页面布局应基于窗口形态（如折叠态/展开态）、宽度和高宽比等动态属性，而非静态设备类型。例如折叠屏设备的折叠态窗口应使用与普通手机相同的布局规则，Mate X5展开态单独设计一套布局。详情可参考[断点](../../../../../best-practices/一次开发，多端部署/多设备界面开发/界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section1532120147301)的使用。
* 非页面布局或功能类问题（例如折叠屏折叠状态切换时重新选择相机重置预览流）：

  手机设备（包括普通手机和折叠屏手机）的[DeviceTypes](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md#devicetypes20>)接口均返回phone，可以通过屏幕属性@ohos.display的[display.isFoldable](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayisfoldable10>)返回是否可折叠。需要注意HUAWEI Pocket 2（纵向折叠屏手机）的isFoldable接口会返回false，需特殊处理。

折叠屏相关的具体开发案例可参考：[折叠屏应用开发](../../../../../best-practices/多端设备体验提升/手机/双折叠应用开发/bpta-foldable-guide.md)。
