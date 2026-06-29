---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test
title: Instrument Test
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > Instrument Test
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:51+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:e9a14ab6a7d58e471cd4c928dff303978428e918e35420351b8f7df32ef2f1a8
---
## 创建ArkTS测试用例

### 创建默认测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Instrument Test**或快捷键**Alt+Enter** **（macOS为Option+Enter）> Create Instrument Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/79P7yn0YSGy99njBNfugew/zh-cn_image_0000002602186603.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=88D87C70B1EA9D2474C5AC7A162B54B88110D8EB5AAF7860A5EF33D2BE0398A7)
2. 在弹出的Create Instrument Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit，JS语言默认为DECC-JSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/q1KCe0n-R72txVusWDPRIA/zh-cn_image_0000002602066535.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=84B8D19936398D5E43BEFD1CD540AC41F9283A998949E536E8A5B064EB571994)
3. DevEco Studio在ohosTest/ets/test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](../../../../../应用测试/单元测试和UI测试/自动化测试框架使用指导/arkxtest-guidelines.md)。

   说明

   * 您也可以手动在ohosTest > ets > test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾，否则将在运行时弹窗提示“Error: Test files must end with '.test.ets'.”请点击**Fix**按钮，DevEco Studio将自动对ohosTest > ets > test目录下的文件名进行修改。
   * 首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UiTest测试能力。

### 自定义Ability和Resources

从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。

说明

如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。

**表1** **新旧版本ohosTest目录对比**

|  |  |
| --- | --- |
| **新版本** | **历史版本** |
|  |  |

1. 创建以下目录或文件，文件内容示例可在[运行Instrument Test测试用例](ide-instrument-test.md#section1574003717165)后，在对应模块的.test/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1及以上版本）或build/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1以下版本）下查看，其中productName是当前生效的product，可以通过点击DevEco Studio右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/4Umf4CcxQteQ_-knH6deSA/zh-cn_image_0000002602186567.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=4D134E5F348B7241720DC675770D593F0C396F185FEF488B5CD19854C3FBFF22)图标进行查看。
   * testability目录 > TestAbility.ets文件
   * testability目录 > pages目录 > Index.ets文件
   * testrunner目录 > OpenHarmonyTestRunner.ets文件
   * resources目录 > base目录 > element目录 > color.json文件
   * resources目录 > base目录 > element目录 > string.json文件
   * resources目录 > base目录 > profile目录 > test\_pages.json文件
2. 在module.json5文件中补充ability配置字段mainElement、pages、abilities，关于字段的具体说明请参考[module.json5配置文件](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)。

   ```
   1. {
   2. "module": {
   3. "name": "entry_test",
   4. "type": "feature",
   5. "description": "$string:module_test_desc",
   6. "mainElement": "TestAbility",                                   // 对应下方abilities中的ability name。
   7. "deviceTypes": [
   8. "phone",
   9. "tablet",
   10. "2in1"
   11. ],
   12. "deliveryWithInstall": true,
   13. "installationFree": false,
   14. "pages": "$profile:test_pages",                                 // 对应resources目录 > base目录 > profile目录 > test_pages.json文件。
   15. "abilities": [                                                  // 添加的ability的配置信息。
   16. {
   17. "name": "TestAbility",
   18. "srcEntry": "./ets/testability/TestAbility.ets",
   19. "description": "$string:TestAbility_desc",
   20. "icon": "$media:icon",    // 确保引用的资源都存在
   21. "label": "$string:TestAbility_label",
   22. "exported": true,
   23. "startWindowIcon": "$media:icon",
   24. "startWindowBackground": "$color:start_window_background"
   25. }
   26. ]
   27. }
   28. }
   ```

## 运行测试用例

### 运行模式

使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考[使用本地真机运行应用](../../../../使用本地真机运行应用/ide-run-device.md)或[使用模拟器运行应用](../../../../使用模拟器运行应用/ide-run-emulator.md)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：

* 在工程目录中，单击**右键 > Run'测试文件名称'**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/9X1_mDmASxCa2UA3RnZP2w/zh-cn_image_0000002571387418.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=ED83EE41378B813DEEB4BF96CD23282CC28E1DBDE2C626D7912A966289B09729)
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/S762F-XrRz63zHcMqgHNJw/zh-cn_image_0000002571387438.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=73DFA61BDC696F88509B1FE8D348C1E5D392996FDA08C69F9DE958A849235521)
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-instrument-test.md#section65264166107)后，通过如下方式的其中之一，执行Instrument Test：
  + 在工具栏主菜单单击**Run > Run'测试名称'**。
  + 在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/kUufZsFjTFSjRawcH43zYA/zh-cn_image_0000002571547060.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=7B917C95DBBCD5DC972400E9DEFA5E8332006FC6016F8ED596D348CDF4AA4745)按钮，执行Instrument Test。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/d7r0Yfj4TtuIJux145G9eg/zh-cn_image_0000002571547058.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=42FB33251843A5303843F694C5B3884F700A9C1C029C16A92245F6DA4A6323FA)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Bt76Ml0gT-KjFGzb50PMjQ/zh-cn_image_0000002602186579.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=1408070CF4763EB64D533C20A2281743D199E77409319F6E38525282F8E9675D)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/hYh7CIhcT2qWfnfTdNUQJA/zh-cn_image_0000002571547040.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=5591F783A88B46824749C82DC02656E0B0EB9ECEEADC776306E48A03C91C7E63)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/i3-OfbfoReuXRfZJmx4yGQ/zh-cn_image_0000002602066551.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=1519B5A6E25D57E08666F78576BD949409211D52BD4E862CE9F196D35B22E180)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ZqMOCr3xQVmhI50Wklvdsg/zh-cn_image_0000002602186571.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=631A5377F3088D044E4AFC96ADE792B92C366DDA1EB759B3DCB3AC9A90AEE02C)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/cHUTjJSrSP6rbbim1NMugw/zh-cn_image_0000002571547034.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=4EF9CAB233C6B0E4B33304B18672CCBD4E192C94D60E03C526889EB0698FD1F0)

