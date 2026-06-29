---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-81
title: 如何通过构建参数传入签名信息
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何通过构建参数传入签名信息
category: harmonyos-faqs
scraped_at: 2026-06-01T17:06:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8a61973d449192fcc3f12bc792e0c58dc7808f6f24525ccb6b6c27d9c0d59261
---
如何通过构建参数传入签名信息，可参考：[准备申请签名所需文件](../../../../harmonyos-guides/命令行工具/搭建流水线/ide-command-line-building-app.md#section6103553181714)。

流水线构建应用可以通过构建命令行传入签名参数，并在自定义构建任务时获取命令行构建参数，但不支持通过自定义任务更改签名的配置。 在编译时进行签名目前可以采取自定义任务的实现方式，在编译打包时插入一个自定义签名任务调用签名工具进行签名，同时屏蔽掉原有的签名流程，可参考：[API使用示例](../../../../harmonyos-guides/构建应用/扩展构建能力/扩展构建API/API使用示例/ide-build-expanding-sample.md)。
