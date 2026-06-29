---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-10
title: 关于BuildProfile自定义字段编译时报错：Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
breadcrumb: FAQ > DevEco Studio > 代码编辑 > 关于BuildProfile自定义字段编译时报错：Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
category: harmonyos-faqs
scraped_at: 2026-06-01T17:05:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8d89ec46308e49e34ea5fee3639bcd28475d4b9966c98217aa80aa19c282e096
---
**问题描述**

项目编译时，关于 BuildProfile 的自定义字段报错如下：

```
1. Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
```

**解决措施**

获取构建参数并生成BuildProfile类文件后，在HSP中可以通过以下方式引入该文件：

```
1. import BuildProfile from '${packageName}/BuildProfile';
```

可参考[在代码中获取构建参数](../../../../harmonyos-guides/构建应用/定制构建/获取自定义编译参数/能力说明/ide-hvigor-get-build-profile-para-guide.md#section195881502412)。
