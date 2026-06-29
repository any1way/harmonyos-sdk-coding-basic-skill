---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-103
title: 编译通过，但是安装时失败报错“Error while Deploy Hap”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译通过，但是安装时失败报错“Error while Deploy Hap”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5937b2175de6c7e87a85d8be2e7533bff80479e971bf90181991f7bcb50eccda
---

**问题描述**

在工程内打包的har包，编译通过，但在安装时失败。

```
1. 04/10 14:01:54: Install Failed: error: failed to install bundle.
2. code:9568278
3. error: install version code not same.
4. $ hdc shell rm -rf data/local/tmp/f47e1222b8c64dbe92f86bc3b55cc3d2
5. Error while Deploy Hap
```

**可能原因**

该报错是由于需要安装的应用与系统已安装的应用中，app.json文件的versionCode字段不一致。

**解决措施**

方案一：开发者可能使用了DevEco Studio的debug按钮安装了该应用。之后，通过打包并使用hdc install命令安装。可以使用命令查看已安装应用的debug字段信息。

```
1. bm dump -n 应用bundleName | grep debug
```

普通应用的卸载与安装：

```
1. >hdc uninstall 应用bundleName
```

清空应用数据：

```
1. hdc shell bm clean -d -n 应用bundleName
```

方案二：保存的数据应用版本与新安装的版本不一致可能导致问题。解决方法：进入“Run”>“Edit Configurations”>“Run/Debug Configuration”，取消选中“Keep Application Data”选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/r67xPpqnTICTDkbgshKklw/zh-cn_image_0000002194159004.png?HW-CC-KV=V1&HW-CC-Date=20260612T024220Z&HW-CC-Expire=86400&HW-CC-Sign=D985C204B8219BF47299CFF799AE93A87A4040C4E265AE6E8DC3A20394539318)
