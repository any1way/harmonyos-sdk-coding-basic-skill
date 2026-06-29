---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-unrestricted-app-list
title: 添加、删除和获取放通应用列表
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 添加、删除和获取放通应用列表
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:08+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1b02f48d2a05c866ccd0ab45de09c5ebfb70407686f46234aa1a1930647fb336
---
说明

从6.1.1(24)版本开始，新增添加、删除和获取放通应用列表的接口，支持用户维护放通应用列表。

## 场景介绍

为应用提供添加、删除和获取放通应用列表的能力，添加到列表中的应用将不受[updatePolicy](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#updatepolicy>)接口下发的网络、U盘、蓝牙、星闪、Samba客户端和服务端策略管控，但打印管控策略仍会受到限制。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md>)。

| 接口名 | 描述 |
| --- | --- |
| [addUnrestrictedApplicationList](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#addunrestrictedapplicationlist>)(appIds: Array<string>, userId?: number): Promise<void> | 使用Promise方式添加放通应用列表。 |
| [removeUnrestrictedApplicationList](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#removeunrestrictedapplicationlist>)(appIds: Array<string>, userId?: number): Promise<void> | 使用Promise方式删除放通应用列表。 |
| [getUnrestrictedApplicationList](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#getunrestrictedapplicationlist>)(userId?: number): Promise<Array<string>> | 使用Promise方式获取放通应用列表。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { osAccount, BusinessError } from '@kit.BasicServicesKit';
   3. import { bundleManager } from '@kit.AbilityKit';
   ```
2. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口[addUnrestrictedApplicationList](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#addunrestrictedapplicationlist>)，添加放通应用列表。

   ```
   1. async function testAddUnrestrictedApplicationList() {
   2. try {
   3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   4. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
   5. let userId: number = await accountManager.getOsAccountLocalId();
   6. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
   7. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
   8. let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
   9. let appId: string = bundleInfo.signatureInfo.appId;
   10. let appIds: string[] = [appId];

   12. guard.addUnrestrictedApplicationList(appIds, userId).then(() => {
   13. console.info(`Succeeded in adding the application to the unrestricted list.`);
   14. }).catch((error: BusinessError) => {
   15. console.error(`Failed to add the application to the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
   16. })
   17. } catch (err) {
   18. console.error(`Failed to test addUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
   19. }
   20. }
   ```
3. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口[getUnrestrictedApplicationList](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#getunrestrictedapplicationlist>)，可以查看放通应用列表。

   ```
   1. async function testGetUnrestrictedApplicationList() {
   2. try {
   3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   4. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
   5. let userId: number = await accountManager.getOsAccountLocalId();

   7. guard.getUnrestrictedApplicationList(userId).then((appIds: string[]) => {
   8. console.info(`Succeeded in getting the application to the unrestricted list. appIds: ${appIds.toString()}`);
   9. }).catch((error: BusinessError) => {
   10. console.error(`Failed to get the application to the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
   11. })
   12. } catch (err) {
   13. console.error(`Failed to test getUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
   14. }
   15. }
   ```
4. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口[removeUnrestrictedApplicationList](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#removeunrestrictedapplicationlist>)，可以删除放通应用列表。

   ```
   1. async function testRemoveUnrestrictedApplicationList() {
   2. try {
   3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   4. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
   5. let userId: number = await accountManager.getOsAccountLocalId();

   7. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
   8. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
   9. let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
   10. let appId: string = bundleInfo.signatureInfo.appId;
   11. let appIds: string[] = [appId];

   13. guard.removeUnrestrictedApplicationList(appIds, userId).then(() => {
   14. console.info(`Succeeded in removing the application to the unrestricted list.`);
   15. }).catch((error: BusinessError) => {
   16. console.error(`Failed to remove the application to the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
   17. })
   18. } catch (err) {
   19. console.error(`Failed to test removeUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
   20. }
   21. }
   ```