说明

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-instrument-test.md#section0164586312)。

### 覆盖率统计模式

在Instrument Test运行的基础上支持代码覆盖率统计。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](../../黑盒覆盖率测试/ide-ui-test.md#section13756446154)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/2xazFbuwSwmSMqdlPIu2Hw/zh-cn_image_0000002602186583.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=38A374016819B6290E69EBD849ED630C45E9A117BCCFF7D72B2E236B9323CFD7)
* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/kRsGsrqJQs-jfeY91Sn0CA/zh-cn_image_0000002571547046.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=151E766AB1A3446B5B276D0F5B26B474ECAB836253C922415D1537ACD730B448)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Gav_8ctNTwCCPQuKRs7q9g/zh-cn_image_0000002602066545.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=980DB25A3C94732F69FF0070175955CEB9B494C450299BC0B291C373FDED7738)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/3b8K24NMTWqpz8IkPtsWaA/zh-cn_image_0000002602066553.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=6E4B40715D905353CE746C7568F41A1CFB0D32B2DEDCA2682CC7DA196AA63CF4)

点击链接可打开报告，查看ArkTS代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](../../黑盒覆盖率测试/ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/imf9qL0URqKxijoj6V8MXA/zh-cn_image_0000002602066557.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=91FCB96EFD57230123364667B4CB0C2E24912B2DD473A1308FA28FE08FBEBB7E)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/ICervgx0Ru6bOwD8cCQCWQ/zh-cn_image_0000002602186573.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=BD83E2F4120B3920F910DF65FDCABEC6EAC6224ED4FC8AD044F226E1CC6250C3)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run** > **Edit Configurations**进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击+按钮，在弹出的下拉菜单中，单击Instrument Test。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/PObWTlRjQxy6u0_tEYqKjA/zh-cn_image_0000002571387434.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=92F39E4ED0E5D788EA2506E3239D05AD146B194C93B0AA70E7D2BBF91089CBC5)
3. 根据实际情况，配置Instrument Test的运行参数。然后单击**OK**，完成配置。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选“**Keep Application Data**”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选“**Auto Dependencies**”，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选“**Only OhosTest Package**”，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Rs4_vfJ8S4yW2_H10LnWGA/zh-cn_image_0000002602186595.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=244502F4645AEE115E5AAD13C2AFBDEF4F76EBB50F730DBEC7ED15F435617111)

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ZlsQNNmbTIa6iWfLnHXAmA/zh-cn_image_0000002602066543.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=E6A5468E80AB649F066551731959A75220CA4BB93E5ACDD8E6E9C7C504D2FF51)
2. 打开**Run/Debug Configurations**窗口，点击Test Args![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/YnWkT-cXQNaciypzCyHSxw/zh-cn_image_0000002602186591.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=D118213099C700FD7CFB1F41259D53B5696BA4D1CC1D6C32B722F64CE545E98F)，打开**Test Args**界面，添加命令行参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/jzeVBI66QdO-Co30AJOZfw/zh-cn_image_0000002571387428.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=09D1B6E6ED5793D09238A61C05BE3D4E0C7A9D00CBAE7EA8DDDD7D44EC466AF5)

   例如将测试参数配置为level=1, size=medium

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/ytVpSpPdQiOQpHpm_q-hPw/zh-cn_image_0000002571387422.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=262E4F3351333EDA2C2EFC8FF250E5557E5A3E6328ED1BB7B4034CD026F2F325)

   **表2** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/91xCPqTHSzWQ4dUPqm1Drg/zh-cn_image_0000002602066527.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=B9262790BA0F08C9C7A468AE607AA5A87BECAE29EE61CDEE84C0EA08A30BD17F)

