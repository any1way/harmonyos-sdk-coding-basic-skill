---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-32
title: 应用能否指定使用某一网络来发请求
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 应用能否指定使用某一网络来发请求
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dc2df9fce0a6575da0a927ab3a88478a0cf174c22897def0bdd0678792d20aae
---
**问题现象**

发网络请求时，指定使用Wi-Fi或蜂窝数据。

**解决措施**

应用可以使用[connection.setAppNet()](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md#connectionsetappnet9-1>)接口将应用绑定到指定网络，此时该应用的所有网络请求将使用该网络。若要使用其他网络，需再次通过[connection.setAppNet()](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md#connectionsetappnet9-1>)将应用绑定到其他网络。

**参考链接**

[@ohos.net.connection (网络连接管理)](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md>)
