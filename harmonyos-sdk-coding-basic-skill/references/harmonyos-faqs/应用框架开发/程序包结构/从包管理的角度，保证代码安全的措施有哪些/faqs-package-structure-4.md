---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-4
title: 从包管理的角度，保证代码安全的措施有哪些
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 从包管理的角度，保证代码安全的措施有哪些
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:138fde6f7329150fdfd20702310d4daa936952b0036a1ecac0d9e95edf76cb88
---
* 编译：编译时，HAR和HSP支持代码混淆。
* 打包：打包时为每个HSP/HAP单独签名，签名后的应用才允许安装。
* 安装：终端设备上的应用市场用于安装和卸载应用，不支持其他安装方式。
* 运行时：提供应用沙箱机制，这是一种以安全防护为目的的隔离机制，防止数据遭受恶意路径穿越访问。

**参考链接**

[混淆加固](../../../../harmonyos-guides/构建应用/混淆加固/ide-build-obfuscation.md)，[Stage模型应用程序包结构](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包结构/Stage模型应用程序包结构/application-package-structure-stage.md)，[应用安装卸载与更新开发指导](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包安装卸载与更新/应用安装卸载与更新开发指导/application-package-install-uninstall.md)，[应用沙箱目录](<../../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md>)
