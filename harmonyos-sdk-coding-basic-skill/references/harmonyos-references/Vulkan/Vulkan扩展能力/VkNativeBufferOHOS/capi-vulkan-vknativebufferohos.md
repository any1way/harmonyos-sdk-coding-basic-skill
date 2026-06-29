---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferohos
title: VkNativeBufferOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferOHOS
category: harmonyos-references
scraped_at: 2026-06-01T16:42:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2f02d18d8e31ce77e06175d3db6103b1cb671232aeb57904588bf5816dec1638
---
```
1. typedef struct VkNativeBufferOHOS {...} VkNativeBufferOHOS
```

## 概述

包含本地显存的参数。

**起始版本：** 10

**相关模块：** [Vulkan](../Vulkan/capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](../vulkan_ohos.h/capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| struct [OHBufferHandle\*](../OHBufferHandle/capi-vulkan-ohbufferhandle.md) handle | 显存句柄。 |
