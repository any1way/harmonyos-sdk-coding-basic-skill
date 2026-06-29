---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-restrict-access-bg-userdata
title: 设置系统服务进程不可访问后台用户数据的功能
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置系统服务进程不可访问后台用户数据的功能
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c50a9d76244b1b863a8751c237c57168ae7213d0427f146cc7f240e4d41f6192
---
## 场景介绍

从6.0.1(21)开始，支持设置系统服务进程不可访问后台用户数据的能力。

Enterprise Space Kit为应用提供设置系统服务进程不可访问后台用户数据的功能。例如，当前台是企业用户，后台是个人用户时，应用设置了对应个人用户的管控，此时不允许系统服务进程访问后台个人用户的数据。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#setrestrictedaccessbackgrounduserdata>)。

| 接口名 | 描述 |
| --- | --- |
| [setRestrictedAccessBackgroundUserdata](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#setrestrictedaccessbackgrounduserdata>)(userData: [UserDataEnum](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#userdataenum>), enable: boolean): Promise<void> | 设置系统服务进程不可访问后台用户数据的功能。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[setRestrictedAccessBackgroundUserdata](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#setrestrictedaccessbackgrounduserdata>)，设置系统服务进程不可访问后台用户数据的功能，并且查看打印信息。

   ```
   1. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
   2. const enable: boolean = false;
   3. try {
   4. await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable)
   5. console.info(`Succeeded in setting restricted access background user data. userData: ${userData}, enable: ${enable}`);
   6. } catch (err) {
   7. console.error(`Failed to set restricted access background user data. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```
