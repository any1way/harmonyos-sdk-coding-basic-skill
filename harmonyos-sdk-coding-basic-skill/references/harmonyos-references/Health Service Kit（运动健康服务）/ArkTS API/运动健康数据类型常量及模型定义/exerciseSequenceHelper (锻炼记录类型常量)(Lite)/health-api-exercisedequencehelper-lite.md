---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisedequencehelper-lite
title: exerciseSequenceHelper (锻炼记录类型常量)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > exerciseSequenceHelper (锻炼记录类型常量)(Lite)
category: harmonyos-references
scraped_at: 2026-06-11T16:44:58+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:2c9b2fa3fc88d853eec460de88f7e30a7e524b40bb5be15aafb793fde131598e
---
本模块提供锻炼记录数据类型常量及数据模型。

**起始版本：** 6.1.1(24)

## 导入模块

Lite Wearable

```
1. import healthStore from '@hms.health.store';
```

说明

此模块为healthStore子模块，需通过healthStore.exerciseSequenceHelper方式使用。

## 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#datatype>) | 锻炼记录数据类型。 |

## badminton

Lite Wearable

羽毛球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#subdatatype>) | 羽毛球子数据类型。 |

### SummaryFields

Lite Wearable

type SummaryFields = healthFields.BadmintonSummary

羽毛球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.BadmintonSummary](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#badmintonsummary>) | 羽毛球统计数据字段列表。 |

### DetailFields

Lite Wearable

type DetailFields = healthFields.BadmintonDetail

羽毛球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.BadmintonDetail](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#badmintondetail>) | 羽毛球详情数据字段列表。 |

## tennis

Lite Wearable

网球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#subdatatype>) | 网球子数据类型。 |

### SummaryFields

Lite Wearable

type SummaryFields = healthFields.TennisSummary

网球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.TennisSummary](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#tennissummary>) | 网球统计数据字段列表。 |

### DetailFields

Lite Wearable

type DetailFields = healthFields.TennisDetail

网球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.TennisDetail](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#tennisdetail>) | 网球详情数据字段列表。 |

## stairClimb

Lite Wearable

爬楼数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#subdatatype>) | 爬楼子数据类型。 |

### SummaryFields

Lite Wearable

type SummaryFields = healthFields.StairClimbSummary

爬楼统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StairClimbSummary](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#stairclimbsummary>) | 爬楼统计数据字段列表。 |

### DetailFields

Lite Wearable

type DetailFields = healthFields.StairClimbDetail

爬楼详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StairClimbDetail](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#stairclimbdetail>) | 爬楼详情数据字段列表。 |

## soccer

Lite Wearable

足球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#subdatatype>) | 足球子数据类型。 |

### SummaryFields

Lite Wearable

type SummaryFields = healthFields.SoccerSummary

足球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SoccerSummary](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#soccersummary>) | 足球统计数据字段列表。 |

### DetailFields

Lite Wearable

type DetailFields = healthFields.SoccerDetail

足球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SoccerDetail](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#soccerdetail>) | 足球详情数据字段列表。 |

## pickleBall

Lite Wearable

匹克球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#subdatatype>) | 匹克球子数据类型。 |

### SummaryFields

Lite Wearable

type SummaryFields = healthFields.PickleBallSummary

匹克球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PickleBallSummary](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#pickleballsummary>) | 匹克球统计数据字段列表。 |

### DetailFields

Lite Wearable

type DetailFields = healthFields.PickleBallDetail

匹克球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PickleBallDetail](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#pickleballdetail>) | 匹克球详情数据字段列表。 |

## strengthTraining

Lite Wearable

力量训练数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

Lite Wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](<../../healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#subdatatype>) | 力量训练子数据类型。 |

### SummaryFields

Lite Wearable

type SummaryFields = healthFields.StrengthTrainingSummary

力量训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StrengthTrainingSummary](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#strengthtrainingsummary>) | 力量训练统计数据字段列表。 |

### DetailFields

Lite Wearable

type DetailFields = healthFields.StrengthTrainingDetail

力量训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StrengthTrainingDetail](<../healthFields (运动健康数据字段)(Lite)/health-api-healthfields-lite.md#strengthtrainingdetail>) | 力量训练详情数据字段列表。 |
