---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-set-multi-window
title: 设置应用内多窗
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置应用内多窗
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:16+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:8bcd84493f4cc81dc3f4b505e00ce4e6275b5a37c7672e0e9c0ee9407296bd15
---
## 场景介绍

从6.0.0(20)版本开始，新增支持应用内多窗。

当应用开发者需要使用应用内多窗图标（分屏按钮）时，可通过配置titleBar中的menu的[multiWindowEntryInAPPMenu](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#hdsnavigationmenucontentoptions>)属性实现该功能。

## 约束条件

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备形态，该组件不可交互，不响应点击事件。

## 开发步骤

1. 导入模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, HdsNavigationMenuContentOptions, HdsNavigationAttribute } from '@kit.UIDesignKit';
   3. import { Want } from '@kit.AbilityKit';
   ```
2. 创建一级导航组件，通过配置titleBar中的menu上的multiWindowEntryInAPPMenu属性，实现应用内多窗图标设置。

   ```
   1. @Entry
   2. @Component
   3. struct MultiWindowEntryInAPPTest {
   4. private want: Want = {
   5. // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
   6. // 注意：以下参数仅为示例，请替换为实际应用的参数
   7. bundleName: 'com.example.myapplication',
   8. moduleName: 'entry',
   9. abilityName: 'FuncAbility',
   10. }
   11. @State menuContent: HdsNavigationMenuContentOptions = {
   12. multiWindowEntryInAPPMenu: {
   13. want: this.want
   14. },
   15. maxCount: 3,
   16. value: [
   17. { content: { label: 'menu1', icon: $r('sys.symbol.search_things'), } },
   18. { content: { label: 'menu2', icon: $r('sys.symbol.plus'), } }
   19. ]
   20. }

   22. build() {
   23. HdsNavigation() {
   24. Stack() {
   25. Text('Page1')
   26. }.alignContent(Alignment.Center)
   27. .width('100%')
   28. .height('100%')
   29. }
   30. .hideToolBar(false)
   31. .navBarWidth('100%')
   32. .titleBar({
   33. content: {
   34. title: {
   35. mainTitle: "Index"
   36. },
   37. menu: this.menuContent
   38. }
   39. })
   40. }
   41. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/pnZzWACpSvS1p84mOj5KBA/zh-cn_image_0000002622858197.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063559Z&HW-CC-Expire=86400&HW-CC-Sign=3BCBD803646D02BB58F8E32DFAACD71E20E0FFC0E14044165A11EAC86DF6F323)
