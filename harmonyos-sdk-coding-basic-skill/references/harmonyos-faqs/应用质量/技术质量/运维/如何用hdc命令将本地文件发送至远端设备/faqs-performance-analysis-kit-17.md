---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-17
title: 如何用hdc命令将本地文件发送至远端设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何用hdc命令将本地文件发送至远端设备
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:806055a13ec44497080d097668a9a55a19d743e6ef89a106389dd603e10376e0
---
从本地向远端设备发送文件，命令格式如下：

```
1. hdc file send local remote
```

local 表示本地待发送的文件路径，remote 表示远程待接收的文件路径。

使用方法：

```
1. hdc file send E:\example.txt /data/local/tmp/example.txt
```

**参考链接**

[hdc-文件相关命令](../../../../../harmonyos-guides/系统/调测调优/调试命令/hdc/hdc.md#文件传输)
