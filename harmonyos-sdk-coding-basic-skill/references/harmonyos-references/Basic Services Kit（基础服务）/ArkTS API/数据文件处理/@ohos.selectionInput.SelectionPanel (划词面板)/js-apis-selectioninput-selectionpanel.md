---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionpanel
title: @ohos.selectionInput.SelectionPanel (划词面板)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.selectionInput.SelectionPanel (划词面板)
category: harmonyos-references
scraped_at: 2026-06-11T16:17:26+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:be7aea8b3091d6c5958eff2daebed293dcb3b2633d3a325e88a80a18852d5b1a
---
本模块提供划词面板的属性信息和类型。

说明

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块仅支持PC/2in1设备。

## 导入模块

PC/2in1

```
1. import { PanelInfo, PanelType } from '@kit.BasicServicesKit';
```

## PanelInfo

PC/2in1

划词面板属性信息。

**系统能力：** SystemCapability.SelectionInput.Selection

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| panelType | [PanelType](js-apis-selectioninput-selectionpanel.md#paneltype) | 否 | 否 | 划词面板类型。 |
| x | number | 否 | 否 | 划词面板左上角的x轴坐标，单位为px。 |
| y | number | 否 | 否 | 划词面板左上角的y轴坐标，单位为px。 |
| width | number | 否 | 否 | 划词面板宽度，单位为px。 |
| height | number | 否 | 否 | 划词面板高度，单位为px。 |

## PanelType

PC/2in1

划词面板类型枚举。

**系统能力：** SystemCapability.SelectionInput.Selection

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MENU\_PANEL | 1 | 菜单面板可以作为一级面板，显示当前应用程序可以提供的功能，如翻译、搜索等。 |
| MAIN\_PANEL | 2 | 主面板可以作为二级面板，当用户点击菜单面板中的功能按钮时弹出，显示特定的翻译或搜索结果等。 |
