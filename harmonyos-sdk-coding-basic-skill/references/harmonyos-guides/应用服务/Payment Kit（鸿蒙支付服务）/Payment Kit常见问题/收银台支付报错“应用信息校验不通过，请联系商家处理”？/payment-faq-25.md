---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-25
title: 收银台支付报错“应用信息校验不通过，请联系商家处理”？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 收银台支付报错“应用信息校验不通过，请联系商家处理”？
category: harmonyos-guides
scraped_at: 2026-06-01T15:08:50+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:826c3c548668bb7793fe43f8341b780a1c1262fc0cb961c8e19ff57b0e1cdd03
---
1. 检查网络是否正常。
2. 检查是否[配置应用属性](../../开发准备/端侧应用配置/payment-config-app-identity-info.md#配置应用属性)，确认appId配置是否有调整。
3. 本地调试的签名证书配置是否为手动签名并且是从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)下载的，参见[应用/服务手动签名](../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)。证书下载后，可打开调试Profile（.p7b）文件，搜索“app-identifier”字段，如果对应的值和预下单请求或orderStr中传递的appId不一致，则证书生成错误，需重新生成证书及配置。
4. 检查是否配置添加了公钥指纹，参见[添加公钥指纹](../../../../应用开发准备/应用开发准备/application-dev-overview.md#条件必选添加公钥指纹)。
5. 检查一下orderStr中merc\_no、app\_id、auth\_id等参数是否正确，merc\_no和auth\_id是否匹配。
6. 服务商模式接入，切换到商户应用/元服务拉起收银台时，需要把app\_id改成商户相应的appId，并在[平台类商户/服务商预下单](<../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/REST API/平台类商户服务商/基础支付/预下单/payment-agent-prepay.md>)接口通过subAppId字段同步传递。
7. 使用“hdc hilog > 日志路径”抓取运行日志，参考[错误码](<../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/ArkTS API/ArkTS API错误码/payment-error-code.md>)及日志来分析具体的报错异常。
