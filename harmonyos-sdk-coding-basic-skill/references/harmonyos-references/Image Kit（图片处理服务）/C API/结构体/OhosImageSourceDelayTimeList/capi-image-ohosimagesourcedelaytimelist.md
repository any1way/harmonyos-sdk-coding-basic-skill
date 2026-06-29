---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcedelaytimelist
title: OhosImageSourceDelayTimeList
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceDelayTimeList
category: harmonyos-references
scraped_at: 2026-06-01T16:23:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:19085007c8101272e0500b0b08179a518d4e66e7ec06a3af312e6464b2664bac
---
```
1. struct OhosImageSourceDelayTimeList {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源延迟时间列表。由[OH\_ImageSource\_GetDelayTime](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_getdelaytime)获取。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t\* delayTimeList | 图像源延迟时间列表头地址。 |
| size\_t size = 0 | 图像源延迟时间列表大小。 |
