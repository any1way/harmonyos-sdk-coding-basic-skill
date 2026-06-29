---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-11
title: Mac安装Python不修改环境变量
breadcrumb: FAQ > DevEco Studio > 应用测试 > Mac安装Python不修改环境变量
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fa396d9acec52ced45737c277b5c20b9415e4833ed6d4b7d002454f23d21277e
---

1. 下载官方Python Mac系统安装包，推荐使用 [3.11.7](https://mirrors.huaweicloud.com/python/3.11.7/python-3.11.7-macos11.pkg)。

2. Mac版本自定义安装可以不修改环境变量，请查看文档：[在 macOS 上使用 Python](https://docs.python.org/zh-cn/3/using/mac.html)不勾选UNIX command-line tools和shell profile updater。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/xjBNEQDvQfKyaH_Pjz3tYg/zh-cn_image_0000002498271829.png?HW-CC-KV=V1&HW-CC-Date=20260612T024543Z&HW-CC-Expire=86400&HW-CC-Sign=A374C8D49BEC53E9B511AFB8293892BD28E3977E0CBFF5177A31C5FE23EBC85D)

3. 关闭DevEco Studio修改other.xml配置 。

```
1. cd ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options
```

```
1. vi other.xml
```

输入： /python，定位到location.python.path这一行, 修改后面的python路径为/Library/Frameworks/Python.framework/Versions/3.11/bin

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uwne5uHxTgGvG8jpoVCYAg/zh-cn_image_0000002465312430.png?HW-CC-KV=V1&HW-CC-Date=20260612T024543Z&HW-CC-Expire=86400&HW-CC-Sign=D81DD35F8D725826106465ED14176D700799260FED84F72A813EE42C82426554)
