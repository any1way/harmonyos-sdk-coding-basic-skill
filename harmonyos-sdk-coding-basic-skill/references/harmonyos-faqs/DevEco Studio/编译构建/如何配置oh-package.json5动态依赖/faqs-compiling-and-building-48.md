---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-48
title: 如何配置oh-package.json5动态依赖
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何配置oh-package.json5动态依赖
category: harmonyos-faqs
scraped_at: 2026-06-01T17:06:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9ff3327c576e437be59ff76357adf950d3d9255bfe7e69032001499d2a65a26c
---
oh-package.json5文件中：

* dependencies（生产依赖）：声明生产依赖，即代码中需要导入的HarmonyOS三方库，用于编译和运行阶段。
* devDependencies（开发依赖）：用于项目的开发或测试阶段。
* dynamicDependencies（动态依赖）：配置用于动态加载的HSP模块。

示例如下：

```
1. {
2. "name": "parameter-test",
3. "version": "@param:version",
4. "modelVersion": "5.0.4",
5. "description": "test desc.",
6. "main": "index.ets",
7. "author": "test author",
8. "license": "ISC",
9. "dependencies": {
10. "libtest1": "@param:dependencies.libtest1"
11. },
12. "devDependencies": {
13. "libtest2": "@param:devDependencies.libtest2"
14. },
15. "dynamicDependencies": {
16. "libtest3": "@param:dynamicDependencies.libtest3"
17. },
18. "parameterFile": '.parameterFile/parameterFile.json5',// Enable parameterization and specify the path to the parameterized configuration file
19. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ParameterTest/oh-package.json5#L3-L21)

**参考链接**

[oh-package.json5文件](../../../../harmonyos-guides/命令行工具/三方依赖管理工具（ohpm）/oh-package.json5/ide-oh-package-json5.md)，[添加依赖项](../../../../harmonyos-guides/构建应用/配置构建流程/添加依赖项/ide-hvigor-dependencies.md)
