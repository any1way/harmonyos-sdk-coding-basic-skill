---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-outputdeviceinfo
title: AVSession_OutputDeviceInfo
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > AVSession_OutputDeviceInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:19:43+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:1bbdea266688d8dae1e1a04178044e0f35b50bf87f6b773328a746a9d76f80bd
---
```
1. typedef struct AVSession_OutputDeviceInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

目标设备信息的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](../../模块/OHAVSession/capi-ohavsession.md)

**所在头文件：** [native\_deviceinfo.h](../../头文件/native_deviceinfo.h/capi-native-deviceinfo-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 设备信息数组的大小。 |
| [AVSession\_DeviceInfo](../AVSession_DeviceInfo/capi-ohavsession-avsession-deviceinfo.md) \*\*deviceInfos | 设备信息数组。 |
