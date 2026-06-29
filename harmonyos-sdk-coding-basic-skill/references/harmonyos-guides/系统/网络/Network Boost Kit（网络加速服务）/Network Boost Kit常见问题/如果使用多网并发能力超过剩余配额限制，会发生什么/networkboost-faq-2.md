---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-faq-2
title: 如果使用多网并发能力超过剩余配额限制，会发生什么
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > Network Boost Kit常见问题 > 如果使用多网并发能力超过剩余配额限制，会发生什么
category: harmonyos-guides
scraped_at: 2026-06-01T11:20:48+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:3d71b4bc63858131c535e129a8097ae37c69fbecf8c04ad38e6d0c9b40553e63
---
配额（次数或时长）耗尽会限制使用，多网会自动释放，应用可以在[netHandover.on('multiPathStateChange')](<../../../../../../harmonyos-references/网络/Network Boost Kit（网络加速服务）/ArkTS API/netHandover（连接迁移）/networkboost-nethandover.md#nethandoveronmultipathstatechange>)中监听到多网退出回调。如果此时再请求多网会抛出错误码，应用可以在[netHandover.requestMultiPath()](<../../../../../../harmonyos-references/网络/Network Boost Kit（网络加速服务）/ArkTS API/netHandover（连接迁移）/networkboost-nethandover.md#nethandoverrequestmultipath>)的错误码中判断错误类型。应用配额以24小时的周期进行刷新。
