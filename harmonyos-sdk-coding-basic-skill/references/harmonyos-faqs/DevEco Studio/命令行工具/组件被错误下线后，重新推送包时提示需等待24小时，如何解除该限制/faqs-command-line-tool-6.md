---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-6
title: 组件被错误下线后，重新推送包时提示需等待24小时，如何解除该限制
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 组件被错误下线后，重新推送包时提示需等待24小时，如何解除该限制
category: harmonyos-faqs
scraped_at: 2026-06-12T10:46:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f7a226a794a18505622a8bec6954b8537e657e22b2202b38e983808b39926f2e
---
**问题描述**

版本上传时发现版本号错误，已下架并修正版本号。重新上传时提示在规定时间内禁止发布。请问能否恢复或告知规定时间是多久？

**解决方案**

修改ohpm-repo里面的配置文件。将重新上架等待小时数修改为如0.00x，然后执行ohpm install并重启ohpm-repo。但使用此方式时，重新上架的版本号需加1，具体可以参考[配置文件](../../../../harmonyos-guides/开发环境搭建/工程创建/模块管理/ohpm-repo私仓搭建工具/配置文件/ide-ohpm-repo-configuration.md)。
