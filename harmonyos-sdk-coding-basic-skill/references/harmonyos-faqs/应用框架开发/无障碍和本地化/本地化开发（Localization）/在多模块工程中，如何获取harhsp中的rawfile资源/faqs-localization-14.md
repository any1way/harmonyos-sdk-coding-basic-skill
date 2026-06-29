---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-14
title: 在多模块工程中，如何获取har/hsp中的rawfile资源
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 在多模块工程中，如何获取har/hsp中的rawfile资源
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:36+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:d047bddf6d6fcbae82acb04d964c46befeb8a0cff99c427b324e0e478459fabb
---
har模块中的资源可以通过[@ohos.resourceManager (资源管理)](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md>)获取，hsp中的资源可以通过application的[application.createModuleContext](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.application (应用工具类)/js-apis-app-ability-application.md#applicationcreatemodulecontext>)接口创建相应模块的context，再通过resourceManager获取。

示例如下：

```
1. import { application, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { buffer } from '@kit.ArkTS';

5. @Entry
6. @Component
7. struct Index {
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. build() {
11. Column() {
12. Button('get rawFile content')
13. .onClick(() => {
14. application.createModuleContext(this.context, 'hsp')
15. .then((data) => {
16. let rawFileData = data.resourceManager.getRawFileContentSync('hsp.txt');
17. let hspContent: string = buffer.from(rawFileData.buffer).toString();
18. })
19. .catch((error: BusinessError) => {
20. console.error(`createModuleContext failed, error.code: ${error.code}, error.message: ${error.message}`);
21. })
22. })
23. }
24. .height('100%')
25. .width('100%')
26. .justifyContent(FlexAlign.Center)
27. }
28. }
```

[GetRawfile.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalizationKit/entry/src/main/ets/pages/GetRawfile.ets#L21-L48)
