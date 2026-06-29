---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferusageohos
title: VkNativeBufferUsageOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferUsageOHOS
category: harmonyos-references
scraped_at: 2026-06-01T16:42:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:be6e889ec0a268a31fc0364f795c2ada6993a631e071cd01ec30411fe24a7e7e
---
```
1. typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
```

## 概述

提供HarmonyOS NativeBuffer用途的说明。

**起始版本：** 10

**相关模块：** [Vulkan](../Vulkan/capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](../vulkan_ohos.h/capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_NATIVE\_BUFFER\_USAGE\_OHOS。 |
| void\* pNext | 下一级结构体指针。 |
| uint64\_t OHOSNativeBufferUsage | NativeBuffer的用途说明。 |
