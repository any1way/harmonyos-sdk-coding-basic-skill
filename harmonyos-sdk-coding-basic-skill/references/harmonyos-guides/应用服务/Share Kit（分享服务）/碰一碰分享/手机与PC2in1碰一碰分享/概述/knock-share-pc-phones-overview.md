---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:15:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8526e833c999ae71197e8a09161abfa4c285a7d154b5234e5296d2629f93a51e
---
## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/xSsnkmGQRfyB0LrVsarp-w/zh-cn_image_0000002622859053.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=9F352FFC443A8E83F2B61076B35BEB92CFAE1E3EAE97059E2CCF81DBD5F12908)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nJJcpVJiQQyaUWLalX8sZg/zh-cn_image_0000002592219624.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=02633A97C2A38DAD39D3CFD9699F43125D0387667C19547B1745205A2E6BFC4E)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/rBt9dESEQje1mQ_pPgl1WQ/zh-cn_image_0000002592379558.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=354F7CA4A96666C86EA66EAED252E1C688BF37DF6828FF5FE3FAC7A67587D6B8)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/XD_THWVdR92wKOGdNU0XFg/zh-cn_image_0000002622859067.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=81E39AC7E0B75616C559EBECE7F51E078B2BD93E55C315E5F8A144699235E15D)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kywUDdGXTiKkw48cPRvlqQ/zh-cn_image_0000002622699187.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=18D674F5E78C81CF78FFD31AD96ADA3E07189D8DC8A85234EE35E276858FFC73)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/dc6kB9utQKGBIN3A-_6VQQ/zh-cn_image_0000002592219626.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=3B01F2723D0DB45DB7F9497C4A85A3AC7B3816644E41202F1516922C6E310CCA)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/PKHGJUOnRYee0sycQmag-Q/zh-cn_image_0000002592379560.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=49DD65475F4A86CAE152823ECDDDF148801C73BB8CAAB8CC45015084DC61BB4C)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/J5G6ik9KRH-sftgrNa1N9Q/zh-cn_image_0000002622859069.png?HW-CC-KV=V1&HW-CC-Date=20260611T071524Z&HW-CC-Expire=86400&HW-CC-Sign=B026EA2FBB46A2A1A275BDB2EA09B1BEDDA931F28A1F7FAAFA4D379273238534)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](<../../../../../../harmonyos-releases/HarmonyOS 6.0.0(20)/版本概览/overview-600.md#section1836613212578>)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](<../../../../../../harmonyos-releases/HarmonyOS 6.0.0(20)/版本概览/overview-600.md#section1836613212578>)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](../../手机与手机碰一碰分享/内容分享/knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](../分享内容直达应用界面/knock-share-pc-phones-sandbox.md)
