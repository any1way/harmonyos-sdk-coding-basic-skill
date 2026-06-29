---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-8
title: 无法获取到头像昵称如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 无法获取到头像昵称如何解决
category: harmonyos-guides
scraped_at: 2026-06-01T14:59:42+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:a201e3f992d5246d96062992ff47bc9edfbeac99e5cfce53659b1b0ccb8e9585
---
1. 确认获取authorizationCode时，调用[AuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidrequest>)接口是否传入正确的scope：'profile'。

   ```
   1. import { authentication } from '@kit.AccountKit';

   3. // 创建授权请求，并设置参数
   4. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   5. // 获取头像昵称需要传如下scope
   6. authRequest.scopes = ['profile'];
   7. // 若开发者需要进行服务端开发，则需传如下permission获取authorizationCode
   8. authRequest.permissions = ['serviceauthcode'];
   ```
2. 确认通过[AuthenticationController.executeRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#executerequest-1>)接口执行授权请求后，响应返回的Authorization Code在5分钟有效期内。
3. 确认调用的是华为账号服务器[获取头像昵称](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/获取用户信息/获取华为账号用户信息-获取头像昵称/account-api-get-user-info-get-nickname-and-avatar.md>)接口。
