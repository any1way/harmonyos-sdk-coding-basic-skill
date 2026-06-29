---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-form-components
title: 构建表单组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建表单组件
category: harmonyos-guides
scraped_at: 2026-06-01T11:07:02+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:5af3e8a05a5be4e971079946589c5a63777f48b8416db9a8ab8af317d7883a12
---
ArkUI NDK提供了多种表单组件，包括[按钮（Button）](<../../UI开发 (ArkTS声明式开发范式)/按钮与选择/按钮 (Button)/arkts-common-components-button.md>)、滑动条[Slider](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md)、[切换按钮（Toggle）](<../../UI开发 (ArkTS声明式开发范式)/按钮与选择/切换按钮 (Toggle)/arkts-common-components-switch.md>)、复选框[Checkbox](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Checkbox/ts-basic-components-checkbox.md)、复选框组[CheckboxGroup](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/CheckboxGroup/ts-basic-components-checkboxgroup.md)和[单选框（Radio）](<../../UI开发 (ArkTS声明式开发范式)/按钮与选择/单选框 (Radio)/arkts-common-components-radio-button.md>)。这些组件是用户交互的基础元素，可以用于构建丰富的表单界面。

表单组件的相关接口定义在[native\_node.h](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md>)中。

本文提供表单组件NDK开发指导，查询之前需要先接入ArkTS页面，具体请参考[接入ArkTS页面](../接入ArkTS页面/ndk-access-the-arkts-page.md)。

## Button按钮组件

Button组件用于创建可点击的按钮，支持多种按钮类型和样式设置。

### 创建Button组件

使用[createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>)接口创建Button组件，节点类型为ARKUI\_NODE\_BUTTON。

```
1. std::shared_ptr<NativeModule::ArkUIBaseNode> CreateButtonExample()
2. {
3. auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
4. column->SetWidth(1, true);
5. column->SetHeight(1, true);
6. column->SetBackgroundColor(0x33ff0000);
7. column->SetPadding(PARAM_20, false);
8. auto button = std::make_shared<NativeModule::ArkUIButtonNode>();
9. button->SetButtonLabel("This is a Normal Button");
10. button->SetMaxFontScale(1.0);
11. auto circleBtn = std::make_shared<NativeModule::ArkUIButtonNode>();
12. circleBtn->SetButtonLabel("Circle");
13. circleBtn->SetButtonType(ARKUI_BUTTON_TYPE_CIRCLE);
14. circleBtn->SetMargin(PARAM_20, false);
15. column->AddChild(button);
16. column->AddChild(circleBtn);
17. // 将Column添加到Content中
18. return column;
19. }
```

### 设置Button类型

Button组件支持通过设置NODE\_BUTTON\_TYPE属性实现不同的按钮类型，包括普通按钮、胶囊按钮、圆形按钮和圆角矩形按钮。按钮类型对应枚举请参考[ArkUI\_ButtonType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_buttontype>)。

下述示例将按钮类型设置为ARKUI\_BUTTON\_TYPE\_CIRCLE圆形按钮。

```
1. auto circleBtn = std::make_shared<NativeModule::ArkUIButtonNode>();
2. circleBtn->SetButtonLabel("Circle");
3. circleBtn->SetButtonType(ARKUI_BUTTON_TYPE_CIRCLE);
4. circleBtn->SetMargin(PARAM_20, false);
```

### Button属性

Button独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_BUTTON\_LABEL | 设置按钮文本标签。 |
| NODE\_BUTTON\_TYPE | 设置按钮类型。 |
| NODE\_BUTTON\_MIN\_FONT\_SCALE | 设置最小字体缩放比例。从API version 18开始支持。 |
| NODE\_BUTTON\_MAX\_FONT\_SCALE | 设置最大字体缩放比例。从API version 18开始支持。 |

## Slider滑动条组件

Slider组件用于创建滑动条，用户可以通过拖动滑块来选择数值。

### 创建Slider组件

使用[createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>)接口创建Slider组件，节点类型为ARKUI\_NODE\_SLIDER。

