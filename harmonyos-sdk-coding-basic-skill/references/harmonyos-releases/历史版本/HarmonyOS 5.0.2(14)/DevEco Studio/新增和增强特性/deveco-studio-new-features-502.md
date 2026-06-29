---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-502
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > DevEco Studio > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-06-01T10:50:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:bbf39fad16c27fd61fd8e1ea148bab0c2c5f8121a62388cc6c8ce5a72c31d180
---
## DevEco Studio 5.0.2 Release（5.0.7.210）兼容性配套关系

DevEco Studio 5.0.7.210携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| DevEco Studio | DevEco Studio 5.0.2 Release（5.0.7.210） | - |
| HarmonyOS SDK | HarmonyOS 5.0.2 Release SDK | - |
| HarmonyOS Emulator | HarmonyOS Emulator 5.0.2 Release（5.0.7.300） | 模拟器，当前支持手机（包括折叠屏）、平板。 |
| Hvigor | 5.14.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.11 | OpenHarmony三方库的包管理工具。 |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.2 | 开发态版本号。 |

DevEco Studio 5.0.7.210配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 5.0.7.210 | 命令行工具集版本。 |
| codelinter | 5.0.400 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 5.14.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.11 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 5.0.2 Release SDK | - |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.2 | 开发态版本号。 |

## DevEco Studio 5.0.2 Release（5.0.7.200）兼容性配套关系

DevEco Studio 5.0.7.200携带的工具列表、支持的API范围及开发态版本号信息如下：

**表3** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| DevEco Studio | DevEco Studio 5.0.2 Release（5.0.7.200） | - |
| HarmonyOS SDK | HarmonyOS 5.0.2 Release SDK | - |
| HarmonyOS Emulator | HarmonyOS Emulator 5.0.2 Release（5.0.7.300） | 模拟器，当前支持手机（包括折叠屏）、平板。 |
| Hvigor | 5.14.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.11 | OpenHarmony三方库的包管理工具。 |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.2 | 开发态版本号。 |

DevEco Studio 5.0.7.200配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表4** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 5.0.7.200 | 命令行工具集版本。 |
| codelinter | 5.0.400 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 5.14.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.11 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 5.0.2 Release SDK | - |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.2 | 开发态版本号。 |

## DevEco Studio 5.0.2 Release（5.0.7.210）新增和增强特性

无新增和增强特性。

## DevEco Studio 5.0.2 Release（5.0.7.200）新增和增强特性

### 新增特性

