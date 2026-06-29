---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating
title: 设置页签栏的悬浮样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的悬浮样式
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:27+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:c10976c0b05fa2cccb41ebb8247ac45decfe381e6e5c383f9aaf274244b8afe8
---
## 场景介绍

从6.1.0(23) 版本开始，新增支持设置页签栏的悬浮样式以及迷你栏。

## 页签栏

页签栏悬浮样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/4g0UaZjTQQyouzXI2OXjqA/zh-cn_image_0000002622858205.png?HW-CC-KV=V1&HW-CC-Date=20260611T063736Z&HW-CC-Expire=86400&HW-CC-Sign=4F6FA866F973D7F4EF9CFC7D894F198144AE27579F66DBB5287E75696E70716C)

## 迷你栏

迷你栏是新增的自定义区域，跟页签栏高度相等且水平对齐，支持展开和折叠两种样式。

迷你栏的折叠样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Nusw3f1eT6KtPJSWV2Jljw/zh-cn_image_0000002622698327.png?HW-CC-KV=V1&HW-CC-Date=20260611T063736Z&HW-CC-Expire=86400&HW-CC-Sign=6C70F64F7A9E4189147FF0EF76E7FD29B4E3D0E31C7F82EC17618296275010E5)

迷你栏的展开样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/gmaGXnqcSg--gv3rA6F8dA/zh-cn_image_0000002592218766.png?HW-CC-KV=V1&HW-CC-Date=20260611T063736Z&HW-CC-Expire=86400&HW-CC-Sign=8B4596439D4A3D8D8EB2853ABB4BF644FC6EEA402E8E8C1785769573EE2AF27E)

## 约束条件

1. 布局位置：设置[barPosition](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md#barposition>)为BarPosition.End且[vertical](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md#vertical>)为false，使页签栏置于容器底部。
2. 层级叠加：设置[barOverlap](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md#baroverlap>)为true，使TabBar悬浮于TabContent。
3. 样式限制，当前仅支持以下样式配置：
   * [BottomTabBarStyle](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/TabContent/ts-container-tabcontent.md#bottomtabbarstyle9)（底部标签栏样式）
   * [CustomBuilder](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#custombuilder8)（自定义构建器）

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   2. import { HdsTabs, HdsTabsAttribute, HdsTabsController, hdsMaterial } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barFloatingStyle样式，并设置barOverlap为true，vertical为false，barPosition为BarPosition.End，可实现页签栏的悬浮样式。若在barFloatingStyle中设置miniBar，则可实现迷你栏。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // 初始化HdsTabs控制器。
   5. private controller: HdsTabsController = new HdsTabsController();

   7. @Builder
   8. miniBarBuilder() {
   9. Row() {
   10. Column() {
   11. Image($r('app.media.alarm_stop'))
   12. .width(40)
   13. .height(40)
   14. .borderRadius(40)
   15. }.width(48).height(48).justifyContent(FlexAlign.Center).margin({left: 4, right: 4})

   17. Text('Hello')

   19. Column() {
   20. Image($r('sys.media.ohos_ic_public_pause'))
   21. .width(40)
   22. .height(40)
   23. .borderRadius(40)
   24. }.width(48).height(48).justifyContent(FlexAlign.Center)
   25. }
   26. }

   28. build() {
   29. Column() {
   30. HdsTabs({ controller: this.controller }) {
   31. TabContent() {
   32. Scroll() {
   33. Column(){
   34. Image($r('app.media.ocean'))
   35. Image($r('app.media.desert'))
   36. Image($r('app.media.mountain'))
   37. Image($r('app.media.sunset'))
   38. }
   39. }
   40. }
   41. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Green'))

   43. TabContent() {
   44. Image($r('app.media.ocean'))
   45. }
   46. .tabBar(new BottomTabBarStyle($r('sys.media.wifi_router_fill'), 'Blue'))

   48. TabContent() {
   49. Image($r('app.media.ocean'))
   50. }
   51. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Yellow'))
   52. }
   53. // 设置barOverlap为true，vertical为false，barPosition为BarPosition.End
   54. .barOverlap(true)
   55. .barPosition(BarPosition.End)
   56. .vertical(false)
   57. // 设置页签栏悬浮样式。
   58. .barFloatingStyle({
   59. barWidth: { smallWidth: 200, mediumWidth: 300, largeWidth: 400 },
   60. barBottomMargin: 28,
   61. gradientMask: { maskColor: '#66F1F3F5', maskHeight: 92 },
   62. systemMaterialEffect: {
   63. materialType: hdsMaterial.MaterialType.IMMERSIVE,
   64. materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
   65. },
   66. // 设置迷你栏，若不设置，则仅有页签栏。
   67. miniBar: {
   68. miniBarBuilder: () => this.miniBarBuilder()
   69. }
   70. })
   71. }
   72. }
   73. }
   ```
