---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-405
title: Navigation路由，如何快速实现RouterMap注册转为wrapBuilder注册
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation路由，如何快速实现RouterMap注册转为wrapBuilder注册
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d71aa6ab4d12119026f6a5ebae1544c9e59f5aa090c882c576cbb565360a4fff
---
可以使用自定义路由表，基本实现跟Router路由类似。

开发者自定义路由管理模块，各个提供路由页面的模块均需要依赖此模块。构建Navigation组件时，将NavPathStack注入路由管理模块，路由管理模块对NavPathStack进行封装，对外提供路由能力。各个路由页面不再直接提供组件，而是提供@Builder封装的构建函数。这些构建函数通过WrappedBuilder进行全局封装。然后，各个路由页面需要将模块名称、路由名称以及封装后的WrappedBuilder构建函数注册到路由模块。

当路由需要跳转到指定路由时，路由模块完成对指定路由模块的动态导入，并完成路由跳转。

参考[动态路由](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/Router切换Navigation/arkts-router-to-navigation.md#动态路由>)中的方案一：自定义路由表。

Navigation自动生成动态路由示例参考：[自动生成动态路由](https://gitcode.com/HarmonyOS-Cases/cases/blob/master/CommonAppDevelopment/common/routermodule/README_AUTO_GENERATE.md)。
