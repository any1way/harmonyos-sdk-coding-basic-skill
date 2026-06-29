---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-37
title: 如何解决单个设备连接设备管理器多出三个设备并无法识别的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决单个设备连接设备管理器多出三个设备并无法识别的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:298e4ba7f1e323b9a0479aefb7fc7b7a6c741f7b5bd734ce9519f0246b44f273
---
**问题现象**

单个设备连接设备管理器时，会多出3个无法识别的设备。

**原因**

驱动程序不兼容或损坏。

**解决措施**

1. 参考解决[设备无法识别问题](<../../../../DevEco Studio/应用调试/真机设备连接后，执行“hdc list targets”命令结果为“[Empty]”/faqs-performance-analysis-kit-32.md>)的重装驱动方法，使用Zadig安装WinUSB设备。
