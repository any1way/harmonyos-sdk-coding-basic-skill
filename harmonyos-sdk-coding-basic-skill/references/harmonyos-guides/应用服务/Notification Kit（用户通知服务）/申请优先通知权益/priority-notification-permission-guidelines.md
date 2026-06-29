---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/priority-notification-permission-guidelines
title: 申请优先通知权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请优先通知权益
category: harmonyos-guides
scraped_at: 2026-06-11T15:11:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0ef53f5a0988c90396347d51a3b8409da8d60f74f5c96bba56236a28b4888eee
---
当用户终端收到携带[priorityNotificationType](<../../../../harmonyos-references/Notification Kit（用户通知服务）/ArkTS API/notification/NotificationRequest/js-apis-inner-notification-notificationrequest.md>)字段的通知消息时，系统会将其识别为优先通知并优先显示。

申请优先通知权益存在以下限制：

1）该优先通知消息仅对商务类、社交通讯类应用开放。

2）应用内需具备重要联系人、@我、加急消息提醒功能，且申请后仅在上述场景中使用该能力，申请时需提供相应功能截图/示意图。

3）重要联系人场景需同时接入跳转应用内“重要联系人列表”能力。详情请参考[应用链接说明](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/应用链接说明/app-uri-config.md>)，[linkFeature](<../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/应用链接说明/app-uri-config.md#linkfeature标签说明>)字段使用PrimaryContactMgmt即可。

说明：优先通知权益仅允许在审核通过的场景中使用，如果申请权限后使用的功能和场景超出申请的范围，则属于违规，平台将禁用应用的优先通知权益。

## 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ntrPvAFJR_qgVYIynQWsbg/zh-cn_image_0000002622858941.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=04787323814B721EB4E19942FA6B783705ED11CFF95A618A8EF18C54AC022C5A)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请优先通知权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/8cGe8l_ET7WC0y36DpwHAg/zh-cn_image_0000002622699061.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=6C2C2AA4D9014BDCE50F2620F7932E31D4EA49E69EF390F4AE4EEB5AA8051308)
3. 进入“项目设置 > 开放能力管理”页面，点击“优先通知”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/yhu0zA9wThaZYjR17Dvgmg/zh-cn_image_0000002592219500.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=5490E226970AF50D03E7313564F22834D8F8A493C55A2474BD5ED7E04461AADC)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/G1QGdjZOQw2Grd8LTHgcHA/zh-cn_image_0000002592379434.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=92375A57AC759BC8F0CE1E4307FEFFF3A75E84E839CCD5A6E2DF4FC83CF014B8)
5. 开发者可通过互动中心的“服务开通申请”消息获取优先通知权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/V9rHedAaTU-eiVJqVNgAkA/zh-cn_image_0000002622858943.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=0A831966F041E4E7676F75F74FB05F5E8C584A064DB7C00E6C62A0ECD421ACBE)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/CeRpv79SR7eR6IDM0y2wOA/zh-cn_image_0000002622699063.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=0D6015E3882773521D0FD97049F4C5ED84B79587AA44F66D45169D09E1C1E96F)
6. 优先通知权益申请通过后，须在“证书、APP ID和Profile”页面下左侧树形菜单的“Profile”页签，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](../../../发布应用/发布应用/ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Ye432UlxSJOwLIbm0XsfMA/zh-cn_image_0000002592219502.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=19B35CB7D23D1C418A7B117D4D1B397E24D63C73B6933838AE0F32EA707E1A8D)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/KUzqpsEUTA-RkQ0hrVXCFg/zh-cn_image_0000002592379436.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=86AA393330C318DD06D9852244B0B463D66C80326E5382DE78E3EA613A0534EC)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/jO2MSAihSLSJfP5uGZdM3A/zh-cn_image_0000002622858945.png?HW-CC-KV=V1&HW-CC-Date=20260611T071115Z&HW-CC-Expire=86400&HW-CC-Sign=05A0E7B7E205451B589413E3E8B0634A5EE09BB4BC060C9731E9BD1CA6DE47AC)
