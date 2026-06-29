---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-16
title: 如何持有wakelock锁，防止系统休眠
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何持有wakelock锁，防止系统休眠
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:7dcf3d1e77a5c24a95ac717dbd15a0786fd66a98b8a8fdac1e2a3f79d971fa4c
---
调用runningLock.create接口创建RunningLock锁。使用[hold()](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.runningLock (RunningLock锁)/js-apis-runninglock.md#hold9>)接口设置锁定持续时间，期间系统不会休眠。锁超时后，若未设置其他RunningLock，锁自动释放，系统进入休眠状态。

**参考链接**

[RunningLock锁](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.runningLock (RunningLock锁)/js-apis-runninglock.md>)
