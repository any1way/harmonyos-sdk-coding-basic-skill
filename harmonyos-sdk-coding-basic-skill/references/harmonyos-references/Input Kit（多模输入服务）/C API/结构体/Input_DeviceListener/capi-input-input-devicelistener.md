---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-devicelistener
title: Input_DeviceListener
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_DeviceListener
category: harmonyos-references
scraped_at: 2026-06-11T16:20:25+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:25fe54d50be9a95e341196110771af43fe8b29aa832f2561518f4d190a09c861
---
```
1. typedef struct Input_DeviceListener {...} Input_DeviceListener
```

## 概述

PhonePC/2in1TabletTVWearable

定义一个结构体用于监听设备热插拔。

**起始版本：** 13

**相关模块：** [input](../../模块/input/capi-input.md)

**所在头文件：** [oh\_input\_manager.h](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| Input\_DeviceAddedCallback deviceAddedCallback | 定义一个回调函数，用于回调设备热插事件。 |
| Input\_DeviceRemovedCallback deviceRemovedCallback | 定义一个回调函数，用于回调设备热拔事件。 |
