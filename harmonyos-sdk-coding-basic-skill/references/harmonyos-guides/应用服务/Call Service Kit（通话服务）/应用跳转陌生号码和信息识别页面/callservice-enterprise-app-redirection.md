---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-app-redirection
title: 应用跳转陌生号码和信息识别页面
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 应用跳转陌生号码和信息识别页面
category: harmonyos-guides
scraped_at: 2026-06-01T15:01:57+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:7938f7e5b41afa73b61a1716d08e8174d4365f10e68e88826796c1953e70833c
---
从6.1.0(23)版本开始，新增支持从应用直接跳转到“电话 > 更多 > 设置 > 陌生号码和信息识别"。

通过[Deep Linking](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/使用Deep Linking实现应用间跳转/deep-linking-startup.md>)方式应用可以直接跳转“陌生号码和信息识别”页面。

以使用openLink实现应用跳转举例，在openLink接口的link字段中传入目标应用的URL信息，并将options字段中的appLinkingOnly配置为false、跳转的URL固定为"callsetting://number\_identity"。

其他跳转方式参考使用Deep Linking实现应用间跳转[拉起方应用实现应用跳转](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/使用Deep Linking实现应用间跳转/deep-linking-startup.md#拉起方应用实现应用跳转>)章节。

示例代码：

```
1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
10. .width('87%')
11. .height('5%')
12. .margin({ bottom: '12vp' })
13. .onClick(() => {
14. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let link: string = 'callsetting://number_identity';
16. let openLinkOptions: OpenLinkOptions = {
17. appLinkingOnly: false
18. };
19. try {
20. context.openLink(link, openLinkOptions)
21. .then(() => {
22. hilog.info(0, 'TAG','Successed in opening link.');
23. }).catch((err: BusinessError) => {
24. hilog.error(0, 'TAG',`Failed to open link. Code is ${err.code}, message is ${err.message}`);
25. });
26. } catch (paramError) {
27. hilog.error(0, 'TAG',`Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
28. }
29. })
30. }
31. }
```
