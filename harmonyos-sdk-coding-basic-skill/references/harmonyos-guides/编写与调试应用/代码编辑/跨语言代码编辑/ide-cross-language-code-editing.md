---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1fb1aa72f06cda40948a71969e60ae95119a43c02e4480fec724c9a077a7ace2
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/BgVXDEacTLKlinuLqpw4CA/zh-cn_image_0000002571387086.png?HW-CC-KV=V1&HW-CC-Date=20260611T072805Z&HW-CC-Expire=86400&HW-CC-Sign=FF12EB8A2D77461CF6E4DF6B685D4984755653C36145A187CC2897DC02E9DD0D "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/nw7x5t3-T3OegBL7XkCCrg/zh-cn_image_0000002602066203.png?HW-CC-KV=V1&HW-CC-Date=20260611T072805Z&HW-CC-Expire=86400&HW-CC-Sign=85671A3BC6D0842A958C79BC199308846745859903F62BD5764DC966E3C964F9)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Pyy6b9OlTWy8YZmXptTqWA/zh-cn_image_0000002571546724.png?HW-CC-KV=V1&HW-CC-Date=20260611T072805Z&HW-CC-Expire=86400&HW-CC-Sign=8A75D9C2C0B5E85A08F293C011FAD77D88252551E08B29A54ABF264F3D4915FD)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/MLFpGYXWR-S2rjWct5xfdg/zh-cn_image_0000002602186255.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072805Z&HW-CC-Expire=86400&HW-CC-Sign=67C347A740CB3CFD959B75B39B58EA54A6D497689AE389874976841A8E0A969F)
