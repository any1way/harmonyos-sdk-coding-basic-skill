---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets
title: ServiceCollaboration_CollaborationDeviceInfoSets
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaboration_CollaborationDeviceInfoSets
category: harmonyos-references
scraped_at: 2026-06-01T16:09:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af770da9007e9c1f0e20cb269cd858161d24146b2572d9715b766c5f56eed0ff
---
## 概述

PhonePC/2in1TabletTV

通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](../../../模块/ServiceCollaboration/servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](../../头文件/service_collaboration_api.h/servicecollaboration-capi-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint32\_t [size](servicecollaboration-co_01549992.md#size) | 对端设备信息对象集合的大小。 |
| [ServiceCollaboration\_CollaborationDeviceInfo](../ServiceCollaboration_CollaborationDeviceInfo/servicecollaboration-collaborationdeviceinfo.md) \* [deviceInfoSets](servicecollaboration-co_01549992.md#deviceinfosets) | 对端设备信息对象集合。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### deviceInfoSets

PhonePC/2in1TabletTV

```
1. ServiceCollaboration_CollaborationDeviceInfo* ServiceCollaboration_CollaborationDeviceInfoSets::deviceInfoSets
```

**描述**

对端设备信息对象集合。

### size

PhonePC/2in1TabletTV

```
1. uint32_t ServiceCollaboration_CollaborationDeviceInfoSets::size
```

**描述**

对端设备信息对象集合的大小。
