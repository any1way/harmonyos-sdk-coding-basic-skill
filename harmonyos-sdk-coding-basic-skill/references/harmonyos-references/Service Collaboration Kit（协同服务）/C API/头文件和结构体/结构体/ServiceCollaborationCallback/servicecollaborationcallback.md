---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback
title: ServiceCollaborationCallback
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaborationCallback
category: harmonyos-references
scraped_at: 2026-06-01T16:09:27+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:4472bf0f24d3dd85cc13a2a35b73c2aff3d515837f60bb82a390463fb883f316
---
## 概述

PhonePC/2in1TabletTV

传给[HMS\_ServiceCollaboration\_StartCollaboration](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)或[HMS\_ServiceCollaboration\_StartCollaborationV2](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)的回调方法，用来传递跨设备互通的状态信息。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](../../头文件/service_collaboration_api.h/servicecollaboration-capi-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t(\* [OnEvent](servicecollaborationcallback.md#onevent) )([ServiceCollaborationEventCode](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code, uint32\_t extraCode) | 在跨设备互通服务状态变化时被调用。 |
| int32\_t(\* [OnDataCallback](servicecollaborationcallback.md#ondatacallback) )([ServiceCollaborationEventCode](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code, [ServiceCollaborationDataType](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#servicecollaborationdatatype-1) dataType, uint32\_t dataSize, char \*data) | 在跨设备互通服务数据返回时被调用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### OnDataCallback

PhonePC/2in1TabletTV

```
1. int32_t(* ServiceCollaborationCallback::OnDataCallback) (ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char *data)
```

**描述**

在跨设备互通服务数据返回时被调用。

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationEventCode](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code | 错误码。 |
| [ServiceCollaborationDataType](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#servicecollaborationdatatype-1) dataType | 回传数据类型。 |
| uint32\_t dataSize | 数据大小，单位是字节。 |
| char \*data | 数据。 |

### OnEvent

PhonePC/2in1TabletTV

```
1. int32_t(* ServiceCollaborationCallback::OnEvent) (ServiceCollaborationEventCode code, uint32_t extraCode)
```

**描述**

在跨设备互通服务状态变化时被调用。

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationEventCode](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code | 错误码。 |
| uint32\_t extraCode | 拓展状态码，携带错误码未提供的额外信息。 |
