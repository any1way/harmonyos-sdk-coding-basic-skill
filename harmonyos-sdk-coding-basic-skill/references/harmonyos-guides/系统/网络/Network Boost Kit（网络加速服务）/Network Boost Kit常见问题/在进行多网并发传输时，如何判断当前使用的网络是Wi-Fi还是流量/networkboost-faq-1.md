---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-faq-1
title: 在进行多网并发传输时，如何判断当前使用的网络是Wi-Fi还是流量
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > Network Boost Kit常见问题 > 在进行多网并发传输时，如何判断当前使用的网络是Wi-Fi还是流量
category: harmonyos-guides
scraped_at: 2026-06-01T11:20:47+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:2c7ad74e42642efc10d5547f01484eafb89172135e1aa9829083d7fd0f93dbde
---
请求多网成功后可以获取到多个可用的netHandle，通过[connection.getNetCapabilities()](<../../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md#connectiongetnetcapabilities>)方法查询网络信息，通过[NetBearType](<../../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md#netbeartype>)字段判断网络类型，其中BEARER\_CELLULAR是蜂窝网络，BEARER\_WIFI是Wi-Fi网络。在设计多网并发策略时可以通过网络类型和网络能力调整对应网络通路的网络任务。
