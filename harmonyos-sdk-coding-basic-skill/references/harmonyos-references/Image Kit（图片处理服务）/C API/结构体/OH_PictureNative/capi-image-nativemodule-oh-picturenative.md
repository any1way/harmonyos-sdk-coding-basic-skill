---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturenative
title: OH_PictureNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PictureNative
category: harmonyos-references
scraped_at: 2026-06-01T16:23:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5fdc4c20a418b1b2cbbc51cf64f7804d5a3ff28fd742b82106df54512d7dbcaf
---
```
1. struct OH_PictureNative
```

## 概述

PhonePC/2in1TabletTVWearable

Picture结构体类型，用于执行picture相关操作。

Picture为多图对象结构体，包含主图、辅助图和元数据。

主图包含图像的大部分信息，主要用于显示图像内容。

辅助图用于存储与主图相关但不同的数据，展示图像更丰富的信息。

元数据一般用来存储关于图像文件的信息。

**起始版本：** 13

**相关模块：** [Image\_NativeModule](../../模块/Image_NativeModule/capi-image-nativemodule.md)

**所在头文件：** [picture\_native.h](../../头文件/picture_native.h/capi-picture-native-h.md)