```
1. std::shared_ptr<NativeModule::ArkUIBaseNode> CreateSliderExample()
2. {
3. auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
4. column->SetWidth(1, true);
5. column->SetHeight(1, true);
6. column->SetBackgroundColor(0x33ff0000);
7. column->SetPadding(PARAM_20, false);
8. auto sliderInSet = std::make_shared<NativeModule::ArkUISliderNode>();
9. sliderInSet->SetSliderValue(PARAM_50);
10. sliderInSet->SetSliderStep(PARAM_10);
11. sliderInSet->SetSliderStyle(ARKUI_SLIDER_STYLE_IN_SET);
12. sliderInSet->SetBlockColor(0xFF00FF00);
13. sliderInSet->SetTrackColor(0xFFFFFF00);
14. auto sliderOutSet = std::make_shared<NativeModule::ArkUISliderNode>();
15. sliderOutSet->SetSliderValue(PARAM_50);
16. sliderOutSet->SetSliderStep(PARAM_10);
17. sliderOutSet->SetSliderStyle(ARKUI_SLIDER_STYLE_OUT_SET);
18. sliderOutSet->SetMargin(PARAM_20, false);
19. sliderOutSet->SetSliderDirection(ARKUI_SLIDER_DIRECTION_VERTICAL);
20. sliderOutSet->SetIsReverse(true);
21. sliderOutSet->SetIsShowSteps(true);
22. column->AddChild(sliderInSet);
23. column->AddChild(sliderOutSet);
24. return column;
25. }
```

### 设置Slider样式

Slider支持两种样式，通过[ARKUI\_SliderStyle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_sliderstyle>)枚举定义：

* ARKUI\_SLIDER\_STYLE\_OUT\_SET：滑块在滑动条外（默认值）。
* ARKUI\_SLIDER\_STYLE\_IN\_SET：滑块在滑动条内。

如下示例代码创建了ARKUI\_SLIDER\_STYLE\_IN\_SET样式的Slider组件并设置了滑块和滑轨颜色。

```
1. auto sliderInSet = std::make_shared<NativeModule::ArkUISliderNode>();
2. sliderInSet->SetSliderValue(PARAM_50);
3. sliderInSet->SetSliderStep(PARAM_10);
4. sliderInSet->SetSliderStyle(ARKUI_SLIDER_STYLE_IN_SET);
5. sliderInSet->SetBlockColor(0xFF00FF00);
6. sliderInSet->SetTrackColor(0xFFFFFF00);
```

### 设置Slider方向和步进

Slider支持设置滑动方向（水平或垂直）、是否反向以及是否显示步进刻度。

```
1. auto sliderOutSet = std::make_shared<NativeModule::ArkUISliderNode>();
2. sliderOutSet->SetSliderValue(PARAM_50);
3. sliderOutSet->SetSliderStep(PARAM_10);
4. sliderOutSet->SetSliderStyle(ARKUI_SLIDER_STYLE_OUT_SET);
5. sliderOutSet->SetMargin(PARAM_20, false);
6. sliderOutSet->SetSliderDirection(ARKUI_SLIDER_DIRECTION_VERTICAL);
7. sliderOutSet->SetIsReverse(true);
8. sliderOutSet->SetIsShowSteps(true);
```

### Slider属性

Slider独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_SLIDER\_VALUE | 设置当前进度值。 |
| NODE\_SLIDER\_MIN\_VALUE | 设置最小值。 |
| NODE\_SLIDER\_MAX\_VALUE | 设置最大值。 |
| NODE\_SLIDER\_STEP | 设置滑动步长。 |
| NODE\_SLIDER\_DIRECTION | 设置滑动条方向。 |
| NODE\_SLIDER\_REVERSE | 设置是否反向。 |
| NODE\_SLIDER\_STYLE | 设置滑动条样式。 |
| NODE\_SLIDER\_BLOCK\_COLOR | 设置滑块颜色。 |
| NODE\_SLIDER\_TRACK\_COLOR | 设置轨道颜色。 |
| NODE\_SLIDER\_SELECTED\_COLOR | 设置已选择部分颜色。 |
| NODE\_SLIDER\_SHOW\_STEPS | 设置是否显示步进刻度。 |

