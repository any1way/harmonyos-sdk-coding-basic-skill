---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-10
title: 编译报错“Failed to get a resolved OhmUrl by filepath xx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to get a resolved OhmUrl by filepath xx”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:05+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:686e796eb96bf5b7009686cf224f97f9310d4cc30c1fee3a7b4f8a00c7d96eab
---
* **场景一：**

  **问题现象**

  如果工程在本地可编译成功，压缩后拷贝到其他环境中再打开该工程编译构建失败，提示 “ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xx”。

  **解决措施**

  该问题源于工程中存在oh\_modules目录。由于oh\_modules中包含软链接，压缩后软链接失效，导致在其他环境中编译时无法找到对应的文件。

  删除工程中的oh\_modules，执行File > Sync and Refresh Project。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/i66Fk9JwQwqQUOAgPfhbbw/zh-cn_image_0000002194158588.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=C4E3ECD9B06C8CE3DABF32D48E7C43E3AC9A8A80A418E1E98905FCE335DC8EEC)
* **场景二：**

  **问题现象**

  当配置第三方包依赖时，如果将依赖配置到devDependencies，而源码中又引用了这些依赖中的 API，会导致编译失败。例如，第三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/gr的 API 时，编译会失败，提示错误信息：“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/h2f0-F-oQ16l7nvuvrVJSw/zh-cn_image_0000002229603977.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=BEAC988052DFF0B6A0D32C280AADE08936E24387D9FB207AA61312E21ECD7EE0)

  **问题确认**
  1. 进入上面标黄色的源码文件中，可以看到依赖有红色告警信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/AuflKULeQgeXM2NhV3ho8w/zh-cn_image_0000002194318188.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=D75680102A7F495064DCEC05CA9289F2D114B5EC6F3721D855007954C16D2752 "点击放大")
  2. 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/vcH7BtTjRMGWISb8GhRXyQ/zh-cn_image_0000002229603989.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=6E9492FD235F3170971EC154E08035CE9E90F0CD5B3B7E6E1E6E419E4DA7888E)

  **解决措施**

  + 向开发团队建议：运行时的依赖不应配置在devDependencies中。
  + 在依赖上层引入对应的devDependencies中的第三方包规避此问题。

* **场景三：**

  **问题现象**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  **问题确认**

  检查工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与实际路径不同，以及是否存在大小写不一致的问题。

  **解决措施**

  将build-profile.json5文件中modules字段的srcPath路径与真实路径保持一致。
* **场景四：**

  **问题现象**

  工程A以相对路径引用了工程B的模块，这种引用会导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/whARJ4ifRrCEqFmNIjFQWQ/zh-cn_image_0000002194318200.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=A03C6476851B87D384AAE5288BB00A651B2CEE45BC523876B43983B4A10AFFF5)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/DxV5Ga4vRJGS0tWGr0m1MQ/zh-cn_image_0000002194158572.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=9DD7063E20B5B46F9EF600F7188A489D6C867063A4737C546C2EBF9CC9AE406A)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/HDY5JqEHT46XBjJD7XfnFg/zh-cn_image_0000002229758449.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=81E03D201C99461A5B695E961D46C64E67145DF7B36A3EEAFDB81058635E8C1D)**处理措施**

  + 将工程B的har转换为工程A的一个模块引用。
  + 把工程B的har提前打包，在A中 以.har的方式引用。
  + 上传到仓库，以版本号的方式引用。
* **场景五：**

  **问题现象**

  DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\\_ignore\\_xxxxx' imported by xxx”。

  **处理措施**

  如果hvigor\_ignore\_xxxxx所在的模块是一个har模块，需要排查oh-package.json5中是否存在“"packageType": "InterfaceHar"”，如果存在，请删除“"packageType": "InterfaceHar"”。

  如果hvigor\_ignore\_xxxxx所在的模块是一个hsp模块，需要排查${模块路径}\build\default\cache\default\default@CompileArkTS\esmodule\${debug/release}\filesInfo.txt文件中是否存在hvigor\_ignore\_xxxxx路径，如果存在，可将hvigor\_ignore\_xxxxx路径所在的模块或包添加到当前编译模块oh-package.json5的dependencies中临时规避。
* **场景六：**

  **问题现象**

  DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for‘xxx’imported by‘yyy’”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/h1DZ2qfqRfegbb-Cy41_bA/zh-cn_image_0000002194318204.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=4B83121F22EEC0A290118577FA56A3FC79E385890951E115D2AAC1D120ECE3C4 "点击放大")

  **问题确认**

  1. 检查yyy所在模块是否为[字节码HAR](../../../../harmonyos-guides/构建应用/配置构建流程/构建HAR/ide-hvigor-build-har.md#section16598338112415)，并查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false）。如果为true，则默认构建字节码har。
  2. 如果yyy模块是字节码har，请检查xxx依赖是否已配置在工程级oh-package.json5的dependencies中，但未配置在yyy模块级oh-package.json5的dependencies中。

  **处理措施**

  + 将xxx依赖配置到yyy模块oh-package.json5的dependencies中。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/HaSODAagS7mTiDhWkFc28Q/zh-cn_image_0000002229603981.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=5A595C33E1F9BF9BC74DB1C0ED8AA5B31D60F34332C30308F02EC4831452F94E "点击放大")
  + 将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。

* **场景七：**

  请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看DevEco Studio和SDK版本，版本配套关系请参考[版本概览](<../../../../harmonyos-releases/历史版本/HarmonyOS 5.0.2(14)/版本概览/overview-502-release.md>)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/k6r4EP6HRF2e4IRTszj1xQ/zh-cn_image_0000002229603985.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=63DFFAEB008B2FA53E414B4D1CE9BB0525F1EF56943F9854018E589F6AAE0CEA)
* **场景八：**

  **问题现象：**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR failed to execute es2abc ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  **处理措施**

  该问题由工程中引用了非标准模块目录（目录内无module.json5）引起，如下图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/6_baM3ZSTCyCKzBlthqTnw/zh-cn_image_0000002194318192.png?HW-CC-KV=V1&HW-CC-Date=20260612T024104Z&HW-CC-Expire=86400&HW-CC-Sign=823547D6F02FC3FB7914A1FBD1C6550756B21E6CD9B3AF9552ABCDEA706E3970)

  请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。
