---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging
title: 三方库源码调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 三方库源码调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:18+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:c24e2ea4398232f8d58064dd37627e0bf2d48685614de476c00d516c09240ffb
---
三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。

## 区分字节码HAR和源码HAR

HAR包分为字节码HAR和源码HAR，同时满足以下两个条件的是字节码HAR，否则是源码HAR，更多关于如何构建源码HAR和字节码HAR的指导请查看[构建HAR](../../../../构建应用/配置构建流程/构建HAR/ide-hvigor-build-har.md)。

1. 查看HAR包的ets目录下存在.abc文件。
2. 查看HAR包的oh-package.json5文件，存在byteCodeHar字段并且值为true。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/eCglfYnLR8CmA9CrEoFWuA/zh-cn_image_0000002571546528.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=670F4AE2CDC35ADDE8F7F56A80D041AF7A81A16963D17AF0921618A4848164E0)

## 字节码HAR调试

### C++代码调试

如果HAP/HSP引用字节码HAR包，同时HAR包中包含C++代码，参考以下步骤对该HAR包进行调试。

1. 点击**Run > Edit Configurations > Debugger** **>** **Symbol Directories**页签，点击**+**，添加带调试信息的so文件，so文件在{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs/default/arm64-v8a路径下。

   说明

   在工程级或模块级build-profile.json5中添加strip字段并设置为false，可以生成带调试信息的so文件，具体请参考[配置CPP](../../../../构建应用/配置构建流程/配置CPP/ide-hvigor-cpp.md#section2182144382320)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Az2S17R4TtWG9iTz5ijjRQ/zh-cn_image_0000002602066007.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=A6D471B7F280D80578674E8EB5E91FFB88E7D87BDB0EC82BACBA4CB4DDF26490)
2. DevEco Studio调试应用时会优先加载配置的so文件，本地so文件包含调试信息时，可以正常调试源码。由于so的源码文件信息为编译时的文件路径，若与本地的源码文件路径不一致时，需要关联源码文件，有两种方式：
   * 方式一：可以在**LLDB Startup Commands**页签中添加命令做映射，示例如下。

     ```
     1. settings set -- target.source-map {old-path} {new-path}
     ```

     + old-path：编译时的文件路径。
     + new-path：本地的源码文件路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/FTW8cZ0JTWm1jegdqCZhmw/zh-cn_image_0000002602186063.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=E9A84DDD55259CA66F521FC320CA24F3907D26D0E75A83C3FD5D952F8DB62407)
   * 方式二：当Step Into进入汇编代码后，会弹出源码关联的提示，请点击**Select file**，选择本地对应C++源码进行关联。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/fDvPQMmdQ063KIbJI8PsCw/zh-cn_image_0000002571386900.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=D755A7AA286DB62056FA8770B23C96B61E58CE1AB8763DBD67F62953FEDBD853)

### ArkTS代码调试

假如在工程A（HAR包工程）中以debug模式编译得到字节码HAR包，工程B（主工程）中引用该字节码HAR包，并且本地有HAR包的源码，要调试该字节码HAR，有两种方式：在主工程中调试或在HAR包工程中调试。

说明

release模式编译的字节码HAR不支持调试。

* **方式一：在主工程中调试。**
  1. 在主工程中导入字节码HAR对应的模块，确保模块的层级目录与HAR包工程的保持一致，例如HAR模块都在工程根目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/yAvak_CPQ4Sr0crW9NSY2A/zh-cn_image_0000002602186067.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=77F01B11415EE841FB2D22F3B951D8BCBEC12FEB869C1A38E277A8EC1A684236)
  2. 导入成功后，由于debug模式编译的字节码HAR中包含[sourceMap](../../../日志与故障分析/故障分析/异常堆栈解析原理/ide-exception-stack-parsing-principle.md)，调试时默认会关联当前工程的源码，此时可以在HAR模块上直接添加断点。