## Toggle开关组件

Toggle组件用于创建开关，用户可以在开和关两种状态之间切换。

### 创建Toggle组件

使用[createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>)接口创建Toggle组件，节点类型为ARKUI\_NODE\_TOGGLE。

```
1. std::shared_ptr<NativeModule::ArkUIBaseNode> CreateToggleExample()
2. {
3. auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
4. column->SetWidth(1, true);
5. column->SetHeight(1, true);
6. column->SetBackgroundColor(0x33ff0000);
7. column->SetPadding(PARAM_20, false);
8. auto toggle = std::make_shared<NativeModule::ArkUIToggleNode>();
9. toggle->SetSelectedColor(0xFFFF0000);
10. toggle->SetUnSelectedColor(0xFF0000FF);
11. toggle->SetSwitchPointColor(0xFF00FF00);
12. column->AddChild(toggle);

14. return column;
15. }
```

### 设置Toggle样式

可以设置Toggle开启状态背景色、关闭状态背景色以及滑块颜色。

```
1. toggle->SetSelectedColor(0xFFFF0000);
2. toggle->SetUnSelectedColor(0xFF0000FF);
3. toggle->SetSwitchPointColor(0xFF00FF00);
```

### Toggle属性

Toggle独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_TOGGLE\_VALUE | 设置开关状态。 |
| NODE\_TOGGLE\_SELECTED\_COLOR | 设置开启状态背景色。 |
| NODE\_TOGGLE\_UNSELECTED\_COLOR | 设置关闭状态背景色。 |
| NODE\_TOGGLE\_SWITCH\_POINT\_COLOR | 设置滑块颜色。 |

## Checkbox复选框组件

Checkbox组件用于创建复选框，用户可以选中或取消选中。CheckboxGroup用于管理多个复选框，实现全选等操作。

### 创建Checkbox组件

使用[createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>)接口创建Checkbox组件，节点类型为ARKUI\_NODE\_CHECKBOX。

```
1. std::shared_ptr<NativeModule::ArkUIBaseNode> CreateCheckboxExample()
2. {
3. auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
4. column->SetWidth(1, true);
5. column->SetHeight(1, true);
6. column->SetBackgroundColor(0x33ff0000);
7. column->SetPadding(PARAM_20, false);
8. auto checkbox1 = std::make_shared<NativeModule::ArkUICheckboxNode>();
9. auto checkbox2 = std::make_shared<NativeModule::ArkUICheckboxNode>();
10. auto checkbox3 = std::make_shared<NativeModule::ArkUICheckboxNode>();
11. auto checkboxGroup = std::make_shared<NativeModule::ArkUICheckboxGroupNode>();
12. checkboxGroup->SetCheckboxGroupName("check_group");
13. checkbox1->SetCheckboxGroup("check_group");
14. checkbox1->SetSelectColor(0xFFFF0000);
15. checkbox2->SetCheckboxGroup("check_group");
16. checkbox2->SetUnSelectColor(0xFFFF0000);
17. checkbox3->SetCheckboxGroup("check_group");
18. checkbox3->SetCheckboxShape(ArkUI_CHECKBOX_SHAPE_ROUNDED_SQUARE);
19. checkbox1->SetCheckboxName("check_group1");
20. checkbox2->SetCheckboxName("check_group2");
21. checkbox3->SetCheckboxName("check_group3");

23. column->AddChild(checkboxGroup);
24. column->AddChild(checkbox1);
25. column->AddChild(checkbox2);
26. column->AddChild(checkbox3);

28. // 将Column添加到Content中
29. return column;
30. }
```

### 创建CheckboxGroup

CheckboxGroup用于管理同一组内的多个复选框，节点类型为ARKUI\_NODE\_CHECKBOX\_GROUP。

```
1. auto checkboxGroup = std::make_shared<NativeModule::ArkUICheckboxGroupNode>();
2. checkboxGroup->SetCheckboxGroupName("check_group");
```

### 设置Checkbox属性

