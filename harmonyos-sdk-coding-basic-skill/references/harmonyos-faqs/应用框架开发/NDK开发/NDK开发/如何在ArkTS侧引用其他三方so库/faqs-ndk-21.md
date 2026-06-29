---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-21
title: 如何在ArkTS侧引用其他三方so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在ArkTS侧引用其他三方so库
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:57+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:14de2741ccab78bcf44f2f747c2b4a1b2bbcd6f61ff8bb3764e93c40e02d0a90
---
**解决措施**

在ArkTS中引用三方库so需要具备以下三个文件：xxx.so、Index.d.ts和oh-package.json5。其中，Index.d.ts和oh-package.json5在C++模板中自带，也可以手动创建。在需要调用的模块根目录下的oh-package.json5中声明so库的根目录路径。然后在代码中使用import语句引用oh-package.json5中声明的依赖名称。此方案仅适用于已经适配了Native的so库。因此，在编译生成so库时，需要实现功能函数并注册其Native侧接口，同时提供对应的Native侧接口声明文件Index.d.ts和配置文件oh-package.json5。

1. 将so文件移动到libs文件夹下对应架构的目录。如果在纯ArkTS工程中，还需将编译三方库时生成的libc++\\_xxx.so移动到该目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/mlYYyrQWQZq4cAHv3r9z3g/zh-cn_image_0000002194318516.png?HW-CC-KV=V1&HW-CC-Date=20260612T022456Z&HW-CC-Expire=86400&HW-CC-Sign=DFDD8F6FBECBDC4C6B3DC44018B99FBC6D9AB138698C4192291B8F8435EFF064 "点击放大")
2. 在src/main/cpp/types目录下创建新目录，并将Index.d.ts和oh-package.json5文件移动到该目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/G8lAm_--RRaN5m-IhGT_bA/zh-cn_image_0000002229604289.png?HW-CC-KV=V1&HW-CC-Date=20260612T022456Z&HW-CC-Expire=86400&HW-CC-Sign=42FBD1D78BA792846D7583CA400B4F2927EBC2988A9764D7F9A503277C6B9D68 "点击放大")
3. 在模块级的oh-package.json5文件中声明该 so 库的根目录路径。

   ```
   1. "dependencies": {
   2. "libimportthirdpartylibraries.so": "file:./src/main/cpp/types/libimportthirdpartylibraries",
   3. "libapplication.so": "file:./src/main/cpp/types/libapplication"
   4. },
   ```

   [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ImportThirdPartyLibraries/oh-package.json5#L12-L15)
4. 在代码中引用并调用oh-package.json5中声明的依赖。

   ```
   1. import testNapi from 'libimportthirdpartylibraries.so';
   2. import myNapi from 'libapplication.so';

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
   16. console.info(`MyTest NAPI 2 + 3 = ${myNapi.add(2, 3)}`);
   17. console.info(`MyTest NAPI 2 - 3 = ${testNapi.sub(2, 3)}`);
   18. })
   19. }
   20. .width('100%')
   21. }
   22. .height('100%')
   23. }
   24. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ImportThirdPartyLibraries/src/main/ets/pages/Index.ets#L19-L42)

运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/99XpBpisT12nWcCozf-lCQ/zh-cn_image_0000002229758785.png?HW-CC-KV=V1&HW-CC-Date=20260612T022456Z&HW-CC-Expire=86400&HW-CC-Sign=97F6DEB5F0008C9E61D07F07338B40B45E30BBAD76967607444DB06C37B35F1E "点击放大")

**参考链接**

[在ArkTS侧引用三方so库](../../../../../best-practices/NDK开发/三方动态链接库集成/bpta-dynamic-link-library.md#section166546365376)
