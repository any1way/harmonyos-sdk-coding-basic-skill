---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-20
title: 修改代码后使用Hot Reload不支持情况说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > 修改代码后使用Hot Reload不支持情况说明
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:49+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:28b01bd7872b190810adda168c14672c64f4556b21b3c41646c63413eee4996e
---
**问题现象**

执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Vc_gzedDSemIqcoF1L0yWQ/zh-cn_image_0000002194318220.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=5BDD18012E0C2C33D7D86777D758C6492608FE9A0C27D67F20A56FDED7490CF4 "点击放大")

**解决措施**

DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](<../../../../harmonyos-guides/编写与调试应用/应用调试/代码调试/Hot Reload/ide-hot-reload.md#section995453874915>)。

**常见不支持代码场景**

* 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/9NqctoE4QMaw2pG2f1Trew/zh-cn_image_0000002229604013.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=094D2658532901C43D7DED63659AF108EFBC3F39E613E0A056DB77A0C6409043 "点击放大")
* 不支持@Entry入口文件内class成员函数的新增。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/nGwZZ2ZdRcKV36QSUVqBjw/zh-cn_image_0000002194158608.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=DE07B8582EA04B99B83BF374FE5AC40995DDBDC9E24DE69731AEB5E0D70A0667 "点击放大")
* 不支持@Entry入口文件内枚举的修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/OUAXa63gQQ-7xNJo8Q0zog/zh-cn_image_0000002194158604.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=CAD2742B4D238E00E01B8BB91027B4A2EEEEC70C3270FD14435F27A15C07F6F7 "点击放大")
* 不支持import未加载的模块的新增、修改。

  若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/x0bDCaAORoKUKdCfRaGtdQ/zh-cn_image_0000002229604005.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=B8A000FC557D608F7A1AB2C16CE5244FF728C5F27F3C5905BC088F1662928BBA "点击放大")

  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/DXoH5HySRzCrjqKKW-4umA/zh-cn_image_0000002194318228.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=956861EB7B87E5C1E3C13F1D978CF4768C06840819C0AFD5E06B47EF585836FF "点击放大")
* 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/czhUqa0sQty8ZH82uZK1QA/zh-cn_image_0000002229758481.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=AB3AE45582F406E054E5C9BA84C2EA3EF53626D751AE2FACF7BCC5627A86911D "点击放大")
* 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/FJb4vcz1SlunPmNFUqiwAg/zh-cn_image_0000002229604009.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=E1DC5BDBFB882180F3C101F37F74DAE8F32DFA33C45A8E1240427ED44297A14F "点击放大")
* 不支持@Entry入口文件内大部分装饰器的修改。

  当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/HKJe4ZdOSlmVpNhICl225A/zh-cn_image_0000002229758473.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=77BEF366A55DE052270AFDC0FE877A0AD5038D83517CF9650B3D6CCB03791985 "点击放大")
* 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/sc1g-HUlSzy-ZUwQYJeMaA/zh-cn_image_0000002194318224.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=FB7BCAD7A43358953C9DEBD2DF405787B92BA3C17A6CFA3E0B690B27DE1936D7 "点击放大")
* 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/zSWQLqQ0QCajkItZMGXfyg/zh-cn_image_0000002194318216.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=69817989D008A45BB167CFD6318CB6F52778E4CFEB5122EF99604C8885F76670 "点击放大")
* 不支持修改非ets/ts代码文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/w68p8EBHToeqE5dJ8KohEw/zh-cn_image_0000002229758489.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=367636299C6A16E9299240017608AEC407F55A02F5B57BCBA4D8923E12F38CAE "点击放大")
* 不支持修改worker线程文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/ciyln2C0SLabDt_kcU2H9A/zh-cn_image_0000002194158612.png?HW-CC-KV=V1&HW-CC-Date=20260612T024448Z&HW-CC-Expire=86400&HW-CC-Sign=056AD1B4FE934AC214E6BCD4D1BFF925BDBDF44F55AB5DF181C4C089C73E6F23 "点击放大")
