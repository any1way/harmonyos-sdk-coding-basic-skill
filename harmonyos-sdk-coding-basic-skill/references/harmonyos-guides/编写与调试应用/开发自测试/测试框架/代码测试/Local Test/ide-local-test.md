---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test
title: Local Test
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > Local Test
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:575e4ff0f618c11ee365e435765663cf200e995853d38654b5279ad9842bb743
---
说明

当前不支持测试C/C++方法及系统API。

## 创建Local Test测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/f67CgkNVRrGzRq8dLUM5jA/zh-cn_image_0000002602186741.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=CE0C38F087E52565DA666502787D14FCE162F898CB53B79EC0F35884154CD4CB)
2. 在弹出的Create Local Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/osh8NDAjSKKLCF0X_LR_Tw/zh-cn_image_0000002602186731.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=9986C0A1293507F8198ABA7EB80C3623C6B5E8BD21C233B226DE48310A061D72)
3. DevEco Studio在test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[单元测试框架](../../../../../应用测试/单元测试和UI测试/自动化测试框架使用指导/单元测试框架使用指导/unittest-guidelines.md)。

   说明

   您也可以手动在test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。

## 运行Local Test测试用例

### 运行模式

可以采用运行工程目录（test）、测试文件（如Index.test.ets）、测试套件（describe）、测试方法（it）的方式来执行Local Test，各级别测试执行入口如下。

|  |  |
| --- | --- |
|  |  |
| 目录级 | 文件级 |
|  |  |
| 套件级 | 方法级 |

以文件级别为例，在工程目录中，选中文件，单击**右键 > Run'测试文件名称'**，执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/j8QzVR6XTw-_pdXqBdbDDQ/zh-cn_image_0000002602186737.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=E781D9A7A0C5A756BFE37E690C57DA3A2ABEEED61152268A6AA1E105A9C8DBCC)

也可以通过如下方式，执行Local Test：

* 在工具栏主菜单单击**Run > Run'测试名称'**。
* 在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/a_n0R8EqTPuB6A5Ancfu2w/zh-cn_image_0000002602066699.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=0492A461A9B4ED06DE29559D2A22161D4D30E2F8239459EE9B087F32F2F636C6)按钮，执行Local Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/q4XhTNnwQ5idUtPu-z5APA/zh-cn_image_0000002602066681.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=3C2841DDCAF7E53FBB69D52C4DDF0E27A54ACF0667114AF153F57076079F1E5E)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/l8kL0QghSnyRl8JLtab__w/zh-cn_image_0000002571547206.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=98F03BB81F0C8486F5516CF30879B135E886DFB1D9516A7F2F5805B9AA04B95E)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/JdTjQGbrQYmOlTNkRwDTEA/zh-cn_image_0000002571387570.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=1DA4ADAD34FB00001695B576C4ADBDF11C9BE0696A4417016CDF1C8D25102EC8)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/1qCqJJwtRb-_u48Zkuo6Kg/zh-cn_image_0000002571387562.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=00E1F49F4999301C62A16F0C5C1CEF25F54E6A817B55CB11BD2215F6FFCA3905)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/szf7ttudQLCB3rsels_Tkg/zh-cn_image_0000002571547220.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=050F590FB1B3EFF09A3BB0EC5FFCE342DD05FA2C5EF28DB6C29D1D7168BA21E5)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/NJf0FhbjTmCI-u-z2ZwbDA/zh-cn_image_0000002571387556.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=09DB7526738912B4B3F65D26CD0FDC79AC3E9B34F8750E5960C6FAA9149E14BE)

### 覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](../../黑盒覆盖率测试/ide-ui-test.md#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/_o4tIpYyTT2rTCpXIBy0Uw/zh-cn_image_0000002602186755.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=C2A1757260480338AE66C63F497D7E9360B24FE3C92D57A0B27E0DEDC9B055D6)

* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/N53dLUXeTlOPYsZQAx7DPg/zh-cn_image_0000002571387572.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=C59D04D54498D731054E4575B208FC8551E6FE6DA99AEE8595A8C5D34C4C7608)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/zF4jZcpxTWOq21s5iyiHvg/zh-cn_image_0000002571387582.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=96A5596B7E5B092A657CA354D257B567CC04435BB48E80CB37FD46745E5E4B4A)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Ko-FI6YMTBSBhzkeiK9nRw/zh-cn_image_0000002602186733.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=3582BAB89D8035AA1D6778FC80AD3C949D5180D1C3CF6557CD323553D82361FC)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](../../黑盒覆盖率测试/ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/P509gqKXSqiSPZ_zdWu-yw/zh-cn_image_0000002602186739.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=9E450F533BC666C70828FBE6647FF26BFD848D87F17484ABA12D936FE065A041)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/A5wTOkDZRGOIlYFMILoFMg/zh-cn_image_0000002571387584.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=171298FC0148717B2FA2C2FD48C9EC85A8E61DD4A967C38E640FDEA8C10BDD7D)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run**>**Edit Configurations**，进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/y9sBFdefSY-O6oXh1HX_Xw/zh-cn_image_0000002602066673.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=F7685AA353E0D86A1764E7F3267A700A0D12D02469D2E6C2F31B6A3FB7156938)
3. 根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/I2shULzaTICtE8gpP5sRQg/zh-cn_image_0000002571547204.png?HW-CC-KV=V1&HW-CC-Date=20260611T072951Z&HW-CC-Expire=86400&HW-CC-Sign=91E7A63AE5F819F6358F9C4773AA3F355EEBCD3D0E4DDA4817C3F2ECDE2E069F)

## 使用命令行执行Local Test

通过命令行方式执行Local Test，在工程根目录下执行命令：

```
1. hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}
```

* module：执行测试的模块。缺省默认是执行所有模块的用例。
* coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/test/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](../../黑盒覆盖率测试/ide-ui-test.md#section10394362109)。
* scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。

说明

* 多个module和scope之间用英文逗号隔开。
* 暂不支持在Linux上执行该命令。

测试结果文件：<module-path>/.test/default/intermediates/test/coverage\_data/test\_result.txt
