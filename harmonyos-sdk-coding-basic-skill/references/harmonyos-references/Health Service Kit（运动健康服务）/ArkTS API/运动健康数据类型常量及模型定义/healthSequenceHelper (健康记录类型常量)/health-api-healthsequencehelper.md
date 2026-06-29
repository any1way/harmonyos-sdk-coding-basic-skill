---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthsequencehelper
title: healthSequenceHelper (健康记录类型常量)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthSequenceHelper (健康记录类型常量)
category: harmonyos-references
scraped_at: 2026-06-01T16:34:35+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:5aa8dccc089987d8f5a75c8953e3c5fa46ae45f184709a57d4a8b7cc9db3757d
---
本模块提供健康记录数据类型常量及数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.healthSequenceHelper方式使用。

## sleepRecord

PhoneTabletWearable

夜间睡眠数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 夜间睡眠数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.SleepRecord

夜间睡眠健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SleepRecord](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#sleeprecord>) | 夜间睡眠健康记录数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.Sleep

夜间睡眠健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.Sleep](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleep>) | 夜间睡眠健康记录数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleepdetail>) | 睡眠详情数据字段列表。 |

## sleepNapRecord

PhoneTabletWearable

零星小睡数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 零星小睡数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.SleepNapRecord

零星小睡健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SleepNapRecord](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#sleepnaprecord>) | 零星小睡健康记录数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.SleepNap

零星小睡健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepNap](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleepnap>) | 零星小睡健康记录数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#sleepdetail>) | 睡眠详情数据字段列表。 |

## menstrualCycle

PhoneTabletWearable

生理周期数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](<../../healthStore (运动健康数据服务)/health-api-healthstore.md#datatype>) | 生理周期数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.MenstrualCycle

生理周期健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.MenstrualCycle](<../healthModels (运动健康数据模型)/health-api-healthmodels.md#menstrualcycle>) | 生理周期健康记录数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.MenstrualCycle

生理周期健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.MenstrualCycle](<../healthFields (运动健康数据字段)/health-api-healthfields.md#menstrualcycle>) | 生理周期健康记录数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.MenstrualCycleDetail

生理周期详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.MenstrualCycleDetail](<../healthFields (运动健康数据字段)/health-api-healthfields.md#menstrualcycledetail>) | 生理周期详情数据字段列表。 |
