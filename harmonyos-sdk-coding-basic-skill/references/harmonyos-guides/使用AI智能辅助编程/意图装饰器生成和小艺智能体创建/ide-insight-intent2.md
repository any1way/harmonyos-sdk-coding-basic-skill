---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2
title: 意图装饰器生成和小艺智能体创建
breadcrumb: 指南 > 使用AI智能辅助编程 > 意图装饰器生成和小艺智能体创建
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:35+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:7ec2bd7f66a22c9c79b5cbc3458e7c66c80ed7f3d4b9d1d52998ec937064ddeb
---
通过装饰类或方法可以将应用的功能定义为"意图"，然后将应用功能以"意图"形式集成至系统入口。用户通过系统入口（如语音助手、智能推荐卡片）触发意图执行，即可便捷使用应用提供的功能。

从DevEco Studio 6.0.0 Beta2开始，CodeGenie新增通过装饰器开发意图的功能，支持生成五类意图装饰器。同时，DevEco Studio新增Application Agent入口，通过该入口可完成意图插件注册、智能体创建等，提升开发效率。

## 使用约束

* 使用API 20及以上版本。
* 仅支持使用团队账号登录时，添加意图插件。个人加入目标团队方式具体可参考[添加成员](https://developer.huawei.com/consumer/cn/doc/app/agc-help-manageaccount-0000002306610129#section151241455193313)。
* 应用在AGC已注册，具体可参考[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506#section1772711713288)。
* 生成意图装饰器时使用HarmonyOS Ask智能体。

## 意图装饰器分类

CodeGenie提供了几类意图装饰器，开发者可根据业务场景进行选择，具体请参考[意图装饰器定义](<../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md>)：

* @InsightIntentLink装饰器：在class头部或内部位置唤起意图装饰器，在class上方插入生成的代码。
* @InsightIntentPage装饰器：在@Component头部/struct结构体内部/选中整个结构体区域唤起意图装饰器，在@Entry上方插入生成的代码。
* @InsightIntentFunction装饰器：在类中静态方法区域唤起意图装饰器，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。
* @InsightIntentForm装饰器：在继承FormExtensionAbility的class头部或内部唤起意图装饰器，在class上方插入生成的代码。
* @InsightIntentEntry装饰器：在直接继承InsightIntentEntryExecutor的class头部或内部唤起意图装饰器，在class上方插入生成的代码。

### @InsightIntentLink装饰器

1. 打开module.json5文件，配置**abilities > skills > uris**字段。uri格式要求请参考[应用链接说明](<../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/应用链接说明/app-uri-config.md>)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/3CxKAkzST8u0FwMNmmWR3w/zh-cn_image_0000002602186303.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=19439A4F77A75E4D62E983B2F4FBF8658EB2D93AF17013B1E896F2E60F129059 "点击放大")
2. 在class头部或内部位置，右键选择 **CodeGenie > Insight Intent > Link Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/tvQH5GsQQXGlm9RA30pmMw/zh-cn_image_0000002571387160.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=7F52D10EEB57B3D3160A779127D8861974585EB82CFC4B2F8914BB2A9906311A)
3. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/u7irI4gvTOaR0fHXTFQ8hA/zh-cn_image_0000002602066273.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=3A29BC38CCC02130194C2F98DF61F875F4DE873043411EA15F564CA259BB12BC)
4. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D-W7thf0RGa1YtmWA_Gesw/zh-cn_image_0000002602186337.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=8F9C67E88F0B2C8884A6F34FF92554FE47B92A4C849194EB762803FF71F39B88)

### @InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

1. 在@Component头部\struct结构体内部\选中整个结构体区域，点击**右键 > CodeGenie > Insight Intent > Page Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/v41-KeKDQ06aNXUTGzWkjw/zh-cn_image_0000002571546800.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=9E5B1FC3E43944D39EB488D6A9FFC5A046DEB17BA4EFC617BA2BB0D3ACA7D3B8)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/YQyn2zpSQJySKwK0cvdBrg/zh-cn_image_0000002571387164.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=F58CCAF9FC5B3D9C11452E13F45020F4D9097B1DC5C8D360419F7DE2A5AE0AC0)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在@Entry上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/2-QHIQpJT3a8UUZJBDHw4w/zh-cn_image_0000002571546798.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=A85D8CFC151AC2B65C17FEF40620E56774D6DA2410501C45E33D9ECB39810864)

