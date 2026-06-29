---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-184
title: 编译报错“Cannot read properties of undefined (reading 'split')”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot read properties of undefined (reading 'split')”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:35+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:480ae75c627b1a9c739754fdfa2439ba254fd87ccf5d3089fe4f2129ed0cd8dd
---

* 场景一：

  **问题现象**

  当前使用的DevEco Studio版本与SDK版本不配套，导致DevEco Studio抛出异常：“TypeError: Cannot read properties of undefined (reading 'split')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/L-b2LNYST-G5PRbb_iMRzw/zh-cn_image_0000002264138776.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=FB3667F54B5427B37E5271C210F8B75440048D1F62A6B3CDA902D7728A13AFB9)

  **解决措施**

  1. 访问华为[开发者官网](https://developer.huawei.com/consumer/cn/download/deveco-studio)下载最新版DevEco Studio。
  2. 使用新版本DevEco Studio打开待迁移项目。
  3. 根据DevEco Studio自动弹出的迁移提示进行操作。
     + 点击“Migrate Assistant”功能。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/3NOoe5EJSLeMCzbZN-d5PA/zh-cn_image_0000002264083104.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=D1197801F8FFBB2A9BFBC31A0676E8362BB56F7ED58D58B1D25320D7142AF5F4)

     + 从版本列表中选择目标迁移版本。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/hj-al2k6Taui7h3nibyZcQ/zh-cn_image_0000002264081160.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=911EC2D9B968C07C7EEBB22E30FCF9FF1FFBD27E99FA64ACD198AC2C5788942E)

     + 按照向导完成项目迁移流程。
* 场景二：

  **问题现象**

  当工程级 build-profile.json5 文件未配置工程外模块依赖，而模块级 oh-package.json5 声明了工程外模块依赖并在代码中实际引用时，编译阶段会抛出异常：”Error: Cannot read properties of undefined (reading 'split')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/CJNi6qV9Siex4SB-t3Z1Hg/zh-cn_image_0000002264140556.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=8F8A521EBD69FDE89EB6883A46C438364AAC4469B24B140F706EBD300217BB54)

  **解决措施**

  1. 检查下报错子模块中所引用的依赖，确保目标模块已在工程级 build-profile.json5 文件的 modules 字段中正确声明。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/AdZ_L_--R8yZ8w04o3tiMQ/zh-cn_image_0000002264140648.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=8F339904E8E9BF8A825B4894D7F29517A1EC1831CDCF94633867463838C20EA7)
  2. 确认当前子模块的 oh-package.json5 中，该模块已添加到 dependencies 依赖列表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/A9hs3h2mTRaINdQwBaaucA/zh-cn_image_0000002298773813.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=0E9B1ED0E013A4199C6CE76B63591E2A98AF477B7E6BAAE021250818937AB051)
  3. 若发现配置缺失，请手动补充完整。删除项目中的 oh\_modules 缓存目录，然后重新执行编译。
* 场景三：

  **问题现象**

  在HAP依赖字节码HAR进行编译的场景下，当import语句中的模块别名与dependencies中声明的别名大小写不一致时，编译系统将无法正确识别该依赖为字节码HAR，进而导致编译错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Jxh1SALSTGqPgP2gkcE-pQ/zh-cn_image_0000002264083960.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=F9C7952E233F4FC07DCC374038FD1A1647268E6AE538B8B6F200B84DCE544E11)

  **解决措施**

  请检查并确保所有import语句的模块别名与其在dependencies中的声明保持完全一致的大小写格式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/5nt2XGKyRdaM-05vq2DQIA/zh-cn_image_0000002298661041.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=3785502674F89F774FA160A74B90C44A1D3C093B75DA67F728C1D6475D2D3ADC)
* 场景四：

  **问题现象**

  在编译字节码HAR时，若将依赖配置于devDependencies下，hvigor构建系统在编译阶段不会收集devDependencies中的依赖项，导致依赖解析失败并引发编译错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/JVo2kIuTQ1Srr7g0yCSRew/zh-cn_image_0000002264141304.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=18B8CBBB00A32A491E48515323DC2F01E8D98F29F629CC62E8A1EA6B78A2ABD4)

  **解决措施**

  请将依赖项从devDependencies移至dependencies。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/wYgEfd-PRLWGi7kBtU-4wg/zh-cn_image_0000002264084432.png?HW-CC-KV=V1&HW-CC-Date=20260612T024334Z&HW-CC-Expire=86400&HW-CC-Sign=97319BA5AC3F2B05AAF4147450340A46C5E1FF0167F8638A0DD05B4BFB33252A)
