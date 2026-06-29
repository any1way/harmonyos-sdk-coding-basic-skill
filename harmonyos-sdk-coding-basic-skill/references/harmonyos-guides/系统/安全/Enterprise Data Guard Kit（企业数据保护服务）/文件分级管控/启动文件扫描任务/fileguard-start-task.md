---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-start-task
title: 启动文件扫描任务
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 启动文件扫描任务
category: harmonyos-guides
scraped_at: 2026-06-01T11:16:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f385175053bb838d1ce2fd2de5c0aaf0c8d6badbb5262bf5ac8a2fdf18f92501
---
## 场景介绍

Enterprise Data Guard Kit为应用提供公共路径和指定目录的扫描能力，获取对应目录下的文件列表。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md>)。

| 接口名 | 描述 |
| --- | --- |
| [startFileScanTask](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#startfilescantask>)(type: [CommonDirScanType](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#commondirscantype>), callback: [ScanFileCallback](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#scanfilecallback>), batchNum?: number): void | 通过Callback的方式，扫描公共目录并返回结果。 |
| [startFileScanTask](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#startfilescantask-1>)(path: string, callback: [ScanFileCallback](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#scanfilecallback>), batchNum?: number): void | 通过Callback的方式，扫描指定目录并返回结果。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   ```
2. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，并且声明扫描结果回调函数。

   * 按照文件类型扫描公共空间文件，查看打印结果。

     ```
     1. function startFileScanTaskUnderCommonDir() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
     4. files.forEach((value: string, index: number) => {
     5. console.info(`Succeeded in getting file: ${value}.`);
     6. })
     7. };
     8. let onCompleteScanTask: (count: number) => void = (count: number) => {
     9. console.info(`Succeeded in getting count: ${count}.`);
     10. };
     11. let scanFileCallback: fileGuard.ScanFileCallback = {
     12. onReceiveFileList: onReceiveFileList,
     13. onTaskCompleted: onCompleteScanTask
     14. };
     15. guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
     16. }
     ```
   * 扫描公共空间指定路径下的文件，查看打印结果。

     ```
     1. function startFileScanTaskUnderSpecifiedDir() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test';
     4. let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
     5. files.forEach((value: string, index: number) => {
     6. console.info(`Succeeded in getting file: ${value}.`);
     7. })
     8. };
     9. let onCompleteScanTask: (count: number) => void = (count: number) => {
     10. console.info(`Succeeded in getting count: ${count}.`);
     11. };
     12. let scanFileCallback: fileGuard.ScanFileCallback = {
     13. onReceiveFileList: onReceiveFileList,
     14. onTaskCompleted: onCompleteScanTask
     15. };
     16. guard.startFileScanTask(path, scanFileCallback);
     17. }
     ```
