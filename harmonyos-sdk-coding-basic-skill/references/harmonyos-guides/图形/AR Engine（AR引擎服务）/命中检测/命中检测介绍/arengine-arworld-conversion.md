---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arworld-conversion
title: 命中检测介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 命中检测 > 命中检测介绍
category: harmonyos-guides
scraped_at: 2026-06-11T14:59:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0f2bb448e79fd0d5084a21c569447c636acda172b2f23dbda485a201a4421028
---

AR Engine通过命中检测（Hit Testing）技术，将终端设备屏幕上的兴趣点映射为现实环境中的兴趣点。命中检测以现实环境中的兴趣点为源，发出一条射线连接到摄像头所在位置，返回射线与平面、稀疏点云、Mesh的交点。

用户可以在平面上放置虚拟物体，实现虚拟和现实的融合。

通过命中检测能力，用户可以点击终端设备屏幕，在虚拟世界中放置虚拟物体，用于虚拟家具试用等，实现虚拟与现实世界融合。

**图1** 命中检测示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/aUz_bzvFT4i9oS9TwVC7zw/zh-cn_image_0000002592378986.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T065918Z&HW-CC-Expire=86400&HW-CC-Sign=91B057DE57D29DE448CFDBF35A98A62DE08651FA0262CCE6A4CB6D8C06D2182A)
