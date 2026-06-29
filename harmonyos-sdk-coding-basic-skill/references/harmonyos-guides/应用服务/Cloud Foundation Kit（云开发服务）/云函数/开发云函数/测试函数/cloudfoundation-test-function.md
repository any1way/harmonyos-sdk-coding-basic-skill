---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-06-11T15:05:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f72fb31766140b4bb1eeb4a1dbb2abc0100077bac09b50be79012e3e32108b0
---

说明

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/DDYXHNMtSjiOiTRDCD-00A/zh-cn_image_0000002592379222.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=71B10725B24FD53C3E3D5E8EFC6896623AA9C8A3E2FDA806DBFA8C42B8E40BA9)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/-2ESlTckQUi59uxSji1bKQ/zh-cn_image_0000002622858731.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=FA407AD3F0554EA1BA95C65881E6973F3DE9FA1936FE68E60FB169BED91A0894)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/eg99drfdScOyRzEkwlr9gA/zh-cn_image_0000002622698851.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=CB59A62A04E82C695E56B8E6FE989E11E89860403A9DD6700F9382F2E81BE963)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/AGg40WR-S4e3VLwqE5oyFQ/zh-cn_image_0000002592219290.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=09D860DB422228801A0B8D636F240079D5062215727C3E8940B5E670CC8E6D09)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          说明

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/na-UxjyAQOWXGUQ0DBeurQ/zh-cn_image_0000002592379224.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=7507458D961FC424DA9F8ED97AC57C26282ABABC5131AE1C00C649F796E4D2AF)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Fq5Mx4A9Sl-C8q7p7h8cGA/zh-cn_image_0000002622858733.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=3D1BC94DD675B40E20E7A61BA1E52037C1032C5A5FB153CA0A4ADF30DC6F0A56)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/TiKxDHsnQC2-qgg10_RRkg/zh-cn_image_0000002622698853.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=C796E3B60427442F6E5CD10C7B56F0FF497691A9185C382CC3712C9BFCA1A857)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/N5fbyw7URhSECbvS6Pdy-A/zh-cn_image_0000002592219292.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=5F0C0042EA8728B31BC80819D46B5202693F5B11AB5996FA020200DF047A3CCF)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/JsxTcPHkTMSG_GM_JgYW_w/zh-cn_image_0000002592379226.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=E4B714F9BF8ECCEA31D79D34A51CF6FCAC7C36ECE8506AB5780ED7253C9DAEFA)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/2_XwwqPtTcet7pDcCD49hg/zh-cn_image_0000002622858735.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=D068E5ECDA4A2D3B62E39CC0805231E7F1A5BA7095A37A8E29646E8357CA0F8D)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Zapjh6QGQWKHV4Yiw8fOYQ/zh-cn_image_0000002622698855.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=4ABF72F67EFCDD1103F9233C0959162BA434AAF7AB1F2E7A4467657C247130FB)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/jRtdV1WuQhGwccQ7RmIgUQ/zh-cn_image_0000002592219294.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=E630DC2903F3DECA9A7DF05B679A95F8E4444EBCD39DF5F65F0C0DFCFBBED21B)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/k-YKjlL_Sj2M_bVlWgpfYA/zh-cn_image_0000002592379228.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=4DD2D6332B4F455EE09AADF881801BFBA9C7A05A0498D66666B6593E812D54E1)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     说明

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/65M5cz18SsWOhJTH0nJR3w/zh-cn_image_0000002622858737.png?HW-CC-KV=V1&HW-CC-Date=20260611T070536Z&HW-CC-Expire=86400&HW-CC-Sign=C8FD32FD345087E1280138B0E656D7738C67D74809BE67B00EAD856B11E15ADF)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
