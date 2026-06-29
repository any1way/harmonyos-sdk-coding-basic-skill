---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-7
title: HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
category: harmonyos-guides
scraped_at: 2026-06-11T15:03:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a77e16e6f8ff60a44baeba2c6263d0231c4cb8f1cabc3b5e0e5173859e71142f
---
终端设备从HarmonyOS 3.x/4.x（简称HarmonyOS）升级到HarmonyOS NEXT/5.0.x及之后版本（简称HarmonyOS NEXT）。

1. HarmonyOS APK应用使用OpenID关联用户数据时，将用户数据关系切换成UnionID，具体切换指导可以参考：[通过OpenID获取UnionID](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/扩展能力/通过OpenID获取UnionID/account-api-get-unionid.md>)。
2. HarmonyOS APK应用使用UnionID关联用户数据时，在HarmonyOS NEXT/5.0.x上接入华为账号一键登录获取手机号后，应用需要同时将UnionID和手机号与用户信息进行关联，最终实现应用使用华为账号一键登录和手机号登录数据互通。详细流程可以参考：[用户场景设计](../../登录/华为账号一键登录（获取手机号和UnionIDOpenID）/account-phone-unionid-login.md#用户场景设计)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/GX6x296_TmafkP8FfD62hg/zh-cn_image_0000002622858637.png?HW-CC-KV=V1&HW-CC-Date=20260611T070311Z&HW-CC-Expire=86400&HW-CC-Sign=E3DACE04F58A1136371E9659EE446DB13550BA27FB69307D308A9D39B843B3FD)
