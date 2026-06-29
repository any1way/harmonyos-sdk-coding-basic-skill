---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-111
title: 构建报错“debug is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“debug is different”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:31d878f65c0b9e6e39a27b2ea596c2cc680148ebe362b347fbc172c1b7e5ddf2
---

**问题现象**

打包应用时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_1HP0WdbR0ixZa-P0lWyxw/zh-cn_image_0000002229758605.png?HW-CC-KV=V1&HW-CC-Date=20260612T024228Z&HW-CC-Expire=86400&HW-CC-Sign=D7186874A787EAA4C2BDD1EB8A383C37519A8923285B0A775C941C64E9BBAB58)

**解决措施**

根据报错日志的Warning信息提示的模块名称，检查模块间的debug字段是否一致，重点关注本地模块与外部引用模块。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/F-ohc9FFSbiJ3qhp14jUSw/zh-cn_image_0000002229604117.png?HW-CC-KV=V1&HW-CC-Date=20260612T024228Z&HW-CC-Expire=86400&HW-CC-Sign=B222274CD6330BF9DED392EEB44080C5A767A7D473C724E2D1F04ECB36C32EF1)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ntNq6w3cQrmEanfs3bBuDg/zh-cn_image_0000002194318344.png?HW-CC-KV=V1&HW-CC-Date=20260612T024228Z&HW-CC-Expire=86400&HW-CC-Sign=F1CB5C397F25AE781D19FD31868A1F8CD92A60BC4252A35FCD574738BC3F83D4)
