---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-preparation
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:24+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:8409890fabd526dc614cddb490e1c7aa4bc15b4fb65efd7d661ca106b7afb84f
---
## FIDO开发准备

开发者的业务需要接入符合FIDO UAF标准的协议，并部署符合FIDO UAF标准协议的FIDO服务端。FIDO网址：<https://fidoalliance.org/> （见[网站链接免责声明](../网站链接免责声明/onlineauthentication-website-disclaimer.md)）。

## IFAA开发准备

开发者的业务接入IIFAA联盟，并接入IIFAA中心服务器。IIFAA网址：<https://www.iifaa.org.cn/technical#paper> （见[网站链接免责声明](../网站链接免责声明/onlineauthentication-website-disclaimer.md)）。

## SOTER开发准备

开发者的业务接入SOTER服务器。SOTER github：<https://github.com/Tencent/soter>（见[网站链接免责声明](../网站链接免责声明/onlineauthentication-website-disclaimer.md)）。

## 通行密钥开发准备

* 开发者基于FIDO2的CAPI接口开发时（调用ArkTs接口时不涉及），需要申请如下通行密钥服务权限。在申请权限前，请保证符合[权限使用的基本原则](../../程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md#权限使用的基本原则)。申请方式请参考：[申请受限权限](../../程序访问控制/应用权限管控/申请应用权限/申请受限权限/declare-permissions-in-acl.md)。

  | 应用能力 | 需要权限 |
  | --- | --- |
  | 通行密钥 | ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH |
* FIDO2协议基于应用的网址域名开通应用的通行密钥，开发者的应用需要关联网址域名，才可使用通行密钥服务。接入需完成四步：[开通App Linking服务](<../../../../应用服务/App Linking Kit（应用链接服务）/开发准备/开通App Linking服务/applinking-enable-applinking.md>) > [建立域名与应用关联关系](<../../../../应用服务/App Linking Kit（应用链接服务）/通过App Linking应用链接拉起指定应用/app-linking-startupapp.md#建立域名与应用关联关系>) > [在AGC为应用创建关联的网址域名](<../../../../应用服务/App Linking Kit（应用链接服务）/通过App Linking应用链接拉起指定应用/app-linking-startupapp.md#在agc为应用创建关联的网址域名>) > [在module.json5中配置关联的网址域名](<../../../../应用服务/App Linking Kit（应用链接服务）/通过App Linking应用链接拉起指定应用/app-linking-startupapp.md#在modulejson5中配置关联的网址域名>)。
