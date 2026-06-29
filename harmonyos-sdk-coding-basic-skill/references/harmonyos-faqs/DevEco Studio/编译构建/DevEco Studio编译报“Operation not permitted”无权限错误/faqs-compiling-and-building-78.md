---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-78
title: DevEco Studio编译报“Operation not permitted”无权限错误
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio编译报“Operation not permitted”无权限错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d9a7c8c136c4d4675e1f25df04a35c7a65f2fd89ffe6c8eeb8e26e7373b70136
---

**问题描述**

DevEco Studio安装完成后一直报Operation not permitted无权限，具体报错如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/7ZNefrMpSNu0YA6Q6OXOhQ/zh-cn_image_0000002194158416.png?HW-CC-KV=V1&HW-CC-Date=20260612T024204Z&HW-CC-Expire=86400&HW-CC-Sign=76E369240F08622E9C7BC365278E414FB545E5B43F7E139C6B8F37E79E8EFB99)

**解决方案**

通过以下命令查看是否有com.example.myapplication标识

xattr -l /path/to/es2abc

用以下命令删除该标识

xattr -d com.example.myapplication/path/to/es2abc

根因：mac系统对文件访问有限制
