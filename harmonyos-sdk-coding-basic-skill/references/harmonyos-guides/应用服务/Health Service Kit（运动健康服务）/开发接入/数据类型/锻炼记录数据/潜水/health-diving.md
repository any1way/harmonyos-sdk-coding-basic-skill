---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-diving
title: 潜水
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 潜水
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1522ef32b23172583ca66b6f754df54338d14f94e7ddd6ae5d89db766fe7fca6
---
## 自由潜水

### 自由潜水相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.diving.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-8>) | 自由潜水 | 部分专业手表 |

### 自由潜水关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.diving.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-7>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| divingFeature | 自由潜水特征数据 | [DivingFeature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#divingfeature>) | M |
| location | 位置统计 | [LocationSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#locationsummary>) | O |
| divingDepth | 潜水深度统计 | [DivingDepthSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#divingdepthsummary>) | O |
| waterTemperature | 水温统计 | [WaterTemperatureSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#watertemperaturesummary>) | O |

### 自由潜水关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.diving.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-7>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| divingDepth | 潜水深度详情 | [DivingDepth](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#divingdepth>)[] | O |
| waterTemperature | 水温详情 | [WaterTemperature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#watertemperature>)[] | O |

## 水肺潜水

### 水肺潜水相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.scubaDiving.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-23>) | 水肺潜水 | 部分专业手表 |

### 水肺潜水关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.scubaDiving.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-22>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| scubaDivingFeature | 水肺潜水特征数据 | [ScubaDivingFeature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#scubadivingfeature>) | M |
| location | 位置统计 | [LocationSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#locationsummary>) | O |
| divingDepth | 潜水深度统计 | [DivingDepthSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#divingdepthsummary>) | O |
| waterTemperature | 水温统计 | [WaterTemperatureSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#watertemperaturesummary>) | O |

### 水肺潜水关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.scubaDiving.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-22>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| divingDepth | 潜水深度详情 | [DivingDepth](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#divingdepth>)[] | O |
| waterTemperature | 水温详情 | [WaterTemperature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#watertemperature>)[] | O |
