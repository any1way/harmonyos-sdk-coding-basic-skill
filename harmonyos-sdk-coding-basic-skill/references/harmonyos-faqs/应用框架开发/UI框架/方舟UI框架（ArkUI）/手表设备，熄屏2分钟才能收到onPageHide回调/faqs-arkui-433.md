---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-433
title: 手表设备，熄屏2分钟才能收到onPageHide回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 手表设备，熄屏2分钟才能收到onPageHide回调
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:03+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:1f32129f482cb77e57186b9f6b2e7edd125c50a678e4a617cb8c715c0b04d8bc
---
**问题描述**

手表设备在系统熄屏后未收到onPageHide回调，屏亮时未收到onPageShow回调。

**解决措施**

在穿戴设备上，因穿戴设备为节省功耗采用延迟回调机制，应用熄屏后需等待两分钟才会收到窗口熄屏的回调，该行为是穿戴设备窗口的默认机制，开发者可以参考[@ohos.power (系统电源管理)](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.power (系统电源管理)/js-apis-power.md>)文档，检测当前设备是否处于活动状态。
