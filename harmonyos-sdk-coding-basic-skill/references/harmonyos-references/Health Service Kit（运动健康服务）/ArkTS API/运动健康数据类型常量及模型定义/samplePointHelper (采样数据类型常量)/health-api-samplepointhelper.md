---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-samplepointhelper
title: samplePointHelper (采样数据类型常量)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > samplePointHelper (采样数据类型常量)
category: harmonyos-references
scraped_at: 2026-06-01T16:34:34+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c42d1392d91e11b627aac75f7ee109924bac86359ae11776707987ab26d3f49b
---
本模块提供采样数据类型常量及数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.samplePointHelper方式使用。

## bloodOxygenSaturation

PhoneTabletWearable

血氧数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 血氧数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.BloodOxygenSaturation

血氧采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BloodOxygenSaturation](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bloodoxygensaturation>) | 血氧采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.BloodOxygenSaturation

血氧采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BloodOxygenSaturation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodoxygensaturation>) | 血氧采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.BloodOxygenSaturationAggregateResult

血氧采样数据聚合统计结果模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BloodOxygenSaturationAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bloodoxygensaturationaggregateresult>) | 血氧采样数据聚合统计结果模型 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.BloodOxygenSaturationAggregateRequest

血氧采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BloodOxygenSaturationAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bloodoxygensaturationaggregaterequest>) | 血氧采样数据聚合统计请求模型 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.BloodOxygenSaturationAggregation

血氧采样数据支持的聚合统计字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BloodOxygenSaturationAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodoxygensaturationaggregation>) | 血氧采样数据支持的聚合统计字段列表。 |

## bloodPressure

PhoneTabletWearable

血压数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 血压数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.BloodPressure

血压采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BloodPressure](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bloodpressure>) | 血压采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.BloodPressure

血压采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BloodPressure](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodpressure>) | 血压采样数据字段列表。 |

## bodyTemperature

PhoneTabletWearable

体温数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 体温数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.BodyTemperature

体温采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BodyTemperature](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bodytemperature>) | 体温采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.BodyTemperature

体温采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BodyTemperature](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bodytemperature>) | 体温采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.BodyTemperatureAggregateResult

体温采样数据聚合统计结果模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BodyTemperatureAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bodytemperatureaggregateresult>) | 体温采样数据聚合统计结果模型。 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.BodyTemperatureAggregateRequest

体温采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BodyTemperatureAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#bodytemperatureaggregaterequest>) | 体温采样数据聚合统计请求模型。 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.BodyTemperatureAggregation

体温采样数据支持的聚合统计字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BodyTemperatureAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bodytemperatureaggregation>) | 体温采样数据支持的聚合统计字段列表。 |

## dailyActivities

PhoneTabletWearable

日常活动数据类型常量及数据模型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 日常活动数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.DailyActivities

日常活动采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.DailyActivities](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#dailyactivities>) | 日常活动采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.DailyActivities

日常活动采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.DailyActivities](<../healthFields (运动健康数据字段)/health-api-healthfields.md#dailyactivities>) | 日常活动采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.DailyActivitiesAggregateResult

日常活动采样数据聚合统计结果模型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.DailyActivitiesAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#dailyactivitiesaggregateresult>) | 日常活动采样数据聚合结果模型。 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.DailyActivitiesAggregateRequest

日常活动采样数据聚合统计请求模型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.DailyActivitiesAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#dailyactivitiesaggregaterequest>) | 日常活动采样数据聚合请求模型。 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.DailyActivitiesAggregation

日常活动采样数据支持的聚合统计字段列表。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.DailyActivitiesAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#dailyactivitiesaggregation>) | 日常活动采样数据支持的聚合统计字段列表。 |

## emotion

PhoneTabletWearable

情绪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 情绪数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Emotion

情绪采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Emotion](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#emotion>) | 情绪采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.Emotion

情绪采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| [healthFields.Emotion](<../healthFields (运动健康数据字段)/health-api-healthfields.md#emotion>) | 情绪采样数据字段列表。 |

## heartRate

PhoneTabletWearable

动态心率数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 动态心率数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.HeartRate

动态心率采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.HeartRate](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#heartrate>) | 动态心率采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.HeartRate

动态心率采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.HeartRate](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartrate>) | 动态心率采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.HeartRateAggregateResult

动态心率采样数据聚合统计结果模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.HeartRateAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#heartrateaggregateresult>) | 动态心率采样数据聚合统计结果模型。 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.HeartRateAggregateRequest

动态心率采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.HeartRateAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#heartrateaggregaterequest>) | 动态心率采样数据聚合统计请求模型。 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.HeartRateAggregation

动态心率采样数据支持的聚合统计字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.HeartRateAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartrateaggregation>) | 动态心率采样数据支持的聚合统计字段列表。 |

