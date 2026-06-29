---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-jumping-rope
title: 跳绳
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 跳绳
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e191e110cfd5c4654ea6610cf6d81474d1b52579c2074592c66b629d44b4998e
---
跳绳相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.jumpingRope.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-16>) | 跳绳 | AI跳绳、智能跳绳设备 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.jumpingRope.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-15>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| jumpingRopeFeature | 跳绳特征数据 | [JumpingRopeFeature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#jumpingropefeature>) | M |
| calorie | 热量统计 | [CalorieSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#caloriesummary>) | M |
| skipSpeed | 跳跃速度统计 | [SkipSpeedSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#skipspeedsummary>) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartratesummary>) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.jumpingRope.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-15>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartrate>)[] | O |
| skipSpeed | 跳跃速度详情 | [SkipSpeed](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#skipspeed>)[] | O |
