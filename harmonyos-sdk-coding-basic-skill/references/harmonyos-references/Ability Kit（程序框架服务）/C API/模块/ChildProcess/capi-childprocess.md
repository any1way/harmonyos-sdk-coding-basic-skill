---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess
title: ChildProcess
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 模块 > ChildProcess
category: harmonyos-references
scraped_at: 2026-06-01T15:32:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6349af6eebbaac2ddf9fca855c0c406338b02028095b7856d89c0eabea82f550
---
## 概述

PhonePC/2in1TabletTVWearable

提供子进程的管理能力，支持创建Native子进程并在父子进程间建立IPC通道，用于实现多进程应用开发。

创建的子进程不支持UI界面，也不支持Context相关的接口调用。通过此模块和[childProcessManager](<../../../ArkTS API/Stage模型能力的接口/@ohos.app.ability.childProcessManager (子进程管理)/js-apis-app-ability-childprocessmanager.md>)（非SELF\_FORK模式）启动的子进程总数最大为512个。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [native\_child\_process.h](../../头文件/native_child_process.h/capi-native-child-process-h.md) | 支持创建Native子进程，并在父子进程间建立IPC通道。  引用文件：<AbilityKit/native\_child\_process.h>  库：libchild\_process.so |
