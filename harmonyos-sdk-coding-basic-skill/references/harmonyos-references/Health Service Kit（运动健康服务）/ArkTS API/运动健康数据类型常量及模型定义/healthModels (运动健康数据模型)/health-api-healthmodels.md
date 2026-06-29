---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels
title: healthModels (运动健康数据模型)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthModels (运动健康数据模型)
category: harmonyos-references
scraped_at: 2026-06-01T16:34:33+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a9c194030bb0d12d687a97a8bee10f3f9f5b939936d9e48bf0ee4169afbef750
---
本模块提供运动健康数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.healthModels方式使用。

## Adventures

PhoneTabletWearable

type Adventures = healthStore.ExerciseSequence<healthFields.AdventuresSummary, healthFields.AdventuresDetail>

户外探险锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.AdventuresSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#adventuressummary>), [healthFields.AdventuresDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#adventuresdetail>)> | 户外探险锻炼记录数据模型。 |

## Basketball

PhoneTabletWearable

type Basketball = healthStore.ExerciseSequence<healthFields.BasketballSummary, healthFields.BasketballDetail>

篮球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.BasketballSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#basketballsummary>), [healthFields.BasketballDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#basketballdetail>)> | 篮球锻炼记录数据模型。 |

## Biathlon

PhoneTabletWearable

type Biathlon = healthStore.ExerciseSequence<healthFields.BiathlonSummary, healthFields.BiathlonDetail>

冬季两项锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.BiathlonSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#biathlonsummary>), [healthFields.BiathlonDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#biathlondetail>)> | 冬季两项锻炼记录数据模型。 |

## BloodOxygenSaturation

PhoneTabletWearable

type BloodOxygenSaturation = healthStore.SamplePoint<healthFields.BloodOxygenSaturation>

血氧采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.BloodOxygenSaturation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodoxygensaturation>)> | 血氧采样数据模型。 |

## BloodOxygenSaturationAggregateRequest

PhoneTabletWearable

type BloodOxygenSaturationAggregateRequest = healthStore.AggregateRequest<healthFields.BloodOxygenSaturationAggregation>

血氧采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.BloodOxygenSaturationAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodoxygensaturationaggregation>)> | 血氧采样数据聚合统计请求模型。 |

## BloodOxygenSaturationAggregateResult

PhoneTabletWearable

type BloodOxygenSaturationAggregateResult = healthStore.AggregateResult<healthFields.BloodOxygenSaturationAggregation>

血氧聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.BloodOxygenSaturationAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodoxygensaturationaggregation>)> | 血氧聚合结果数据模型。 |

## BloodPressure

PhoneTabletWearable

type BloodPressure = healthStore.SamplePoint<healthFields.BloodPressure>

血压采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.BloodPressure](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bloodpressure>)> | 血压采样数据模型。 |

## Bmx

PhoneTabletWearable

type Bmx = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

BMX自行车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.CyclingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingsummary>), [healthFields.CyclingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingdetail>)> | BMX自行车锻炼记录数据模型。 |

## BodyTemperature

PhoneTabletWearable

type BodyTemperature = healthStore.SamplePoint<healthFields.BodyTemperature>

体温采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.BodyTemperature](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bodytemperature>)> | 体温采样数据模型。 |

## BodyTemperatureAggregateRequest

PhoneTabletWearable

type BodyTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.BodyTemperatureAggregation>

体温采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.BodyTemperatureAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bodytemperatureaggregation>)> | 体温采样数据聚合统计请求模型。 |

## BodyTemperatureAggregateResult

PhoneTabletWearable

type BodyTemperatureAggregateResult = healthStore.AggregateResult<healthFields.BodyTemperatureAggregation>

体温聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.BodyTemperatureAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#bodytemperatureaggregation>)> | 体温聚合结果数据模型。 |

## BreathHoldingTest

PhoneTabletWearable

type BreathHoldingTest = healthStore.ExerciseSequence<healthFields.BreathHoldingTestSummary, healthFields.BreathHoldingTestDetail>

闭气测试锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.BreathHoldingTestSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#breathholdingtestsummary>), [healthFields.BreathHoldingTestDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#breathholdingtestdetail>)> | 闭气测试锻炼记录数据模型。 |

## BreathHoldingTrain

PhoneTabletWearable

type BreathHoldingTrain = healthStore.ExerciseSequence<healthFields.BreathHoldingTrainSummary, healthFields.BreathHoldingTrainDetail>

闭气训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.BreathHoldingTrainSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#breathholdingtrainsummary>), [healthFields.BreathHoldingTrainDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#breathholdingtraindetail>)> | 闭气训练锻炼记录数据模型。 |

