---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-faq-3
title: 游戏如何实现不展示官方账号登录
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > Game Service Kit常见问题 > 基础游戏服务 > 游戏如何实现不展示官方账号登录
category: harmonyos-guides
scraped_at: 2026-06-11T15:07:32+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:771f6c3ff4f947126e901da487f0989c23b7204b362cef16e82b4e841478b3f8
---
在游戏调用[unionLogin](<../../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePlayer（基础游戏服务）/gameservice-gameplayer.md#gameplayerunionlogin>)接口时，将thirdAccountInfos参数传空数组，即可实现玩家登录游戏时不展示“游戏官方账号登录”选项，默认使用华为账号登录。
