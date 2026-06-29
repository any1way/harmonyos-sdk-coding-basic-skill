---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-06-11T15:03:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:735e2ca0f11053ea4de05c8815deba7e03f0fd40603cf7eb6d074ee348596275
---
**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](../../获取华为账号用户信息/获取风险等级/概述/account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](../../开发准备/申请账号权限/account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/8KG4B5_yT2ar2QrJlWXAPQ/zh-cn_image_0000002592219174.png?HW-CC-KV=V1&HW-CC-Date=20260611T070306Z&HW-CC-Expire=86400&HW-CC-Sign=B1103488C0B654B5EB79221A8328B03B5EBCB36816748155348BB89A78532F22)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Fk2d7dopSRexLuIgexCedg/zh-cn_image_0000002622858615.png?HW-CC-KV=V1&HW-CC-Date=20260611T070306Z&HW-CC-Expire=86400&HW-CC-Sign=A5932F57A978596AB0E71DC2A92C7A6F4A048526794FE5B8DDC10639F282FA13)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/QUkHgAnTSYeYDnIDr6L9Kg/zh-cn_image_0000002622698737.png?HW-CC-KV=V1&HW-CC-Date=20260611T070306Z&HW-CC-Expire=86400&HW-CC-Sign=3A7044D433A4631BCF5E266D5677EB61B1031DE6DACA398B43EE1D6E40E7F302)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](../../获取华为账号用户信息/获取风险等级/概述/account-get-risklevel-introduction.md)申请对应权限。