### @InsightIntentFunction装饰器

1. 在类中静态方法区域，右键选择 **CodeGenie > Insight Intent > Function Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/GXhrizWtQyy5tNz2hRZ1zA/zh-cn_image_0000002571546804.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=B04EE322E7D024A501EB151A643DDFAC5F31301AEC9C0F04ADD62284AD716FD1)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/yl8_wXYUTZisSMk6Dpz1wA/zh-cn_image_0000002602066285.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=B7F64324C63C92A9F3248B30CCC9E2E1EC8F988368E9B1D960DA5976B5ABE3DC)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/-96u_qcQRr63_2art2_QNA/zh-cn_image_0000002602066283.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=73E02278953CAD4D5A96DA8E36C2A3AD56CC42EC86B30BE752EFCEB288FD64CE)

### @InsightIntentForm装饰器

1. 基于FormExtensionAbility使用，在继承FormExtensionAbility的class头部或内部，右键选择**CodeGenie > Insight Intent > Form Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/cTlCd0wZTkm14yF5phPeKg/zh-cn_image_0000002602066247.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=DAD20660060C4D2C9747DAAC2EECC8BD7BDAF7C714889642F84FFA82A0E766F6)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ML9ucyacR5eqnWdGQdyxnQ/zh-cn_image_0000002602186299.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=89F9872F72539C3B731B69E2C42ED6B370076411792B3B2ADD07D6868154E197)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/mNtpAU7rQMSmgiwNcD59tw/zh-cn_image_0000002571387170.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=56C6724A0FEF03A20A24FBA6C8CC2E516A8534E82E9DC75E256E8A64E285471E)

### @InsightIntentEntry装饰器

1. 基于InsightIntentEntryExecutor使用，在直接继承InsightIntentEntryExecutor的class头部或内部，右键选择**CodeGenie > Insight Intent > Entry Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/FAjuFGNvS0WmuqnlmUd-QQ/zh-cn_image_0000002571387134.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=FADC2671F56DB9BABB6FC3E9E83EE46EE583AE0D62EDCB618ECE8D163B984975)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/d-RLdhiAQDCWhd_Mxd5gjw/zh-cn_image_0000002571546796.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=94D204AF2C560A9E5DD0D0B0CD911D57F3CF14BED65390F038990BF4AD7818EC)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/yPc3f5Q8TwWmGa9eEALtzg/zh-cn_image_0000002571546770.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=A17B369B91C0AECB124354B722A8245902F41D249AE3B2479793438E37FC8841)

## 生成意图插件和创建小艺智能体

1. 点击DevEco Studio右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/MnDwYIhjQmCdITLkmqZFMw/zh-cn_image_0000002571546766.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=B8D464C93C19481D7C5C0D053F5990B232A40651F569FD9377D01DAC0837330F)图标登录个人账号，再切换至个人所在的团队账号。

   说明

   * 个人账号需要完成实名认证，具体请参考[实名认证](https://developer.huawei.com/consumer/cn/doc/start/rna-0000001062530373)。
   * 如下企业开发者账号为某团队账号名称，仅供参考。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/LrogTEV6RIim07wu6d9rHQ/zh-cn_image_0000002571546806.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=39B54F64552B8EA1E8B22BF531DFFACB3BFAD32A10658FC40330C6AA4AFB5852)
2. 在意图注解代码块内部任意位置，右键选择**CodeGenie > Add Intent Plugin**，生成的意图注解插件将注册到小艺智能平台中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/UV5es2bTRNe7n9JKLU3g_w/zh-cn_image_0000002571387156.png?HW-CC-KV=V1&HW-CC-Date=20260611T072233Z&HW-CC-Expire=86400&HW-CC-Sign=112EFE20AD1F82D6E416D425BCBF236A0659C9F0FB1B6985052FA463E3CB08C8)
3. 在DevEco Studio菜单栏点击**View > Tool Windows > Application Agent** ，打开内嵌的小艺智能平台新建智能体和添加插件。小艺智能平台更多具体操作可参考[鸿蒙智能体](https://developer.huawei.com/consumer/cn/doc/service/developer-guide-0000002469667881)。
