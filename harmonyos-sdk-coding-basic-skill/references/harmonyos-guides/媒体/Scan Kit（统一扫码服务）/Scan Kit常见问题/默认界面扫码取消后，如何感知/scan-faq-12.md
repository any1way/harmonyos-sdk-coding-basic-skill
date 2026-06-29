---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-12
title: 默认界面扫码取消后，如何感知
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 默认界面扫码取消后，如何感知
category: harmonyos-guides
scraped_at: 2026-06-01T14:55:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:892d5c2eed251c15783ec9d40cc010b86dd412558905a0e02597087205b120cc
---
**问题现象**

调用默认界面扫码功能，没有扫码直接关闭，如何在逻辑中判断？

**解决措施**

开启扫码，却没有进行任何扫码操作而直接取消扫码，可以从回调中获取返回错误码：[1000500002](<../../../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/ArkTS API错误码/scan-error-code.md#section1000500002-用户取消扫码>)，用户取消扫码，据此自行修改逻辑操作。
