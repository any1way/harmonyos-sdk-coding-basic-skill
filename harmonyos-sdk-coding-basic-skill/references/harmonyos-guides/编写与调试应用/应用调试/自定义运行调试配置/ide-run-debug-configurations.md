---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:53+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:d8eb86b89b497e11276e1144d594ec288003a5d2ccc20e9c88d5e0125ad05b69
---
## 配置应用可调试

应用是否支持调试，根据app.json5的debug字段和build-profile.json5的debuggable字段综合判断，app.json5的优先级高于build-profile.json5。

1. 在app.json5中配置debug字段：
   * true：应用支持调试。
   * false：应用不支持调试。
2. 如果没有配置debug字段，则根据build-profile.json5的debuggable字段判断应用是否支持调试。
   * true：应用支持调试。当[编译模式](../../../构建应用/定制构建/灵活定制编译选项/能力说明/ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)不是release时，debuggable的缺省值是true，即支持调试。
   * false：应用不支持调试。当编译模式为release时，debuggable的缺省值是false，即不支持调试。

## 设置调试代码类型

点击**Run > Edit Configurations > Debugger**，选择相应模块，设置Debug type即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/jRTZRTMiQtm3LHyizPM26g/zh-cn_image_0000002602186461.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=0E91209F99375493595D66E0D66A8E2E6E95D165298CDE9ACD8485AD9761AE17)

工程调试类型默认为**Detect Automatically**，关于各调试类型的说明如下表所示：

**表1** 调试类型配置项

| 调试类型 | 调试代码 |
| --- | --- |
| **Detect Automatically** | 新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 |
| **ArkTS/JS** | * 调试ArkTS代码 * 调试JS代码 |
| **Native** | 仅调试C/C++代码 |
| **Dual(ArkTS/JS + Native)** | 调试C/C++工程的ArkTS/JS和C/C++代码 |

## 设置HAP安装方式

在调试阶段，HAP在设备上的安装方式有2种，可以根据实际需要进行设置。

* 安装方式一：先卸载应用/元服务后，再重新安装，该方式会清除设备上应用/元服务所有的缓存数据。

  从DevEco Studio 4.1 Canary2版本开始，支持当代码无变化时，不进行推包安装。即根据模块有无变化来判断是否重新推送安装模块包，在运行调试时仅将有变化的模块及依赖它的模块重新推送安装至设备上。如entry依赖了HSP模块，当HSP模块有变化，运行调试时将同时推送安装HSP模块和entry模块。
* 安装方式二：采用覆盖安装方式，不卸载应用/元服务，该方式会保留应用/元服务的缓存数据。

设置方法如下：

单击**Run > Edit Configurations**，设置指定模块的HAP安装方式，勾选**Keep Application Data**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/zkzp7mnfTcaIJfIj4mOhLQ/zh-cn_image_0000002602066385.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=3B05980BEB70540A7F2900F5EF3AAB726A95E52444C3D3E9D4A2FCFEFAA81199)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在“Installation Options”和“Launch Options”下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/JI36u97mTeKMCpXSQ05qww/zh-cn_image_0000002602066379.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=814BE6C61176DD9D0CE317E7D39D09CAA28FDACB5631013F28FF53E2CD65D976)

* Installation Options
  + DebugLine Support：勾选Enable DebugLine表示在build产物中系统组件增加debugline属性，用于开启[ArkUI Inspector源码跳转](../布局分析/ide-arkui-inspector.md#section1226015494335)功能。
  + Install Flags：输入bm install命令相关的选项，请参见[bm install 参数](../../../系统/调测调优/调试命令/bm工具/bm-tool.md#安装命令install)。如可以设置“-w 360”，表示将超时等待时间设置为360秒。
* Launch Options
  + Launch：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/kqI_seDiTUa1fdzlaon63A/zh-cn_image_0000002602066381.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=C58F18F52B3E43EA75B7E56CF2CB8DEFD39549406376E647472939DBF3B28F04)
    - Nothing：只安装不启动任何Ability。
    - Default Ability：默认的EntryAbility。
      * Stage模型：module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/GuzpZiXxS4KVvbtpGMskrw/zh-cn_image_0000002602186441.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=38E86661C2D92D924B7B5CC70FCB1FAC8B228DEDC3D84DFD97480E8B384021D2 "点击放大")
      * FA模型：config.json文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainAbility”指定的ability（该ability需存在于“abilities”数组内）；若“mainAbility”未指定，则取“abilities”数组内的第一个ability。
    - Specified Ability：工程中的UIAbility或ExtensionAbility。

      您可以在工程中添加UIAbility或ExtensionAbility，详细请查看[UIAbility开发指导](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/uiability.md>)或[ExtensionAbility开发指导](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/extensionability-overview.md>)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ax1X0sG0R7W-PZF_Lcqk8A/zh-cn_image_0000002602066383.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=09CBA6B0566D2ED5AD49C6EC1203E63BF2617DE5330BD6DBB417A21F43AAE345)
  + Launch Flags：输入aa start命令相关的选项，请参见[aa start 参数](../../../系统/调测调优/调试命令/aa工具/aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可在**Environment Variables**下配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/LmbLBTynRL-bdvJclfr9OA/zh-cn_image_0000002571387268.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=ED3D7CE0B584B04D240535DE7CF486566FCA44A1DF2792620D7BB8867D733A0C)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/GmtKr8oYSSi6WzZveToOoQ/zh-cn_image_0000002571387286.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=86C9912A4B8DDDD9C723AA6F50E1AA8C487DB56F993A4A87A657CFF1192E43EF)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/使用ASan检测内存错误/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

