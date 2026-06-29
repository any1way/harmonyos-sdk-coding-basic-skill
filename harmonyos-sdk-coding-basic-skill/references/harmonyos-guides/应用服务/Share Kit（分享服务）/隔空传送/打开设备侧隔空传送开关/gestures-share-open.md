---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gestures-share-open
title: 打开设备侧隔空传送开关
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 隔空传送 > 打开设备侧隔空传送开关
category: harmonyos-guides
scraped_at: 2026-06-11T15:15:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f3a53ffceb26b8fdf7de9c8c14291604cefc9c669aa4c13dd87072767af040b
---

使用隔空传送功能前，需要先打开隔空传送开关。

开启路径：设置 > 系统 > 快捷启动和手势 > 隔空传送。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/OWaEJAj7TmefszYzuU0FQw/zh-cn_image_0000002592379562.png?HW-CC-KV=V1&HW-CC-Date=20260611T071531Z&HW-CC-Expire=86400&HW-CC-Sign=C50733F0F93C5D5C1263DA54E3EEDD1698260E054AB8CA2AC00D60BAA6D6F2EE)

## 隔空传送与隔空截屏的联动

隔空传送与隔空截屏使用相同的手势触发，开关是否开启影响如下：

| 隔空传送开启 | 隔空传送关闭 |
| --- | --- |
| 隔空截屏开启：图库场景传输原图；其他场景传送截屏。  隔空截屏关闭：图库场景传送原图；其他场景无截屏，不传送。 | 隔空截屏开启：仅截屏，不传送。  隔空截屏关闭：无截屏，不传送。 |

当隔空传送和隔空截屏开关同时开启，且当前界面已注册隔空传送事件时，用户抓取握拳会同时触发隔空传送和隔空截屏，此时隔空传送的卡片下方同步出现保存截屏的提示（首次默认不保存）。

用户可手动勾选“保存截屏至本机”，则传送的同时截屏图片会被保存至图库。系统会记录本次选择结果，并作为下次操作的默认值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/wDFgrDULScW_KFIp_9uSrw/zh-cn_image_0000002622859071.png?HW-CC-KV=V1&HW-CC-Date=20260611T071531Z&HW-CC-Expire=86400&HW-CC-Sign=23437FF0D23AF3FFCFE850D4D78920AF3558830AD96E621CEEF342045F12C73B)