## Cycling

PhoneTabletWearable

type Cycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

户外骑行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.CyclingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingsummary>), [healthFields.CyclingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingdetail>)> | 户外骑行锻炼记录数据模型。 |

## DailyActivities

PhoneTabletWearable

type DailyActivities = healthStore.SamplePoint<healthFields.DailyActivities>

日常活动采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.DailyActivities](<../healthFields (运动健康数据字段)/health-api-healthfields.md#dailyactivities>)> | 日常活动采样数据模型。 |

## DailyActivitiesAggregateRequest

PhoneTabletWearable

type DailyActivitiesAggregateRequest = healthStore.AggregateRequest<healthFields.DailyActivitiesAggregation>

日常活动采样数据聚合统计请求模型。

**元服务API**：从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.DailyActivitiesAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#dailyactivitiesaggregation>)> | 日常活动采样数据聚合统计请求模型。 |

## DailyActivitiesAggregateResult

PhoneTabletWearable

type DailyActivitiesAggregateResult = healthStore.AggregateResult<healthFields.DailyActivitiesAggregation>

日常活动聚合结果数据模型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.DailyActivitiesAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#dailyactivitiesaggregation>)> | 日常活动聚合结果数据模型。 |

## Diving

PhoneTabletWearable

type Diving = healthStore.ExerciseSequence<healthFields.DivingSummary, healthFields.DivingDetail>

自由潜水锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.DivingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#divingsummary>), [healthFields.DivingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#divingdetail>)> | 自由潜水锻炼记录数据模型。 |

## Elliptical

PhoneTabletWearable

type Elliptical = healthStore.ExerciseSequence<healthFields.EllipticalSummary, healthFields.EllipticalDetail>

椭圆机锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.EllipticalSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#ellipticalsummary>), [healthFields.EllipticalDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#ellipticaldetail>)> | 椭圆机锻炼记录数据模型。 |

## Emotion

PhoneTabletWearable

type Emotion = healthStore.SamplePoint<healthFields.Emotion>

情绪采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.Emotion](<../healthFields (运动健康数据字段)/health-api-healthfields.md#emotion>)> | 情绪采样数据模型。 |

## GolfCourseModel

PhoneTabletWearable

type GolfCourseModel = healthStore.ExerciseSequence<healthFields.GolfCourseModelSummary, healthFields.GolfCourseModelDetail>

高尔夫场地模式锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.GolfCourseModelSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#golfcoursemodelsummary>), [healthFields.GolfCourseModelDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#golfcoursemodeldetail>)> | 高尔夫场地模式锻炼记录数据模型。 |

## GolfPractice

PhoneTabletWearable

type GolfPractice = healthStore.ExerciseSequence<healthFields.GolfPracticeSummary, healthFields.GolfPracticeDetail>

高尔夫练习场模式锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.GolfPracticeSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#golfpracticesummary>), [healthFields.GolfPracticeDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#golfpracticedetail>)> | 高尔夫练习场模式锻炼记录数据模型。 |

## HeartRate

PhoneTabletWearable

type HeartRate = healthStore.SamplePoint<healthFields.HeartRate>

动态心率采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.HeartRate](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartrate>)> | 动态心率采样数据模型。 |

## HeartRateAggregateRequest

PhoneTabletWearable

type HeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.HeartRateAggregation>

动态心率采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.HeartRateAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartrateaggregation>)> | 动态心率采样数据聚合统计请求模型。 |

## HeartRateAggregateResult

PhoneTabletWearable

type HeartRateAggregateResult = healthStore.AggregateResult<healthFields.HeartRateAggregation>

动态心率聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.HeartRateAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartrateaggregation>)> | 动态心率聚合结果数据模型。 |

## HeartRateVariability

PhoneTabletWearable

type HeartRateVariability = healthStore.SamplePoint<healthFields.HeartRateVariability>

心率变异性采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.HeartRateVariability](<../healthFields (运动健康数据字段)/health-api-healthfields.md#heartratevariability>)> | 心率变异性采样数据模型。 |

## Height

PhoneTabletWearable

type Height = healthStore.SamplePoint<healthFields.Height>

身高采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.Height](<../healthFields (运动健康数据字段)/health-api-healthfields.md#height>)> | 身高采样数据模型。 |

## Hiking

PhoneTabletWearable

type Hiking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

徒步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.WalkingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#walkingsummary>), [healthFields.WalkingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#walkingdetail>)> | 徒步锻炼记录数据模型。 |

## IndoorCycling

PhoneTabletWearable

type IndoorCycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

室内单车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.CyclingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingsummary>), [healthFields.CyclingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingdetail>)> | 室内单车锻炼记录数据模型。 |

