---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-print-startup-event
title: 订阅或取消订阅打印服务启动事件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 订阅或取消订阅打印服务启动事件
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:10+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:261a470255c0d78e7af764ba2f5452ed3c1fd16f85635beea4f132020d39d861
---
说明

从6.1.1(24)版本开始，新增订阅或取消订阅打印服务启动事件接口，帮助用户获取打印服务启动时机，便于及时注册水印回调，从而启用打印水印功能。

## 场景介绍

应用需注册打印服务提供的水印注册函数以实现打印水印功能。由于打印服务并非常驻进程，应用可通过监听提供的onPrintStartup回调函数，获取打印服务启动的时机；在接收到回调后，即可向打印服务[注册水印回调](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.print (打印)/js-apis-print.md#printregisterwatermarkcallback24>)，从而完成水印功能的启用。同时，调用[onPrintStartup](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#onprintstartup>)回调本身也作为打印水印功能的使能标志，调用[offPrintStartup](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#offprintstartup>)则会关闭打印水印功能。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md>)。

| 接口名 | 描述 |
| --- | --- |
| [onPrintStartup](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#onprintstartup>)(callback: Callback<void>): void | 订阅打印服务启动事件。 |
| [offPrintStartup](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#offprintstartup>)(callback?: Callback<void>): void | 取消订阅打印服务启动事件。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   ```
2. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口[onPrintStartup](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#onprintstartup>)，订阅打印服务启动事件。

   ```
   1. function testOnPrintStartup() {
   2. console.info(`onPrintStartup start.`);
   3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   4. guard.onPrintStartup(() => {
   5. console.info(`Succeeded in listening print-startup.`);
   6. });
   7. }
   ```
3. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口[offPrintStartup](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#offprintstartup>)，取消订阅打印服务启动事件。

   ```
   1. function testOffPrintStartup() {
   2. console.info(`offPrintStartup start.`);
   3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   4. guard.offPrintStartup();
   5. }
   ```
