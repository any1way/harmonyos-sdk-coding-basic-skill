---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-get-file-url
title: 获取文件URI
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 获取文件URI
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6e20031ed0dd8dd62de5ae0dbae48dfa91a62e85573798dc68a6e5a2c635180c
---
## 场景介绍

Enterprise Data Guard Kit为应用提供获取文件路径信息的能力，该路径可被应用直接打开，从而辅助判断是否是KIA文件。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md>)。

| 接口名 | 描述 |
| --- | --- |
| [getFileUri](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#getfileuri>)(path: string, callback: AsyncCallback<[FilePathInfo](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#filepathinfo>)>): void | 使用Callback方式获取文件路径信息。 |
| [getFileUri](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#getfileuri-1>)(path: string): Promise<[FilePathInfo](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#filepathinfo>)> | 使用Promise方式获取文件路径信息。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口getFileUri，获取文件URI。

   * 通过回调函数方式，获取文件URI。

     ```
     1. function getFileUriCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/test/test.txt';
     4. guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
     5. if (err) {
     6. console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
     7. } else {
     8. console.info(`Succeeded in getting file uri.`);
     9. }
     10. });
     11. }
     ```
   * 通过Promise方式，获取文件URI。

     ```
     1. function getFileUriPromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/test/test.txt';
     4. guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
     5. console.info(`Succeeded in getting the uri of file.`);
     6. }).catch((err: BusinessError) => {
     7. console.error(`Failed to get the uri of file. Code: ${err.code}, message: ${err.message}.`);
     8. });
     9. }
     ```
