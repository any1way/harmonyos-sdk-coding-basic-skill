---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:793dabc93552d960c6edaabd4dab8ba27f2ed73fa332351c2fdcd4afada4130d
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-XamPZhrQ3edEZ70J5KJUQ/zh-cn_image_0000002583119532.png?HW-CC-KV=V1&HW-CC-Date=20260601T070411Z&HW-CC-Expire=86400&HW-CC-Sign=B6267F425C7ABBECB3C33BF58347B8D282154F9AECAEDC74B1D693C20DB16377)
2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

   ```
   1. "module": {
   2. "name": "xxxx",
   3. "type": "entry",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [],
   7. "pages": "xxxx",
   8. "abilities": [],
   9. "metadata": [ // 配置如下信息
   10. {
   11. "name": "client_id",
   12. "value": "xxxxxx"
   13. }
   14. ]
   15. }
   ```