可以设置复选框的选中颜色、未选中颜色、形状以及所属组名。

```
1. checkbox1->SetCheckboxGroup("check_group");
2. checkbox1->SetSelectColor(0xFFFF0000);
3. checkbox2->SetCheckboxGroup("check_group");
4. checkbox2->SetUnSelectColor(0xFFFF0000);
5. checkbox3->SetCheckboxGroup("check_group");
6. checkbox3->SetCheckboxShape(ArkUI_CHECKBOX_SHAPE_ROUNDED_SQUARE);
7. checkbox1->SetCheckboxName("check_group1");
8. checkbox2->SetCheckboxName("check_group2");
9. checkbox3->SetCheckboxName("check_group3");
```

### Checkbox属性

Checkbox独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_CHECKBOX\_SELECT | 设置是否选中。 |
| NODE\_CHECKBOX\_SELECT\_COLOR | 设置选中状态颜色。 |
| NODE\_CHECKBOX\_UNSELECT\_COLOR | 设置未选中状态颜色。 |
| NODE\_CHECKBOX\_MARK | 设置勾选标记样式。 |
| NODE\_CHECKBOX\_SHAPE | 设置复选框形状。 |
| NODE\_CHECKBOX\_NAME | 设置复选框名称。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP | 设置复选框组名称，用于CheckboxGroup管理。从API version 15开始支持。 |

### CheckboxGroup属性

CheckboxGroup独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_CHECKBOX\_GROUP\_NAME | 设置复选框组名称。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_SELECT\_ALL | 设置是否全选。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_SELECTED\_COLOR | 设置选中状态颜色。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_UNSELECTED\_COLOR | 设置未选中状态颜色。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_MARK | 设置勾选标记样式。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_SHAPE | 设置复选框形状。从API version 15开始支持。 |

## Radio单选按钮组件

Radio组件用于创建单选按钮，同一组内的单选按钮只能选中一个。

### 创建Radio组件

使用[createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>)接口创建Radio组件，节点类型为ARKUI\_NODE\_RADIO。

```
1. std::shared_ptr<NativeModule::ArkUIBaseNode> CreateRadioExample()
2. {
3. auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
4. column->SetWidth(1, true);
5. column->SetHeight(1, true);
6. column->SetBackgroundColor(0x33ff0000);
7. column->SetPadding(PARAM_20, false);
8. auto radio1 = std::make_shared<NativeModule::ArkUIRadioNode>();
9. auto radio2 = std::make_shared<NativeModule::ArkUIRadioNode>();
10. auto radio3 = std::make_shared<NativeModule::ArkUIRadioNode>();
11. radio1->SetIsOn(true);
12. radio1->SetRadioGroup("radio_group");
13. radio2->SetRadioGroup("radio_group");
14. radio3->SetRadioGroup("radio_group");
15. radio3->SetRadioStyle(0xFFFF0000, 0xFF00FF00, 0xFF00FFFF);

17. column->AddChild(radio1);
18. column->AddChild(radio2);
19. column->AddChild(radio3);

21. return column;
22. }
```

### 设置Radio组

同一组内的Radio组件只能选中一个，通过设置相同的组名实现互斥。

```
1. radio1->SetIsOn(true);
2. radio1->SetRadioGroup("radio_group");
3. radio2->SetRadioGroup("radio_group");
4. radio3->SetRadioGroup("radio_group");
```

### 设置Radio样式

可以设置单选按钮的样式，包括未选中状态颜色、选中状态内部圆环颜色和选中状态外环颜色。

```
1. radio3->SetRadioStyle(0xFFFF0000, 0xFF00FF00, 0xFF00FFFF);
```

### Radio属性

Radio独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_RADIO\_CHECKED | 设置是否选中。 |
| NODE\_RADIO\_STYLE | 设置单选按钮样式（未选中颜色、选中内部圆环颜色、选中外环颜色）。 |
| NODE\_RADIO\_VALUE | 设置单选按钮值。 |
| NODE\_RADIO\_GROUP | 设置所属组名，同一组内的Radio互斥。 |
