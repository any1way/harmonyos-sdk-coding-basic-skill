---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-customized-area
title: 设置自定义区域
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置自定义区域
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:13+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:a01576d41e8a89400d704bd550f8fa29549ff7231cd513a31d6a654ee578acc5
---
## 场景介绍

从6.0.0(20)版本开始，导航组件支持设置标题栏的[stackBuilder](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#titlebarcontentoptions>)和[bottomBuilder](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#titlebarcontentoptions>)，允许开发者自定义标题栏样式，以匹配应用的视觉风格。

当应用开发者需要在标题栏区域增加自定义节点时，例如在标题栏上方区域增加分段按钮，标题下方区域增加搜索框、页签时，可以使用标题栏自定义区域设置能力。由于标题栏高度通常由系统或框架统一控制，开发者在添加自定义节点时需注意不要超出标题栏的可用空间，否则可能导致布局溢出或视觉混乱。自定义区域可能会覆盖或影响默认标题栏组件（如返回按钮、标题文字），需谨慎布局，避免交互冲突或遮挡关键元素。如果在标题栏中添加大量交互复杂、渲染频率高的组件，可能会对性能产生影响。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/b_9iCIs4SzmPLesgbQ4Psw/zh-cn_image_0000002592378688.png?HW-CC-KV=V1&HW-CC-Date=20260611T063558Z&HW-CC-Expire=86400&HW-CC-Sign=2A776998B88B9771A8F6908EF547489A28D87B7649097373C6348E37D3809F52 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/y7TXM9RqQGmBatlAtuynIw/zh-cn_image_0000002622858195.png?HW-CC-KV=V1&HW-CC-Date=20260611T063558Z&HW-CC-Expire=86400&HW-CC-Sign=9BB24477BCADC40942EF9C0A6A1358FB24F3B6D526464951BBC8E3EA9756913A "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, HdsNavigationTitleMode, HdsNavigationAttribute } from '@kit.UIDesignKit';
   3. import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem } from '@kit.ArkUI';
   ```
2. 创建一级导航组件，通过配置titleBar中content属性的stackBuilder以及bottomBuilder属性，即可实现导航组件的自定义区域设置。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
   5. scroller: Scroller = new Scroller();
   6. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
   7. buttons: [{ text: '备忘' }, { text: '待办' }] as ItemRestriction<SegmentButtonTextItem>,
   8. selectedFontColor: '#ffe6ba0b',
   9. selectedBackgroundColor: Color.White,
   10. textPadding: {
   11. top: 5,
   12. right: 5,
   13. bottom: 5,
   14. left: 5
   15. }
   16. });
   17. @State tabSelectedIndexes: number[] = [0];

   19. @Builder
   20. stackBuilder() {
   21. Row() {
   22. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
   23. Button() {
   24. SymbolGlyph($r('sys.symbol.open_sidebar'))
   25. .fontColor([$r('sys.color.icon_primary')])
   26. .fontSize(24)
   27. .width(24)
   28. .height(24)
   29. }
   30. .width(40)
   31. .height(40)
   32. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))

   34. SegmentButton({
   35. options: this.tabOptions,
   36. selectedIndexes: $tabSelectedIndexes
   37. })
   38. .width(150)

   40. Button() {
   41. SymbolGlyph($r('sys.symbol.dot_grid_2x2'))
   42. .fontColor([$r('sys.color.icon_primary')])
   43. .fontSize(24)
   44. .width(24)
   45. .height(24)
   46. }
   47. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
   48. .width(40)
   49. .height(40)
   50. }
   51. .margin({ left: 16, right: 16 })
   52. }
   53. .width('100%')
   54. }

   56. build() {
   57. HdsNavigation(this.pageInfos) { // 创建HdsNavigation组件
   58. Row() {
   59. Text('全部备忘')
   60. .fontSize(26)
   61. .fontWeight(FontWeight.Bold)
   62. .layoutWeight(1)
   63. .onClick(() => {
   64. this.pageInfos.pushPath({ name: 'pageOne' });
   65. })
   66. }
   67. .margin({ left: 16, top: 16 })
   68. .justifyContent(FlexAlign.Start)
   69. }
   70. .titleBar({
   71. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   72. content: {
   73. title: { mainTitle: '' },
   74. // 设置HdsNavigation 自定义标题区
   75. stackBuilder: (): void => this.stackBuilder(),
   76. }
   77. })
   78. .hideBackButton(true)
   79. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   80. .titleMode(HdsNavigationTitleMode.MINI)
   81. }
   82. }
   ```
3. 在PageOne页面创建二级导航组件。通过titleBar接口设置HdsNavDestination标题栏HarmonyOS风格化样式及内容设置。展示NavPathStack路由使用示例。

   ```
   1. // PageOne.ets
   2. // 模块导入
   3. // 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
   4. import { BottomBuilderShowType, HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';

   6. @Builder
   7. export function PageOneBuilder() {
   8. PageOne()
   9. }

   11. @Component
   12. export struct PageOne {
   13. @Consume('pageInfos') pageInfos: NavPathStack;
   14. scroller: Scroller = new Scroller();

   16. @Builder
   17. bottomBuilder() {
   18. Column() {
   19. Search({ placeholder: 'Search' })
   20. .height(40)
   21. .placeholderColor($r('sys.color.font_primary'))
   22. .margin({ left: 16, right: 16 })
   23. }
   24. .width('100%')
   25. }

   27. build() {
   28. HdsNavDestination() { // 创建HdsNavDestination组件
   29. Scroll(this.scroller) { // HdsNavDestination内容区设置可滚动容器组件，用于实现内容区滚动联动标题栏动态模糊样式
   30. Image($r('app.media.scenery2')) // scenery2为自定义资源，开发者需替换本地资源
   31. .height('100%')
   32. }
   33. .edgeEffect(EdgeEffect.Spring)
   34. .scrollBar(BarState.Off)
   35. .margin({ left: 16, right: 16 })
   36. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   37. }
   38. .titleBar({
   39. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   40. content: {
   41. // HdsNavigation标题栏内容区设置
   42. title: {
   43. // HdsNavigation标题栏标题设置
   44. mainTitle: 'PageOne',
   45. },
   46. // HdsNavigation标题栏返回按钮设置
   47. backIcon: {
   48. label: 'backIcon', // 无障碍播报内容
   49. componentId: 'backIconId', // 返回按钮id
   50. },
   51. // 设置标题栏下方自定义区域，包括设置高度，显示类型
   52. bottomBuilder: {
   53. builder: (): void => this.bottomBuilder(),
   54. height: 56,
   55. showType: BottomBuilderShowType.DIRECTLY_SHOW
   56. },
   57. menu: {
   58. // HdsNavigation标题栏菜单设置
   59. value: [{
   60. // 菜单项内容设置
   61. content: {
   62. label: 'menu',
   63. icon: $r('sys.symbol.ohos_circle'),
   64. },
   65. }]
   66. },
   67. }
   68. })
   69. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   70. }
   71. }
   ```
4. 工程entry/src/main/module.json5文件中的“module”下新增如下配置，用于页面跳转。

   ```
   1. "routerMap": "$profile:route_map"
   ```
5. 工程entry/src/main/resources/base/profile目录下增加route\_map.json文件。

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "pageOne",
   5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
   6. "buildFunction": "PageOneBuilder",
   7. "data": {
   8. "description": "this is pageOne"
   9. }
   10. }
   11. ]
   12. }
   ```
