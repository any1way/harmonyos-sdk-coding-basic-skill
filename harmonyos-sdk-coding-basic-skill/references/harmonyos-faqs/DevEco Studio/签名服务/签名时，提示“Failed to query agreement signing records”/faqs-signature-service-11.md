---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-11
title: 签名时，提示“Failed to query agreement signing records”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名时，提示“Failed to query agreement signing records”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b04180f30984f86a924eef7fb0bbc8a582178874b63f2e737c938aa8b852d4c5
---
**问题现象**

使用未实名认证的华为账号登录会导致签名错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/83uW_losT7SS9GouxK9Okg/zh-cn_image_0000002194318468.png?HW-CC-KV=V1&HW-CC-Date=20260612T024358Z&HW-CC-Expire=86400&HW-CC-Sign=236C003E9A57700CB601F2F7FFC6637144B81D05BBE7FA8027B6B7C2380EB9F1)

**解决措施**

出现该问题的原因是签名过程中，DevEco Studio与查询协议的连接通道发生异常

请尝试以下两种方法解决此问题

方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](../../../../harmonyos-guides/编写与调试应用/附录/配置代理/ide-environment-config.md)。

方式二：进行开发者实名认证，具体指导可以参考[实名认证介绍](https://developer.huawei.com/consumer/cn/doc/start/itrna-0000001076878172)。
