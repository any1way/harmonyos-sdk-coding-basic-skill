---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-scenario1
title: 保护密码类数据
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > 常见场景 > 保护密码类数据
category: harmonyos-guides
scraped_at: 2026-06-11T14:40:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:64c25f47f279bc7b9190c7d8281c71a3e239fefcbb843314cbf9f53c692e0346
---
说明

密码类数据可以是密码、登录令牌、信用卡号等用户敏感数据。

## 场景描述

用户在应用/浏览器中登录账号时，可以选择“记住密码”（如图）。针对此种场景，应用/浏览器可以将用户密码存储在ASSET中，由ASSET保证用户密码的安全性。

用户再次打开登录界面时，应用/浏览器可以从ASSET中查询用户密码，并将其自动填充到密码输入框，用户只需点击“登录”按钮即可完成账号登录，极大地提升了用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/NNbtJRbcTMuxRRV3KuKong/zh-cn_image_0000002592378728.png?HW-CC-KV=V1&HW-CC-Date=20260611T064030Z&HW-CC-Expire=86400&HW-CC-Sign=B02E6D0B09BA0D3F1574A0C8F2C05CB9250767F299EE11A37F507CFB5973DE2C)

## 关键流程

业务调用ASSET保护密码类数据（后文统称为“关键资产”），可以参照以下流程进行开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/zT6GS0CwRMO-xAmzN0jlWw/zh-cn_image_0000002622858235.png?HW-CC-KV=V1&HW-CC-Date=20260611T064030Z&HW-CC-Expire=86400&HW-CC-Sign=9EFFD3EC178BDA9469F0A9DD346646F2E78C3899FA964013AB05454611535710)

1. 业务查询符合条件的关键资产属性，根据查询成功/失败，判断关键资产是否存在。

   * 开发步骤参考[查询关键资产(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/查询关键资产(ArkTS)/asset-js-query.md>) / [查询关键资产(C/C++)](<../../Asset Store Kit开发指导(CC++)/查询关键资产(CC++)/asset-native-query.md>)，代码示例参考[查询单条关键资产属性(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/查询关键资产(ArkTS)/asset-js-query.md#查询单条关键资产属性>) / [查询单条关键资产属性(C/C++)](<../../Asset Store Kit开发指导(CC++)/查询关键资产(CC++)/asset-native-query.md#查询单条关键资产属性>)。
2. 如果关键资产不存在，业务可选择：

   * 新增关键资产，开发步骤参考[新增关键资产(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/新增关键资产(ArkTS)/asset-js-add.md>) / [新增关键资产(C/C++)](<../../Asset Store Kit开发指导(CC++)/新增关键资产(CC++)/asset-native-add.md>)。
3. 如果关键资产存在，业务可选择：

   * 删除关键资产，开发步骤参考[删除关键资产(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/删除关键资产(ArkTS)/asset-js-remove.md>) / [删除关键资产(C/C++)](<../../Asset Store Kit开发指导(CC++)/删除关键资产(CC++)/asset-native-remove.md>)。
   * 更新关键资产，开发步骤参考[更新关键资产(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/更新关键资产(ArkTS)/asset-js-update.md>) / [更新关键资产(C/C++)](<../../Asset Store Kit开发指导(CC++)/更新关键资产(CC++)/asset-native-update.md>)。
   * 查询关键资产明文，开发步骤参考[查询关键资产(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/查询关键资产(ArkTS)/asset-js-query.md>) / [查询关键资产(C/C++)](<../../Asset Store Kit开发指导(CC++)/查询关键资产(CC++)/asset-native-query.md>)，代码示例参考[查询单条关键资产明文(ArkTS)](<../../Asset Store Kit开发指导(ArkTS)/查询关键资产(ArkTS)/asset-js-query.md#查询单条关键资产明文>) / [查询单条关键资产明文(C/C++)](<../../Asset Store Kit开发指导(CC++)/查询关键资产(CC++)/asset-native-query.md#查询单条关键资产明文>)。
