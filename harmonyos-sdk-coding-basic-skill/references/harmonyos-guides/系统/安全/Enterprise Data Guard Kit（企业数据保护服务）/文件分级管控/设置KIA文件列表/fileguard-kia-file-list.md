---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-file-list
title: 设置KIA文件列表
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置KIA文件列表
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:05+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:81f13ad37b58bee600473abf3b669b4fed61deca0a027c582565f4c83c02dad5
---
## 场景介绍

Enterprise Data Guard Kit为应用提供设置KIA文件列表的能力，HarmonyOS系统根据管控策略对KIA文件列表中的文件实行管控。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md>)。

| 接口名 | 描述 |
| --- | --- |
| [setKiaFilelist](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#setkiafilelist>)(filelist: string, callback: AsyncCallback<void>): void | 使用Callback方式设置KIA文件列表。 |
| [setKiaFilelist](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#setkiafilelist-1>)(filelist: string): Promise<void> | 使用Promise方式设置KIA文件列表。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { osAccount, BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，将KIA文件列表对象转为字符串，调用接口setKiaFilelist，设置KIA文件列表。

   * 通过回调函数方式，设置KIA文件列表。

     ```
     1. async function setKiaFilelistCallback() {
     2. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
     3. let userId: number = await accountManager.getOsAccountLocalId();

     5. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     6. let fileListStr: string =
     7. '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
     8. '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
     9. '"kia_keyword":["key1","key2","key3"],' +
     10. '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
     11. '"compress_suffix":[".rar", ".zip"],' +
     12. `"user_id":${userId},` +
     13. '"kia_update_type":0}';
     14. guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
     15. if (err) {
     16. console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
     17. } else {
     18. console.info(`Succeeded in setting the list of KIA file.`);
     19. }
     20. });
     21. }
     ```
   * 通过Promise方式，设置KIA文件列表。

     ```
     1. async function setKiaFilelistPromise() {
     2. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
     3. let userId: number = await accountManager.getOsAccountLocalId();

     5. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     6. let fileListStr: string =
     7. '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
     8. '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
     9. '"kia_keyword":["key1","key2","key3"],' +
     10. '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
     11. '"compress_suffix":[".rar", ".zip"],' +
     12. `"user_id":${userId},` +
     13. '"kia_update_type":0}';
     14. guard.setKiaFilelist(fileListStr).then(() => {
     15. console.info(`Succeeded in setting the list of KIA file.`);
     16. }).catch((err: BusinessError) => {
     17. console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
     18. });
     19. }
     ```
