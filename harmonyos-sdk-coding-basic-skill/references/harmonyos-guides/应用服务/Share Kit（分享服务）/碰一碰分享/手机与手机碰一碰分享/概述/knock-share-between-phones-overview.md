---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与手机碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:15:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3977c34861d7be536387bc27aed343cedbcf36745ff46108e02262ad2e62d3c5
---
Share Kit推出碰一碰分享，支持用户通过碰一碰发起跨端分享，可实现传输图片、共享Wi-Fi等。

## 场景介绍

* 宿主应用进入一个可以分享的界面，比如打开或者选中的一个文件、一条备忘录、一个联系人详情，或个人热点/Wi-Fi等。
* 宿主应用可以分享多个内容，如选中的多张图片等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/QegGo931TcmP_eao7UYNpQ/zh-cn_image_0000002592379544.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071520Z&HW-CC-Expire=86400&HW-CC-Sign=2C29F6FA861679CF07DFEC9598B135736C5E81EE078FFE3F18CF655A232F66C1)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/5Wt6NURgTJenqDN7m828Gg/zh-cn_image_0000002622859059.png?HW-CC-KV=V1&HW-CC-Date=20260611T071520Z&HW-CC-Expire=86400&HW-CC-Sign=A41C02B68B9AA4E82DC60B8B181C804CDFA6064002C652DEDB35DB692B8858AE)

流程说明：

1. 宿主应用注册碰一碰分享事件，并与亮屏且解锁的对端设备碰一碰。
2. 宿主应用发现设备，调用碰一碰分享事件回调，在回调事件中构造分享数据并发送。
3. 目标设备接收并处理分享数据。
4. 宿主应用解除注册碰一碰分享事件。

## 使用约束

手机应用发起碰一碰分享时，双端设备需要在**亮屏、且解锁**的状态下并且都已开启华为分享服务（系统默认开启），设备顶部轻碰即可触发。如果用户已手动关闭华为分享服务开关，轻碰事件触发时，用户会接收到系统通知提示开启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/C9xuZROvS3W3yezonC1V3A/zh-cn_image_0000002622699179.png?HW-CC-KV=V1&HW-CC-Date=20260611T071520Z&HW-CC-Expire=86400&HW-CC-Sign=006380C29AFB0C72C0C55C1EF929C021F2CD5F3603EC37C0D41B31D3C2F09C8C)

Share Kit的处理机制：

* 任意一端设备不支持碰一碰能力时，轻碰无任何响应。
* 宿主应用无法获得分享结果，Share Kit会通过系统通知消息告知用户对端接收或拒绝。

## 环境要求

* 支持的手机系统：[HarmonyOS NEXT Release](<../../../../../../harmonyos-releases/历史版本/HarmonyOS 5.0.0(12)/版本概览/overview-500.md#section62333015377>)及以上版本，可使用[canIUse](<../../../../../../harmonyos-references/ArkTS API/SysCap (系统能力)/js-apis-syscap.md#caniuse>)判断系统能力是否支持。

  ```
  1. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
  2. // 支持一碰分享的能力.
  3. }
  ```
* 集成开发环境：[DevEco Studio NEXT Beta1](<../../../../../../harmonyos-releases/历史版本/HarmonyOS 5.0.0(12)/版本概览/overview-500.md#section1457031563711>)及以上版本。
