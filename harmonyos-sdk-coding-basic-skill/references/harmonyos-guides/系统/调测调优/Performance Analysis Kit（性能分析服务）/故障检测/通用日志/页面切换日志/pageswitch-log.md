---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageswitch-log
title: 页面切换日志
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > 通用日志 > 页面切换日志
category: harmonyos-guides
scraped_at: 2026-06-01T11:24:49+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:13e827b425f905dab82617b4ed4dc518f9af8f576e73f7918b114a741a91817b
---
## 简介

页面切换日志用于记录应用页面切换栈，比如窗口创建销毁、页面切换等信息，帮助开发者通过该日志分析故障发生前用户操作，提高问题定位效率。

## 日志获取

如果进程通过hiappevent接口在某故障事件配置策略中，使能页面切换日志，例如[崩溃事件配置策略](<../../../../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiviewdfx.hiAppEvent (应用事件打点)/js-apis-hiviewdfx-hiappevent.md#appcrashpolicy24>)，当应用发生该故障时，hiappevent会将对应的页面切换日志快照文件返回给应用用于故障分析，日志快照文件格式如下所示：

```
1. page_switch-com.example.myapplication-1-1-20260509142812417.log
```

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 日志前缀 | 进程名 | 实例索引 | 文件索引 | 时间戳 | 日志后缀 |
| page\_switch | com.example.myapplication | 1 | 1 | 20260509142812417 | log |

说明

进程名：进程名中包含:、/、- 字符时，对应字符统一替换为 \_。

实例索引：多个进程共用沙箱场景（例如[多实例](../../../../../../基础入门/开发基础知识/典型场景的开发指导/创建应用多实例/multiinstance.md)或[ExtensionAbility组件](<../../../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/ExtensionAbility组件/extensionability-overview.md>)）会出现日志写冲突，所以页面切换日志会为每个进程创建一组日志文件，使用实例索引用于标识不同进程。取值范围：[1, 10]。

文件索引：同一进程名及实例索引下最多保留 2 个文件。取值范围：[1, 2]。

时间戳：格式为 YYYYMMDDhhmmssSSS，其中年（YYYY）占4位，月（MM）、日（DD）、时（hh）、分（mm）、秒（ss）各占2位，毫秒（SSS）占3位。

## 日志格式

日志快照文件中日志格式如下所示：

```
1. 2026-03-24 17:03:55.361   2569   2569 Hap onBackground
```

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 |
| --- | --- | --- | --- | --- |
| 日期 | 时间戳 | 进程号 | 线程号 | 日志内容 |
| 2026-03-24 | 17:03:55.361 | 2569 | 2569 | Hap onBackground |

说明

日志内容最多支持1024字节，超出截断处理。
