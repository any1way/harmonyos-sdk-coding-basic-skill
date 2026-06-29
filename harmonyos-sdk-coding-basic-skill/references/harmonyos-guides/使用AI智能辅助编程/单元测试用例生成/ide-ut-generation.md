---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ut-generation
title: 单元测试用例生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 单元测试用例生成
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:be017ed6a9f6a91d9e3f4ccf40b38d12fdc59d4dd08561d60eb5d90b9ec85d66
---
根据选中的ArkTS方法名称，CodeGenie支持自动生成对应单元测试用例，提升测试覆盖率。

## 使用约束

* 该功能最多支持解读30000字符以内的代码片段。
* ArkUI代码、生命周期函数、@Extend/@Styles/@Builder修饰的函数、private修饰的私有函数不支持生成单元测试用例。
* 单元测试用例生成时使用HarmonyOS Ask智能体。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后，在ArkTS文档中，光标放置于方法名称上或框选完整的待测试方法代码块，右键选择**CodeGenie > Generate UT**，开始生成单元测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/N4v1uaZrTzKfYX0nA0ZT5w/zh-cn_image_0000002571546514.png?HW-CC-KV=V1&HW-CC-Date=20260611T072229Z&HW-CC-Expire=86400&HW-CC-Sign=10C6FAC54F607B19AD2D82EE09DD28F5B7823EBECD39F4CD050D4CFE1541F374)
2. 在问答对话区生成单元测试用例后，点击Code Genie问答区中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/a8WPIPF4TIa2d_D4Q_9WNg/zh-cn_image_0000002571386888.png?HW-CC-KV=V1&HW-CC-Date=20260611T072229Z&HW-CC-Expire=86400&HW-CC-Sign=8517F7E18EEAE67A82C7DE035E85531CFC3335BBDD27FBD29E5FBB2C44D75013)可复制生成的代码，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/JExXqoUgQbe6IWoNxkAr_w/zh-cn_image_0000002571386882.png?HW-CC-KV=V1&HW-CC-Date=20260611T072229Z&HW-CC-Expire=86400&HW-CC-Sign=2E050B4B4A6C66D9CF925F3873E973DF1B9A820DAF50A656BB56A3C8B91F0DEF)将生成的代码插入到代码文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/k-s9qDZMRRWIK696BG2hmw/zh-cn_image_0000002571546526.png?HW-CC-KV=V1&HW-CC-Date=20260611T072229Z&HW-CC-Expire=86400&HW-CC-Sign=BE8EA591A59C63EF8C9EBEEDB610E0F1EFAF31CF2D3847845112E47CBCBB8254)弹出文件另存为框，填写文件名称后点击**OK**按钮保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/rF6073DGRdqeYGO-Ir_h7A/zh-cn_image_0000002602066005.png?HW-CC-KV=V1&HW-CC-Date=20260611T072229Z&HW-CC-Expire=86400&HW-CC-Sign=BBC01EC56748AE05955682A6D1AD079C874062AE547DA72FDF622B863E01FAE5)
3. 生成的单元测试用例文件被保存在待测函数所在模块下的**ohosTest/ets/test**目录，目录结构和待测函数保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/AE7aMSHUQtGYVdJiKzj8tg/zh-cn_image_0000002571386884.png?HW-CC-KV=V1&HW-CC-Date=20260611T072229Z&HW-CC-Expire=86400&HW-CC-Sign=C3E06D9E8B0F5E5C531B0AAC6085612A696EC0998835F72680B58BE1B3DF310B)
4. 运行单元测试用例，具体请参考[运行测试用例](<../../编写与调试应用/开发自测试/测试框架/代码测试/Instrument Test/ide-instrument-test.md#section14415226122419>)。
