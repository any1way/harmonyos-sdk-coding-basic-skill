---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-shortcut-settings
title: 应用内通知设置快捷入口开发指导
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 应用内通知设置快捷入口开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T15:11:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:26630b854ab375681e9f325a72fcf4aac1d8c2366a21b5084b84791a906e47a7
---
## 使用场景

应用的通知设置页面属于3层页面，用户查找难度较大，导致应用的通知关闭率上升。

为改善这一情况，我们在通知消息的左滑菜单和系统的应用通知设置页面中，添加了快速进入应用内通知设置功能页面的入口，直接引导用户跳转至应用内的通知分类管理页面，提升用户通知管理的体验，降低应用通知关闭率。

“设置 > 通知和状态栏 > XX应用”页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/7WBuLnZfTGOzwGe8a4dTpg/zh-cn_image_0000002622699065.png?HW-CC-KV=V1&HW-CC-Date=20260611T071116Z&HW-CC-Expire=86400&HW-CC-Sign=57A44F99D01D6810581E4154660406BD7EA3F5F04B2B6FAA6D2128CF1FC5DA47)

通知中心页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/2Xgp363lQA6JpIdnr6ijyg/zh-cn_image_0000002592219504.png?HW-CC-KV=V1&HW-CC-Date=20260611T071116Z&HW-CC-Expire=86400&HW-CC-Sign=6D6D446923D04A308866498308772F4CBE83D8C5CD77A96469C36969AE32238D)

## 开发准备

详情请参考[应用链接说明](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/应用链接说明/app-uri-config.md>)，其中[linkFeature](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/应用链接说明/app-uri-config.md#linkfeature标签说明>)使用AppNotificationMgmt即可。

## 功能验证

* 场景1

  1. 在手机的“设置 > 通知和状态栏”页面，选择当前应用，进入应用详情页。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
* 场景2

  1. 在手机通知中心页面，左滑应用已发布的通知。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
