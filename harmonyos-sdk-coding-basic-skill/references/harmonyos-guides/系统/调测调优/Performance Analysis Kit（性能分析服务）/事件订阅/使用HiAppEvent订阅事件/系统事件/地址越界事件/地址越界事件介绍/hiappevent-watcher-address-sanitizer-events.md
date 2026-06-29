---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events
title: 地址越界事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 地址越界事件 > 地址越界事件介绍
category: harmonyos-guides
scraped_at: 2026-06-01T11:25:10+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:9d0863ed7bc33d733c08a6aea7648f82c6b53fd71d0973df2a0356ed2a930a86
---
## 概述

地址越界问题是指访问了不合法的地址，导致程序运行出现异常，通常表现为应用崩溃。

开发者可通过HiAppEvent接口订阅地址越界事件，请参考以下文档。目前提供ArkTS和C/C++两种接口，按需选择。

* [订阅地址越界事件（ArkTS）](../订阅地址越界事件（ArkTS）/hiappevent-watcher-address-sanitizer-events-arkts.md)
* [订阅地址越界事件（C/C++）](../订阅地址越界事件（CC++）/hiappevent-watcher-address-sanitizer-events-ndk.md)

说明

地址越界事件支持在[应用分身](../../../../../../../../基础入门/开发基础知识/典型场景的开发指导/创建应用分身/app-clone.md)场景下使用 HiAppEvent 进行订阅，从 API version 22 开始支持在[输入法应用](<../../../../../../../../应用框架/IME Kit（输入法开发服务）/实现一个输入法应用/inputmethod-application-guide.md>)场景下使用 HiAppEvent 进行订阅。不支持在元服务场景下使用 HiAppEvent 进行订阅。

## 检测原理

详见[地址越界类问题检测](../../../../../故障检测/AddrSanitizer（地址越界）检测/address-sanitizer-guidelines.md)。

## 页面切换日志规格自定义参数

从**API version 24**开始支持页面切换日志配置。当应用发生地址越界故障时，系统可以收集并上报页面切换日志，帮助开发者定位问题。

### configEventPolicy接口说明

| 接口名 | 描述 |
| --- | --- |
| [configEventPolicy](<../../../../../../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiviewdfx.hiAppEvent (应用事件打点)/js-apis-hiviewdfx-hiappevent.md#hiappeventconfigeventpolicy22>) (policy: EventPolicy): Promise<void> | 设置地址越界事件策略参数接口，支持开启地址越界事件的页面切换日志采集。 |

### configEventPolicy接口参数设置说明

开发者可以通过设置[EventPolicy](<../../../../../../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiviewdfx.hiAppEvent (应用事件打点)/js-apis-hiviewdfx-hiappevent.md#eventpolicy22>) 的参数来开启地址越界事件的页面切换日志采集。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| addressSanitizerPolicy | [AddressSanitizerPolicy](<../../../../../../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiviewdfx.hiAppEvent (应用事件打点)/js-apis-hiviewdfx-hiappevent.md#addresssanitizerpolicy24>) | 否 | 是 | 地址越界事件配置策略。 |

参数配置示例：

```
1. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';
2. import { deviceInfo, BusinessError } from '@kit.BasicServicesKit';

4. let policy: hiAppEvent.EventPolicy = {
5. "addressSanitizerPolicy": {
6. "pageSwitchLogEnable": true // 启用页面切换日志
7. }
8. };
9. hiAppEvent.configEventPolicy(policy).then(() => {
10. hilog.info(0x0000, 'hiAppEvent', `Set addressSanitizer config policy successfully.`);
11. }).catch((err: BusinessError) => {
12. hilog.error(0x0000, 'hiAppEvent', `Failed to set addressSanitizer config policy. code: ${err.code}, message: ${err.message}`);
13. });
```

## 事件字段说明

### params字段说明

地址越界事件信息中params属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位：ms。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| pid | number | 应用的进程id。 |
| uid | number | 应用的用户id。 |
| type | string | 地址越界错误类型，取值范围详见type属性。 |
| external\_log | string[] | 故障日志文件路径。**为避免目录空间超限（限制参考log\_over\_limit），导致新生成的日志文件写入失败，日志文件处理完后请及时删除。** |
| log\_over\_limit | boolean | 生成的故障日志文件与已存在的日志文件总大小是否超过5M上限。true表示超过上限，日志写入失败；false表示未超过上限。 |
| page\_switch\_log | string | 页面切换日志路径，日志介绍详见[页面切换日志](../../../../../故障检测/通用日志/页面切换日志/pageswitch-log.md)。  **说明**：从API version 24开始支持。 |

### type字段说明

地址越界事件信息中type的详细描述如下：

| 取值 | 说明 |
| --- | --- |
| GWP-ASAN | 由[GWP-ASan](../../../../../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/使用GWP-ASan检测内存错误/bpta-stability-gwpasan-detection.md)触发的错误类型。 |
| UBSAN | 由[UBSan](../../../../../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/使用UBSan检测未定义行为/bpta-stability-ubsan-detection.md)触发的错误类型。 |
| TSAN | 由[TSan](../../../../../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/线程并发类问题检测/使用TSan检测线程问题/bpta-stability-tsan-detection.md)触发的错误类型。 |
| FDSAN | 从API version 20开始，可以支持订阅由[fdsan](../../../../../../../../NDK开发/代码开发/CC++标准库/fdsan使用指导/fdsan.md)触发的错误类型。 |
| stack tag-mismatch | [HWASan](../../../../../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/使用HWASan检测内存错误/bpta-stability-hwasan-detection.md)检测堆栈标记不匹配，可能是因为堆栈返回后使用、堆栈范围外使用或出界。 |
| alloc-dealloc-mismatch | 内存分配和释放方式不匹配。 |
| allocation-size-too-big | 分配过大的堆内存。 |
| calloc-overflow | calloc分配内存错误。 |
| container-overflow | 容器溢出。 |
| double-free | 重复释放的内存。 |
| dynamic-stack-buffer-overflow | 缓冲区访问超出堆栈分配对象的边界。 |
| global-buffer-overflow | 全局缓冲区溢出。 |
| heap-buffer-overflow | 堆缓冲区溢出。 |
| heap-use-after-free | 使用已释放的堆内存。 |
| invalid-allocation-alignment | 无效的内存分配对齐方式。 |
| memcpy-param-overlap | memcpy不支持重叠内存。 |
| new-delete-type-mismatch | 内存释放大小与分配大小不一致。 |
| stack-buffer-overflow | 堆栈缓冲区溢出。 |
| stack-buffer-underflow | 堆栈缓冲区下溢。 |
| stack-use-after-return | 在返回后使用堆栈内存。 |
| stack-use-after-scope | 使用超出范围的堆栈内存。 |
| strcat-param-overlap | 在重叠缓冲区中移动内存导致的错误。 |
| use-after-poison | 对内存地址投毒后被使用。 |
