---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-del-restricted-access-process-list
title: 删除系统服务进程不可访问后台用户数据路径列表
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 删除系统服务进程不可访问后台用户数据路径列表
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:055e49b6f78b2f4a2536e638b6a360fa4a03b722fb1190a910c49a054d051ad1
---
## 场景介绍

从6.0.1(21)开始，支持删除系统服务进程不可访问后台用户数据路径列表的能力。

Enterprise Space Kit为应用提供删除系统服务进程不可访问后台用户数据路径列表的功能。用于应用删除管控系统服务进程时的场景。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#deleterestrictedaccessbackgrounduserdataprocesslist>)。

| 接口名 | 描述 |
| --- | --- |
| [deleteRestrictedAccessBackgroundUserdataProcessList](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#deleterestrictedaccessbackgrounduserdataprocesslist>)(userData: [UserDataEnum](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#userdataenum>)), processName: string): Promise<void> | 删除系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[deleteRestrictedAccessBackgroundUserdataProcessList](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#deleterestrictedaccessbackgrounduserdataprocesslist>)，删除系统服务进程不可访问后台用户数据路径列表，并且查看打印信息。

   ```
   1. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
   2. const processName: string = 'testSa';
   3. try {
   4. await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
   5. console.info(`Succeeded in deleting restricted access background user data process list`);
   6. } catch (err) {
   7. console.error(`Failed to delete restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```
