---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-in-depth-convergence
title: 深度融合
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 深度融合
category: harmonyos-guides
scraped_at: 2026-06-01T15:12:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fbaf22a042c2862589cbbb28a3277d7528da96a3841bab8d12040a35740aa1f4
---
模型推理时结合硬件深度融合，减少对DDR的访问，提升能效比。目前仅支持编译前可变shape场景，调用[HMS\_HiAIOptions\_SetTuningStrategy](<../../../../../harmonyos-references/CANN Kit（CANN异构计算框架服务）/C API/模块/CANN/cannkit.md#hms_hiaioptions_settuningstrategy>)设置模型优化策略为"HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING"。