## IndoorRunning

PhoneTabletWearable

type IndoorRunning = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

室内跑步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.RunningSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#runningsummary>), [healthFields.RunningDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#runningdetail>)> | 室内跑步锻炼记录数据模型。 |

## IndoorWalking

PhoneTabletWearable

type IndoorWalking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

室内步行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.WalkingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#walkingsummary>), [healthFields.WalkingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#walkingdetail>)> | 室内步行锻炼记录数据模型。 |

## JumpingRope

PhoneTabletWearable

type JumpingRope = healthStore.ExerciseSequence<healthFields.JumpingRopeSummary, healthFields.JumpingRopeDetail>

跳绳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.JumpingRopeSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#jumpingropesummary>), [healthFields.JumpingRopeDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#jumpingropedetail>)> | 跳绳锻炼记录数据模型。 |

## MenstrualCycle

PhoneTabletWearable

type MenstrualCycle = healthStore.HealthSequence<healthFields.MenstrualCycle, healthFields.MenstrualCycleDetail>

生理周期健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.HealthSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#healthsequence>)<[healthFields.MenstrualCycle](<../healthFields (运动健康数据字段)/health-api-healthfields.md#menstrualcycle>), [healthFields.MenstrualCycleDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#menstrualcycledetail>)> | 生理周期健康记录数据模型。 |

## MountainHike

PhoneTabletWearable

type MountainHike = healthStore.ExerciseSequence<healthFields.MountainHikeSummary, healthFields.MountainHikeDetail>

登山锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.MountainHikeSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#mountainhikesummary>), [healthFields.MountainHikeDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#mountainhikedetail>)> | 登山锻炼记录数据模型。 |

## OpenWaterSwim

PhoneTabletWearable

type OpenWaterSwim = healthStore.ExerciseSequence<healthFields.OpenWaterSwimSummary, healthFields.OpenWaterSwimDetail>

开放水域游泳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.OpenWaterSwimSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#openwaterswimsummary>), [healthFields.OpenWaterSwimDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#openwaterswimdetail>)> | 开放水域游泳锻炼记录数据模型。 |

## PoolSwim

PhoneTabletWearable

type PoolSwim = healthStore.ExerciseSequence<healthFields.PoolSwimSummary, healthFields.PoolSwimDetail>

泳池游泳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.PoolSwimSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#poolswimsummary>), [healthFields.PoolSwimDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#poolswimdetail>)> | 泳池游泳锻炼记录数据模型。 |

## RestingHeartRate

PhoneTabletWearable

type RestingHeartRate = healthStore.SamplePoint<healthFields.RestingHeartRate>

静息心率采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.RestingHeartRate](<../healthFields (运动健康数据字段)/health-api-healthfields.md#restingheartrate>)> | 静息心率采样数据模型。 |

## RestingHeartRateAggregateRequest

PhoneTabletWearable

type RestingHeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.RestingHeartRateAggregation>

静息心率采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.RestingHeartRateAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#restingheartrateaggregation>)> | 静息心率采样数据聚合统计请求模型。 |

## RestingHeartRateAggregateResult

PhoneTabletWearable

type RestingHeartRateAggregateResult = healthStore.AggregateResult<healthFields.RestingHeartRateAggregation>

静息心率聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.RestingHeartRateAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#restingheartrateaggregation>)> | 静息心率聚合结果数据模型。 |

## Rower

PhoneTabletWearable

type Rower = healthStore.ExerciseSequence<healthFields.RowerSummary, healthFields.RowerDetail>

划船机锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.RowerSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#rowersummary>), [healthFields.RowerDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#rowerdetail>)> | 划船机锻炼记录数据模型。 |

## Rowing

PhoneTabletWearable

type Rowing = healthStore.ExerciseSequence<healthFields.RowingSummary, healthFields.RowingDetail>

赛艇锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.RowingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#rowingsummary>), [healthFields.RowingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#rowingdetail>)> | 赛艇锻炼记录数据模型。 |

## Running

PhoneTabletWearable

type Running = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

户外跑步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.RunningSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#runningsummary>), [healthFields.RunningDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#runningdetail>)> | 户外跑步锻炼记录数据模型。 |

## ScubaDiving

PhoneTabletWearable

type ScubaDiving = healthStore.ExerciseSequence<healthFields.ScubaDivingSummary, healthFields.ScubaDivingDetail>

水肺潜水锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.ScubaDivingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#scubadivingsummary>), [healthFields.ScubaDivingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#scubadivingdetail>)> | 水肺潜水锻炼记录数据模型。 |

## Skiing

PhoneTabletWearable

type Skiing = healthStore.ExerciseSequence<healthFields.SkiingSummary, healthFields.SkiingDetail>

滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.SkiingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skiingsummary>), [healthFields.SkiingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skiingdetail>)> | 滑雪锻炼记录数据模型。 |

