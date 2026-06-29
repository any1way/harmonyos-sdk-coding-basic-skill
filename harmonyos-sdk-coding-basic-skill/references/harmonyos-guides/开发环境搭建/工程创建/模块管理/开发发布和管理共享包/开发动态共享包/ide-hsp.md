---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:04+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:db6424e2cccb9eff28481fe54e6e4a4b86652f1056befeb4b9528df8a4e47f8a
---
DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](../../../../../基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

说明

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* 集成态HSP：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名。

## 使用约束

* HSP及其使用方都必须是API 10及以上版本Stage模型。
* HSP及其使用方都必须使用[模块化编译](../../../../../构建应用/提升构建效率/模块化编译/ide-hvigor-esmodule-compile.md)模式。
* 从DevEco Studio 6.0.1 Beta1开始，创建HSP模块时支持选择C++版本。

## 创建HSP模块

1. 通过如下两种方法，在工程中添加新的Module。
   * 方法1：鼠标移到工程目录顶部，单击鼠标右键，选择**New > Module**，开始创建新的Module。
   * 方法2：选中工程目录中任意文件，然后在菜单栏选择**File > New > Module**，开始创建新的Module。
2. 模板类型选择**Shared Library**，点击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Du802EDySOyDbppaOvaYYw/zh-cn_image_0000002602186103.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=1CC75817572631D1E923C4557E17135A8B71F9F1CCCABCAE44313A5D73185864)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/8n3tl1qeSJe1KyMgyJse3w/zh-cn_image_0000002571386934.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=4C9E0881C466E93A8E5C1711BAB09D730C4D04BC240FB10E8DA5567084036565)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/d7bQChT9SBeWE1jCTvN2DQ/zh-cn_image_0000002571546574.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=0299797275B0E6FC37DD60970CDB05B17AABBC8376CFA31B8C6AF38978ABA7C2)

## 编译HSP模块

说明

如果HSP未开启[混淆](../../../../../构建应用/混淆加固/ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](../../../../../基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/zNolzAaSRSynt0I0mrz2jA/zh-cn_image_0000002571386930.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=C70DD70B986B0BB5878E9678EF83F4590CD827416F4AB35A9CDA34235829B596)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/jZpPJRInQmOKxzmyb3f9nA/zh-cn_image_0000002571386936.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=81BF4EE512B09CFAEB76BEB1629841DE5B7F540374E536F3D7418164A9A07F7B)

如需在应用内共享HSP，请将HSP共享包上传至私仓（请参考[将三方库发布到 ohpm-repo](../../ohpm-repo私仓搭建工具/快速开始/ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_从ohpm-repo获取三方库)），请先按以下操作编译生成\*.tgz包。

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/zlobIy06THu-gBb9Kzxjxg/zh-cn_image_0000002602066047.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=71DED59903675B6F37C1926F1F45D693B0C7923A61537A240AA3CF689D17BF79)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/VRPW3PUGTCOc5J4lI08-hA/zh-cn_image_0000002602066045.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=6FAA600E97EDDD2E54ED5E0C58F53BB3875294DA6094EFFEDF9BAEAB2950EC21)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/eRr4LEPgR06PPxlp4mnnIQ/zh-cn_image_0000002602066055.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=D9573921816588CBF56A3B85324F07D4E23C6E2B4D3E4F84773FE9E4133280F5)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/fTFlISVVT8Ks0rvH382QTA/zh-cn_image_0000002571546566.png?HW-CC-KV=V1&HW-CC-Date=20260611T072203Z&HW-CC-Expire=86400&HW-CC-Sign=AB350F3957AB85E8B8B7EA479E4FF563E1D90C38003D5278A851D98E34D23DEF)
