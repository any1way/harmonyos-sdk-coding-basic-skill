---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-scan
title: 启动应用目录文件扫描任务
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 文件访问与处置 > 启动应用目录文件扫描任务
category: harmonyos-guides
scraped_at: 2026-06-11T14:45:09+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:efe5aa8042f971549679cd1aa4c016b2c0428e1df73db7e5b739bbda4179ce0c
---
## 基本概念

启动应用目录文件扫描功能帮助安全防护类应用在开始扫描前获取应用文件列表。

## 场景介绍

由于应用沙箱限制，安全防护类应用无法获取设备上安装应用的相关文件。启动应用目录文件扫描任务可帮助安全防护类应用获取应用安装包目录与应用el2级别加密数据目录下的文件列表，为威胁分析扫描和处置奠定基础。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#scanbundlefiles>)。

| 接口 | 描述 |
| --- | --- |
| scanBundleFiles(type: [ScanTargetType](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#scantargettype>), callback: [ScanCallback](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#scancallback>), bundleName?: string, batchNum?: number): void | 扫描应用安装包目录或应用el2级别加密数据目录并返回指定目录下的路径列表。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 通过声明扫描结果回调scanFileCallback，并调用接口[scanBundleFiles](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#scanbundlefiles>)，实现目标目录下文件列表的获取。bundleName参数用于指定要扫描的应用包名，不填则返回所有允许扫描的应用的文件。

   ```
   1. // 按照目标类型扫描对应目录的文件，查看打印结果
   2. function startFileScanTask() {
   3. // 接收扫描结果的回调函数，用于处理扫描得到的文件路径列表
   4. let onReceive: (paths: string[]) => void = (files: Array<string>) => {
   5. files.forEach((value: string, index: number) => {
   6. console.info(`Succeeded in getting file: ${value}.`);
   7. })
   8. };
   9. // 扫描完成通知回调
   10. let onComplete: () => void = () => {
   11. console.info(`Scan completed`);
   12. };
   13. // 扫描错误报告回调
   14. let onError: (code: number, message: string) => void = (code: number, message: string) => {
   15. console.error(`Scan error, error code: ${code}, message: ${message}`);
   16. }
   17. let scanFileCallback: virusRemediation.ScanCallback = {
   18. onReceive: onReceive,
   19. onComplete: onComplete,
   20. onError: onError
   21. };
   22. // 调用 scanBundleFiles 方法扫描应用安装包目录下的文件，并通过 scanFileCallback 回调处理结果
   23. try {
   24. virusRemediation.scanBundleFiles(virusRemediation.ScanTargetType.BUNDLE, scanFileCallback);
   25. } catch (error) {
   26. console.error(`Failed to scan bundle files. Error: ${error}`);
   27. }
   28. }
   ```
