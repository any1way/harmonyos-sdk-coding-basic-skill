---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-15
title: DevEco Studio中如何设置超长日志自动换行
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio中如何设置超长日志自动换行
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b67032e53a49fe27b1282e03f89ba38a58d19b6b473fef9edfd8d7bcafd600bb
---

启用Soft-Wrap功能以实现日志消息的自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/9qJ6Q2OnTBeus1y_ufHLJw/zh-cn_image_0000002194158840.png?HW-CC-KV=V1&HW-CC-Date=20260612T024015Z&HW-CC-Expire=86400&HW-CC-Sign=96DCDC47F3989B9F39BD7778CCE5AF5F74FE00792F5C3D8BA0B432FFCE6F9AF0 "点击放大")

日志单条打印的最大长度为4096个字符。建议在应用的日志框架中，对日志长度进行判断，若超过该长度则分段打印，以避免日志丢失。
