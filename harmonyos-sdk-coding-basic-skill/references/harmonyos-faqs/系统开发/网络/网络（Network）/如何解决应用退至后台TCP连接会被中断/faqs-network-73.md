---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-73
title: 如何解决应用退至后台TCP连接会被中断
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决应用退至后台TCP连接会被中断
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2d2452ec999886c99729a4f1f25dba15fc10a130fa10b32459bc7f4ec3f56c60
---
* 应用进入后台会触发系统后台功耗管控策略，创建的所有网络连接在较短时间内都会被杀死。
* [网络资源合理使用](../../../../../best-practices/功耗/应用功耗优化/后台任务低功耗/后台硬件资源合理使用/网络资源合理使用/bpta-reasonable-network-use.md)：无长时任务的应用退到后台主动断开socket连接，包含TCP和UDP连接。
* 应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请[长时任务](<../../../../../harmonyos-guides/应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)，让应用在后台长时间运行。当前长时任务支持的类型，包含数据传输、音视频播放、录制、定位导航、蓝牙相关业务、多设备互联、WLAN相关业务和计算任务。
