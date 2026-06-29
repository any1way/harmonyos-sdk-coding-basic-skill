---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceupdatedata
title: OhosImageSourceUpdateData
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceUpdateData
category: harmonyos-references
scraped_at: 2026-06-01T16:23:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f2df626264909aef0b3f4ed1b26f1dfec4b9325a6cf2a9734df6d8c93cd0f2ca
---
```
1. struct OhosImageSourceUpdateData {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源更新数据选项，由[OH\_ImageSource\_UpdateData](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_updatedata)获取。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* buffer = nullptr | 图像源更新数据缓冲区。 |
| size\_t bufferSize = 0 | 图像源更新数据缓冲区大小。 |
| uint32\_t offset = 0 | 图像源更新数据缓冲区的开端。 |
| uint32\_t updateLength = 0 | 图像源更新数据缓冲区的更新数据长度。 |
| int8\_t isCompleted = 0 | 图像源更新数据在此节中完成。 |
