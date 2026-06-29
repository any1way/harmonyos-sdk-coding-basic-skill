---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mgmt-overview
title: Network Kit简介
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > Network Kit简介
category: harmonyos-guides
scraped_at: 2026-06-01T11:20:00+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:05579d157a0226d9d1158717cd2a8304e9d4d1dffcb97f97fbd36777a108e1e7
---
Network Kit（网络服务）主要提供以下功能：

* [HTTP数据请求](../访问网络/使用HTTP访问网络/http-request.md)：通过HTTP发起一个数据请求。
* [WebSocket连接](../访问网络/使用WebSocket访问网络/websocket-connection.md)：使用WebSocket建立服务器与客户端的双向连接。
* [Socket连接](../访问网络/使用Socket访问网络/socket-connection.md)：通过Socket进行数据传输。
* [网络连接管理](../连接网络/管理网络连接/net-connection-manager.md)：网络连接管理提供管理网络一些基础能力，包括WiFi/蜂窝/Ethernet等多网络连接优先级管理、网络质量评估、订阅默认/指定网络连接状态变化、查询网络连接信息、DNS解析等功能。
* [MDNS管理](../访问网络/使用MDNS访问局域网服务/net-mdns.md)：MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、删除、发现、解析等能力。

## 模拟器支持情况

Network Kit支持模拟器，但与真机存在差异，具体差异如下。

* 通用差异：详情请参见“[模拟器与真机的差异](../../../../编写与调试应用/使用模拟器运行应用/概述/模拟器与真机的差异/ide-emulator-specification.md#section1227613205203)”。
* 模拟器不支持VPN功能。

## 约束与限制

使用网络管理模块的相关功能时，需要请求相应的权限。

在申请权限前，请保证符合[权限使用的基本原则](../../../安全/程序访问控制/应用权限管控/应用权限管控概述/app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](../../../安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)声明对应权限。

| 权限名 | 说明 |
| --- | --- |
| ohos.permission.GET\_NETWORK\_INFO | 获取网络连接信息。 |
| ohos.permission.INTERNET | 允许程序打开网络套接字，进行网络连接。 |
