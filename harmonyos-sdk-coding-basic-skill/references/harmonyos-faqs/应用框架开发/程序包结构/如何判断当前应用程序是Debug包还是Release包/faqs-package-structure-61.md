---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-61
title: 如何判断当前应用程序是Debug包还是Release包
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何判断当前应用程序是Debug包还是Release包
category: harmonyos-faqs
scraped_at: 2026-06-01T17:04:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a6fdc165f63b771d53b43ba77f4df2d1090cdae765bb50efc7594e39454f2297
---
在编译构建时，Hvigor会生成BuildProfile类，可以通过该类在运行时获取编译构建参数，BuildProfile.BUILD\_MODE\_NAME即为编译模式。编译模式为“debug”表示Debug包，“release”则表示Release包。

**参考链接**

[获取自定义编译参数-能力说明](../../../../harmonyos-guides/构建应用/定制构建/获取自定义编译参数/能力说明/ide-hvigor-get-build-profile-para-guide.md)
