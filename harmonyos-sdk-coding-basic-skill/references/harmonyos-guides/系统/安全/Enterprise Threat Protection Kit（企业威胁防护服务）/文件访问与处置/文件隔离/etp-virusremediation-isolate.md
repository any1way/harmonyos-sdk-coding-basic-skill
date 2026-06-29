---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-isolate
title: 文件隔离
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 文件访问与处置 > 文件隔离
category: harmonyos-guides
scraped_at: 2026-06-11T14:45:11+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:b836ee0ebee19b6cc9e637c9ae4cc8dcd460ba5c8311e040dad05fac13f5867d
---
## 基本概念

文件隔离是指将检测到的威胁文件转移到安全隔离区。

## 场景介绍

在安全防护类应用检测到病毒、木马等恶意文件后可以使用文件隔离接口将恶意文件转移到安全隔离区，实现安全防护类应用对恶意文件的隔离能力。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#isolatethreatfile>)。

| 接口 | 描述 |
| --- | --- |
| isolateThreatFile(path: string): Promise<string> | 对指定路径文件进行隔离并获得隔离ID。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
   ```
2. 通过调用接口[isolateThreatFile](<../../../../../../harmonyos-references/Enterprise Threat Protection Kit（企业威胁防护服务）/ArkTS API/virusRemediation（文件访问与处置）/etp-virusremediation-interface.md#isolatethreatfile>)，实现对恶意文件的安全隔离。path参数为目标文件的绝对路径。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. // 隔离文件，打印被隔离文件对应的隔离id
   4. function isolateFilePromise() {
   5. // 恶意文件路径，此处为示例路径，实际使用时需替换为真实文件路径
   6. let maliciousFilePath: string = '/data/service/el2/test/test.txt';
   7. virusRemediation.isolateThreatFile(maliciousFilePath).then((id: string) => {
   8. console.info(`Succeeded in isolating file. Path: ${maliciousFilePath}, ID: ${id}.`);
   9. }).catch((err: BusinessError) => {
   10. // 根据错误码进行不同的业务处理
   11. if (err.code === 1023804001) {
   12. console.error('Invalid file type, only single files are supported.');
   13. } else if (err.code === 1023804002) {
   14. console.error('Application bundle path detected, please uninstall the app or disable running.');
   15. } else {
   16. console.error(`Failed to isolate file. Code: ${err.code}, message: ${err.message}.`);
   17. }
   18. });
   19. }
   ```
