---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-filterdelegate
title: ImageEffect_FilterDelegate
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageEffect_FilterDelegate
category: harmonyos-references
scraped_at: 2026-06-01T16:23:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e7dcca2e7b127bac4a26679f34c4f3962895d087f49aa417529242b3193d1200
---
```
1. typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterDelegate
```

## 概述

PhonePC/2in1TabletTV

自定义滤镜回调函数结构体。

**起始版本：** 12

**相关模块：** [ImageEffect](../../模块/ImageEffect/capi-imageeffect.md)

**所在头文件：** [image\_effect\_filter.h](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_EffectFilterDelegate\_SetValue](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#oh_effectfilterdelegate_setvalue) setValue | 参数设置函数指针。 |
| [OH\_EffectFilterDelegate\_Render](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#oh_effectfilterdelegate_render) render | 滤镜渲染函数指针。 |
| [OH\_EffectFilterDelegate\_Save](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#oh_effectfilterdelegate_save) save | 序列化效果器函数指针。 |
| [OH\_EffectFilterDelegate\_Restore](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#oh_effectfilterdelegate_restore) restore | 反序列化效果器函数指针。 |
