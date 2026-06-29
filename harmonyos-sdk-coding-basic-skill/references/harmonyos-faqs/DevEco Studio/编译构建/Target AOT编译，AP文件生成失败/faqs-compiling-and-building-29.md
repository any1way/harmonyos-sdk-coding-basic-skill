---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-29
title: Target AOT编译，AP文件生成失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > Target AOT编译，AP文件生成失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4af78039b32f0fd87dd734443849f706578e056d09e3f2e564736f261db32b23
---

**问题现象**

Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vRRg6FqwT82B4H6nmELRhw/zh-cn_image_0000002229758617.png?HW-CC-KV=V1&HW-CC-Date=20260612T024118Z&HW-CC-Expire=86400&HW-CC-Sign=C4639863CAF1CB5FF649E1C542CC877CD649FB1773FFF97D1AE7225F02DD639C)

**解决措施**

errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。

```
1. hdc shell
2. setenforce 0
```

以上设置重启将会失效，若设备重启请重新进行以上设置
