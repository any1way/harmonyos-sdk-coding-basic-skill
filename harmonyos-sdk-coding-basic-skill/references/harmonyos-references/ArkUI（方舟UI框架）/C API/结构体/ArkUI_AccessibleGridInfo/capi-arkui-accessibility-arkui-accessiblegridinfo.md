---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo
title: ArkUI_AccessibleGridInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibleGridInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:50:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:06fcb415e57eec8a8878e155e5644a345f142b0a3b66a2cda4a2439cb661ebab
---
```
1. typedef struct {...} ArkUI_AccessibleGridInfo
```

## 概述

PhonePC/2in1TabletTVWearable

用于配置特定组件（如[List](../../../ArkTS组件/滚动与滑动/List/ts-container-list.md)、[Flex](../../../ArkTS组件/行列与堆叠/Flex/ts-container-flex.md)、[Select](../../../ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[Swiper](../../../ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)组件）的网格布局属性。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](../../模块/ArkUI_Accessibility/capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](../../头文件/native_interface_accessibility.h/capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t rowCount | 组件的行数。取值范围为大于0的整数。 |
| int32\_t columnCount | 组件的列数。取值范围为大于0的整数。 |
| int32\_t selectionMode | 值为0时表示仅选中网格的一行，非0值时表示选中网格的多行。 |