### 设置调试代码类型

点击**Run > Edit Configurations**，打开**Run/Debug Configurations**窗口，选择Instrument Test，点击**Debugger**页签，设置Debug type。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/f9prL0S2SCmUtk3-YVQBXg/zh-cn_image_0000002602066521.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=40A0135E4D1EBA1C39A1CB6AB928C1D4CF05E2D5B37AD62450F1EC268B65C889)

调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：

| 调试类型 | 调试代码 |
| --- | --- |
| Detect Automatically | 自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。  如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。 |
| ArkTS/JS | 只调试ArkTS/JS，只出现PandaDebugger调试窗口。 |
| Native | 单独调试C++，只出现Native调试窗口。 |
| Dual(ArkTS/JS + Native) | 支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。 |

说明

调试C++代码时，当前模块及所有依赖的HSP模块的[Address Sanitizer配置](ide-instrument-test.md#section8352185341915)要保持一致，若不一致，可能无法进入C++代码的断点处。

### ASan检测

Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](../../../../日志与故障分析/故障分析/使用ASan检测内存错误/ide-asan.md)，当前不支持JS语言。

1. 在运行/调试配置窗口，选择对应的Instrument Test，点击**Diagnostics**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/TGaTqOt-QyWEIV3eWJ0JRA/zh-cn_image_0000002602066541.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=FCF2E72EE62141800202AC2C248D358B94F5D8C87ED80A0D78CF5EBFA00BF9DB)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/3grC8lWOQJqIU0Xi2x4TQw/zh-cn_image_0000002571387430.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=6211933033D037E1F7482B0267A3FFB5099B218082406CBAA083E42612550384)
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/YERqPuh5Sw-Fxrw8jKiH7w/zh-cn_image_0000002602066547.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=A2C04F7C35E3FE1BC0253FCF2D9CCE73A0AB45CD80FD5308AE31712BF3327B55)

## 测试C++代码

从DevEco Studio 6.0.0 Beta5版本开始，支持对C++代码进行测试，包括运行/调试C++测试代码、对C++代码进行覆盖率统计。

由于C++的测试so无法直接在设备上运行，需要通过Node-API的方式拉起，即通过ArkTS/JS语言拉起C/C++测试用例。

### 运行C++测试代码

1. 创建cpp测试目录，鼠标右键单击ohosTest目录，选择**New > C/C++ File(Napi)**，在ohosTest下生成cpp测试目录，以entry模块为例，目录结构如下。
   * **src > ohosTest > cpp > types**：用于存放C++的API接口描述文件。
   * **src > ohosTest > cpp > types** **> libentry\_test > index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。
   * **src > ohosTest > cpp > types** **> libentry\_test > oh-package.json5**：配置.so三方包声明文件的入口及包名。
   * **src > ohosTest > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
   * **src > ohosTest > cpp > napi\_init.cpp：**定义C++ API接口的文件**。**

   说明

   DevEco Studio生成的cpp测试目录中不包含C++测试框架，需要开发者自行选择开源测试框架使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/ckikVzMVSeWrkmnQ2wa-Mw/zh-cn_image_0000002571547076.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=26E0EC452C959D569D353FEAC06E592F88608B7C89B81AB50AA7891022A79C26)
