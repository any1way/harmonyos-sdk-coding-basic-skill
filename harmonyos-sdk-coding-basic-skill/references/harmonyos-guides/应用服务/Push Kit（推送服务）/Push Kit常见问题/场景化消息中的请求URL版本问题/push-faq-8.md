---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-8
title: 场景化消息中的请求URL版本问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 场景化消息中的请求URL版本问题
category: harmonyos-guides
scraped_at: 2026-06-01T15:09:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:744a4d7dee748f19470ff3c4b552b8f367f60c44744f838f9a91f8bb1edbefdf
---
场景化消息[请求体结构](<../../../../../harmonyos-references/Push Kit（推送服务）/REST API/场景化消息/请求体结构说明/push-scenariozed-api-request-struct.md>)中，请求URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

**请使用V3版本**的请求URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）进行消息推送。
