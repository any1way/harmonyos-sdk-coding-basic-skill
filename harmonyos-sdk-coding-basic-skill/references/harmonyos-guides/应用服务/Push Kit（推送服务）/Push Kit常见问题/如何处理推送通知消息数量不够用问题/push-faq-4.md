---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-4
title: 如何处理推送通知消息数量不够用问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 如何处理推送通知消息数量不够用问题
category: harmonyos-guides
scraped_at: 2026-06-01T15:09:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e324fdc9df04f6f3775c5ca8de27397eaa214d72233c0e84e57bcb6ca1b04942
---
建议您优化推送策略，做精细化推送，尽量减少或避免全量用户的推送。如果您的消息内容中有符合服务与通讯类消息的内容，建议您申请和接入消息自分类，详情请参见[通知消息分类标准与提醒方式](../../开发准备/申请推送场景化消息权益/push-apply-right.md#通知消息分类标准与提醒方式)，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。
