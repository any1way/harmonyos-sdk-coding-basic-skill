---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-112
title: 构建报错“proxy data is duplicated”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“proxy data is duplicated”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e3d5373080ef8fb575cfad5bdad6002e6854adb60cfb283c40aa9eaa124060e
---

**问题现象**

打包APP时，出现“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”的提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/XEW74L5uR_ObrPL4CwgJyA/zh-cn_image_0000002229758777.png?HW-CC-KV=V1&HW-CC-Date=20260612T024230Z&HW-CC-Expire=86400&HW-CC-Sign=5420709866BC6F3E0836D5A96F1B690DC9EBE084932C37B0358EA7F272CBDD97)

**解决措施**

proxyData 标识模块提供的数据代理列表，仅允许 entry 和 feature 配置，不同 proxyData 中配置的 URI 不得重复。遇到此问题，检查模块间是否配置了相同的 URI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/iWcKs1zkTsafs-B2rkVYtw/zh-cn_image_0000002194158904.png?HW-CC-KV=V1&HW-CC-Date=20260612T024230Z&HW-CC-Expire=86400&HW-CC-Sign=099E4D79501317FEA143023FD8DA7BC62926296A3CDCE0F8AB43BF93243EC3E9)
