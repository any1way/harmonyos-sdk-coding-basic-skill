---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-6004
title: OS平台API行为的变更
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta5引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-06-01T10:42:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3d05716d20b8dbf9835dd82bd9b3c8872d8eae6e1a8aca5578f777296f3a088b
---
## ArkTS

### 禁止在编译产物为JS的HAR包中使用注解

**变更原因**

应用开发中，在[release模式下构建](../../../../../../harmonyos-guides/构建应用/配置构建流程/构建HAR/ide-hvigor-build-har.md#section19788284410)源码HAR，并同时[开启混淆](../../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS编译工具链/ArkGuard源码混淆工具/ArkGuard混淆原理及功能/source-obfuscation.md)时，由于编译产物为JS文件，而在JS中没有注解的实现机制，因此会在编译过程中被移除，导致无法通过注解实现AOP插桩。

为避免因此引起的功能异常，禁止在JS HAR(编译产物中存在JS的HAR包)中使用注解。

**变更影响**

此变更涉及应用适配。

变更前：构建JS HAR时，若代码中存在注解，编译不会报错。

如下代码在JS形态的HAR包中编译时不会报错。

```
1. // test.ets
2. @interface ClassAuthor {
3. authorName: string
4. }

6. @ClassAuthor({authorName: "Bob"})
7. class MyClass {
8. /* body */
9. }
```

变更后：构建JS HAR时，若代码中存在注解，编译会报错。

**起始API Level**

不涉及

**变更的接口/组件**

不涉及

**适配指导**

删除JS HAR中的注解声明和调用，或者重新编译成其他形态的HAR包，例如[字节码HAR](../../../../../../harmonyos-guides/构建应用/配置构建流程/构建HAR/ide-hvigor-build-har.md#section16598338112415)。
