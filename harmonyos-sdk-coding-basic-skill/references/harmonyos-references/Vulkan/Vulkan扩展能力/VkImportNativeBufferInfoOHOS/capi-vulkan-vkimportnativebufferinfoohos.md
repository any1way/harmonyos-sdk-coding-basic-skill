---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkimportnativebufferinfoohos
title: VkImportNativeBufferInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkImportNativeBufferInfoOHOS
category: harmonyos-references
scraped_at: 2026-06-01T16:42:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9bce9dd175d98f4cc1bbd2504363423b90036f41f1c9cfa0594175fde515792a
---
```
1. typedef struct VkImportNativeBufferInfoOHOS {...} VkImportNativeBufferInfoOHOS
```

## 概述

包含了OH\_NativeBuffer结构体的指针。

**起始版本：** 10

**相关模块：** [Vulkan](../Vulkan/capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](../vulkan_ohos.h/capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针。 |
| struct [OH\_NativeBuffer](../OH_NativeBuffer/capi-vulkan-oh-nativebuffer.md)\* buffer | OH\_NativeBuffer结构体的指针。 |
