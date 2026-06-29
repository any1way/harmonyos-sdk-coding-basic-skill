---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-lockdown-exemption-apps
title: 查询深度冻结豁免名单
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 查询深度冻结豁免名单
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4de52ee8fee466c51472a699837568bf613e3102843bdd5267048cf1cd352e85
---
## 场景介绍

从6.0.2(22)开始，支持查询深度冻结豁免名单的能力。

Enterprise Space Kit为应用提供查询深度冻结豁免名单的能力。当设置深度冻结豁免名单后，可使用该接口查询深度冻结豁免名单。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#getlockdownexemptionapps>)。

| 接口名 | 描述 |
| --- | --- |
| [getLockdownExemptionApps](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#getlockdownexemptionapps>)(workspaceId?: number): Promise<string[]> | 查询深度冻结豁免名单。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块和相关依赖模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[getLockdownExemptionApps](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#getlockdownexemptionapps>)，查询深度冻结豁免名单，并且查看打印信息。

```
1. const workspaceId: number = 100;
2. try {
3. const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
4. console.info(`Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
5. } catch (err) {
6. console.error(`Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
7. }
```
