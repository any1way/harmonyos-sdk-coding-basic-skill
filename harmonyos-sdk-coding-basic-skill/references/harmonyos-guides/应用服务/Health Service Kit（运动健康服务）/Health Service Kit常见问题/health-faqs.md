---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-faqs
title: Health Service Kit常见问题
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > Health Service Kit常见问题
category: harmonyos-guides
scraped_at: 2026-06-01T15:05:01+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:7523048c8294a4a1a37ba3761181d65a9f7dd52f19231360a54745865dc9828c
---
## 读取今天的日常活动数据统计，与运动健康App页面数据不一致

[聚合查询](../开发接入/PhoneTablet应用开发/管理运动健康数据/运动健康采样数据/health-samplepoint-manage.md#聚合查询)接口读取今日日常活动数据，数据上报存在延时，读取实时日常活动数据建议使用[读取实时三环数据](../开发接入/PhoneTablet应用开发/管理运动健康数据/实时三环数据/health-three-ring-read.md)接口。

## 授权后仍然没有数据类型权限

鉴权时使用的权限是用户授权的权限与应用申请的权限的交集，需确认：

1. 应用已申请了对应的数据类型权限，申请步骤请参考[申请运动健康服务](../开发接入/开发准备/申请运动健康服务/health-apply.md)，数据类型对应的权限参考[权限说明](../开发接入/数据类型/权限说明/health-permission-description.md)。
2. 用户授权已勾选对应的权限。

## 在授权时上报1001502003错误

参考[配置Client ID](<../开发接入/开发准备/配置Client ID/health-configuration-client-id.md>)，请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，确认代码中配置的包名与client ID是匹配的。若问题仍未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

更多错误码请参考[ArkTS API错误码](<../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API错误码/errorcode-healthservice.md>)。

## 在授权时上报1001502014错误

确保授权请求参数中的数据类型已经在**Health Service Kit**卡片中申请相应的权限，申请步骤请参考[申请运动健康服务](../开发接入/开发准备/申请运动健康服务/health-apply.md)，数据类型对应的权限参考[权限说明](../开发接入/数据类型/权限说明/health-permission-description.md)。

更多错误码请参考[ArkTS API错误码](<../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API错误码/errorcode-healthservice.md>)。

## 用户隐私未同意，如何引导用户打开运动健康App

接口响应错误码1002703001，可通过以下方式引导用户打开运动健康App，同意隐私授权：

调用[canOpenLink](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md#bundlemanagercanopenlink12>)判断运动健康App是否安装。运动健康App Scheme：huaweischeme://healthapp/home/main。

* App已安装，调用[openLink](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#openlink12>)接口拉起运动健康App。运动健康App Scheme：huaweischeme://healthapp/home/main。
* App未安装，调用[应用市场推荐](<../../AppGallery Kit（应用市场服务）/应用市场推荐/展示应用详情页面/appgallery-productview-loadproduct.md>)接口，引导用户下载运动健康App，运动健康App包名：com.huawei.hmos.health。
