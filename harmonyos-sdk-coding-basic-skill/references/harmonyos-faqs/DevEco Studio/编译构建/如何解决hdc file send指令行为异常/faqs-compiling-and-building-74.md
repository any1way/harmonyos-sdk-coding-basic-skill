---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-74
title: 如何解决hdc file send指令行为异常
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决hdc file send指令行为异常
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:02+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:910a631a11c5ebc20fc399cb37460b55d8f29d6df0da8914ad7e7c723ce33ef0
---

**问题现象**

使用hdc file send向手机发送hap包和hsp包，文件被转换为3.4KB的文件夹。执行install命令时提示解析错误。点击DevEco Studio右上角的绿色小三角按钮，当应用构建成功后，在项目根目录下执行hdc file send "./entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/app/entry-default-signed.hap"命令，最终推送到手机上的仍然不是单个hap包。目录结构如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Y77-NpSpQJm3C0SYES7Hsg/zh-cn_image_0000002229758677.png?HW-CC-KV=V1&HW-CC-Date=20260612T024201Z&HW-CC-Expire=86400&HW-CC-Sign=B060485410BA86A10C9CA659573461102C21FC0C9078349018CA80FCFD6A7AD3 "点击放大")

**解决措施**

路径只能使用\\绝对路径，不能使用/相对路径。

绝对路径在DevEco Studio中复制。复制方法：

选中需要发送的文件，右键选择Copy Path/Reference... ->Absolute Path 或者选中文件后按快捷键Ctrl+Shift+C
