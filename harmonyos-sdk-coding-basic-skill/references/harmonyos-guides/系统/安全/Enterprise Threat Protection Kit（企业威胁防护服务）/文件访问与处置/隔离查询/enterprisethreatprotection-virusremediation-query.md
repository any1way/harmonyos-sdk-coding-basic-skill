---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-query
title: 隔离查询
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 文件访问与处置 > 隔离查询
category: harmonyos-guides
scraped_at: 2026-06-11T14:45:14+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:50c2619024857383814bba5d645bd59c76ba315416714343855010c8d9b907a3
---
## 基本概念

隔离查询功能帮助安全防护类应用获取当前用户下由该应用隔离的处于隔离状态的文件信息列表。

## 场景介绍

当安全防护类应用更新或卸载，导致原本存储在应用数据库中的隔离信息丢失时，可通过隔离查询接口，为安全防护类应用提供隔离信息查询的能力，快速获取自身应用已隔离的当前用户的文件信息，保障隔离恢复和隔离查询的可操作性。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#queryisolatedfiles>)。

| 接口 | 描述 |
| --- | --- |
| queryIsolatedFiles(callback: [QueryCallback](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#querycallback>), batchNum?: number): void | 获取已隔离文件的文件信息。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 通过声明查询结果回调queryCallback，并调用[queryIsolatedFiles](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#queryisolatedfiles>)接口，获取已隔离文件的文件信息。

   ```
   1. function startQueryTask() {
   2. // 查询隔离文件信息回调
   3. let onQuery: (files: virusRemediation.IsolatedFileInfo[]) => void = (files: virusRemediation.IsolatedFileInfo[]) => {
   4. files.forEach((value: virusRemediation.IsolatedFileInfo, index: number) => {
   5. console.info(`Succeeded in getting isolated file, file id: ${value.id}.`);
   6. })
   7. };
   8. // 查询隔离文件信息结束通知
   9. let onComplete: () => void = () => {
   10. console.info(`Query completed`);
   11. };
   12. // 查询隔离文件信息错误报告
   13. let onError: (code: number, message: string) => void = (code: number, message: string) => {
   14. console.error(`Query error, error code: ${code}, message: ${message}`);
   15. }
   16. let queryCallback: virusRemediation.QueryCallback = {
   17. onQuery: onQuery,
   18. onComplete: onComplete,
   19. onError: onError
   20. };
   21. try {
   22. virusRemediation.queryIsolatedFiles(queryCallback);
   23. } catch (error) {
   24. console.error(`Failed to get isolated file. Error: ${error}`);
   25. }
   26. }
   ```
