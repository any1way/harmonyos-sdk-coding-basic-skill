---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 秒级启动 > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-11T15:01:40+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:ab88cc0eafff148fc2b984e36e27258aa3c5fc0550613d279badcbbf711c2002
---
请先参考[应用开发准备](../../../../../应用开发准备/应用开发准备/application-dev-overview.md)完成基本准备工作，再继续以下开发准备项。

## 申请秒级启动开放能力

基于安全考虑，系统侧对秒级启动功能做了权限保护处理，使用相关接口开发者需先提交“秒级启动”能力开关的申请，在申请通过后，再使用该能力开关。

### 审核规则

1. 仅对游戏类应用开放。
2. 游戏冷启动时长需大于5秒。

### 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请秒级启动功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，点击“秒级启动”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/l13xHbAIR0GjTM9H1Ex6fw/zh-cn_image_0000002622698721.png?HW-CC-KV=V1&HW-CC-Date=20260611T070139Z&HW-CC-Expire=86400&HW-CC-Sign=A2D7DF8BACE6921481A12929FE25B899E6110EF611E6AA22ACCB018327F471BC)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/4YjoyZhvRP6b6cVYLtSMZw/zh-cn_image_0000002592219160.png?HW-CC-KV=V1&HW-CC-Date=20260611T070139Z&HW-CC-Expire=86400&HW-CC-Sign=90AD7FFFDE5E3208F06E9C526D5DE6A60B8F2AE294691CC1455F44C0D6ACAD56)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/6lKVgjn7RhWDlDfjWyF2YA/zh-cn_image_0000002592379094.png?HW-CC-KV=V1&HW-CC-Date=20260611T070139Z&HW-CC-Expire=86400&HW-CC-Sign=8C67E1FB538E1D3327194A72F4A1E600C1A50E0DC40B4EA400AD6C34DC9E771C)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启秒级启动开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/l-pqFDh6Spa6eO4sgz8v5g/zh-cn_image_0000002622858601.png?HW-CC-KV=V1&HW-CC-Date=20260611T070139Z&HW-CC-Expire=86400&HW-CC-Sign=9538986DBEFD25A005EA4E59B479BA5E3E79373644E5D74F2865238FCD33F47A)
