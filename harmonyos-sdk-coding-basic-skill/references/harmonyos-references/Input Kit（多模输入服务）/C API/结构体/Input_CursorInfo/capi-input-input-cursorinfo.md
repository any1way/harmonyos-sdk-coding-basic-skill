---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorinfo
title: Input_CursorInfo
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_CursorInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:20:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d27bc95079b0feff39738df9a058494d376e237d2d26f16406f29f48dbc0a08e
---
```
1. typedef struct Input_CursorInfo Input_CursorInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。

**起始版本：** 22

**相关模块：** [input](../../模块/input/capi-input.md)

**所在头文件：** [oh\_input\_manager.h](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CursorInfo\_Create](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_cursorinfo_create) | 创建鼠标光标信息对象。通过调用[OH\_Input\_CursorInfo\_Destroy](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy)销毁鼠标光标信息对象。 |
| [OH\_Input\_CursorInfo\_Destroy](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy) | 销毁鼠标光标信息对象。 |
