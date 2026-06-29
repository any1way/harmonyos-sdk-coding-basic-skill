---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-9
title: emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息
category: harmonyos-faqs
scraped_at: 2026-06-01T17:04:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a62e1c036a769dcafd230c47a288669f8408cb46c39452fce139f46e0eda1cd2
---
是的，emitter.off取消订阅某个事件后，所有订阅这个事件的地方都不会再收到这个事件的消息。

参考代码如下：

```
1. emitter.off(1);
```

[EmitterOff.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Notificationkit/entry/src/main/ets/pages/EmitterOff.ets#L22-L22)

**参考链接**

[emitter.off](<../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.events.emitter (Emitter)/js-apis-emitter.md#emitteroff>)
