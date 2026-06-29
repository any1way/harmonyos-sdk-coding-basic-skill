---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1
title: 调试过程中无法添加断点
breadcrumb: FAQ > DevEco Studio > 应用调试 > 调试过程中无法添加断点
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:36+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:29ad44d0d2c4e95cea8ef706c68675d681253d112c5094a6fadd3520f4ed170b
---

**问题现象**

调试过程中无法添加断点，提示“Can't set breakpoint to remote debug server”，如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/JvcPjJJqQnOWSh40G6pTmg/zh-cn_image_0000002250578541.png?HW-CC-KV=V1&HW-CC-Date=20260612T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5FEA556913DFD238B28A719BC4FDD30C53DB7D0B645C589B04448B0C6E94913D)

**解决措施**

请使用以下方法排查原因：

1. 检查是否存在xx.map文件。如果不存在，则需重新编译构建生成map文件，然后进行断点调试。

   * 对于stage模型工程，需检查sourceMaps.map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图1** stage模型工程中sourceMaps.map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/sb1LB0d3Q6CMt9VTJ4Q_eA/zh-cn_image_0000002250498437.png?HW-CC-KV=V1&HW-CC-Date=20260612T024435Z&HW-CC-Expire=86400&HW-CC-Sign=1EF7CF9BC1848439935F1081E7040EE8F7AD86698890F69203FE3CF15422EFCD)
   * 对于FA模型工程，需检查断点所在文件对应的map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图2** FA模型工程中map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/gvJ8X4yIR4uU1I6P829KNg/zh-cn_image_0000002215658548.png?HW-CC-KV=V1&HW-CC-Date=20260612T024435Z&HW-CC-Expire=86400&HW-CC-Sign=6870455989E6B12DCF23CEF187D55B0B1EBBCFD82651901089C5890C583283A3)

2. 检查代码文件是否已加载。启动调试后，如果断点所在代码文件未加载（已加载的代码文件会显示在下方**Console**中），则断点将无法添加。程序运行并加载代码文件后，断点即可正常添加。代码文件未加载的原因是未被入口模块直接或间接引入。

   **图3** 断点所在代码文件未加载  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/UstYSrsjRpy1qwoYMrymXA/zh-cn_image_0000002215498752.png?HW-CC-KV=V1&HW-CC-Date=20260612T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B4529F48D3DD1E92532C407D2F19D6E8CF21EDE37E63EEE58CAEC60C07DC62B7 "点击放大")
3. 断点添加位置无效。ArkTS不支持在方法的右括号单独所在行添加断点。

   **图4** 断点位置无效  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/B2WiWl3PSsiml6XLAQn9jA/zh-cn_image_0000002250578549.png?HW-CC-KV=V1&HW-CC-Date=20260612T024435Z&HW-CC-Expire=86400&HW-CC-Sign=6E918A0AC5C4218806DDF064DA905BB6CC35F61BACEC4B36C5F8060F6A336BC3 "点击放大")
