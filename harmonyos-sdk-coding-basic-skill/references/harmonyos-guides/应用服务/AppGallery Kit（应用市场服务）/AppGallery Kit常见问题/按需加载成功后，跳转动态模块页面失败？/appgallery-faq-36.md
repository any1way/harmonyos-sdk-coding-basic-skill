---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-faq-36
title: 按需加载成功后，跳转动态模块页面失败？
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 按需加载成功后，跳转动态模块页面失败？
category: harmonyos-guides
scraped_at: 2026-06-01T15:01:22+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:d712303ef2d16d50874a7a75c7b018586d9d4c6e360c4fa94001534a411b534a
---
**问题现象**

按需加载成功后，开发者业务需要跳转到动态模块的页面，使用Navigation跨包路由时返回100005错误码。

**可能原因**

6.0.2(22)及之前版本，不支持Navigation跨包路由方式，从6.1.0(23)开始，[支持开发者使用Navigation跨包路由跳转到动态安装的HSP中的页面](<../../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation跨包路由/arkts-navigation-cross-package.md#系统路由表>)，建议检查升级HarmonyOS版本。
