---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-367
title: 如何获取ArkTS状态管理框架代理前的原始对象
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取ArkTS状态管理框架代理前的原始对象
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cdac068973c26cb80e40bf468b41bf6db921b4cd763e67bbb5d9f2c37976205f
---
使用getTarget接口获取状态管理框架代理前的原始对象。

参考示例如下：

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Observed
4. class UserInfo {
5. name: string = 'Tom';
6. }

8. @Entry
9. @Component
10. struct GetTargetDemo {
11. @State info: UserInfo = new UserInfo();

13. build() {
14. Column() {
15. Text(`info.name: ${this.info.name}`)
16. Button('Change the properties of the proxy object')
17. .onClick(() => {
18. this.info.name = 'Alice'; // The Text component can refresh
19. })
20. Button('更改原始对象的属性')
21. .onClick(() => {
22. let rawInfo: UserInfo = UIUtils.getTarget(this.info);
23. if (rawInfo) {
24. rawInfo.name = 'Bob'; // The Text component cannot be refreshed
25. }
26. })
27. }
28. }
29. }
```

[ObtainStateManagementFramework.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ObtainStateManagementFramework.ets#L21-L50)

参考链接

[getTarget接口：获取状态管理框架代理前的原始对象](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/辅助接口/getTarget接口：获取状态管理框架代理前的原始对象/arkts-new-gettarget.md>)
