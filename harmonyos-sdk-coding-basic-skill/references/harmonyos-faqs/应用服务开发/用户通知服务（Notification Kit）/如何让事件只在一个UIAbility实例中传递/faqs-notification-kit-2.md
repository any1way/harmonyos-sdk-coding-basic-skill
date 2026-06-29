---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-2
title: 如何让事件只在一个UIAbility实例中传递
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何让事件只在一个UIAbility实例中传递
category: harmonyos-faqs
scraped_at: 2026-06-01T17:04:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:67447751c46ea0553db3b3ab2acc88960823f07dd35caa0177ccb67bcd1e4ea4
---
在UIAbility中使用EventHub订阅事件，EventHub模块提供了事件中心，订阅、取消订阅、触发事件的能力。

参考代码如下：

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onForeground() {
5. this.context.eventHub.on('myEvent', this.eventFunc);
6. // result：
7. // eventFunc is called,undefined,undefined
8. this.context.eventHub.emit('myEvent');
9. // result：
10. // eventFunc is called,1,undefined
11. this.context.eventHub.emit('myEvent', 1);
12. // result：
13. // eventFunc is called,1,2
14. this.context.eventHub.emit('myEvent', 1, 2);
15. }

17. eventFunc(argOne: number, argTwo: number) {
18. console.log(`eventFunc is called, ${argOne}, ${argTwo}`);
19. }
20. }
```

[EntryAbility2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Notificationkit/entry/src/main/ets/entryability/EntryAbility2.ets#L6-L25)

**参考链接**

[使用EventHub进行数据通信](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件与UI的数据同步/uiability-data-sync-with-ui.md#使用eventhub进行数据通信>)