## SkinTemperature

PhoneTabletWearable

type SkinTemperature = healthStore.SamplePoint<healthFields.SkinTemperature>

皮肤体温采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.SkinTemperature](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skintemperature>)> | 皮肤体温采样数据模型。 |

## SkinTemperatureAggregateRequest

PhoneTabletWearable

type SkinTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.SkinTemperatureAggregation>

皮肤体温采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.SkinTemperatureAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skintemperatureaggregation>)> | 皮肤体温采样数据聚合统计请求模型。 |

## SkinTemperatureAggregateResult

PhoneTabletWearable

type SkinTemperatureAggregateResult = healthStore.AggregateResult<healthFields.SkinTemperatureAggregation>

皮肤体温聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.SkinTemperatureAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#skintemperatureaggregation>)> | 皮肤体温聚合结果数据模型。 |

## Sled

PhoneTabletWearable

type Sled = healthStore.ExerciseSequence<healthFields.SledSummary, healthFields.SledDetail>

滑雪橇锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.SledSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sledsummary>), [healthFields.SledDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleddetail>)> | 滑雪橇锻炼记录数据模型。 |

## SleepNapRecord

PhoneTabletWearable

type SleepNapRecord = healthStore.HealthSequence<healthFields.SleepNap, healthFields.SleepDetail>

零星小睡健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.HealthSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#healthsequence>)<[healthFields.SleepNap](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleepnap>), [healthFields.SleepDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleepdetail>)> | 零星小睡健康记录数据模型。 |

## SleepRecord

PhoneTabletWearable

type SleepRecord = healthStore.HealthSequence<healthFields.Sleep, healthFields.SleepDetail>

夜间睡眠健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.HealthSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#healthsequence>)<[healthFields.Sleep](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleep>), [healthFields.SleepDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleepdetail>)> | 夜间睡眠健康记录数据模型。 |

## Snowboarding

PhoneTabletWearable

type Snowboarding = healthStore.ExerciseSequence<healthFields.SnowboardingSummary, healthFields.SnowboardingDetail>

单板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.SnowboardingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#snowboardingsummary>), [healthFields.SnowboardingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#snowboardingdetail>)> | 单板滑雪锻炼记录数据模型。 |

## Spinning

PhoneTabletWearable

type Spinning = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

动感单车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.CyclingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingsummary>), [healthFields.CyclingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#cyclingdetail>)> | 动感单车锻炼记录数据模型。 |

## Sports

PhoneTabletWearable

type Sports = healthStore.ExerciseSequence<healthFields.SportsSummary, healthFields.SportsDetail>

通用锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.SportsSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sportssummary>), [healthFields.SportsDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sportsdetail>)> | 通用锻炼记录数据模型。 |

## Stress

PhoneTabletWearable

type Stress = healthStore.SamplePoint<healthFields.Stress>

压力采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.Stress](<../healthFields (运动健康数据字段)/health-api-healthfields.md#stress>)> | 压力采样数据模型。 |

## StressAggregateRequest

PhoneTabletWearable

type StressAggregateRequest = healthStore.AggregateRequest<healthFields.StressAggregation>

压力采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregaterequest>)<[healthFields.StressAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#stressaggregation>)> | 压力采样数据聚合统计请求模型。 |

## StressAggregateResult

PhoneTabletWearable

type StressAggregateResult = healthStore.AggregateResult<healthFields.StressAggregation>

压力聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#aggregateresult>)<[healthFields.StressAggregation](<../healthFields (运动健康数据字段)/health-api-healthfields.md#stressaggregation>)> | 压力聚合结果数据模型。 |

## TrailRunning

PhoneTabletWearable

type TrailRunning = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

越野跑锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.RunningSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#runningsummary>), [healthFields.RunningDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#runningdetail>)> | 越野跑锻炼记录数据模型。 |

## Walking

PhoneTabletWearable

type Walking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

户外步行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)<[healthFields.WalkingSummary](<../healthFields (运动健康数据字段)/health-api-healthfields.md#walkingsummary>), [healthFields.WalkingDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#walkingdetail>)> | 户外步行锻炼数据模型记录。 |

## Weight

PhoneTabletWearable

type Weight = healthStore.SamplePoint<healthFields.Weight>

体重采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#samplepoint>)<[healthFields.Weight](<../healthFields (运动健康数据字段)/health-api-healthfields.md#weight>)> | 体重采样数据模型。 |
