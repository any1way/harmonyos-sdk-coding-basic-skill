---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-testing-faq-2
title: 设备已连接，为什么设备列表中未显示该设备
breadcrumb: FAQ > DevEco Testing > 常见问题 > 设备已连接，为什么设备列表中未显示该设备
category: harmonyos-faqs
scraped_at: 2026-06-01T17:09:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a41e461a57648b10df27ac5783726fc41e8c777edb39948cedac77abc9ba36c7
---
需满足以下条件，才能使用DevEco Testing识别设备并进行测试。

1. 设备系统版本为HarmonyOS 5.0及以上。
2. PC与本地设备通过USB连接，设备需进入设置-系统-开发者模式，开启开发者模式和USB调试权限。
3. 将DevEco Testing安装目录下的hdc路径配置至系统环境变量中。
4. 在CMD窗口中执行hdc list targets命令，可以识别到设备。

**参考链接**

[开发者选项](../../../../harmonyos-guides/编写与调试应用/应用调试/开发者模式/开发者选项/ide-developer-mode.md)
