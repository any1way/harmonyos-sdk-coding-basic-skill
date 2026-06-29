---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:56+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6b3ac926cb2bf295d5a45f64791311cf68601578d941077e5bf68828e1f4f295
---
可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](<../../../../../../harmonyos-faqs/DevEco Studio/应用调试/调试过程中无法添加断点/faqs-app-debugging-1.md>)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/LW0zqs-TTOO97zCcNPSdbw/zh-cn_image_0000002602066083.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=1337069D1C57B5EA11192250DF084756E2E699389042B7AF85FD7339D5EF9C28)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/jxzKdKikQOWo9e2PN9Mrmg/zh-cn_image_0000002571546600.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=DEEBB522B51BBA7D77C69B6020B312403750A80E973D8060C4356DBAF8BB5953)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](../../../自定义运行调试配置/ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/pSOPSFF3TM2eHzvrg2SFVA/zh-cn_image_0000002602186133.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=9B5D231BA9D6079A31FFC5AE841772DBA21E3C566CF29584825186165E18CC1F)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/T8gKmBdISTmZFgHGfkpovg/zh-cn_image_0000002602186135.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=69F06A1F67FC6094B7B59FAE4EDBC0D759166FB698AAE466BBE4E68FB9B6094C)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/brm9dx42Qz6Cc9O4UDFLCA/zh-cn_image_0000002602186137.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=034A9D672D0D7812222971BEC3711E35D60A197DA347F1154058E2D42692F81B)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/0exhe0FgSf-qppRIVywoEg/zh-cn_image_0000002602186139.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=236922FEC2DB0566217235B3F4C2E906412B10E3E0253C1B567AA4E3BCF60C33)
5. 启动调试后，开发者可以通过[调试器](../../使用调试器/ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/dBguf3rKSaGZF_5_zwBFEw/zh-cn_image_0000002571546602.png?HW-CC-KV=V1&HW-CC-Date=20260611T072855Z&HW-CC-Expire=86400&HW-CC-Sign=6176329223DF8487221F338D6FB177AF2D315987F238917BB14F69658DE8DD5C)
