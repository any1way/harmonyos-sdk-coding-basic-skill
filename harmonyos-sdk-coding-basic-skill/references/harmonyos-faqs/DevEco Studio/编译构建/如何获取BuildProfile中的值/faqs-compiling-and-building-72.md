---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-72
title: 如何获取BuildProfile中的值
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何获取BuildProfile中的值
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:66db2de0c0899658363bfc341eb4e0d8ea488c2457322a650cbf06d7c17ba8cc
---
生成 BuildProfile 文件后，可以通过相对路径在代码中引入该文件。例如，在 HAR 模块的 Index.ets 文件中使用该文件：

```
1. import BuildProfile from './BuildProfile';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library/Index.ets#L3-L4)

获取 BuildProfile 类中的值：

```
1. const HAR_VERSION: string = BuildProfile.HAR_VERSION;
2. const BUILD_MODE_NAME: string = BuildProfile.BUILD_MODE_NAME;
3. const DEBUG: boolean = BuildProfile.DEBUG;
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library/Index.ets#L8-L11)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/lMnA4U00TT6aKwxjNSJNxA/zh-cn_image_0000002229604169.png?HW-CC-KV=V1&HW-CC-Date=20260612T024159Z&HW-CC-Expire=86400&HW-CC-Sign=8818914469EC04127A86C5FF75036A0947595D56568292595F7BAB678663EC7C "点击放大")

**参考链接**

[HAR运行时获取编译构建参数](../../../../harmonyos-guides/构建应用/定制构建/获取自定义编译参数/能力说明/ide-hvigor-get-build-profile-para-guide.md#section68146594553)
