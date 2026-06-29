---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-standard-protocol
title: 意图标准协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > 意图标准协议上架指导
category: harmonyos-guides
scraped_at: 2026-06-11T15:19:07+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:f4b4e8837bc9ccf30045cf548b85d7ddd9cef0c3e6e623863e9a8f5c9b0b0807
---
该配置需开发者完成自测后，先将携有对应意图信息的App在AppGallery Connect（以下简称AGC）完成应用上架，具体操作步骤参见[应用开发准备](../../../../应用开发准备/应用开发准备/application-dev-overview.md)。

## **意图注册配置操作步骤**

1. 账号登录：

   1. 通过“[华为开发者联盟](https://developer.huawei.com/consumer/cn/) > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口，需使用与应用上架相同的账号登录。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/TGoIg6HmS1KzDsTctvBHLg/zh-cn_image_0000002622859211.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=C782C1C58D89DE02B199C8B3F55C52884A88CD679C06FCAEE7563359B73B6817)
   2. 点击“立即体验”即可进入意图注册入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/K27qQWXKSuqyM0TK55NSYQ/zh-cn_image_0000002622699331.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=492AF874CF1E51E5CD3EF57FC84E1FF59586DD10FCC07244B188BA08E6A3026A)
2. 选择意图集：在“小艺开放平台”首页“意图集（插件）”中，携有意图声明文件的应用在AGC**正式上架**后可**自动生成**一条草稿态的记录，记录中包含开发者在意图配置文件中声明的所有**端侧意图**（云侧意图需手动新增，见下图）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/QVuy8zLuTOesx1dlQENzIQ/zh-cn_image_0000002592379712.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=CACA703309FAA375B7426FD947355AA7E943DDE2533DCBAA46AD2CD5FF5D1886)
3. 基本信息编辑：点击对应的意图集记录的“编辑”按钮，进入基本信息编辑页面，开发者补充完基本信息后点击“保存”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/-2d5d0B-REmeTGaCcYmgSQ/zh-cn_image_0000002622859221.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=D36CE08523C97F6CE6C317839FB2E697BB6C99309EC97403F0049F950E95829E)

   此处的版本号和版本描述为智慧分发配置的版本信息，用于开发者记录和识别智慧分发配置版本变更，与APP软件包版本无关，意图注册名称与APP名称保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/REH47LrcTmGm4b6z3qoIvw/zh-cn_image_0000002622699341.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=CFBC203A798385B4A337623B6BB45672D81E4D3A79C0E2A04242D5D76FCF3707)
4. 意图检查：切换至“意图”页签，点击“保存”会触发刷新，需检查接入特性所依赖的全量意图是否在此页面都已列出，同时打开意图使用样本中“是否已提供线下样本”开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/iXXI5hyRQieK0iKQ2Y636Q/zh-cn_image_0000002592219780.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=F10044BEEAA28991D06069B466DBE5D2F25333E3A245F5EE446FF6C164CC9EE5)

   1. 其中，“端云类型”涉及端的意图需在APP软件包中定义，此处会自动呈现。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/3ugMwP_AQAuQwnzgydKrGQ/zh-cn_image_0000002592379714.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=104A4FA860722D241A43765015F74A95170DCCE5691B485E279891408013D475)
   2. “端云类型”仅涉及云的意图需要需手动添加该意图。可参照如下步骤配置：

      1. 点击添加进行意图新增。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/xk9uHLXBSiaZXDT_7AxujQ/zh-cn_image_0000002592219778.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=D8657159050719F8E4CDC585CA148D730314AEDF56DD9860E0496DEA7AE62DD0)
      2. 选择云侧意图分类，搜索意图名称，勾选所需意图进行添加（若没有找到对应意图可联系华为工程师，检查是否未配置该意图）。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/mhyU3xy_SKmiIJ6meAnWyA/zh-cn_image_0000002622859223.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=A8E94EAC43440175E41DD1C63FBD335379FFB5DFB3D5EBF6C039E207A83B2904)
      3. 添加完成后，需录入接口信息配置，具体信息如下：

         1. API：即开发者的URL地址信息，供华为侧服务器进行云侧意图调用。
         2. 认证方式：如果涉及接口鉴权，则选择认证方式（例如AK/SK认证）并配置密钥信息；如果不涉及则选择不认证。
         3. 个人数据授权：该信息是指华为侧服务器携带对应信息访问开发者服务器，当有个性化推荐诉求时需要填写，默认不填写；比如选中“用户授权的用户唯一标识”（即SID），则华为侧服务器访问开发者服务器时会携带SID，开发者服务器则可以识别用户返回个性化的数据用户推荐展示。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/uMZ-BBziRsai3shUYgHH-g/zh-cn_image_0000002622699343.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=91B3BF5EE816A6F676BB867769BA11F85701C5310860FB943B120F667B1AE237)
   3. 如仍未全部列出，检查软件包中意图注册配置文件是否漏配，若漏配则在意图配置文件中补充配置，并重新在AGC进行应用上架/升级，完成后在小艺开放平台进行意图注册。
   4. 如果提示声明意图不存在，则说明华为意图框架后台未配置该意图。开发者可以继续点击保存走完本次流程，但相应意图和关联特性不会生效；可联系华为工程师，检查是否未配置该意图。
5. 检查完成：如果特性依赖的所有意图都已列出，检查意图名称、意图调用配置和意图共享配置等是否正确，正确则点击“保存”，进入下一步。
6. 发布选择“发布”页签，进入配置检查页面。

   1. 点击“开始检查”，检查接入特性和其关联的意图是否正确，如下图所示。生成特性时会同时生成abilityId，若开发者接入特性的方案涉及此参数，则事件推荐请求字段abilityId参数需要填写当前界面的abilityId值。若提示特性undefined，则联系华为工程师，检查是否未配置该特性。
   2. 配置检查完成后点击“提交审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/i1VeyWd1S86nrxBBfWRtig/zh-cn_image_0000002592219782.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=476F8CD7ED2DBCBB5BC48BBEBDCCF177ACAE55D79D17102CB9E1066F5BD4AF9D)
7. 审核：提交审核后，在“小艺开放平台> 意图集”中，该条记录状态变为“上架审核中”，一般审核周期为3-5个工作日，审核通过后状态变为“已上架”，至此意图注册及特性选择已完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/8RRAk-3sTjmTy-0z9JOKeg/zh-cn_image_0000002592379716.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=997C42CA2C7C8B5B511FB6FE11862E6CE75D840C9DFE8FDD78CF66DBF10DB94D)
8. 新增意图：若开发者有新意图上架，可在同一条记录上进行编辑后提交，操作流程同上述步骤，未提交审核不影响已经注册的意图。
