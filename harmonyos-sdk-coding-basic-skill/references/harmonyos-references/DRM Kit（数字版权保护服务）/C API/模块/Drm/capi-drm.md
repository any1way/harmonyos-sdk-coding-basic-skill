---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm
title: Drm
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 模块 > Drm
category: harmonyos-references
scraped_at: 2026-06-01T16:21:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c33a8d93fe13f51ccdc36e105a91f50e4ebd7dc1834ba27d2775f473b162b06f
---
## 概述

PhonePC/2in1TabletTVWearable

提供数字版权保护能力的API。

开发者可根据实际的开发需求，参考对应的开发指南及样例：

* [数字版权保护(C/C++)](<../../../../../harmonyos-guides/媒体/DRM Kit（数字版权保护服务）/数字版权保护(CC++)/drm-c-dev-guide.md>)
* [基于AVCodec播放DRM节目(C/C++)](<../../../../../harmonyos-guides/媒体/DRM Kit（数字版权保护服务）/基于AVCodec播放DRM节目(CC++)/drm-avcodec-integration.md>)

**起始版本：** 11

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md) | 定义DRM数据类型。 |
| [native\_drm\_err.h](../../头文件/native_drm_err.h/capi-native-drm-err-h.md) | 定义DRM错误码。 |
| [native\_mediakeysession.h](../../头文件/native_mediakeysession.h/capi-native-mediakeysession-h.md) | 定义Drm MediaKeySession API。提供以下功能：  生成媒体密钥请求、处理媒体密钥响应、事件监听、获取内容保护级别、检查媒体密钥状态、删除媒体密钥等。 |
| [native\_mediakeysystem.h](../../头文件/native_mediakeysystem.h/capi-native-mediakeysystem-h.md) | 定义Drm MediaKeySystem API。提供以下功能：  查询是否支持特定的drm、创建媒体密钥会话、获取和设置配置、获取统计信息、获取内容保护级别、生成提供请求、处理提供响应、事件监听、获取内容防护级别、管理离线媒体密钥等。 |
