---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-22
title: 1001502003 输入参数值无效的可能原因和解决办法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502003 输入参数值无效的可能原因和解决办法
category: harmonyos-guides
scraped_at: 2026-06-11T15:03:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:115a4f2f008dfc4ac570d4adb47debf89b6fc57d6e61ae30d97776564aeca510
---
**问题现象**

调用接口报错1001502003 输入参数值无效。

**可能原因**

1. client\_id未配置或配置错误。
2. Profile文件无效。
3. 一键登录场景，传入的匿名手机号不正确，或是未调用授权API（[AuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidrequest>)）获取匿名手机号。
4. 接口传参异常，如调用授权API（[AuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidrequest>)）时scopes和permissions属性均为空。

**解决措施**

1. 在 AppGallery Connect（简称AGC）的[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中，选择对应的项目和对应的应用，在“常规 > 应用 ”下，找到**应用**的Client ID和APP ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/6myGW4HcRgusX_1w9cPLZQ/zh-cn_image_0000002622858617.png?HW-CC-KV=V1&HW-CC-Date=20260611T070321Z&HW-CC-Expire=86400&HW-CC-Sign=2B5BA0D39BBC7AAF6B9B1F338E0FA4CFE761CC6C72B2ED62B4E96DE75385F302)

   * 若Client ID和APP ID不同：请检查module type为entry的模块下module.json5中的client\_id是否配置或配置的值是否正确，参考[配置Client ID](<../../开发准备/配置Client ID/account-client-id.md>)。
   * 若Client ID和APP ID相同：可无需配置Client ID。
2. 请在AppGallery Connect中重新申请Profile文件并重新进行签名。在调试阶段，请参考[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)，完成Profile申请并重新手动签名；在发布阶段，请参考[申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)，完成Profile申请并重新手动签名。
3. 需要通过授权API（[AuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidrequest>)）获取到匿名手机号，将其作为参数调用一键登录接口。
4. 检查[authentication](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md>)相关接口参数。
