---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window (窗口) > 模块描述
category: harmonyos-references
scraped_at: 2026-06-01T15:38:12+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:ae9bad3c179983dfb89f898a9f27b72424ea67f942cb0c44ab0c661d05685ef1
---
提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。

该模块提供以下窗口相关的常用功能：

* [Window](<../Interface (Window)/arkts-apis-window-window.md>)：当前窗口实例，窗口管理器管理的基本单元。
* [WindowStage](<../Interface (WindowStage)/arkts-apis-window-windowstage.md>)：窗口管理器。管理各个基本窗口单元。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](<../../../../../ArkTS API/SysCap (系统能力)/js-apis-syscap.md#caniuse>)接口判断当前设备是否支持此syscap及对应接口。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { window } from '@kit.ArkUI';
```
