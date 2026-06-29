---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-28
title: 在应用中如何区分真机和模拟器
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在应用中如何区分真机和模拟器
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8034d0607fe52a4fb83a252c4425f7d31d2bde860735a4a5c48c03d770125fb4
---
**问题现象**

在调试应用代码时，需要判断当前运行的设备是真机还是模拟器，可以通过检查特定的系统属性或环境变量来实现区分。

**解决措施**

在应用中，使用[@ohos.deviceInfo](<../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md>)模块的productModel属性来区分真机和模拟器。模拟器上，productModel的值为emulator。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/PkMOoVOFSmyGkwf0GD2rnw/zh-cn_image_0000002229603717.png?HW-CC-KV=V1&HW-CC-Date=20260612T024422Z&HW-CC-Expire=86400&HW-CC-Sign=88C68DB61C38C877BCCF0F3CE16483BD0E6C332C61BE58944EAE205FF82F1890 "点击放大")
