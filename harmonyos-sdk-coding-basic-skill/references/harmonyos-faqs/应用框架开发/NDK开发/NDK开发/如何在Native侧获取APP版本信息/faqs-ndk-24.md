---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-24
title: 如何在Native侧获取APP版本信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧获取APP版本信息
category: harmonyos-faqs
scraped_at: 2026-06-12T10:25:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:968ae1e9b621f9fe39acd55d845192e1213ce5991c6486d02ce909e308f0cb78
---
Native侧目前没有获取APP版本信息的接口。如需获取APP版本信息，可以在ArkTS侧获取，然后传递到Native侧。

通过@kit.AbilityKit模块中的bundleManager查询bundleInfo。bundleInfo包含App版本号和版本名。

ArkTS侧传递数据到Native侧可参考链接：

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. Row() {
11. Column() {
12. Text(this.message)
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo)=>{
17. let versionName = bundleInfo.versionName;//Application version name
18. let versionNo = bundleInfo.versionCode;//Application version number
19. }).catch((error : BusinessError)=>{
20. console.error("get bundleInfo failed,error is "+error)})
21. })
22. }
23. .width('100%')
24. }
25. .height('100%')
26. }
27. }
```

[BundInfoPage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/BundInfoPage.ets#L3-L29)

ArkTS侧传递数据到Native侧可参考链接：

[使用Node-API实现跨语言交互开发流程](../../../../../harmonyos-guides/NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md)

获取模块相关信息参考链接：

[bundleInfo](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1>)

[@ohos.bundle.bundleManager (应用程序包管理模块)](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md>)