说明

当配置Environment Variables后，“Keep Application Data”覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选，勾选后点击**Apply**才可生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Rg6MUkyqRQWMMYO1oteWjw/zh-cn_image_0000002571387270.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=34E53D93C52D09D7B7080B6E79FC3FEC13F9ABDF150B4AC20C80EC511C3B77A9)

## 自动映射WebView调试链接

当应用中含有需要调试的WebView组件页面时，可以通过浏览器的DevTools工具进行页面调试，具体可参考[使用DevTools工具调试前端页面](../../../应用框架/ArkWeb（方舟Web）/Web调试维测/使用DevTools工具调试前端页面/web-debugging-with-devtools.md)。调试WebView组件需要执行转发端口等繁琐的命令行操作，因此可以在DevEco Studio中勾选**Auto WebView Debug**，该操作会在应用启动后两分钟内自动监听可调试的WebView进程并完成端口转发。

该功能从DevEco Studio 5.0.5 Release版本开始支持。

设置方法如下：

单击**Run** **>** **Edit Configurations**，在**General**中，勾选**Auto WebView Debug**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ZUcleXrXQAKs9UmIW2P2-Q/zh-cn_image_0000002602066373.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=386D36C1F27E8040C8A953F5AF158E0A422BE0AC8E79DF9C5A14D2FC245CD313)

开启后，当检测到设备上有可调试的WebView组件进程时，会在Run面板中打印转发成功的端口，通过浏览器的DevTools工具连接该端口即可进行WebView调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/-9rQzZ3tSYKtGBHd3SrQig/zh-cn_image_0000002571387292.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=80DAEFFDD7503597373EE192639DAB80BE4607A90D78DC35CC752E46F332156B)

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**Deploy Multi Hap****/Hsp**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**Deploy Multi Hap****/Hsp**中，勾选**Deploy Multi Hap/Hsp Packages**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Bp-tHQe8Qka0HzZhGzmQTg/zh-cn_image_0000002571387258.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=DC1D2974D01FEEDEE08A515811D637180EEB24A04DA28F872F1F9875F3949349)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以设置**Auto Dependencies**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**General**中，勾选**Auto Dependencies。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/yTgFLJCuTGCVebo8BhODxw/zh-cn_image_0000002571387288.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=81A07076623A6108E09D6B498DCF37ECF2BC70441640B59A7874D543B9553776)

在Before launch窗格中，您可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/aPwvVbs5RVukAL7jhl4Kvg/zh-cn_image_0000002571387290.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=7635C69AD4AFF06B991034A2C786DA9D008790E805A47E72FA632B9CC5D64AA7)添加应用启动前的任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/7l9gXOOAR2Ca3Dp37qGAdA/zh-cn_image_0000002602066387.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=68C3B43ABB1E1369702B7E05F34F44A41E03BF575022678742D535A0C1A5723E)

也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/9zbE67EdS7ei8xGufH9qBA/zh-cn_image_0000002602186455.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=BC058DC2433ACF6BE1CE6DF744B7502FB2063CE9F002E664CF914736B33A3386)移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/WFBaqdAWTg28dK6nk8IfgA/zh-cn_image_0000002571387260.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=BA1511BC2DB3135872204D6BE3755A01EE79AA8D93BA93BAB34D85344922BD40)

在勾选**Auto Dependencies**后，可以同时勾选**Deploy Multi Hap/Hsp Packages**，从而达到推送所有包的效果。

## 多设备运行

从DevEco Studio 6.0.2 Beta1版本开始，支持同时在多个设备上运行应用，包括真机和已启动的模拟器。

1. 在设备选择框中，点击**Select Multiple Devices**，弹出多设备选择框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/XUSB_MIZTk-5VjuwMeEaKw/zh-cn_image_0000002602066377.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=E6F01CF595F6D8C47F5A05F5AA530ED9983DF824E33AA3AACE92CE5AF323E1BC)
2. 选择需要推包运行的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/dESqQrEoQayXTrWnDILDpw/zh-cn_image_0000002602066405.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=F37BA5501F9FAE0998007130259F61FA30600D5076E5AF9B60EDAC0A02D2AE7A)
3. 设备栏会出现Multiple Devices(N)，表示选中N个设备，点击运行按钮即可同时在选中设备上运行应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/TJd9rN95QHWYa-Mxzstepg/zh-cn_image_0000002571546908.png?HW-CC-KV=V1&HW-CC-Date=20260611T072852Z&HW-CC-Expire=86400&HW-CC-Sign=31307DF2D7472DF464DEF19B110025BC6F153A5D343B7940F2DDE7F83FE3D3BE)
