---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-110
title: 构建报错“input module releaseType is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“input module releaseType is different”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9c2519c955e8baf8188ccbb5da45d0b4c243458e59d9be1992472182c98ae916
---

**问题现象**

在打包APP时，如果提示“input module releaseType is different”，请检查输入模块的发布类型是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/0u1AyTXyRt-YtAXuAO3OXQ/zh-cn_image_0000002194318432.png?HW-CC-KV=V1&HW-CC-Date=20260612T024228Z&HW-CC-Expire=86400&HW-CC-Sign=D87F3D9F9D82A840382F9BDA951DA30C4497D113A842DC3AB079E33B0F933081)

**解决措施**

根据报错日志中的Warning信息提示的模块名称，检查模块间的apiReleaseType字段是否一致。

apiReleaseType字段由编译构建工具自动生成并保存在HAP/HSP包的module.json文件中。请确认各模块间该字段是否一致。如果存在不一致，需使用相同版本的SDK重新打包应用的各个模块，然后重新打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/U4pcVyjNSMuiqjaRfi9nNw/zh-cn_image_0000002229604205.png?HW-CC-KV=V1&HW-CC-Date=20260612T024228Z&HW-CC-Expire=86400&HW-CC-Sign=B3E9162FD5634AEE55B7A4166E68F52E938F0ACBD3C8D8DF7778B16206B0F4C9)
