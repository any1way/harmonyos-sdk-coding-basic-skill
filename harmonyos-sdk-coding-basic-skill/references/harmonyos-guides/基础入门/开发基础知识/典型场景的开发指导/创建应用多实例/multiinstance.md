---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multiinstance
title: 创建应用多实例
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用多实例
category: harmonyos-guides
scraped_at: 2026-06-01T10:56:51+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:a07e4474a888e30a8bebc63a6dc2ea9b3d1dea33e6e1379ed7179177d72156d9
---
应用多实例允许一个应用同时运行多个进程，实现多个账号同时登录使用，且互不影响。主要应用场景包括社交账户多开和游戏大小号多开等，无需切换账号从而避免频繁登录的繁琐操作。

桌面上的多个应用实例都是独立的进程，各个进程的运行、通知等都是彼此独立的；各实例共享数据，可通过账号进行切换。

应用多实例间的关系：

* 多实例的应用图标相同。
* 各实例共享[应用文件目录](<../../../../应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md#应用文件目录与应用文件路径>)下的文件数据。
* 可通过账号进行切换，单个实例可以切换不同的账号登录。

## 约束限制

应用多实例仅支持2in1设备。

## 应用多实例的开发步骤

1. 应用多实例的配置方法。

   在工程项目中对App/app.json5配置文件配置[multiAppMode](../../应用配置文件（Stage模型）/app.json5配置文件/app-configuration-file.md#multiappmode标签)字段。具体配置如下：

   ```
   1. {
   2. "app": {
   3. // ...
   4. "multiAppMode": {
   5. "multiAppModeType": "multiInstance",
   6. "maxCount": 5
   7. }
   8. }
   9. }
   ```

   [app.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/bmsSample/Multiinstance/AppScope/app.json5#L16-L33)
2. 创建应用多实例。

* 将已配置好的工程编译打包安装到设备上。
* 首次右击桌面应用图标启动一个应用进程，然后再次右击该应用图标，选择“打开”。此时桌面上会显示同一个应用的两个进程页面。
