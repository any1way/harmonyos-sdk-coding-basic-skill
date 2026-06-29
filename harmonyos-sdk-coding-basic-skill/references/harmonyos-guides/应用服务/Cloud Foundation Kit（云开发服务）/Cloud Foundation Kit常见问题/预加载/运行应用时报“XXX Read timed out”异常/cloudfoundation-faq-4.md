---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-4
title: 运行应用时报“XXX Read timed out”异常
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时报“XXX Read timed out”异常
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:be4463c5d2e273506d6060bff127dbbea5193d7e9a4fff958e9eddfb10e3523e
---

**问题现象**

运行应用时报“XXX Read timed out”异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/uSP-q6dVR0K--cQteN6kzQ/zh-cn_image_0000002622698879.png?HW-CC-KV=V1&HW-CC-Date=20260611T070621Z&HW-CC-Expire=86400&HW-CC-Sign=438ED6DE9C5A9CFF6072A3CC50C7EE99747352890E5CBEBBAA012A53C8816CAF)

**解决措施**

出现此错误，是因为云侧没有启动云函数实例，卸载应用重新安装即可。
