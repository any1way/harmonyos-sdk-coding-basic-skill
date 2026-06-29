---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-480
title: 如何实现护眼模式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现护眼模式
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:63a3c9a265f8235d68fbd5647fcc814f8b5cafe5903ffbccdfb9dc9f71343654
---
**解决措施**

当前实现护眼模式可以采用下面两种方式：

方案一：可通过深色模式的方式，进行应用适配；深色模式的开发可以参考：[深色模式适配](../../../../../best-practices/主题与样式/深色模式适配/bpta-dark-mode-adaptation.md)。

方案二：可通过系统设置全局开启护眼模式，通过应用内指引用户跳转设置页面手动打开护眼模式。

```
1. import { common } from "@kit.AbilityKit";
2. import { BusinessError } from "@kit.BasicServicesKit";

4. @Entry
5. @Component
6. export struct ImplementEyeProtectionMode {
7. build() {
8. Row() {
9. Button('跳转显示设置页面')
10. .onClick(() => {
11. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. context.startAbility({
13. bundleName: 'com.huawei.hmos.settings',
14. abilityName: 'com.huawei.hmos.settings.MainAbility',
15. uri: 'display_settings'
16. }).catch((err: BusinessError) => {
17. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
18. })
19. })
20. }
21. .width('100%')
22. .height('100%')
23. .alignItems(VerticalAlign.Center)
24. .justifyContent(FlexAlign.Center)
25. }
26. }
```

[ImplementEyeProtectionMode.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementEyeProtectionMode.ets#L21-L47)