* DevEco Studio支持开发API 14工程。
* 端云一体化工程默认提供云对象的调用接口类存放目录，具体请参考[在端侧调用云对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudobj)。
* HSP支持配置UIAbility组件，但不支持配置入口Ability，不支持依赖带入口Ability的HAR。具体请参考[HSP](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md#约束限制)。
* DevEco Studio新增混淆助手工具ObfuscationHelper，支持对源码进行扫描，快速识别需要配置的保留选项和白名单字段，开发者可以一键生成白名单混淆规则文件；部分场景需要开发者根据业务进一步排查识别白名单后进行配置。具体请参考[通过混淆助手配置保留选项](../../../../../harmonyos-guides/构建应用/混淆加固/ide-build-obfuscation.md#section19439175917123)。
* hvigor-config.json5新增以下字段。具体可参考[hvigor-config.json5](../../../../../harmonyos-guides/构建应用/配置文件/hvigor-config.json5文件/ide-hvigor-set-options.md)。
  + properties下新增ohos.collect.debugSymbol字段，用于指定是否将sourceMap、nameCache和带调试信息的so文件归档到产物路径下。
  + 新增javaOptions/Xmx字段，用于设置JVM最大堆内存，单位为MB，默认为512MB。
* 工程级和模块级build-profile.json5文件新增以下字段。具体可参考[build-profile.json5](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md)。
  + buildOption/nativeLib下新增excludeSoFromInterfaceHar字段，用于指定编译HSP模块时，打包的HAR产物是否排除so文件，减少.tgz包体积大小。
  + buildOption/arkOptions下新增autoLazyImport字段，用于指定编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。
* BuildAnalyzer新增支持导入report.json文件，查看历史或其他工程的构建日志。具体请参考[导入日志](../../../../../harmonyos-guides/构建应用/提升构建效率/分析构建过程/ide-hvigor-build-analyzer.md#section26761217305)。
* DevEco Profiler支持Raw Heap离线导入。具体请参考[Snapshot模板基本操作](../../../../../harmonyos-guides/优化应用性能/内存泄露：Snapshot分析/Snapshot模板基本操作/ide-snapshot-basic-operations.md)。
* Instrument Test新增运行参数Auto Dependencies和Only OhosTest Package。具体请参考[自定义测试用例运行任务](<../../../../../harmonyos-guides/编写与调试应用/开发自测试/测试框架/代码测试/Instrument Test/ide-instrument-test.md#section65264166107>)。
  + Auto Dependencies：默认勾选，测试阶段会自动将所有依赖的模块都安装到设备上。
  + Only OhosTest Package：如果不涉及UI测试，勾选后只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。
* 应用与元服务体检新增支持场景化体检，开发者可以基于实际的应用场景、对特定的页面进行测试，测试结果可以更清晰地指导开发者对某个页面某个场景的某个指标进行优化。具体请参考[应用与元服务体检](../../../../../harmonyos-guides/编写与调试应用/开发自测试/应用与元服务体检/ide-app-analyzer.md)。

### 增强特性

* 新建工程模板代码根据Code Linter规则优化。
* Code Linter新增性能、安全及正确性代码检查规则。具体请参考[规则变更说明](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查规则/规则变更说明/ide-codelinter-rules-change.md>)。
* 端云一体化工程优化基于云开发模板创建应用/元服务的流程，具体请参考[创建端云一体化开发工程](../../../../../harmonyos-guides/开发环境搭建/工程创建/模块管理/端云一体化开发/开发端云工程/创建端云一体化开发工程/agc-harmonyos-clouddev-devproject.md)。
* DevEco Profiler全局搜索功能优化，并支持使用“/”展示快捷键使用说明。具体请参考[调优工具简介](<../../../../../harmonyos-guides/优化应用性能/DevEco Profiler调优工具简介/ide-profiler.md>)。
* DevEco Studio内上传软件包支持同时上传符号表信息。具体请参考[上传软件包](../../../../../harmonyos-guides/发布应用/发布应用/ide-publish-app.md#section97874500234)。
* release构建模式下，如果app.json5的debug字段为true，则支持调试。

### 变更特性

* 已上架应用市场的应用不支持使用DevEco Profiler工具录制Anomaly泳道。
* @typescript-eslint/prefer-readonly-parameter-types和@typescript-eslint/no-magic-numbers中，规则的默认告警级别由error改为warn。具体请参考[规则变更说明](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查规则/规则变更说明/ide-codelinter-rules-change.md>)。
* @typescript-eslint/lines-between-class-members默认检查规则从成员变量之间必须有空行分隔，变更为成员变量和成员变量之间不需要有空行分隔。具体请参考[规则变更说明](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查规则/规则变更说明/ide-codelinter-rules-change.md>)。
* 覆盖率测试报告不再包含语句覆盖率，行覆盖率的统计方式存在变更。具体请参考[查看覆盖率报告](../../../../../harmonyos-guides/编写与调试应用/开发自测试/测试框架/黑盒覆盖率测试/ide-ui-test.md#section10394362109)。
* DevEco Studio已内置DevEco CodeGenie功能，无需额外下载插件。具体请参考[CodeGenie](../../../../../harmonyos-guides/使用AI智能辅助编程/工具概述/ide-codegenie.md)。
* 应用与元服务体检下线部分体检规则。具体请参考[规则总览](../../../../../harmonyos-guides/编写与调试应用/开发自测试/应用与元服务体检/附录/体检规则/规则总览/ide-app-analyzer-all-rules.md)。
