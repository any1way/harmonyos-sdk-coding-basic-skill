---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-entry
title: @Entry：页面入口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > @Entry：页面入口
category: harmonyos-references
scraped_at: 2026-06-11T15:49:49+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:419d78789b0295c8afab97afd3db7f986e600721de06fee038b68f644e91838b
---
@Entry装饰的自定义组件将作为UI页面的入口。

说明

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @Entry

PhonePC/2in1TabletTVWearable

在单个UI页面中，仅允许存在一个由@Entry装饰的自定义组件作为页面的入口。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // @Entry装饰的自定义组件作为UI页面的入口
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Text('@Entry Test')
7. }
8. }
```

## EntryOptions10+

PhonePC/2in1TabletTVWearable

命名路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routeName | string | 否 | 是 | 表示作为命名路由页面的名字。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| storage | [LocalStorage](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md>) | 否 | 是 | 页面级的UI状态存储。当未传入时，框架会创建一个新的LocalStorage实例作为默认值。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| useSharedStorage12+ | boolean | 否 | 是 | 是否使用[loadContent](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#loadcontent9>)传入的LocalStorage实例对象。默认值false。true：使用共享的LocalStorage实例对象。false：不使用共享的LocalStorage实例对象。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

**示例：**

```
1. // 设置路由页面名字为myPage
2. @Entry({ routeName: 'myPage' })
3. @Component
4. struct Index {
5. build() {
6. Text('Index')
7. }
8. }
```
