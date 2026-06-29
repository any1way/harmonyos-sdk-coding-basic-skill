---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceproperty
title: OhosImageSourceProperty
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceProperty
category: harmonyos-references
scraped_at: 2026-06-01T16:23:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:60417c78003f88abab12f148af44f2739878e9a226bad3c065871e47da203a06
---
```
1. struct OhosImageSourceProperty {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源属性键值字符串。此选项给[OH\_ImageSource\_GetImageProperty](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* value = nullptr | 定义图像源属性键值字符串头地址。 |
| size\_t size = 0 | 定义图像源属性键值字符串大小。 |
