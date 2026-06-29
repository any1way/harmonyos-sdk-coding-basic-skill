---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-149
title: 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c6a9ce5dc97aa34ca0535fe175f6a8c8fa298bccb866eb993828bba9c2d07242
---

**错误描述**

oh-package.json5文件中的version字段不能包含tag标签。

**可能原因**

使用parameterFile参数化配置版本号时，oh-package.json5文件中的version字段不能包含tag标签。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/k9x5w1drSgirurozzH-1Zg/zh-cn_image_0000002229604173.png?HW-CC-KV=V1&HW-CC-Date=20260612T024309Z&HW-CC-Expire=86400&HW-CC-Sign=2115930238482C8FCFCCAB3412E57618B25903A17573B285EBD2092F61CFA8FF)

**解决措施**

当oh-package.json5文件中的version字段引用parameterFile时，开发者不应使用tag标签。
