---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:59c4bc9aa4419190161f32efa79845b5557a120fcbcd53d779fd701286addab7
---
TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/线程并发类问题检测/使用TSan检测线程问题/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。
* TSan不支持静态链接libc或libc++库。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击**Run > Edit Configurations >** **Diagnostics**，勾选**Thread Sanitizer**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ZFJNqvomTom3drU9GP9uxQ/zh-cn_image_0000002571387464.png?HW-CC-KV=V1&HW-CC-Date=20260611T072944Z&HW-CC-Expire=86400&HW-CC-Sign=4A3F642CCFA7F883F2B705CDCA9002DDBD6F285457C2951404D9CFBC5B721DB5)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/t_aUPnUEQgu4CnuRQDcLVA/zh-cn_image_0000002571547106.png?HW-CC-KV=V1&HW-CC-Date=20260611T072944Z&HW-CC-Expire=86400&HW-CC-Sign=FAFBD706731AE931F7BF20BD9C0C7F127F333223F663101CD6600196A023790B)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```
   1. "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/DnU32JjDQKSJO8XfYdX9TQ/zh-cn_image_0000002571547104.png?HW-CC-KV=V1&HW-CC-Date=20260611T072944Z&HW-CC-Expire=86400&HW-CC-Sign=469AA35BFCC2CE77D243FB43150BD406819A95BF6D40673563B9B4CCA98D9131)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```
   1. "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/5nA2vzshSmOZvm6Fb3RD7Q/zh-cn_image_0000002571547102.png?HW-CC-KV=V1&HW-CC-Date=20260611T072944Z&HW-CC-Expire=86400&HW-CC-Sign=CE5EDC582F18DEA5ED12684D09715B27D0807CCD4452536016A3E1BA875D66FB)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/线程并发类问题检测/使用TSan检测线程问题/bpta-stability-tsan-detection.md#section1180812915516)。

   说明

   当前使用call\_once接口会存在TSan误报的现象，开发者可以在调用该接口的函数前添加\_\_attribute\_\_((no\_sanitize("thread")))来屏蔽该问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/X7w73LuLTCCV6m34NQ5Yqg/zh-cn_image_0000002602186637.png?HW-CC-KV=V1&HW-CC-Date=20260611T072944Z&HW-CC-Expire=86400&HW-CC-Sign=4C269EB51CE1CB7488D42CF470BB6DD213ABE96D0049F310D71F82E12EDD6A8D)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Axk3GV2gTCyjEIq4zKqSzw/zh-cn_image_0000002602186639.png?HW-CC-KV=V1&HW-CC-Date=20260611T072944Z&HW-CC-Expire=86400&HW-CC-Sign=0BAAF4C3A0A5767F4FD3A79329550A9D8A1440420E2EDCE05FEA7DEF0A49B259 "点击放大")
