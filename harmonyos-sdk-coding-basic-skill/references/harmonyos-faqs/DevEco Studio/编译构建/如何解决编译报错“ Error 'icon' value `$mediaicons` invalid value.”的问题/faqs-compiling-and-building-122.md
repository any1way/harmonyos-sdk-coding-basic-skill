---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-122
title: 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:79ae4baf7c1221d47e64ddf70512003709364f93ffa9db74d4a83a5d7ebe4491
---

**问题现象**

编译报错。

```
1. ERROR: Failed :entry:default@CompileResource...
2. ERROR: Tools execution failed.
3. Error: ref `$media:icons` don't be defined.
4. Error: 'icon' value `$media:icons` invalid value.
5. at D:\project\process_profile\default\module.json
6. Detail: Please check the message from tools.
```

**报错原因**

引用的资源不存在时，编译错误指向build目录中的文件路径。

**常见场景**

1. 资源文件未添加。
2. 资源文件被意外删除。

**解决方案**

根据报错的资源ID全局搜索，使用右上角的查找按钮，确认报错的资源是否存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/xoUhSkR4T5SNau4bTd0Q_Q/zh-cn_image_0000002262335589.png?HW-CC-KV=V1&HW-CC-Date=20260612T024242Z&HW-CC-Expire=86400&HW-CC-Sign=29EBFE1EC4FC63CB1987152BD72AF6345A66259289E121ED0041CCDC1536F511 "点击放大")
