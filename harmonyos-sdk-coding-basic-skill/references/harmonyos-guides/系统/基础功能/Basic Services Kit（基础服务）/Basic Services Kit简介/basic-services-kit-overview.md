---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/basic-services-kit-overview
title: Basic Services Kit简介
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > Basic Services Kit简介
category: harmonyos-guides
scraped_at: 2026-06-01T11:21:39+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:6d1b520ab549be7b15f4bfde4a8f055bd7af24fe4a36492defc6e74de72c0b0e
---
Basic Services Kit（基础服务）作为基础服务套件，为应用开发者提供常用的基础能力。比如常用的剪贴板读写、文件上传下载、文件压缩、文件打印、进程间/线程间通信、设备管理、应用账号管理等能力都由本Kit提供。

## 使用场景

Basic Services Kit为开发者提供了多种基础能力，满足开发者不同场景的开发需求。

典型使用场景举例：

* 剪贴板读写：

  + 本地复制粘贴：比如在A应用中复制一段文字，粘贴到其他应用中。
  + 跨设备复制粘贴：比如在A设备浏览器复制一段文本，粘贴到B设备的备忘录中。
* 文件上传下载：

  + 小文件前台上传下载：发布社交动态（图片、短视频等）、发送文件给好友、保存图片到本地等，通常数据量较小，要给用户即时反馈。
  + 大文件后台上传下载：云盘数据同步、下载电影，通常数据量较大，可后台执行，支持断点续传。
* 进程间/线程间通信：

  + 进程间通信：比如ExtensionAbility发送事件给主进程。
  + 线程间通信：比如worker线程处理完网络请求后将事件传递回UI主线程。

## 能力范围

根据不同使用场景分类，本Kit主要包含如下能力：

* 数据文件处理：

  + [剪贴板](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.pasteboard (剪贴板)/js-apis-pasteboard.md>)：提供内容复制粘贴能力，支持多种数据类型包括文本、HTML数据、URI、PixelMap等。
  + [压缩](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.zlib (Zip模块)/js-apis-zlib.md>)：提供文件压缩解压缩的能力。
  + [打印](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.print (打印)/js-apis-print.md>)：提供基础文件打印的能力，比如传入文件进行打印、设置打印参数等。
  + [上传下载](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.request (上传下载)/js-apis-request.md>)：提供文件上传下载、后台传输代理的基础能力。
  + [划词服务](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md>)：提供划词信息监听、划词窗口管理能力。
* 进程间/线程间通信：

  + [公共事件](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md>)：提供进程间通信的能力，包括订阅、发布、退订公共事件等，相关开发指南请参考[公共事件简介](../进程线程通信/使用公共事件进行进程间通信/公共事件简介/common-event-overview.md)。
  + [Emitter](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.events.emitter (Emitter)/js-apis-emitter.md>)：提供线程内通信的能力，包括订阅、发布、退订自定义事件等，相关开发指南请参考[使用Emitter进行线程间通信](../进程线程通信/使用Emitter进行线程间通信/itc-with-emitter.md)。
* 设备管理：

  + [设备信息](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md>)：提供查询产品信息的能力，比如查询设备类型、设备品牌名称、产品系列、产品版本号等。
  + [设置数据项](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.settings (设置数据项名称)/js-apis-settings.md>)：提供查询系统设置数据项的能力，比如查询是否启用飞行模式、是否启用触摸浏览等。
  + [电量信息查询](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.batteryInfo (电量信息)/js-apis-battery-info.md>)：提供查询电量信息的能力。
  + [系统电源管理](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.power (系统电源管理)/js-apis-power.md>)：提供系统电源管理相关的能力，比如查询屏幕状态能力等。
  + [RunningLock锁操作](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.runningLock (RunningLock锁)/js-apis-runninglock.md>)：提供RunningLock锁相关操作的能力，包括创建、查询、持锁、释放锁等操作。
  + [热管理](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.thermal (热管理)/js-apis-thermal.md>)：提供热管理相关的能力，比如热档位查询等。
  + [USB管理](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.usbManager (USB管理)/js-apis-usbmanager.md>)：提供USB设备管理相关的能力，比如查询USB设备列表、批量数据传输、控制命令传输、权限控制等，相关开发指南请参考[USB服务开发概述](../USB服务/开发USB服务/USB服务开发概述/usbhost-overview.md)。
* 其他：

  + [应用账号管理](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.appAccount (应用账号管理)/js-apis-appaccount.md>)：提供应用账号的期管理以及数据管理的能力，相关开发指南请参考[管理应用账号](../账号管理/应用账号/管理应用账号/manage-application-account.md)。
  + [公共回调](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.base (公共回调信息)/js-apis-base.md>)：定义了HarmonyOS ArkTS接口的公共回调类型，包括接口调用时出现的公共回调和公共错误信息。
  + [时间时区](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.systemDateTime (系统时间、时区)/js-apis-date-time.md>)：提供获取系统时间以及系统时区的能力。

## 与其他kit的关系

* [ArkTS Kit](../../../../应用框架/ArkTS（方舟编程语言）/ArkTS简介/arkts-overview.md)：ArkTS Kit中的[多线程并发(Worker和Taskpool)](../../../../应用框架/ArkTS（方舟编程语言）/ArkTS并发/多线程并发/多线程并发概述/multi-thread-concurrency-overview.md)需要使用本Kit中的Emitter进行线程间通信。
* [Ability Kit](<../../../../应用框架/Ability Kit（程序框架服务）/Ability Kit简介/abilitykit-overview.md>)：Ability Kit中的进程间通信需要使用本Kit中的公共事件。
* [Core File Kit](<../../../../应用框架/Core File Kit（文件基础服务）/Core File Kit简介/core-file-kit-intro.md>)：与Core File Kit的使用场景不同，Core File Kit主要提供访问和管理文件的能力，开发者可以在应用文件访问和文件分享、应用数据备份恢复等场景使用Core File Kit进行开发，而涉及到文件压缩、文件上传下载、文件打印等场景时需要使用本Kit进行开发。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](../../../../编写与调试应用/使用模拟器运行应用/概述/模拟器与真机的差异/ide-emulator-specification.md)”。
