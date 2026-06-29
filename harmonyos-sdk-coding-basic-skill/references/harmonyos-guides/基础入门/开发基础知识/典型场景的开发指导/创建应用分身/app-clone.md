---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-06-12T11:54:05+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1f9197363eebc32895308e1a9ce6b3433c474e36e22e7726c6baba20cea136f1
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/t5YB1-rMRTqTm8te3i-rJA/zh-cn_image_0000002622857293.png?HW-CC-KV=V1&HW-CC-Date=20260612T035404Z&HW-CC-Expire=86400&HW-CC-Sign=32BE8EE013CD5D18B6423BBDC151457C883216D9FEDD532E269637684CF06927)

## 约束与限制

输入法应用配置分身无效，无法创建应用分身。

## 应用分身的开发步骤

1. 配置应用分身的方法。

   在工程项目中对AppScope/app.json5配置文件配置[multiAppMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#multiappmode标签)字段。具体配置如下：

   ```
   1. {
   2. "app": {
   3. // ...
   4. "multiAppMode": {
   5. "multiAppModeType": "appClone",
   6. "maxCount": 2
   7. }
   8. }
   9. }
   ```

   [app.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/bmsSample/AppClone/AppScope/app.json5#L16-L33)
2. 创建分身应用。

   * 首先将已配置好的工程编译打包安装到设备上。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/v8C_I3ZeSPuqDYgWrU1qpw/zh-cn_image_0000002622697415.png?HW-CC-KV=V1&HW-CC-Date=20260612T035404Z&HW-CC-Expire=86400&HW-CC-Sign=139AE05F4EF8340928F75E7D9F7C991309BD958A73B14FE7B567922EEFA9F969)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/X3JhjWwoRw2GcfEyGogITA/zh-cn_image_0000002592217854.png?HW-CC-KV=V1&HW-CC-Date=20260612T035404Z&HW-CC-Expire=86400&HW-CC-Sign=E27D0FAC68B2996A46B87BC095739C39F2DBAE226ADB56347D45B1A95A373769)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/yCLrUH1mSEqlFb-LBVihxA/zh-cn_image_0000002592377788.png?HW-CC-KV=V1&HW-CC-Date=20260612T035404Z&HW-CC-Expire=86400&HW-CC-Sign=77A57363365277675C01A3ED2461C5319916877B95D3F62CEAEDBC6C4971A965)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/DRLSh8ZiQfeAAGz4MQ_jeg/zh-cn_image_0000002622857293.png?HW-CC-KV=V1&HW-CC-Date=20260612T035404Z&HW-CC-Expire=86400&HW-CC-Sign=95339B9520E10DF3CC34A772DBB20ADD1034F4EF5569B2513179BE64E98ECB37)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
