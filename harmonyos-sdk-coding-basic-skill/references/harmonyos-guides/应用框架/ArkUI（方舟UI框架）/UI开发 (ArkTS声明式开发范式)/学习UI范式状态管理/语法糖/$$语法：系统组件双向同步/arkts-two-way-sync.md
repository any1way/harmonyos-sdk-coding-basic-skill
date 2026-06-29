---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync
title: $$语法：系统组件双向同步
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 语法糖 > $$语法：系统组件双向同步
category: harmonyos-guides
scraped_at: 2026-06-11T14:29:32+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:d6e0df02186cb678ede6bf36a7a0103c57c15afb9a8a9dcd6b1879bc1e2a6c50
---
$$运算符为系统组件提供TS变量的引用，使得TS变量和系统组件的内部状态保持同步。

内部状态的具体含义取决于组件。例如，[TextInput](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)组件的text参数。

## 使用规则

* 当前$$支持基础类型变量，当该变量使用[@State](../../状态管理（V1）/管理组件拥有的状态/@State装饰器：组件内状态/arkts-state.md)、[@Link](../../状态管理（V1）/管理组件拥有的状态/@Link装饰器：父子双向同步/arkts-link.md)、[@Prop](../../状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md)、[@Provide](../../状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md)等状态管理V1装饰器装饰，或者[@Local](../../状态管理（V2）/管理组件拥有的状态/@Local装饰器：组件内部状态/arkts-new-local.md)等状态管理V2装饰器装饰时，变量值的变化会触发UI刷新。
* 当前$$支持的组件：

  | 组件 | 支持的参数/属性 | 起始API版本 |
  | --- | --- | --- |
  | [Checkbox](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Checkbox/ts-basic-components-checkbox.md) | select | 10 |
  | [CheckboxGroup](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/CheckboxGroup/ts-basic-components-checkboxgroup.md) | selectAll | 10 |
  | [DatePicker](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/DatePicker/ts-basic-components-datepicker.md) | selected | 10 |
  | [TimePicker](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TimePicker/ts-basic-components-timepicker.md) | selected | 10 |
  | [MenuItem](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/菜单/MenuItem/ts-basic-components-menuitem.md) | selected | 10 |
  | [Panel](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/已停止维护的组件与接口/Panel/ts-container-panel.md) | mode | 10 |
  | [Radio](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Radio/ts-basic-components-radio.md) | checked | 10 |
  | [Rating](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Rating/ts-basic-components-rating.md) | rating | 10 |
  | [Search](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Search/ts-basic-components-search.md) | value | 10 |
  | [SideBarContainer](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md) | showSideBar | 10 |
  | [Slider](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md) | value | 10 |
  | [Stepper](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/已停止维护的组件与接口/Stepper/ts-basic-components-stepper.md) | index | 10 |
  | [Swiper](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md) | index | 10 |
  | [Tabs](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md) | index | 10 |
  | [TextArea](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md) | text | 10 |
  | [TextInput](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md) | text | 10 |
  | [TextPicker](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md) | selected、value | 10 |
  | [Toggle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md) | isOn | 10 |
  | [AlphabetIndexer](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md) | selected | 10 |
  | [Select](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md) | selected、value | 10 |
  | [BindSheet](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#bindsheet) | isShow | 10 |
  | [BindContentCover](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/全屏模态转场/ts-universal-attributes-modal-transition.md#bindcontentcover) | isShow | 10 |
  | [Refresh](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Refresh/ts-container-refresh.md) | refreshing | 8 |
  | [GridItem](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/GridItem/ts-container-griditem.md) | selected | 10 |
  | [ListItem](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ListItem/ts-container-listitem.md) | selected | 10 |

## 使用示例

以[TextInput](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)方法的text参数为例：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = '';
6. controller: TextInputController = new TextInputController();

8. build() {
9. Column({ space: 20 }) {
10. Text(this.text)
11. TextInput({ text: $$this.text, placeholder: 'input your word...', controller: this.controller })
12. .placeholderColor(Color.Grey)
13. .placeholderFont({ size: 14, weight: 400 })
14. .caretColor(Color.Blue)
15. .width(300)
16. }
17. .width('100%')
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }
21. }
```

[SyncUsageExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/syncStateManager/SyncUsageExample.ets#L30-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/TyeC6uFBTKGFsYDuQtPUWA/zh-cn_image_0000002592377946.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062930Z&HW-CC-Expire=86400&HW-CC-Sign=9A2F19DC20B62D279C426C3BD316E0B75B4EDCB206438D1174ADAE76456F4676)