* **方式二：在HAR包工程中调试，****通过修改前缀配置进行attach调试。**
  1. 在HAR包工程新建一个entry类型的demo主模块，如果主模块已存在则跳过本步骤。
  2. 在demo主模块的oh-package.json5中配置对字节码HAR包的依赖。

     ```
     1. // demo主模块的oh-package.json5
     2. "dependencies": {
     3. "@ohos/test_stage_ets_library": "file:./lib/test_stage_ets_library.har",
     4. }
     ```

     说明

     如果在demo主模块的oh-package.json5中，配置对字节码HAR模块的依赖，如file:../test\_stage\_ets\_library，调试时可能导致断点无效。
  3. 在HAR包工程主模块中调用HAR模块的接口，确保编译后主模块的sourceMap文件中包含HAR模块的相关信息。
  4. 构建HAR包工程，打开主模块的sourceMap，根据HAR的oh-package.json5中的name进行查找，将Index文件的前缀路径记录为localUrl，例如以下的demo|test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Vqy-yWvvQs69skS8V81XUg/zh-cn_image_0000002602186061.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=B056A4E05E4F83549DC2701DD636D3492A3D17D10065FA30404823FA6E3BB18D)
  5. 主工程应用在设备上运行起来后，在HAR包工程中通过attach方式对该应用进行调试，在Debug窗口获取程序加载时的前缀，记录为remoteUrl，例如以下的entry|@ohos/test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/YaqED2fdQqehyMzqkgnXoQ/zh-cn_image_0000002602066013.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=912CE24CA50E8AE9AE9BABC8591AE3AC7543F5F86ED32C6C3EA0A0A179C75855)
  6. 点击**Run > Edit Configurations > Debugger** **> Ets Source Pairs**，点击**+**，填写前两个步骤获取到的**remoteUrl**和**localUrl**。
     + remoteUrl：应用程序加载HAR包的前缀路径。
     + localUrl：本地生成sourceMap中HAR的前缀路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/8Xv7WpLcQ_-6MKv9edJ0mg/zh-cn_image_0000002571386892.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=8BA4D59371A44EA2382F54120F186C30D659AF3385BA45D6F6BA800D6BAE7234)
  7. 在HAR包工程中重新通过attach方式对主工程应用进行调试，此时可以在HAR模块上添加断点进行调试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/GJFQrT3xQ0upCWKpN6K_Rg/zh-cn_image_0000002602066009.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=F28DD6A4EBE87EE3B31221301100B0D54B67A70856F1D360A89BB210A907A7BB)

  说明

  如果在HAR包工程中同时配置[Symbol Directories](ide-source-code-debugging.md#section177418333199)和Ets Source Pairs，可同时attach调试ArkTS和C++断点。

## 源码HAR调试

### C++代码调试

如果HAP/HSP引用源码HAR包，同时HAR包中包含C++代码，可参考[字节码HAR](ide-source-code-debugging.md#section177418333199)进行调试。

### ArkTS代码调试

工程中引用源码HAR包，对该HAR包进行调试，根据本地是否有源码，调试方式分别如下：

* 如果HAR包在本地没有对应源码，此时应用构建打包时引用的源码来源是工程级oh\_modules目录下的源码，只能针对oh\_modules下的源码进行调试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/wD5b-a6wTMmLtg-3L2HMzA/zh-cn_image_0000002602066011.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=8BF585333117771AAF12658EB091419CC92052670AA8EF0FC65031776DD74EEE)
* 如果HAR包在本地有对应源码，调试时可关联本地源码以实现对源码的调试，有两种方式。
  + 方式一：参考[字节码HAR调试](ide-source-code-debugging.md#section1035165781918)。
  + 方式二：当Step Into进入oh\_modules中的ets代码后，会弹出源码关联的提示时，请点击**Choose Sources**，选择本地对应ets源码进行关联。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/kqVZcZ1KRyKzeuFmJjt-8A/zh-cn_image_0000002571546530.png?HW-CC-KV=V1&HW-CC-Date=20260611T072917Z&HW-CC-Expire=86400&HW-CC-Sign=4307D9145E5AC990B3135C6E01CD831C5F77B3D4B47479E9096223830E70E029)

## HSP源码调试

如果要调试HSP源码，需要将源码置于本地工程模块下，参考[字节码HAR的方式一](ide-source-code-debugging.md#li17359570194)进行调试。
