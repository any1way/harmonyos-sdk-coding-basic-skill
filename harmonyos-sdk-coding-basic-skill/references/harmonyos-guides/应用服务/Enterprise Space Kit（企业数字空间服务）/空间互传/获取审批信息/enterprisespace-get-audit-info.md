---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-audit-info
title: 获取审批信息
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间互传 > 获取审批信息
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:987456a4494cf24c952a7b22348f0acac610b258db531d50a8a9a7c5cfd87c8f
---
## 场景介绍

Enterprise Space Kit为应用提供获取审批信息的能力。文件外发需经过审批流程控制，通过调用审批状态同步接口实时获取审批结果，审批完成后允许文件外发至个人空间，若审批被拒绝或撤销则禁止外发。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceDataTransfer (空间数据传输)/enterprisespace-spacedatatransfer.md#getauditinfo>)。

| 接口名 | 描述 |
| --- | --- |
| [getAuditInfo](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceDataTransfer (空间数据传输)/enterprisespace-spacedatatransfer.md#getauditinfo>)(transactionNum: string): [AuditInfo](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceDataTransfer (空间数据传输)/enterprisespace-spacedatatransfer.md#auditinfo>) | 获取审批信息。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[getAuditInfo](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceDataTransfer (空间数据传输)/enterprisespace-spacedatatransfer.md#getauditinfo>)接口，获取审批信息，并且查看打印信息。

   ```
   1. const transactionNum: string = '1111111';
   2. try {
   3. const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
   4. console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
   5. } catch (err) {
   6. console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
