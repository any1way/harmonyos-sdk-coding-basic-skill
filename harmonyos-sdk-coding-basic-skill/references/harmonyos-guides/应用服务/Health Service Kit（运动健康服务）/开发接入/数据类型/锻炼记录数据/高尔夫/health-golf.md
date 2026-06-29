---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-golf
title: 高尔夫
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 高尔夫
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3bdbb667b32f804fb7dbc2ba80b3793570fd4b1d9b6baad35b3656e16902fb1d
---
## 高尔夫练习场

### 高尔夫练习场相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.golfPractice.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-11>) | 高尔夫练习场 | 手环、手表 |

### 高尔夫练习场关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.golfPractice.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-10>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| golfPracticeFeature | 高尔夫练习场特征数据 | [GolfPracticeFeature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#golfpracticefeature>) | M |
| calorie | 热量统计 | [CalorieSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#caloriesummary>) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartratesummary>) | O |

### 高尔夫练习场关联的明细数据说明

字段定义：[exerciseSequenceHelper.golfPractice.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-10>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartrate>)[] | O |

## 高尔夫场地模式

### 高尔夫场地模式相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.golfCourseModel.EXERCISE\_TYPE](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#常量-10>) | 高尔夫场地模式 | 手环、手表 |

### 高尔夫场地模式关联的统计数据说明

字段定义：[exerciseSequenceHelper.golfCourseModel.SummaryFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#summaryfields-9>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| golfCourseModelFeature | 高尔夫场地模式特征数据 | [GolfCourseModelFeature](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#golfcoursemodelfeature>) | M |
| calorie | 热量统计 | [CalorieSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#caloriesummary>) | M |
| step | 步数统计 | [StepSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#stepsummary>) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartratesummary>) | O |
| distance | 距离统计 | [DistanceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#distancesummary>) | O |
| cadence | 步频统计 | [CadenceSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#cadencesummary>) | O |
| altitude | 海拔统计 | [AltitudeSummary](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#altitudesummary>) | O |

### 高尔夫场地模式关联的明细数据说明

字段定义：[exerciseSequenceHelper.golfCourseModel.DetailFields](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/exerciseSequenceHelper (锻炼记录类型常量)/health-api-exercisedequencehelper.md#detailfields-9>)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#exerciseheartrate>)[] | O |
| altitude | 海拔详情 | [Altitude](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/运动健康数据类型常量及模型定义/healthFields (运动健康数据字段)/health-api-healthfields.md#altitude>)[] | O |
