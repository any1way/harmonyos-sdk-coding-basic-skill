---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-faultlog-appkilled
title: 查看App Killed（应用终止）日志
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 查看App Killed（应用终止）日志
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:40+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:7ec32c8a453c41564b9895d7f8ebf4cc46c918f64c7a6dfbb852da0d6f99ae36
---
从DevEco Studio 6.0.2 Beta1版本开始，提供**AppKilled**窗口，用于查看设备上应用终止的相关信息，包括应用异常退出的时间、进程名、是否前台应用、异常退出原因，点击**recordId**可以查看详细的FaultLog信息。支持按设备、应用和异常原因对信息进行过滤。

AppKilled窗口中支持查看的异常退出原因请参考[reason字段说明](../../../../系统/调测调优/调试命令/hidumper/hidumper/hidumper.md#reason字段说明)，如需对问题进行排查处理，请参考[App Killed（应用终止）检测](<../../../../系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/App Killed（应用终止）检测/appkilled-guidelines.md>)。

说明

2in1、Tablet设备不支持查看APP\_INPUT\_BLOCK和THREAD\_BLOCK\_6S类型的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/kiCBqUH4Quurr55VZwNb0w/zh-cn_image_0000002571546872.png?HW-CC-KV=V1&HW-CC-Date=20260611T072939Z&HW-CC-Expire=86400&HW-CC-Sign=788FEF5C7F0B867DA8680E09C7C1B50B49C3A352BCDB1844C7236EC39F9E4723)
