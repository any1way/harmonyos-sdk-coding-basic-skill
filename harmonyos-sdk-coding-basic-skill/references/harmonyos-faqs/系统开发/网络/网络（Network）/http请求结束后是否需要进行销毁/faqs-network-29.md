---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-29
title: http请求结束后是否需要进行销毁
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求结束后是否需要进行销毁
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f0e626c4c0c383c2f08fe5153ac7bfd780513a5ea6457e1164689b0d8a132d38
---
http请求对象，在请求成功或者失败后，都需要调用destroy()接口进行销毁，以节省资源消耗。详细请参见[使用HTTP访问网络](<../../../../../harmonyos-guides/系统/网络/Network Kit（网络服务）/访问网络/使用HTTP访问网络/http-request.md>)。
