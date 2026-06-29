---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-access-flow
title: Intents Kit接入流程
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > Intents Kit接入流程
category: harmonyos-guides
scraped_at: 2026-06-11T15:18:05+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:29d37360e14a5d876ce9fe599bb86bbbec982f2d850be54468ac70fb58475dea
---
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/gho6Zn3vTWSgd3PM5W7a5A/zh-cn_image_0000002592219746.png?HW-CC-KV=V1&HW-CC-Date=20260611T071801Z&HW-CC-Expire=86400&HW-CC-Sign=76E8AF3F4AED7244C1DAEDE75717C5407762DB622BA833578D4CC45EF56EDEA3)

**阶段一：意向**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 选择特性确定意图 | 开发者根据想达成的用户体验，确定好涉及的系统入口和特性类型，基于已发布的特性列表选择需实现的意图。如果已发布的特性列表中没能找到合适的意图，则只需要确定好系统入口和特性类型即可。 | 开发者想实现“歌曲续听推荐”的特性，根据智慧分发特性的场景描述，该特性属于小艺建议系统入口下的习惯推荐特性类型，需要实现“播放歌曲”意图。 | [歌曲续听推荐](https://developer.huawei.com/consumer/cn/doc/service/intents-ai-distribution-characteristic-0000001901922213) |
| 能力申请 | 确定好特性后，开发者在AppGallery Connect平台上提交对应特性类型的能力申请。 | 见下文图示。 | / |

**能力申请步骤**

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”，在项目列表选择项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/iT3Dl7FyReKgB4nYfCj-KQ/zh-cn_image_0000002592379680.png?HW-CC-KV=V1&HW-CC-Date=20260611T071801Z&HW-CC-Expire=86400&HW-CC-Sign=0C58C2CAE49EF4807D0F5B16E80B36DACF30B8F4123181244422A877B5DF8DCC)
2. 选择项目后，选择需要申请开通能力的应用。
3. 进入“项目设置 > 开放能力管理”页面，点击“意图框架”对应能力的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/kdhVvnl4S-6AeRR-YWCL-w/zh-cn_image_0000002622859189.png?HW-CC-KV=V1&HW-CC-Date=20260611T071801Z&HW-CC-Expire=86400&HW-CC-Sign=81BD6AA76E2D416D315C0B4F962268CFEF3DF8DC00E4CC7B336578CA1AF927B9)
4. 参考“申请原因”中的模版，提供必要的申请信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/4iRGI33ZSZ6Vh5Bm45ogYQ/zh-cn_image_0000002622699309.png?HW-CC-KV=V1&HW-CC-Date=20260611T071801Z&HW-CC-Expire=86400&HW-CC-Sign=E7C99A14D0BDE271F6E4A53129DF70ED65F3CC6C1893D4B2CD36E8E8865FA180)
5. 返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果。申请结果请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/u9FIuY6oTByhnjgbR7blFg/zh-cn_image_0000002592219748.png?HW-CC-KV=V1&HW-CC-Date=20260611T071801Z&HW-CC-Expire=86400&HW-CC-Sign=F532CE7DC4154B065A0A012EEA834EE803499310FF14BE691F6C0193228DABEF)

**阶段二：开发**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 意图调试申请 | 申请能力通过后，开发者可根据审核成功的反馈提示，提供测试应用的信息，用于开通意图调试权限。 | 1. 应用名称：华为音乐。  2. 应用包名：com.xxxx。  3. 接入意图名称：“播放歌曲”。  4. 应用图标：jpg、png……。  5. APP ID：1234567。  6. Client ID：1234567。  7. 华为账号（UID）：1234567、7654321……。 | 见各特性类型  习惯推荐：[开发者测试](../习惯推荐方案/开发者测试/intents-habit-rec-dp-self-validation.md)  事件推荐：[开发者测试](../事件推荐方案/开发者测试/intents-event-rec-dp-self-validation.md)  技能调用：[开发者测试](../技能调用方案/开发者测试/配置文件接入方式自测试方案/intents-skill-all-rec-dp-self-validation-con.md) |
| 意图声明文件中注册意图 | 在DevEco Studio中开发时，注册对应的意图。 | 注册“播放歌曲”意图。 | [意图注册](../习惯推荐方案/接入方案/intents-habit-rec-access-programme.md#意图注册) |
| 开发实现意图共享 | 开发应用/元服务的意图共享接口，使其可以通过HarmonyOS接口完成意图数据共享。 | 开发“播放歌曲”意图中的意图共享接口。 | [端侧意图共享](../习惯推荐方案/接入方案/intents-habit-rec-access-programme.md#端侧意图共享) |
| 开发实现意图调用 | 开发应用/元服务的意图调用接口，使其可以通过HarmonyOS接口被正确调用。 | 开发“播放歌曲”意图中的意图调用接口。 | [端侧意图调用](../习惯推荐方案/接入方案/intents-habit-rec-access-programme.md#端侧意图调用) |

**阶段三：验证**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 端到端验证特性 | 使用华为侧提供的测试能力完成目标特性的端到端联调测试，联调测试完成后，提交智慧分发配置至审核。 | 在设备上对应入口进行“华为音乐-歌曲续听推荐”的特性端到端测试，测试完成后点击提交智慧分发配置。 | / |

**阶段四：上架**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 应用市场上架软件包（应用/元服务） | 开发完成并打包好软件包后，在应用市场上传软件包。 | 打包“华为音乐”软件包并通过应用市场上架。 | [应用市场上架流程](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-0000002235870050) |
| 意图框架注册 | 在小艺开放平台进行意图注册配置并提交审核。由华为工程师审核，一般情况在3个工作日内完成。 | 注册“播放歌曲”意图。 | [意图标准协议上架指导](../意图框架上架配置指导/意图标准协议上架指导/intents-kit-listing-standard-protocol.md) |
