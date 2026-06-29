---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-editer-overview
title: 代码阅读
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:47+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:031600e63e79b563a045d6f2e633520f1bb25db3a53d864ff36531a76f9b39dd
---
DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码关键字、运算符、字符串、类、标识符、注释等进行高亮显示，您可以打开**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**）面板，在**Editor > Color Scheme**自定义各字段的高亮显示颜色**。**默认情况下，您可以在**Language Defaults**中设置源代码中的各种高亮显示方案，该设置将对所有语言生效；如果您需要针对具体语言的源码高亮显示方案进行定制，可以在左侧边栏选择对应的语言，然后取消“Inherit values from”选项后设置对应的颜色即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/dyd6lRaWTfqEGKqi-4nDOw/zh-cn_image_0000002602186689.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=E6446A5DDA11FC6B2A76307FDB3934970D9A276239736811DEBB545B3F28FDC1)

## 代码跳转

在编辑器中，可以按住**Ctrl**键（macOS为**Command**键），鼠标单击代码中引用的类、方法、参数、变量等名称，自动跳转到定义处。若单击定义处的类、变量等名称，当仅有一处引用时，可直接跳转到引用位置；若有多处引用，在弹窗中可以选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/_St14Oc2TQqFuf0IKyMMyg/zh-cn_image_0000002571387520.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=C586121A90C4EA74F42BC09F2B93CE8DF03846C754E2F20055528722F9A2D55A)

## 跨语言跳转

DevEco Studio支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转其对应的C/C++函数，从而提升混合语言开发时的开发效率。您可以选中接口名称单击右键，在弹出的菜单中选择**Go To > Implementation(s)**（或使用快捷键**Ctrl+Alt+B**，macOS为****Command**+Option+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/6KmUfO8tSlObGLjTLENskA/zh-cn_image_0000002571387516.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=8A46163AC680338202FD1302404A80F2BB640F2AC664D58F1C0DB44FAFB54C7C)

## 代码格式化

代码格式化功能可以帮助您快速的调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，您也可以个性化的设置各个文件的格式化规范，设置方式如下：在**File > Settings > Editor > Code Style**（macOS为**DevEco Studio > Preferences/Settings > Editor > Code Style**）下，选择需要定制的文件类型，如ArkTS，然后自定义格式化规范即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/pK6Vh26GSWGIYV4Ik6tIZg/zh-cn_image_0000002571547176.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=E13C4FC63985F2CF60596A350140092AAE73BC99E0CC28F0B13F3B9BD4B008E9)

在使用代码格式化功能时，您可以使用快捷键**Ctrl + Alt + L**（macOS为**Option+Command +L**） 快速对选定范围的代码进行格式化。

如果部分代码片段不需要进行自动的格式化处理，可以通过如下方式进行设置：

1. 在**File > Settings >Editor > Code Style**（macOS为**DevEco Studio > Preferences/Settings > Editor > Code Style**），单击“Formatter”，勾选“Turn formatter on/off with markers in code comments”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/OzQ0OxkjTZuAtzhl0FHu4Q/zh-cn_image_0000002602186699.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=699087C5536A1AD726AA651D5102C6E9A5586DB3FBC6CC787A463DFF1E3A079A)
2. 在不需要进行格式化操作的代码块前增加“//@formatter:off”，并在该代码块的最后增加“//@formatter:on”，即表示对该范围的代码块不需要进行格式化操作。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/2_460B1TQj6C64p5ORWYjQ/zh-cn_image_0000002602066645.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=B67C6F19F22B6EB372AF0580680B278E9E937ABA296C5AD720EBD701E531F248)

