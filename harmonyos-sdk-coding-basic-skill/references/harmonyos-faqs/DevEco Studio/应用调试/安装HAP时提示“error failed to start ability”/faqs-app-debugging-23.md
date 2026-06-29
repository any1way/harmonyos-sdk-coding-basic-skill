---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-23
title: 安装HAP时提示“error: failed to start ability”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 安装HAP时提示“error: failed to start ability”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f9f3d76fe6738f4f7c7e7edc9051932d96bd35fa2a47e6228e9b5d6212aea24c
---

**问题现象**

启动调试或运行应用/服务时，如果安装HAP出错，提示“error: failed to start ability. error: ability visible false deny request”，请检查应用的可见性设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/CHfcF6u0QQecDlVyuu3-Rg/zh-cn_image_0000002229758621.png?HW-CC-KV=V1&HW-CC-Date=20260612T024442Z&HW-CC-Expire=86400&HW-CC-Sign=DF352D285849D96B88C3F7F0DB8F4066325392C34FFA5516C2FB8501544BA8A2)

**解决措施**

* 在Stage模型工程的module.json5文件中，将abilities字段内的exported设置为true。
* FA模型工程：在config.json文件的abilities字段中，将visible设置为true。
