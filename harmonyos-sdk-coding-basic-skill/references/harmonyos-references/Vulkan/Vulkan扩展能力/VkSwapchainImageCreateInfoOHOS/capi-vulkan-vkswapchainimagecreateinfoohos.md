---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkswapchainimagecreateinfoohos
title: VkSwapchainImageCreateInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkSwapchainImageCreateInfoOHOS
category: harmonyos-references
scraped_at: 2026-06-11T16:53:54+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:d3f2fdf0839170db36962c5b042485c2c83063e60b0cd5dc528a09d88f5e362a
---
```
1. typedef struct VkSwapchainImageCreateInfoOHOS {...} VkSwapchainImageCreateInfoOHOS
```

## 概述

包含创建Image时必要的参数。

**起始版本：** 10

**废弃版本：** 23

**相关模块：** [Vulkan](../Vulkan/capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](../vulkan_ohos.h/capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| VkSwapchainImageUsageFlagsOHOS usage | 交换链图像的使用标志。 |