若工程已配置code-linter.json5文件，选中code-linter.json5文件右键选择**Apply CodeLinter Style Rules**，代码格式化规则将与已配置的code-linter.json5文件中相关规则保持一致。code-linter.json5文件配置请参考[配置代码检查规则](<../代码检查/Code Linter代码检查/ide-code-linter.md#section19310459444>)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/JF3xtUYZSKKxukw1V92XTg/zh-cn_image_0000002602186681.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=456B61F9643F01F14E1AFBDBDAC228D00500ABA2EFB5CA374871A0CF4B5007FA)

## 代码折叠

支持对代码块的快速折叠和展开，既可以单击编辑器左侧边栏的折叠和展开按钮对代码块进行折叠和展开操作，还可以对选中的代码块单击鼠标右键选择折叠方式，包括折叠、递归折叠、全部折叠等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/A3iP3FKyRm2ltMhjZCECWg/zh-cn_image_0000002571547136.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=115FA2473001FA1D621156C340FDBF0620D32E87AE0E7022961F0A892C77799E)

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**（macOS为**Command+/**）进行快速注释。对于已注释的代码块，再次使用快捷键**Ctrl+/**（macOS为**Command+/**）取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/5Sn9rOPEQNWWSvlFeWIuDQ/zh-cn_image_0000002602066659.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=CF6157B20CCE5AA1D8F0D9705039FDDE85D8DF2A40615D5EEC08C85D766B445A)

## 代码结构树

使用快捷键**Alt + 7 / Ctrl + F12**（macOS为**Command+7**）打开代码结构树，快速查看文件代码的结构树，包括全局变量和函数，类成员变量和方法等，并可以跳转到对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/azJ0eru6RTmdJbjMQQwsMQ/zh-cn_image_0000002602066639.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=7D5B16236DE8A0C7B2769A27D5C364BFFE02582E24206DF8AA7B9060B9F571A0)

## 代码引用查找

提供Find Usages代码引用查找功能，帮助开发者快速查看某个对象（变量、函数或者类等）被引用的地方，用于后续的代码重构，可以极大的提升开发者的开发效率。

使用方法：在要查找的对象上，单击鼠标**右键 > Find Usages**或使用快捷键**Alt +F7**（macOS为**Option +** **F7**）。可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/YZarj49-R4yYySLdh5w0WA/zh-cn_image_0000002602066651.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=94EF941A5691F3B6C161B0AD5B3A7142E1EA0145F6CE2EBAA1A514DABEFE3205)图标查看变量赋值位置，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/QHN7uEAhRQCXf7CmIBSe6w/zh-cn_image_0000002602066611.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=35C838AB7194C71BEFF1F1E0F87EBE0D75B83D72A9F0FFFF7F37583016CE9C88)图标查看变量引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/K18gYEi_TUeOiAEstCyifw/zh-cn_image_0000002602186667.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=061F4C919FBF65A853F9737FECF21ED3FC774FF2308E5E8D0E1A29BB6C2A26DB)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**“/\*\*”+回车键**，快速生成注释信息。

说明

C++文件同时支持使用**“//!”+回车****键**快速生成注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/htS1TZGoRD6mfIZNYTNjOA/zh-cn_image_0000002571387514.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=8370C12E43D1DCAA143B84FA7C05E1041B4CB9F1E51FAFCE9CF39E58E876440E)

## 代码查找

通过对符号、类或文件的即时导航来查找代码。检查调用或类型层次结构，轻松地搜索工程里的所有内容。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/3f6-23z7SMW0oYEQ9t0EeQ/zh-cn_image_0000002602066609.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=A4284B6F5ECA6CC417D02D2953EAFBB4C8BAA534FE66AEFD5DCF0DC148455270)

## 快速查阅API接口及组件参考文档

从DevEco Studio 6.0.2 Beta1开始，Show in API Reference新增快捷键功能。

在编辑器中调用ArkTS/JS API或组件时，支持在编辑器中快速、精准调取出对应的参考文档。

可在编辑器中，鼠标悬停在需要查阅的接口或组件，弹窗将显示当前接口/组件在不同API版本下的参数等信息，单击弹窗右下角**Show in API Reference**；或选中接口或组件，右键点击**Show in API Reference**（或使用快捷键**Alt+A**，macOS为**Option+A**），可以快速查阅更详细的API文档。

说明

DevEco Studio集成了离线版API参考类文档，最新版本请参考官网[HarmonyOS API参考](../../../../harmonyos-references/开发说明/development-intro-api.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Fiy4AcjfR4Ort1p5_2Evgg/zh-cn_image_0000002571547152.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=A661D1D12EA58DD863CE6BF78AAD195225E6E917F38CF9D8B794E3A98A88A5E9 "点击放大")

在弹窗中可以查看：

1. 使用的API是否涉及权限申请或仅支持在测试框架下使用。
2. 使用的接口状态。**deprecated**标签表示即将废弃的API接口，可使用**useinstead**标记的API进行替代，请开发时关注。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/O7BB6zDDSouH5jdXb4xWVA/zh-cn_image_0000002571387544.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=9363D4D77075CC770D8FB4ABA161F76A3A34C0CDC0EAE59572F17CBD70D96CA5)

## Optimize Imports功能

使用编辑器提供的Optimize Imports，可以快速清除未使用的import，并根据设置的规则对import进行合并或排序。选择文件或目录，使用快捷键**Ctrl+Alt+O**（macOS为**Control+Option+O**），或单击菜单栏**Code > Optimize Imports**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ZP0m3owlRBuxAX_5TLQs_w/zh-cn_image_0000002571547134.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=B045E32E92B155578D7330AA1DB6A94C035E580C4B7EBBE0F01FB98194B94687)

如需修改优化配置，进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> Editor > Code Style**，选择开发语言（当前以ArkTS为例），在**Imports**标签页中，可选择在优化时是否需合并来自同一模块的import，是否需要对同一条import语句导入的元素进行排序，或对多条import语句按模块排序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/DgrUwy5YQmGoq9zQogzEbA/zh-cn_image_0000002571547156.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=AF96435415F2428CC983EE117E00EE5DDA38F77FBB397DA50ADD9C7B67265FD0)

## API变更查询

从DevEco Studio 5.1.0 Release版本开始，DevEco Studio中支持查询、对比从某个选定的SDK版本开始，当前工程中使用到的ArkTS API是否存在行为变更，并提供相应适配指导链接，帮助开发者完成工程代码适配修改。

从DevEco Studio 5.1.1 Release版本开始，支持对C API的变更情况进行查询，提供跨版本查询能力。

从DevEco Studio 6.0.2 Beta1版本开始，新增扫描进度提示功能，以及变更接口在代码文件中具体位置需在Code Location中查看。

从DevEco Studio 6.1.0 Beta2版本开始，API变更查询接入CodeGenie快速问答功能，CodeGenie提供根据代码文件和变更文档输出非兼容API的修改建议，以及新增筛选API变更类型功能。

### 使用约束

* 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* API废弃情况不在API变更查询的扫描范围。

* ArkTS API函数调用过程中，当开发者使用的API存在泛型参数和包含extends或keyof关键字时，不支持变更查询。示例如下：

  ```
  1. // API定义
  2. interface ProgressInterface {
  3. <Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>;   //包含extends或keyof关键字不支持变更查询
  4. }
  5. // API调用
  6. Progress({ value: 10, type: ProgressType.Capsule })
  7. .style({content:'Install'})
  ```

* 使用C++语法实现的API函数变更，不支持查询。示例如下：

  ```
  1. template <class _Rep, class _Period>
  2. cv_status condition_variable::wait_for(unique_lock<mutex>& __lk,const chrono::duration<_Rep, _Period>& __d)  //C++语法实现的API函数不支持查询
  ```

* C API扫描过程中，若存在与变更接口同名的函数，扫描结果可能会出现误报。
* 特殊调用方式下，不支持API变更查询。示例如下：

  ```
  1. // 反例：函数指针方式
  2. int (*sigptr)(int, const struct sigaction *__restrict, struct sigaction *__restrict) = &sigaction;
  3. sigptr(NULL,NULL);
  4. // 反例：回调方式
  5. callback(sigaction);
  6. // 反例：自定义宏
  7. #define MySig sigaction
  8. MySig(NULL,NULL);
  ```

### 操作步骤

**使用DevEco Studio 6.0.0 Release及以上版本，按以下步骤操作：**

1. 在菜单栏点击**Tools > API Change Assistant**，编辑区下方的API Change Assistant页签中，支持按模块查看API变更情况，选择需要对比的SDK版本号范围，点击**Start Scan**开始扫描。同时，有进度条提示扫描进度。

   说明

   API变更查询以选择的起始版本为基线，查询当前工程中所使用的API是否存在行为变更。如选择的SDK版本为5.0.0(12) Release 到 6.0.0(20) Release，查询的是5.0.1(13) Beta3到6.0.0(20) Release版本相比5.0.0(12) Release的API变更。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/9IGmKJoaTGmMFPSH37-cng/zh-cn_image_0000002571387530.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=4F870AFB9AB67BAD0973FA924563C9C683F273D6321CF5792307EE60CE1CC678)
2. 点击扫描结果中的代码地址，跳转到相应的代码编写位置；点击蓝色高亮的变更描述，跳转至版本说明文档中查看详情；修改完后可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/e_jD092WRyuY5ppi3SyJvw/zh-cn_image_0000002571387502.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=BEA6A68F53FDC59D1BFF806E80BB14D58EE2C4330C13CBF0C0E8C4A9ACB4C81A)图标，标注已修改。同时，可通过如下入口搜索或筛选API变更扫描结果、导出扫描结果数据等。
   * **Search**：支持在Search框中输入API名称或文件路径，对扫描结果搜索。
   * **API Version**：通过选择API版本，对扫描结果筛选。
   * **Language**：通过ArkTS或C语言，对扫描结果筛选。
   * **API ID**：通过行为变更的API接口，对扫描结果筛选。
   * **API Change Type**：API变更类型，取值包括All、UX visual Layout Change（UX视觉布局变更）、UX Interaction Behavior Change（UX交互行为变更）、API Behavior Change（接口行为变更）、API Change Deprecation（接口废弃变更）、API Definition Change（接口定义变更）。
   * **Fix Status**：API变更扫描结果的修复情况，All表示所有，Fixed表示已修复，Unfixed表示未修复。通过修复情况，对扫描结果筛选。
   * **Scan Again**：重新扫描。
   * **Export**：将API变更扫描结果数据导出到本地。
   * **Settings**：设置在扫描API时，可使用的最大堆内存的大小，默认值为3072MB。当工程代码量较大导致扫描缓慢时，可以调整该参数。
   * **Code Location**：变更接口在代码文件中的具体位置，点击可跳转至接口所在的代码行。点击位置右侧的**Quick Ask**可打开CodeGenie，在CodeGenie对话框点击发送，会根据代码文件和变更文档输出不兼容API修改建议；若文件中存在多处变更，CodeGenie根据文件中所有变更点输出不兼容API修改建议。

   说明

   通过Quick Ask打开CodeGenie后，仅支持使用HarmonyOS Ask智能体进行快速问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/zAx0kf_vS3uKkf9UGSCsDA/zh-cn_image_0000002602186695.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=F1ECEE1FBD66B4DF86B39F964EED2367D077F9C80FE6BB8344A440F9055C1398 "点击放大")

**使用DevEco Studio 6.0.0 Release以下版本，按以下步骤操作：**

1. 在菜单栏点击**Tools > API Change Assistant**，编辑区下方的API Change Assistant页签中，支持按模块查看API变更情况，选择需要对比的SDK版本号范围，点击**Start Scan**开始扫描。

   说明

   API变更查询以选择的起始版本为基线，查询当前工程中所使用的API是否存在行为变更。如选择的SDK版本为5.0.0(12) Release 到 6.0.0(20) Release，查询的是5.0.1(13) Beta3到6.0.0(20) Release版本相比5.0.0(12) Release的API变更。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/FZdphwd6SVSHft6ufDm81w/zh-cn_image_0000002602186717.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=21FE6143A33DC6349134CE005DC812736F401C73E12476EFC9D263BEF77190A4)
2. 点击Code Location中的代码地址，跳转到相应的代码编写位置；如需更多指导，可点击Guidance link中的链接，跳转至版本说明文档中查看详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/oap2qeXaRZewNOHn0px1AQ/zh-cn_image_0000002602066637.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=09BF404D11E4EC8C181E768FF09F5E07D7FE3EA82276B9818B4CEE15B623AC51)
3. 点击**Export**，选择API变更的存放位置后导出变更数据；点击**Scan Again**可重新进行扫描。通过右侧**Settings**按钮，可以设置在扫描API时，可使用的最大堆内存的大小，默认值为3072MB，当工程代码量较大导致扫描缓慢时，可以调整该参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/0XV27TO9RFWuE8VcdzOmzQ/zh-cn_image_0000002602066621.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=E5BFB584972AC7031E5F1AFE6D44E5B80F3A34E53D25C656F5A098F3DDA1B86C)

## 父/子类快速跳转

编辑器支持快速跳转至当前接口、类、方法、属性的子类/父类。点击代码编辑区域左侧的Gutter Icons（装订线图标）可以跳转到对应的父/子接口或类。如有多个继承关系，在弹窗的文件列表中选择需要查看的接口/类即可。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/OWyYQ6V1St24mWZoRJOD0g/zh-cn_image_0000002571387522.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=8B859B79F322E3A52185CA52834C7DFA955529D7B493DE606F37D964F67257D4)Implemented：支持跳转到对应的实现类或子接口及其对应的属性/方法。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/5gu_EahjQ5Cxer6rYvDIIg/zh-cn_image_0000002571387494.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=84D1A28C81A28C531B26EF499258174276990634E51D1492FA801B34D118156B)Implementing：支持跳转到对应的父接口或父接口的属性/方法。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/8U4muYKiSySKF266Zub7qA/zh-cn_image_0000002602186713.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=A5C6BB7E9390882BC0DAFA4D223DA9496760A3688AFC62ECBB55239F2013097F)Overridden：支持跳转到对应的子类或子类的属性/方法。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/alMs4iuxR6-H9p0vQl12Sg/zh-cn_image_0000002602186671.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=A34CC360A63ADF89B3B1D72337E66EB7C872B34AF81F52FBDFD86DD7609D6FC5)Overriding：支持跳转到对应的父类或父类的属性/方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/agbggTGRTlqk_QmBbzsR2w/zh-cn_image_0000002571547154.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=91AABEEAA3420E64B352217F74021A2C0E08465F6EDABAF6938F3D10DDF5105A "点击放大")

本功能默认开启，可以通过菜单栏进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> Editor > General > Gutter Icons**，通过勾选或取消勾选Implemented、Implementing、Overridden、Overriding四项可以开启或关闭该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/H7612JGVRzKVgxvVdH-l1Q/zh-cn_image_0000002571547144.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=F17C46CEF3800C65F3A8384B69644BD2887D320E0E2F3B21780757D76FBF7E3A)

## 查看接口/类的层次结构

编辑器支持查看当前接口/类父类或子类的层次结构。选中或将光标放置于类/接口名称处，使用**快捷键Ctrl+H**（macOS为**Control+H**），或在菜单栏**Navigate**页签下选择**Type Hierarchy**，在弹出的Hierarchy窗口中查看接口/类的继承关系结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/cnm68LuQRhisNP5-qfVvOg/zh-cn_image_0000002571387538.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=F9CAB4AB46C768ADFED9FEF5C6068FE17D7AA3A5D3D0B7D806EAB680EC6AECCF)

Hierarchy窗口按钮功能：

| 图标 | 功能 |
| --- | --- |
|  | 显示所选类的父类和子类。  该功能不支持查看接口的继承关系。 |
|  | 显示当前类/接口的父类。 |
|  | 显示当前类/接口的子类。 |
|  | 按字母顺序对继承关系结构树中的所有同级元素进行排序。 |
|  | 更新显示所有的类/接口的继承关系结构。 |
|  | 默认双击结构树中类/接口名称时，编辑窗口将跳转至所选类/接口所在的代码位置。勾选该选项后，单击结构树中类/接口名称，即可跳转访问。 |
|  | 展开/折叠继承关系结构。 |
|  | 锁定当前Hierarchy窗口显示于编辑窗口上。 |
|  | 将类/接口的继承关系结构导出到文本文件中。 |
|  | 关闭工具窗口。 |

## 添加嵌入提示

从DevEco Studio 6.0.0 Beta2 版本开始，在编辑时启用Inlay Hints嵌入提示功能，可以提供有关参数名称、类型等代码说明信息，提升代码可读性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/v3feFVyyT6O61K0YkbskMg/zh-cn_image_0000002602066647.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=DAE69A5FDF98D5055134E7706B08C2C4F06393080C17B0E0D42BC9A415E7753F)

进入**File > Settings**（macOS为**DevEco Studio > Preferences****/Settings**） **> Editor >** **Inlay Hints**，配置勾选希望展示的变量名称、属性、参数、返回值类型，点击**OK**后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/ANrhpLbXRXSxuqSMi1Ovpw/zh-cn_image_0000002602066643.png?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=C40AE8AA4A09E78B096E65494A29FA594A0D6AEC2BDA67EE24FEF248D7DAC7D4)

## Copy Reference

从DevEco Studio 6.0.0 Beta2 版本开始，在编辑页面选中代码行或类、方法、参数、变量等名称，右键选择**Copy / Paste Special > Copy Reference**，将自动复制定义处的地址。复制成功的地址可以在双击**Shift**弹出的搜索框中进行搜索，帮助开发者快速找到该接口的定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/1rE7PRpbR_6V3e6DwL-1Sg/zh-cn_image_0000002571387534.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071846Z&HW-CC-Expire=86400&HW-CC-Sign=3DDB19A7AEDA9BEE41B355353E5942A82EF0379FB09A1A6F92E14FB24AE86C7B)
