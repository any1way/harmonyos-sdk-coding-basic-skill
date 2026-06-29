---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugfunc
title: 调试函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 调试函数
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3fc60fbb738aa3a28042aa0233fe58de47db8ae31d3c9c662b74b2cc3cb2f0ec
---
函数开发完成后，您可以对函数进行调试，以验证函数代码运行是否正常。

目前DevEco Studio函数调试支持本地调用和远程调用，请根据实际场景选择使用：

* [通过本地调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section248615546567)：在DevEco Studio调试本地开发好的函数。支持单个调试和批量调试，并支持Run和Debug两种模式，调试功能丰富，常在函数开发过程或问题定位过程中使用。
* [通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)：先将函数部署至AGC云端，然后直接在DevEco Studio调用云端函数。此方式主要用于测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调用方式中发现的问题。

## 前提条件

* 请确保您已登录。
* 如果您的工程有代码逻辑涉及云函数调用云数据库，您需在调试前先[将整个云工程部署到AGC云端](../../../部署云侧工程/agc-harmonyos-clouddev-deploy.md)，否则云端将没有相关数据及环境变量。

## 通过本地调用方式调试函数

您可在DevEco Studio调试本地开发好的函数，支持单个调试和批量调试，并支持Run和Debug两种模式。

* 单个调试和批量调试流程相同，区别仅在于：单个调试是一次只为一个函数启动本地调试，之后只能调用该函数；批量调试是一次为“cloudfunctions”目录下所有函数启动本地调试、然后逐个调用各个函数。
* Run模式和Debug模式的区别在于：Debug模式支持使用断点来追踪函数的运行情况，Run模式则不支持。

下文以Debug模式下调试单个函数“my-cloud-function”为例，介绍如何在DevEco Studio调试本地函数。

1. 右击“my-cloud-function”函数目录，选择“Debug 'my-cloud-function'”。

   说明

   * 直接从当前路径下Debug，使用的是默认的Debug配置，您也可[自定义Debug配置](agc-harmonyos-clouddev-debugfunc.md#section65830284215)。自定义Debug配置后再从此路径下Debug，将优先采用自定义Debug配置。
   * 如需批量调试多个函数，右击“cloudfunctions”目录，选择“Debug Cloud Functions”，即可启动该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，将会启动所有的云函数和云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/yA4YmGVWQIeGMzaeP0bOXA/zh-cn_image_0000002214858717.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=CF558BCBFD08CF5F2E2E4A8FDF02C134F35180D9FB80772A48D19870F07EC7F3)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示函数成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zRbFK7W-TkiWKVHMo5ijGQ/zh-cn_image_0000002214704369.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=1714B7801525848E099EDDB3E3DF9BB8079175B0B63310C438035406846922D4)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行15）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/uftoMu23Tiu1Zy7xEp43pA/zh-cn_image_0000002533684069.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=22361CDDE958A4A3A8CA24116F8999230A6CA611F8DE8254DD3E77D94AF6BB18)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/kiPwfaB_SQOq89IZxfmisA/zh-cn_image_0000002179338456.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=AC768D99811F3329559CA8DADBF07B496E9E0AA1CA6C8D2D7FF4E889432264E1)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Local”，表示本地调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/VU93WatdRWm6Sesw4aLHwQ/zh-cn_image_0000002179338412.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=839ED986FF0178ABD5F6F93B9D18F05F7EFD4F2A9B1CB9F9C47244A19A265E83)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/i7R7iutgSy2r01lH0uJH7A/zh-cn_image_0000002179498072.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=A00965FA033A55DF6B704FC0AEAEE5512143745EA0A07C628997176CBEAF9EBA)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WPyWk3dxSJW-S8QtqfW7SA/zh-cn_image_0000002179498132.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=B59C45722899A75B8ACC229818837D382BF8CFFAB464992892824D02AF0552DC)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/CDz1dFgoQm-e1MCPKLDscg/zh-cn_image_0000002278063192.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=BF249ABAD8581034BE9CFF64061C746CAC2ABDD5B9AE5E770D54F2A4395167DD)
7. 点击“Trigger”， 将会触发执行用户函数代码。执行结果将展示在“Result”框内，“cloudfunctions”窗口同时打印调试日志。

   说明

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/2z7metrES0yTsve0F9r3Ow/zh-cn_image_0000002503613920.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=DF2552A5207CDB52F866243946CAAE11C219EEC4C2F4278F775DA701C3637744)
8. （可选）如[配置了环境变量](agc-harmonyos-clouddev-debugfunc.md#li15793566149)，可将变量信息传入到函数执行环境中，用于函数运行时读取。

   ```
   1. logger.info(context.env.name);//name为环境变量名称
   ```

   如下图，函数“my-cloud-function”配置了环境变量“env1”，可成功访问环境变量“env1”的值“value1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/fM7BWGiRS-CHrgVR-c84AA/zh-cn_image_0000002503615754.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=C5C6627618F7BE874BB1A14AF43B6FDABB5899943F672DD3C53BF432D2BBF8DE)
9. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/YQBFNYMbSuWXxc9gLECOeQ/zh-cn_image_0000002179338396.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=F74AEF0BA65C931A7AF4997371D36BC2F6374E1EC113F39D46C62A94E83BA379)，可停止调试。
10. 根据调试结果修改函数代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/hIQOfMDlRa2CfLldyYCkaQ/zh-cn_image_0000002179338420.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=75181FDAA526ACF5BF00B034D7D4117A8CF0C1A87D7FA337F7286EFB4C9E6C99)重新以Debug模式启动调试，直至没有问题。
11. 参考步骤5~10，完成其他函数的调试。

## 通过远程调用方式调试函数

您还可以将函数部署至AGC云端，然后在DevEco Studio调用云端函数，以测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署函数](../部署函数/agc-harmonyos-clouddev-deployfunc.md)将需要调试的函数部署至AGC云端。
2. （可选）如函数代码涉及访问环境变量，需在AGC Portal函数列表中点击函数名称，为函数配置环境变量的值，供函数在运行时读取和使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/lQOKK5s2QjSLrAzFdaXsOQ/zh-cn_image_0000002214858729.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=03BF272AE1D8D3AC9F061D029564A632C53090450CCA5DB598E1E8F8FC7D4CA0)
3. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/omFiczxBT8axkQbZALT9oQ/zh-cn_image_0000002179498140.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=04020F7B878BBA0D952BCDDBB2ACC66BA0B678CCE2879012755A8F1D3AD22B81)
4. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处依然以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Remote”，表示远程调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/jobdzVVnTmiDyOVMPGltdQ/zh-cn_image_0000002179338388.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=76EE0B853059515E2458AE6F9707690D9E5A3FAD4ADA3E8FEC03449DA5720D65)
5. 点击“Trigger”， 将会触发执行用户函数代码，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/KaNgjRMATECb2ErTK3FGcA/zh-cn_image_0000002214704345.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=F0BAC526A83649672375A7BDAD736313130F84F6CE0E2520F55FC1202C6B5FA4)
6. 点击“Logs”页签，可查看打印的日志定位问题。修改函数代码、重新部署函数后再次执行远程调用，直至没有问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/xdN0UaCyQSKnNcfneRHEtw/zh-cn_image_0000002535303613.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=A87613DCED497F68B5DEC75FED6BBCFE8BD0B5A5E7422C89D40464A68D4EDD01)
7. 参考步骤1~5，完成其他函数的调试。

## （可选）自定义Run/Debug配置

直接启动函数调试采用的是默认的Run/Debug配置。如有特殊需求，您也可使用自定义Run/Debug配置项来进行调试。

1. 在菜单栏选择“Run > Edit Configurations”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/qTaW8T_4SKKCB_rEz3QoNA/zh-cn_image_0000002179498096.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=756CA0DFF018636F30D2C0F0B31E5B13BA56748C13FD4D2E737E0AF3382B8DF4)
2. 在“Run/Debug Configurations”窗口，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/JqHo83UqQ8yYrHGrIK2SPw/zh-cn_image_0000002214858773.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=AB4313F096F46BDEA72E9528A1E05B70CD598E367A362F46BA6158CD65DE1C9D)，选择“Cloud Functions”，新增一个Run/Debug配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/hv1NQCqUSB2DbukUQ17cTA/zh-cn_image_0000002214704341.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=F3D5CF8CA0A9179F6A819DC2EBC539A8E5192FF0166CB8118BBA909C18AADBE0)
3. 自定义Run/Debug配置，完成后点击“Run”或“Debug”即可立即按当前自定义配置启动本地调试。

   如当前暂不使用自定义配置，可点击“OK”保存配置。后续有需要时再选择自定义配置，分别点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/GC27aGQ3RY2fqaHyECZK-Q/zh-cn_image_0000002179338416.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=7CEA0AFE1BAB9DE97917A32F08E34271ABFB3B674105CDEC58A37766E7CA8DCF)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/hyjI7DYbTGCLa26AWMn6ZA/zh-cn_image_0000002214704373.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=3533357700604D13C21FE43D2328190BD99509548DB7D3024A1AEAAC85AB7890)进行Run或Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/1LpCk8GYTAGIuCTk1seUsQ/zh-cn_image_0000002214704377.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=3C8592AFEA9DABDDF514E60CC30088107BB57E9A545D842A30F669D83E57F627)
   * Name：Run/Debug配置的名称，如“functions-custom1”。
   * Server IP Address：HTTP服务端监听IP地址，默认为localhost，支持切换为您的局域网IP地址。
   * Server Port：HTTP服务端监听端口。默认为“18090”，自定义端口号建议大于1024。勾选“Auto increment”表示如当前端口被占用则端口号自动加“1”。
   * Environment variables：函数运行的环境变量，为key-value形式。

     点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/QaFZslAhQKqoRBW3gp6Rhw/zh-cn_image_0000002179338424.png?HW-CC-KV=V1&HW-CC-Date=20260601T071823Z&HW-CC-Expire=86400&HW-CC-Sign=C09D7E978F6BBC3DC616E50149F409C4673A445C60604507769CDE6B9DBBE182)
