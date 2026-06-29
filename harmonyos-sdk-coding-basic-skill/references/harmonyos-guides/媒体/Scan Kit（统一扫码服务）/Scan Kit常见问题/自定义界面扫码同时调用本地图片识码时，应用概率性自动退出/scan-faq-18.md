---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-18
title: 自定义界面扫码同时调用本地图片识码时，应用概率性自动退出
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码同时调用本地图片识码时，应用概率性自动退出
category: harmonyos-guides
scraped_at: 2026-06-01T14:55:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f07c12560f832509787ce0bf32b5c02d010439a9cc109ca72b1ec9997401fc1a
---
**问题现象**

自定义界面扫码，点击图库，选中图片进行本地图片识码时，应用概率性的自动退出。

**解决措施**

自定义界面扫码接口和识别本地图片接口不支持并发执行。

点击图库按钮的时候，需要先暂停并释放相机流（customScan.[stop](<../../../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/customScan (自定义界面扫码)/scan-customscan-api.md#customscanstop>)、customScan.[release](<../../../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/customScan (自定义界面扫码)/scan-customscan-api.md#customscanrelease>)），再进行本地图片识码。