2. 通过ArkTS测试用例拉起C++测试，示例如下。

   ```
   1. // ArkTS测试文件Ability.test.ets
   2. import entryTest from 'libentry_test.so';
   3. export default function abilityTest() {
   4. describe('ActsAbilityTest', () => {
   5. ...
   6. it('testNative', 0, () => {
   7. hilog.info(0x0000, 'testTag', '%{public}s', 'testNative it begin');
   8. let result = entryTest.runNativeTest();
   9. hilog.info(0x0000, 'testTag', '%{public}s', result)
   10. expect(result).assertContain("ended");
   11. })
   12. })
   13. }
   ```
3. 运行testNative测试用例，查看测试结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/me6uI_PcQFWwl88FHiK3FA/zh-cn_image_0000002571387432.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=354D9DF5D5B00634D53273E00500F6EF626B53667831E7F2FAB699E8A74DA5C8)

### 收集代码覆盖率

DevEco Studio默认不收集C++代码覆盖率，需要通过以下方式开启。

1. 在测试目录下的CMakeLists.txt中添加以下代码，开启覆盖率编译插桩能力。

   ```
   1. // DevEco Studio 6.0.2 Beta1之前版本
   2. set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   3. set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")

   5. // DevEco Studio 6.0.2 Beta1及以上版本，OHOS_TEST_COVERAGE在覆盖率模式下为true，在调试/运行模式下为false
   6. if(OHOS_TEST_COVERAGE)
   7. set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   8. set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   9. endif()
   ```
2. 在napi\_init.cpp文件的RunNativeTest方法中，调用\_\_llvm\_profile\_write\_file方法，将覆盖率数据保存到设备的/data/storage/el2/base路径下的c++\_coverage.profraw文件中，该路径和文件名不可修改，示例代码如下。

   ```
   1. extern "C" {
   2. void __llvm_profile_set_filename(char *);
   3. int __llvm_profile_write_file(void);
   4. }

   6. static napi_value RunNativeTest(napi_env env, napi_callback_info info)
   7. {
   8. char filename[256];
   9. snprintf(filename, sizeof(filename), "/data/storage/el2/base/c++_coverage.profraw"); // 覆盖率报告文件路径和文件名，不可修改
   10. __llvm_profile_set_filename(filename);
   11. // 开启测试
   12. ...
   13. // 结束测试，保存数据
   14. __llvm_profile_write_file();
   15. ...
   16. }
   ```
3. 运行覆盖率测试，选中ArkTS测试文件，单击**右键 >** **Run '测试文件名称' with Coverage**，执行测试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/nWAvQUm6TTeS89xCLZf6ZA/zh-cn_image_0000002571547038.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=18D6837B084480D513E247C569F490AAF1A369087299CE16E5E5FDF35D59E1EA)

   启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ETXVmrMbSfGFiE3V9Wq9Ng/zh-cn_image_0000002571547036.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=2C75D5E308BCFEF4E5ACE66120C8FBA54ACED51F401EAAEF42305673A68BE8DC)

   点击链接可打开报告，查看C++代码覆盖率详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/hx-MvkgdROeRVQutaTWrmw/zh-cn_image_0000002571547050.png?HW-CC-KV=V1&HW-CC-Date=20260611T072949Z&HW-CC-Expire=86400&HW-CC-Sign=B78F34EC9BA5648D2D5129D3A73BCECC92996EFB5AEE68A480A6E7623A67276E)

## 使用命令行执行测试Instrument Test

通过命令行方式执行Instrument Test，在工程根目录下执行命令：

```
1. hvigorw onDeviceTest -p module={moduleName} -p coverage={true|false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false}
```

* module：执行测试的模块，缺省默认是执行所有模块的用例。
* coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/ohosTest/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](../../黑盒覆盖率测试/ide-ui-test.md#section10394362109)。

  如果开启了C++代码覆盖率测试，会生成C++代码的覆盖率报告，路径：<module-path>/.test/default/outputs/ohosTest/cpp\_reports/index.html
* scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
* ohos-debug-asan：是否启用ASan检测，缺省默认是false。从DevEco Studio 5.1.1 Beta1版本开始支持。

  ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage\_data

说明

* 通过命令行执行测试时，不支持配置product，默认为default。
* 多个module和scope之间用逗号隔开。

测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt
