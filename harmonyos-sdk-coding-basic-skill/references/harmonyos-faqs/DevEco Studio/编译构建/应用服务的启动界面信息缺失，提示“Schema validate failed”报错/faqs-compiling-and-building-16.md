---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-16
title: 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bd1cf6161b27ec57cff0af3330ab446e8efd8aedb29f655fcd4a1df46a5cbb96
---
**问题现象**

在工程同步或编译构建时，出现“Schema validate failed”的错误提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/SpbYWRcfSPOiRgUebdUlLQ/zh-cn_image_0000002229604277.png?HW-CC-KV=V1&HW-CC-Date=20260612T024110Z&HW-CC-Expire=86400&HW-CC-Sign=780581FB96C3A3B8255E8EE76CC47299790F29DBEB06FA33AD4DEC0E095FB868)

**解决措施**

在开发应用/服务时，创建工程后，默认设置了启动界面信息。如果开发者误删其中某个字段，将导致报错。下面以重新设置启动界面信息为例，为提高冷启动性能，可以通过以下方式设置启动界面的图标和背景颜色。

1. 在模块的**resources > base > element**目录下，右键点击并选择**New > Element Resource File**来创建资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/O21x3LYrToK1nkpqlJHkUA/zh-cn_image_0000002194318512.png?HW-CC-KV=V1&HW-CC-Date=20260612T024110Z&HW-CC-Expire=86400&HW-CC-Sign=7678A91D794BB73EAA08270E100408A11ADEB6DA9F6CC4E35661A67E0B208859)
2. 在弹出的对话框中，开发者可以自定义“File name”，例如 color；“Root element”请选择 **color**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hagu7BrwRtS0BZR3LeTJAg/zh-cn_image_0000002194158900.png?HW-CC-KV=V1&HW-CC-Date=20260612T024110Z&HW-CC-Expire=86400&HW-CC-Sign=856741B24C172DE9EDF5CBF0DEF36853DDA0366CEDE11139519D49794275AA47)

   创建完成后，color.json文件如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/8Ly-mByGSKi11QMYt4TLtQ/zh-cn_image_0000002194318508.png?HW-CC-KV=V1&HW-CC-Date=20260612T024110Z&HW-CC-Expire=86400&HW-CC-Sign=0EB034977F4E5A7947ECFF112A5FC381DF6B71EADCF720B8803A83A1F8974D21)
3. 将[2](faqs-compiling-and-building-16.md#zh-cn_topic_0000001233028585_li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/C7CX0LC4TxCkJ4gxcAqfZQ/zh-cn_image_0000002229604281.png?HW-CC-KV=V1&HW-CC-Date=20260612T024110Z&HW-CC-Expire=86400&HW-CC-Sign=2EEDDFBD19DCD31D3D46868DC763161F932B1BB81F7897B387607950769E8741)
4. 在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。若缺少任一字段，将出现ERROR: Schema validate failed报错。startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element > color.json**中的颜色。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/DcykktDNQnmKaaAzuUFoRA/zh-cn_image_0000002194318504.png?HW-CC-KV=V1&HW-CC-Date=20260612T024110Z&HW-CC-Expire=86400&HW-CC-Sign=9CC32707F6259CAF3ED5F3921BC3DFD07D11BF33EF19AC6BC220926B919CBB45)
5. 在**src > ohosTest > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段引用模块ohosTest下 **resources > base > media**中的图标资源，startWindowBackground字段引用 **resources > base > element > color.json**中的颜色。
