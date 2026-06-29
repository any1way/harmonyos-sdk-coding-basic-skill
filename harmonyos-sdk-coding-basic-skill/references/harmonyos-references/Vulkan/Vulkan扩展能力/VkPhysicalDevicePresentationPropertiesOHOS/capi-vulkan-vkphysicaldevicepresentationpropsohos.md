---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkphysicaldevicepresentationpropertiesohos
title: VkPhysicalDevicePresentationPropertiesOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkPhysicalDevicePresentationPropertiesOHOS
category: harmonyos-references
scraped_at: 2026-06-11T16:53:55+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:d01502a28d480b39eb630aa1f33a313b8f3fa7253b134bb4c802e90c5446f3e3
---
```
1. typedef struct VkPhysicalDevicePresentationPropertiesOHOS {...} VkPhysicalDevicePresentationPropertiesOHOS
```

## 概述

包含设备的显示属性的参数。

**起始版本：** 10

**废弃版本：** 23

**相关模块：** [Vulkan](../Vulkan/capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](../vulkan_ohos.h/capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| VkBool32 sharedImage | 共享图像标志。 |
