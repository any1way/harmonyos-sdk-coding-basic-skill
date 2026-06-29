---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-rules
title: 规则体检
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 规则体检
category: harmonyos-guides
scraped_at: 2026-06-11T15:30:02+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:7575751b1d78b4aa8e6be212cfebc8c77a94f328171d6bb731ea6bf7c6b17416
---
规则体检支持兼容性、性能、功耗等多种测试类型，开发者可自主选择不同的规则进行测试。

## 前置操作

1. 通过以下任意一种方式，打开AppAnalyzer。
   * 单击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/tklEBlpNTLGWXZM3XWF_og/zh-cn_image_0000002571546758.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=C9D8CC250327E14DE4DAE873621DE2C409703C16BA4566526997B367BCB47EC7)，打开AppAnalyzer页面。
2. 连接设备或启动模拟器，并对应用进行[签名](../../../配置调试签名/ide-signing.md)。
   * 真机：参考[使用本地真机运行应用](../../../使用本地真机运行应用/ide-run-device.md)连接真机。
   * 模拟器：在AppAnalyzer首页创建或启动模拟器，具体请参考[管理模拟器](../../../使用模拟器运行应用/管理模拟器/ide-emulator-management.md)。
3. 如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部**Python 配置**按钮进行配置。
4. 如果使用DevEco Studio 6.0.0 Beta2之前的版本，需要先编译生成HAP或HSP。使用Beta2及以上的版本，无需提前编译。

## 进行体检

### DevEco Studio 6.0.1 Beta1及以上版本

1. 点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/QXgrhpSIRjG56DlFFB1GEg/zh-cn_image_0000002602186281.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=FE83C07307B5D1DEC8A26F0BA7EF00897199E79D3F4CA065D1E010AB65A78438)图标选择Product、Target和构建模式，点击**Apply**后，在AppAnalyzer的首页中可查看对应的编译产物和构建模式。关于Product、Target、构建模式的介绍请参考[配置多目标产物](../../../../构建应用/配置构建流程/配置多目标产物/能力说明/ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](../../../../构建应用/定制构建/灵活定制编译选项/能力说明/ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/eNPbqVW3RT-F8VMTRU43Hw/zh-cn_image_0000002571546740.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=E7F7365780716C49008DA4D8927132BD440FFDC8B2D2CAB7408E54D8A7D6119E)
2. 在**AppAnalyzer**页面，选择**规则体检**，选择预置的体检卡片，或根据需要自定义卡片。
   * 点击预置的体检卡片开始体检，如需查看卡片包含的体检规则，请点击卡片右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YSvrbHeYTdmZm9UJbcazFw/zh-cn_image_0000002602066233.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=14E38B4E54403834B2CCFB50066AD6F411AF58C95BEA0695593FE52807D3BB47)按钮，规则详情请参考[规则总览](../附录/体检规则/规则总览/ide-app-analyzer-all-rules.md)。
   * 如果需要自定义体检规则，点击**+**，选择自动/手动测试和体检规则，部分规则可修改单次录制时长，请根据界面提示进行修改。

     如果仅选择稳定性规则，从DevEco Studio 6.0.2 Beta1版本开始，支持录制回放遍历模式，开发者先手动录制在设备上的操作，录制结束后AppAnalyzer会自动保存录制文件，选择录制文件开始体检后，AppAnalyzer会按照设置的回放时长，自动循环执行录制的操作，体检结束后可[查看报告](ide-app-analyzer-rules.md#li22241112508)。

     说明

     请确保录制过程可循环，例如从B页面开始录制，最后结束录制时要停留在B页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/MKiDlqbBQHqwLalHiFGlYQ/zh-cn_image_0000002602186277.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=76BC1C75CEA4F977C57565021EC7FE123AF3F0C2A5DA153B9D6EC20E64F3EB77)

   说明

   以下体检规则不支持在编译模式为release下运行，请把编译模式切换到debug再重新检测：组件树节点数目过大、执行函数耗时过长、渲染界面耗时过长、ForEach中item数量过大。
3. 开始体检后，请等待AppAnalyzer完成构建、签名、安装等操作。如果本次体检依赖Python三方库并且本地未安装，AppAnalyzer会同步下载安装三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。
   * 如果是自动测试，根据界面提示，登录应用账号后点击继续按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/7CPLUZ3fT8izla_ctRha1w/zh-cn_image_0000002571387118.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=50688D5B6F3165233808D01E9A57A75E75E250104DF89493747A5101BE187800)，继续测试；或者无需登录账号，直接点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/oStEshgGQ7mXjPtCYwCd3g/zh-cn_image_0000002571546738.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=3DA17D232E9931B2D9A75B3DAA90FC48FB7829A6DF502C5F660D86FFF9BF6A0E)按钮继续测试。
   * 如果是手动测试，根据界面提示，点击开始按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/giWB2SnwSnOmco0hXrbUlg/zh-cn_image_0000002571387114.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=3E381240F23E7C56E88F002117B3A8222B19663BC3808934FC4BDD0E30F8D853)开始录制，并手动遍历应用/元服务的功能。如果在录制时间范围内未遍历完成，可继续点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/ymxU-Km5RzC65LfzhZ745Q/zh-cn_image_0000002602066225.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=E522FB2B4248C5861CFB167F8DA2D923F02A5065D2BBC5EB38BAD8243572F71B)按钮，进行多次遍历，遍历完成后点击结束按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/dmb74_zPRf2zbAlcdTo--A/zh-cn_image_0000002571546752.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=49105400A584C46334724E8196F6E5B46620100D862F3FC5AE9D386F491A3920)。
