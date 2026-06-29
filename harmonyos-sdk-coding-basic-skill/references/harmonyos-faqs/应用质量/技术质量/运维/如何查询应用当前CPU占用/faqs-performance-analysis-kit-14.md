---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-14
title: 如何查询应用当前CPU占用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查询应用当前CPU占用
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c7e2674461dd4b3c08e0e9b50de09aa7231e2014f4ebab7e380818de7f238abd
---
目前有两种方式查询当前CPU占用：

在代码中查询：

可以使用 `hidebug.getCpuUsage` 接口查询 CPU 占用。参考代码如下：

```
1. let cpuUsage: number = hidebug.getCpuUsage();
```

[Hidebug.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/Hidebug.ets#L8-L8)

在命令行中查询：

* 根据hdc命令行工具指导，完成[环境准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hdc-V14#环境准备)。
* 正常连接设备。

  ```
  1. hidumper --cpuusage <pid>
  2. hidumper --cpuusage
  ```

**参考链接**

[hidebug.getCpuUsage](<../../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hidebug (Debug调试)/js-apis-hidebug.md#hidebuggetcpuusage9>)

[hidumper](../../../../../harmonyos-guides/系统/调测调优/调试命令/hidumper/hidumper/hidumper.md)
