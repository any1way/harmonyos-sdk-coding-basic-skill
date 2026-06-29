---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-running
title: 跑步
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 跑步
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d21a146220430b868aeea2c49c7ede297b6fb78627c90bfff4c7391622580a2
---
跑步相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.running.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-22>) | 户外跑步 | 手机、手表、手环 |
| [exerciseSequenceHelper.indoorRunning.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-14>) | 室内跑步/跑步机 | 手机、手表、手环 |
| [exerciseSequenceHelper.trailRunning.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-29>) | 越野跑 | 手机、手表、手环 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.running.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-21>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#distancesummary>) | M |
| calorie | 热量统计 | [CalorieSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#caloriesummary>) | M |
| speed | 速度统计 | [SpeedSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#speedsummary>) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartratesummary>) | O |
| step | 步数统计 | [StepSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#stepsummary>) | O |
| cadence | 步频统计 | [CadenceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#cadencesummary>) | O |
| altitude | 海拔统计 | [AltitudeSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#altitudesummary>) | O |
| location | 位置统计 | [LocationSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#locationsummary>) | O |
| runningForm | 跑姿统计 | [RunningFormSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#runningformsummary>) | O |
| runningFeature | 跑步特征数据 | [RunningFeature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#runningfeature>) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.running.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-21>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartrate>)[] | O |
| speed | 速度详情 | [Speed](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#speed>)[] | O |
| cadence | 步频详情 | [Cadence](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#cadence>)[] | O |
| runningForm | 跑姿详情 | [RunningForm](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#runningform>)[] | O |
| location | 位置详情 | [Location](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#location>)[] | O |
| altitude | 海拔详情 | [Altitude](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#altitude>)[] | O |