4. 查看测试报告，包含以下内容。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对检测出来的问题，给出对应的最佳实践，点击链接可跳转至官网文档。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看[导出报告](../管理体检报告/ide-app-analyzer-history-reports.md#section78017171818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/n8pAtVu8QGOTDqqDTEK7PQ/zh-cn_image_0000002602186291.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=CA0333ECC4A593092706B8913C1962B90B3DA80FAA755A36521F24682A4FF871)

### DevEco Studio 6.0.1 Beta1以下版本

1. 如果使用DevEco Studio 6.0.0 Beta2及以上的版本，支持在体检过程中自动编译构建打包。点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/0S_-vyUwSoGFWuqs4sF4iQ/zh-cn_image_0000002571546756.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=9E12FE2EA45AAC98665A9F416F032ECF7CB4E0F5DBA435102ED3AD90568255D9)图标选择Product、Target和构建模式，关于Product、Target、构建模式的介绍请参考[配置多目标产物](../../../../构建应用/配置构建流程/配置多目标产物/能力说明/ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](../../../../构建应用/定制构建/灵活定制编译选项/能力说明/ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。
2. 在**AppAnalyzer**页面，选择**规则体检**，选择自动或手动方式，**模块**选择框选择HarmonyOS应用/元服务工程模块。
   * 自动方式：体检时无需手动遍历，AppAnalyzer会自动检测。
   * 手动方式：体检时需要根据提示手动遍历HarmonyOS应用/元服务的功能。

   说明

   * 如果使用DevEco Studio 6.0.0 Beta2之前的版本，只有已经完成签名编译打包的模块才能被选中。
   * 支持同时添加多个模块，要求所有模块的“bundleName”相同，且多个模块中只能包含一个entry。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/cE3W07LLRTavH6IEI2NW3w/zh-cn_image_0000002602066221.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=3CDB3A08CC85FAF62EC13BC60244B3C9D53FEF72B15A8384CBB035949F5DE214)
3. 选择待测试的规则，规则详情请参考[规则总览](../附录/体检规则/规则总览/ide-app-analyzer-all-rules.md)，然后在**AppAnalyzer**页面底部单击**开始**按钮，开始测试。部分测试规则依赖Python，请根据AppAnalyzer的指引，下载Python及三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。

   说明

   * 请勿在测试完成前点击结束，如果提前结束测试会导致测试结果不准确。
   * 支持Python 3.9~3.12版本，推荐使用Python 3.11.7版本。
   * 部分规则体检会进行投屏，如果测试过程中同时使用其他投屏工具，如DevEco Testing，可能会对UX测试的投屏造成干扰。如果投屏中断或不同步，可点击左上角刷新按钮重新投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/oiQY2gdGSJGWw7BTdXdITQ/zh-cn_image_0000002571546748.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=A7CBCCC7B3DF9AD57C43A08D859BA0D4282126B5E9F74050C92FF4C703CF38E2)
4. 如果是手动方式，在安装应用/元服务完成后，需要根据提示手动遍历HarmonyOS应用/元服务的功能。手动遍历完成后点击**结束**按钮停止测试任务，等待数据解析完成后，查看测试结果如下。

   * 测试报告：检测结果的汇总信息，点击**详情链接**可跳转到对应的详情报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/OVHvG9QFRZKD-JRuobJghQ/zh-cn_image_0000002571387108.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=3CC7021EBA5E22F6203FC14FF56D66D3FE31E2BD22F94876069C0BAF4568BCBF)
   * 详情报告：只包含检测失败的规则，给出详细的测试结果、相关的定位文件和对应的优化建议。
     + **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
     + **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
     + **优化建议**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行优化。
     + **Code Linter**：在“最佳实践测试”项目中，可直接在拉起Code Linter的同时，传递有问题的代码文件名，自动执行代码检查。在“快速性能测试”和“性能测试”项目中，因无代码文件名等信息，部分检测规则不支持自动执行代码检查，仅支持拉起Code Linter。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/6Bd0cxA0SDSiSs3RnUHGeg/zh-cn_image_0000002602066235.png?HW-CC-KV=V1&HW-CC-Date=20260611T073001Z&HW-CC-Expire=86400&HW-CC-Sign=8DB6D2550E992E0328756E416CBB71CD6E5FF5FF7D2E7DD60B88155F4F69389D)
