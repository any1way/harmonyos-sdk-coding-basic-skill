---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-accessibility-arkui-accessiblegriditeminfo
title: ArkUI_AccessibleGridItemInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleGridItemInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:50:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d1fd7ef69d723c26d69c10fe47e2cbc101756875579bb8006e2127a3980c7419
---
```
1. typedef struct {...} ArkUI_AccessibleGridItemInfo
```

## 概述

PhonePC/2in1TabletTVWearable

用于配置特定组件（[List](../../../ArkTS组件/滚动与滑动/List/ts-container-list.md)、[Flex](../../../ArkTS组件/行列与堆叠/Flex/ts-container-flex.md)、[Select](../../../ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[Swiper](../../../ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)组件）的属性值。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](../../模块/ArkUI_Accessibility/capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](../../头文件/native_interface_accessibility.h/capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool heading | 是否是标题。true表示是标题，false表示不是标题。 |
| bool selected | 是否被选中。true表示被选中，false表示未被选中。 |
| int32\_t columnIndex | 列下标。取值范围为大于0的整数。 |
| int32\_t rowIndex | 行下标。取值范围为大于0的整数。 |
| int32\_t columnSpan | 列跨度。取值范围为大于0的整数。 |
| int32\_t rowSpan | 行跨度。取值范围为大于0的整数。 |
