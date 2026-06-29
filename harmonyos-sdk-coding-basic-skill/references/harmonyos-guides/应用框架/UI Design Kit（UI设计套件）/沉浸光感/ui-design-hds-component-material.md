---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-component-material
title: 沉浸光感
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 沉浸光感
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:44+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:9a94c45796d4f5d5239efbfaf45eab78483046ae07577ac112ddb68e99ce63e1
---
## 场景介绍

从6.1.0(23) 版本开始，新增支持HDS组件的沉浸光感材质能力。

* **HDS导航**：通过设置[TitleBarStyleOptions](<../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#titlebarstyleoptions>)的systemMaterialEffect参数，可为标题栏按钮设置沉浸光感视效。
* **HDS底部页签**：通过设置[HdsTabsFloatingStyle](<../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md#hdstabsfloatingstyle>)的systemMaterialEffect参数，可为底部页签设置沉浸光感视效。

## 使用系统自适应的沉浸光感

推荐使用系统自适应的沉浸光感效果，系统会根据当前设备的算力动态调整组件的材质效果，实现性能与显示效果的最佳平衡体验。

### 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsNavigation, HdsNavigationTitleMode, HdsTabs, HdsTabsController, HdsNavigationMenuContentOptions, ScrollEffectType, hdsMaterial } from '@kit.UIDesignKit';
   2. import { SymbolGlyphModifier } from '@kit.ArkUI';
   ```
2. 创建HDS导航和底部页签组件。导航标题栏包含1个返回按钮和3个功能按钮，底部页签包含3个子项。

   以下示例代码为底部页签和标题栏的4个按钮设置了沉浸光感效果，该效果将根据系统能力自适应调整。

   ```
   1. @Entry
   2. @Component
   3. export struct Index {
   4. private scrollerForScroll: Scroller = new Scroller();
   5. private controller: HdsTabsController = new HdsTabsController();

   7. private menus: HdsNavigationMenuContentOptions = {
   8. value: [{
   9. content: {
   10. label: 'menu1',
   11. icon: $r('sys.symbol.square_and_pencil')
   12. }
   13. }, {
   14. content: {
   15. label: 'menu2',
   16. icon: $r('sys.symbol.star')
   17. }
   18. },{
   19. content: {
   20. label: 'menu3',
   21. icon: $r('sys.symbol.more')
   22. }
   23. }
   24. ]
   25. };

   27. build() {
   28. HdsNavigation() {
   29. HdsTabs({ controller: this.controller }) {
   30. ForEach(MENU_CONFIG, (item: MenuItem) => {
   31. TabContent() {
   32. Stack() {
   33. Scroll(this.scrollerForScroll) {
   34. Column() {
   35. Image($r('app.media.scenery01')).width('100%') // scenery为自定义资源，开发者需替换本地资源
   36. }
   37. }
   38. .clipContent(ContentClipMode.SAFE_AREA)
   39. .height('100%')
   40. }
   41. }
   42. .tabBar(new BottomTabBarStyle({
   43. normal: item.symbolGlyph, selected: item.symbolGlyph1
   44. }, item.label))
   45. })
   46. }
   47. .barOverlap(true)
   48. .vertical(false)
   49. .barPosition(BarPosition.End)
   50. .barFloatingStyle({
   51. barBottomMargin: 28,
   52. // 设置沉浸光感效果：ADAPTIVE类型表示自适应系统材质，ADAPTIVE等级表示材质生效策略由系统根据设备性能自适应决定
   53. systemMaterialEffect: {
   54. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   55. materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE // 底部悬浮页签沉浸光感效果跟随系统策略自适应
   56. }
   57. })
   58. }
   59. .mode(NavigationMode.Stack)
   60. .titleBar({
   61. content: {
   62. title: {
   63. mainTitle: 'MainTitle',
   64. },
   65. menu: this.menus,
   66. },
   67. style: {
   68. scrollEffectOpts: {
   69. enableScrollEffect: false,
   70. scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
   71. },
   72. // 设置沉浸光感效果：ADAPTIVE类型表示自适应系统材质，ADAPTIVE等级表示材质生效策略由系统根据设备性能自适应决定
   73. systemMaterialEffect: {
   74. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   75. materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE // 标题栏按钮沉浸光感效果跟随系统策略自适应
   76. },
   77. },
   78. avoidLayoutSafeArea: false,
   79. enableComponentSafeArea: false
   80. })
   81. .bindToScrollable([this.scrollerForScroll])
   82. .hideBackButton(false)
   83. .titleMode(HdsNavigationTitleMode.MINI)
   84. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
   85. }
   86. }

   88. interface MenuItem {
   89. symbolGlyph: SymbolGlyphModifier,
   90. symbolGlyph1: SymbolGlyphModifier,
   91. label: string,
   92. defaultBgColor: ResourceColor,
   93. hoverBgColor: ResourceColor,
   94. pressBgColor: ResourceColor,
   95. };

   97. const MENU_CONFIG: MenuItem[] = [
   98. {
   99. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   100. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   101. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   102. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   103. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   104. label: '闹钟',
   105. defaultBgColor: Color.Transparent,
   106. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   107. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   108. },
   109. {
   110. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   111. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   112. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   113. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   114. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   115. label: '时钟',
   116. defaultBgColor: Color.Transparent,
   117. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   118. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   119. },
   120. {
   121. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   122. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   123. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   124. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   125. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   126. label: '秒表',
   127. defaultBgColor: Color.Transparent,
   128. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   129. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   130. }
   131. ];
   ```

## 使用自定义沉浸光感效果

如果使用自定义沉浸光感的视觉效果，请先调用[getSystemMaterialTypes()](<../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS API/hdsMaterial/ui-design-hdsmaterial.md#getsystemmaterialtypes>)接口查询当前设备所支持的材质能力，再根据查询结果选用相应的材质效果枚举：

1. 如果查询结果显示当前设备支持IMMERSIVE材质类型，可选用EXQUISITE或GENTLE效果。
2. 如果查询结果显示当前设备不支持IMMERSIVE材质类型，则建议使用SMOOTH效果，以降低卡顿和发热风险，保障用户体验。

### 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsNavigation, HdsNavigationTitleMode, HdsTabs, HdsTabsController, HdsNavigationMenuContentOptions, ScrollEffectType, hdsMaterial } from '@kit.UIDesignKit';
   2. import { SymbolGlyphModifier } from '@kit.ArkUI';
   ```
2. 创建HDS导航和底部页签组件。导航标题栏包含1个返回按钮和3个功能按钮，底部页签包含3个子项。

   以下示例代码为底部页签和标题栏的4个按钮设置了沉浸光感效果，根据设备所能支持的材质能力自定义动态切换显示效果。

   ```
   1. @Entry
   2. @Component
   3. export struct Index {
   4. private scrollerForScroll: Scroller = new Scroller();
   5. private controller: HdsTabsController = new HdsTabsController();
   6. @State customMaterialLevel: hdsMaterial.MaterialLevel = hdsMaterial.MaterialLevel.EXQUISITE;

   8. private menus: HdsNavigationMenuContentOptions = {
   9. value: [{
   10. content: {
   11. label: 'menu1',
   12. icon: $r('sys.symbol.square_and_pencil')
   13. }
   14. }, {
   15. content: {
   16. label: 'menu2',
   17. icon: $r('sys.symbol.star')
   18. }
   19. },{
   20. content: {
   21. label: 'menu3',
   22. icon: $r('sys.symbol.more')
   23. }
   24. }
   25. ]
   26. };

   28. aboutToAppear(): void {
   29. // 获取系统支持的材质类型，用于根据设备能力选择合适的材质等级
   30. let materialTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
   31. if (materialTypes.indexOf(hdsMaterial.MaterialType.IMMERSIVE) < 0) {
   32. // 当前设备不支持IMMERSIVE材质类型，则使用SMOOTH效果以优化性能，降低卡顿和发热风险
   33. this.customMaterialLevel = hdsMaterial.MaterialLevel.SMOOTH;
   34. }
   35. }

   37. build() {
   38. HdsNavigation() {
   39. HdsTabs({ controller: this.controller }) {
   40. ForEach(MENU_CONFIG, (item: MenuItem) => {
   41. TabContent() {
   42. Stack() {
   43. Scroll(this.scrollerForScroll) {
   44. Column() {
   45. Image($r('app.media.scenery01')).width('100%') // scenery为自定义资源，开发者需替换本地资源
   46. }
   47. }
   48. .clipContent(ContentClipMode.SAFE_AREA)
   49. .height('100%')
   50. }
   51. }
   52. .tabBar(new BottomTabBarStyle({
   53. normal: item.symbolGlyph, selected: item.symbolGlyph1
   54. }, item.label))
   55. })
   56. }
   57. .barOverlap(true)
   58. .vertical(false)
   59. .barPosition(BarPosition.End)
   60. .barFloatingStyle({
   61. barBottomMargin: 28,
   62. systemMaterialEffect: {
   63. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   64. materialLevel: this.customMaterialLevel // 底部悬浮页签自定义沉浸光感材质效果
   65. }
   66. })
   67. }
   68. .mode(NavigationMode.Stack)
   69. .titleBar({
   70. content: {
   71. title: {
   72. mainTitle: 'MainTitle',
   73. },
   74. menu: this.menus,
   75. },
   76. style: {
   77. scrollEffectOpts: {
   78. enableScrollEffect: false,
   79. scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
   80. },
   81. systemMaterialEffect: {
   82. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   83. materialLevel: this.customMaterialLevel // 标题栏按钮自定义沉浸光感材质效果
   84. },
   85. },
   86. avoidLayoutSafeArea: false,
   87. enableComponentSafeArea: false
   88. })
   89. .bindToScrollable([this.scrollerForScroll])
   90. .hideBackButton(false)
   91. .titleMode(HdsNavigationTitleMode.MINI)
   92. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
   93. }
   94. }

   96. interface MenuItem {
   97. symbolGlyph: SymbolGlyphModifier,
   98. symbolGlyph1: SymbolGlyphModifier,
   99. label: string,
   100. defaultBgColor: ResourceColor,
   101. hoverBgColor: ResourceColor,
   102. pressBgColor: ResourceColor,
   103. };

   105. const MENU_CONFIG: MenuItem[] = [
   106. {
   107. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   108. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   109. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   110. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   111. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   112. label: '闹钟',
   113. defaultBgColor: Color.Transparent,
   114. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   115. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   116. },
   117. {
   118. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   119. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   120. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   121. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   122. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   123. label: '时钟',
   124. defaultBgColor: Color.Transparent,
   125. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   126. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   127. },
   128. {
   129. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   130. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   131. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   132. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   133. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   134. label: '秒表',
   135. defaultBgColor: Color.Transparent,
   136. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   137. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   138. }
   139. ];
   ```

   **沉浸光感材质效果展示**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/LTutEgoJSWqlTwqw6fW9TA/zh-cn_image_0000002592218774.png?HW-CC-KV=V1&HW-CC-Date=20260611T063943Z&HW-CC-Expire=86400&HW-CC-Sign=03CE3A6BDD8F70C0AF79FA4A8441FCECEA35ED1B3876CAFF31BDE42C841926A4)
