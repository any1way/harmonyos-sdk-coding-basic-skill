---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-elliptical
title: 椭圆机
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 椭圆机
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:788ecf272e4c703e6530772afeaac3531d67162fce0b5d984298a9dfbe167b44
---
椭圆机相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.elliptical.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-9>) | 椭圆机 | 手环、手表 |

## 椭圆机关联的统计数据说明

字段定义：[exerciseSequenceHelper.elliptical.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-8>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| calorie | 热量统计 | [CalorieSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#caloriesummary>) | M |
| distance | 距离统计 | [DistanceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#distancesummary>) | O |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartratesummary>) | O |
| speed | 速度统计 | [SpeedSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#speedsummary>) | O |
| step | 步数统计 | [StepSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#stepsummary>) | O |
| cadence | 步频统计 | [CadenceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#cadencesummary>) | O |
| resistance | 阻力统计 | [ResistanceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#resistancesummary>) | O |
| pedalingCadence | 踏频统计 | [PedalingCadenceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#pedalingcadencesummary>) | O |
| power | 功率统计 | [PowerSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#powersummary>) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.elliptical.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-8>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartrate>)[] | O |
| speed | 速度详情 | [Speed](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#speed>)[] | O |
| pedalingCadence | 踏频详情 | [PedalingCadence](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#pedalingcadence>)[] | O |
| power | 功率详情 | [Power](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#power>)[] | O |
| cadence | 步频详情 | [Cadence](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#cadence>)[] | O |
