---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4b8e6de4643b67df0e2475ee8c160b3cd14abf2b99095f9364cdc96ae352465b
---
开发者可通过两种方式对[Extension Ability](<../../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/extensionability-overview.md>)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](../等待调试/ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/3_pma22ySXq4RoqwsjjM-A/zh-cn_image_0000002602186643.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=CC6AE11A3748B4CB39B0E13FABA58CEC6B2AD97F0E442E27F4A3E1D0FDD766CC)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/97WLqVw0TbK4iKUfrEv8qw/zh-cn_image_0000002571387474.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=73AE3C20BD96C74F143481DBDEDF78BDC4D5B5A32FA64ABC7AAF91FDBE1FB58D)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/ZvbRakz8Qf6xBMEGeFEg-A/zh-cn_image_0000002571547108.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=7A683F54091663156D2BFB7662551830C433BBCED2B503A0AF461CFE8E20D1EA)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/FNw7hA_1RrGcFo3iiT4-jw/zh-cn_image_0000002571547114.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=7AAEF1B1DC85656F5D48633581D4677BB5E46ADE705166DA0F041EFB31FE9FAF)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/ZvLIjvjqSxq88UMgEQiwAA/zh-cn_image_0000002602066591.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=011A0B0811E3617F22BEF888B61DB0B187C051E8C3579882F202BCB977D40AE3)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Jub1yVb3SPCGNAFfoCJCAQ/zh-cn_image_0000002602186649.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=D796166077DC74DF74A38A051DC8F2DC95DA07C052DE066E70A9B84FAC5D0D6D)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/InrF4mVCTqCanY5qas-yBQ/zh-cn_image_0000002571387476.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=1F7BD33D9C0896B191A2DA562B0D6BCF58D74E144FC826F0F6C39D0A2AA719B8)
