---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-81
title: 如何查询应用进程的pid信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何查询应用进程的pid信息
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:58+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:7416d46fdfc3759bf492a4b56b072303f7fa155832a69af2c9b31bae02ceabf9
---
可以通过以下两种方式获取：

* 方式一：通过以下命令查询应用进程信息。

  执行hdc shell命令，进入设备的命令行。执行“ps -ef”命令，查看所有正在运行的进程信息。
* 方式二：通过调用[process](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.process (获取进程相关的信息)/js-apis-process.md>)相关接口查询。

  ```
  1. import { process } from '@kit.ArkTS';

  3. let pid = process.pid;
  ```

  [PidMsg.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/PidMsg.ets#L5-L7)
