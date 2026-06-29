---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-185
title: 升级react-native-openharmony编译出错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 升级react-native-openharmony编译出错
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:266e1736882a88a97ec972d9c18ef2e9cd823252542990abccacb819d22063fa
---

**问题现象**

升级react-native-openharmony编译出错，类似如下报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/EZxwAPhyTwOXl6Z5VrTlVw/zh-cn_image_0000002304734606.png?HW-CC-KV=V1&HW-CC-Date=20260612T024336Z&HW-CC-Expire=86400&HW-CC-Sign=6E403C56562E268EA40C8D42294177D7A30D9663467C824EF3A04CBCD5A1463B)

**问题原因**

旧版本的react-native-openharmony缓存还在,导致某些链接找不到。

**解决措施**

删除要编译的模块根目录下的.cxx和build目录,然后重新触发编译。
