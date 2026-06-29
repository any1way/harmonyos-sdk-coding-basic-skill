---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-3
title: GET请求的bodySign是对谁签名得到的？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > GET请求的bodySign是对谁签名得到的？
category: harmonyos-guides
scraped_at: 2026-06-01T15:08:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d5bebbbdc9d1c3b38c73799314e5ee02e359a1338907c1b0acf8e9bc934186a1
---
GET请求需要对path url进行签名，例如[查询支付订单](<../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/REST API/直连商户/基础支付/查询支付订单/通过sysTransOrderNo查询订单信息/payment-sys-query-order.md>)的待签名内容是：“/api/v2/aggr/transactions/orders/{sysTransOrderNo}”。