## heartRateVariability

PhoneTabletWearable

心率变异性数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 心率变异性数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.HeartRateVariability

心率变异性采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| [healthModels.HeartRateVariability](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#heartratevariability>) | 心率变异性采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.HeartRateVariability

心率变异性采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| [healthFields.HeartRateVariability](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartratevariability>) | 心率变异性采样数据字段列表。 |

## height

PhoneTabletWearable

身高数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 身高数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Height

身高采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Height](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#height>) | 身高采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.Height

身高采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.Height](<../healthFields (运动健康数据字段)/health-api-healthfields.md#height>) | 身高采样数据字段列表。 |

## restingHeartRate

PhoneTabletWearable

静息心率数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 静息心率数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.RestingHeartRate

静息心率采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.RestingHeartRate](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#restingheartrate>) | 静息心率采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.RestingHeartRate

静息心率采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RestingHeartRate](<../healthFields (运动健康数据字段)/health-api-healthfields.md#restingheartrate>) | 静息心率采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.RestingHeartRateAggregateResult

静息心率采样数据聚合统计结果模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.RestingHeartRateAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#restingheartrateaggregateresult>) | 静息心率采样数据聚合统计结果模型。 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.RestingHeartRateAggregateRequest

静息心率采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.RestingHeartRateAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#restingheartrateaggregaterequest>) | 静息心率采样数据聚合统计请求模型。 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.RestingHeartRateAggregation

静息心率采样数据支持的聚合统计字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RestingHeartRateAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#restingheartrateaggregation>) | 静息心率采样数据支持的聚合统计字段列表。 |

## skinTemperature

PhoneTabletWearable

皮肤体温数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 皮肤体温数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.SkinTemperature

皮肤体温采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SkinTemperature](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#skintemperature>) | 皮肤体温采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.SkinTemperature

皮肤体温采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SkinTemperature](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skintemperature>) | 皮肤体温采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.SkinTemperatureAggregateResult

皮肤体温采样数据聚合统计结果模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SkinTemperatureAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#skintemperatureaggregateresult>) | 皮肤体温采样数据聚合统计结果模型。 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.SkinTemperatureAggregateRequest

皮肤体温采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SkinTemperatureAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#skintemperatureaggregaterequest>) | 皮肤体温采样数据聚合统计请求模型。 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.SkinTemperatureAggregation

皮肤体温采样数据支持的聚合统计字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SkinTemperatureAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skintemperatureaggregation>) | 皮肤体温采样数据支持的聚合统计字段列表。 |

## stress

PhoneTabletWearable

压力数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 压力数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Stress

压力采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Stress](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#stress>) | 压力采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.Stress

压力采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.Stress](<../healthFields (运动健康数据字段)/health-api-healthfields.md#stress>) | 压力采样数据字段列表。 |

### AggregateResult

PhoneTabletWearable

type AggregateResult = healthModels.StressAggregateResult

压力采样数据聚合统计结果模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.StressAggregateResult](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#stressaggregateresult>) | 压力采样数据聚合统计结果模型。 |

### AggregateRequest

PhoneTabletWearable

type AggregateRequest = healthModels.StressAggregateRequest

压力采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.StressAggregateRequest](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#stressaggregaterequest>) | 压力采样数据聚合统计请求模型。 |

### AggregateFields

PhoneTabletWearable

type AggregateFields = healthFields.StressAggregation

压力采样数据支持的聚合统计字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.StressAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#stressaggregation>) | 压力采样数据支持的聚合统计字段列表。 |

## weight

PhoneTabletWearable

体重数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 体重数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Weight

体重采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Weight](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#weight>) | 体重采样数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.Weight

体重采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.Weight](<../healthFields (运动健康数据字段)/health-api-healthfields.md#weight>) | 体重采样数据字段列表。 |
