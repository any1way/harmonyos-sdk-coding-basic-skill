---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy
title: Clang-Tidy代码检查
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Clang-Tidy代码检查
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:04+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:e88b354ccb94641e95053e6536e5dd01b18bd460c224bf10a19633e0aa63c473
---
DevEco Studio支持通过内置的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。

## 检查规则配置

当前支持通过三种方式配置检查规则。

### 方式一：在Clang-Tidy Checks中配置

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/71fWbGGWQ3Sa-JcgALqyRA/zh-cn_image_0000002572181928.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=328DDA04A76BD9DAD906FAD596B7D2AB949DCD0E1491BEC816FABE5F93B559B1)
2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/F-poghnQQmuebR9j_l9A0w/zh-cn_image_0000002602661389.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=70221A10D07FF995022EFD6EE8A72B5D2C6D56F597697BF23C561580A1E0DE15)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/4eq00gNUQy-oHi3xoTbVBQ/zh-cn_image_0000002572022288.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=1747497C4C52942D16B01124DF60858F2FCCDBB1FE8B4F283578EFC6665276E4)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/gAcsDL9cSRCUxla9EV8h9Q/zh-cn_image_0000002602781447.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=EE1F9D28B027EDA7AE4D0F838055A5DEFFC93290AB8EA953E435C93039427F24)

### 方式二：在 .clang-tidy文件中配置

1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/RYDtv1-LRN26RJH6chG2iA/zh-cn_image_0000002572181930.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=497F8D3E42C254922668A2F78EE341C8B562DED7DEC4366BFA84923E5C2E1922)

### 方式三：在Inspection-checks中配置

1. 通过如下两种方法进入Inspect Code。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jZ5OwLvmT4e63QeLTBe5oA/zh-cn_image_0000002602661391.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=7D6EE2187D3D314EC8FFCE4C09BAF1A74B1DC5A88FDCBAC2D22CF06294A719EF)
2. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/L4G4tMWLT5inA6SC02vv3g/zh-cn_image_0000002572022290.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=8296C16229F408DCCEAFBD32E597626DE5282AC0AE15F4A574B1883AC5466BA0)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/CXmYt56mTLSBNRCpGSXplQ/zh-cn_image_0000002602781449.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=874E82A7775492167CF66DAE2ED81276A72AB39AB858C5D730AD4A21540C8313)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/xBcxN_sGREWGUQN4ve5DTw/zh-cn_image_0000002572181932.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=901DA57AEE54FBDCFD6992E503C00D85888233616D4284ADEC11AC77DF725AEE)

## 代码检查

使用内置Clang-Tidy进行代码自动实时检查和手动检查。

### 自动实时检查

**生效规则**

若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)、[.clang-tidy文件](ide-clang-tidy.md#section158716295189)和[Inspection-checks中](ide-clang-tidy.md#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)和 [.clang-tidy文件](ide-clang-tidy.md#section158716295189)中配置的规则生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/bpdYs3LvRXWyFWrv6cnmZQ/zh-cn_image_0000002602661393.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=0936E247769C68A567FF02AF42D82D4CC09677E23740448C9FE4E9D6B4F42C4A)

**操作步骤**

代码编辑时，工具自动提示语法错误等，将标放置在错误代码处会显示详细的错误信息。

### 手动检查

**生效规则**

手动检查时，仅[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 通过如下两种方法，进入手动检查入口。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/V2zeVhVRT1WyBVgTsQ98kg/zh-cn_image_0000002572022292.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=B376901E44AE7CD4A1FD80ABB754B96DACCABE7FA01453FE0FD2E9275D597D19)
2. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/lafhaVulQ6OlYwyXS4EHww/zh-cn_image_0000002602781451.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=E09A47CC76ECDCF2775475AF5617786272F7F34A4EFFD61C838C53DC95F56DB8)
3. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/AP-DH_IPTJiy7hd6_HjZew/zh-cn_image_0000002611471503.png?HW-CC-KV=V1&HW-CC-Date=20260611T072802Z&HW-CC-Expire=86400&HW-CC-Sign=B63F29EDFCC73FF0D45557A556CDC5E4660B9B0669A649ECF57951C4248CE52B)
