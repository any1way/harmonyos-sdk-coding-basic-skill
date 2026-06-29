---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-icon-type
title: 图标类型设置
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 图标类型设置
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:14+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:61c923e94b5c6375199701d76f8203c4b22a66545a6f77e29205489a88cff91e
---
## 场景介绍

从6.0.0(20)版本开始，导航组件新增了对文本型与图片型图标类型的支持。

当应用开发者需要配置图片型图标，或者使用普通文字型图标、单字图标时，可通过设置titleBar图标内容配置中的[type](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#hdsnavigationiconoptions>)属性实现该功能。

图片型图标([IconStyleMode.LARGE](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#iconstylemode>))：适用于需要展示完整图像的场景，例如应用的Logo、用户头像、宣传图或自定义图形按钮。

普通文字型图标([TextStyleMode.NORMAL](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#textstylemode>))：常规的文本按钮，适用于功能选项、操作按钮等需要清晰表达文本含义的场景。

单字图标([TextStyleMode.SINGLE\_CHARACTER](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsNavigation/ui-design-hdsnavigation.md#textstylemode>))：适用于需要节省空间的紧凑布局，常用于快速操作入口，建议仅在单个文字或字母的场景使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/zGsVmikrQtCqdnE3H8kr7w/zh-cn_image_0000002592378690.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063601Z&HW-CC-Expire=86400&HW-CC-Sign=8DA680BF07111FC3AEE5A1F0135BCF557501F82BFEEDEB9836BA30B82E861B33 "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { TextStyleMode, IconStyleMode, HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
   ```
2. 创建一级导航组件，通过配置titleBar中的menu上的type属性，实现文字型图标以及图片型图标大小设置。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. HdsNavigation() { // 创建HdsNavigation组件
   6. }
   7. .titleBar({
   8. content: {
   9. title: { mainTitle: '标题' },
   10. subIcon: {
   11. content: {
   12. // 设置用户头像，图片型图标类型
   13. icon: $r('app.media.contacts'), // contacts为自定义资源，开发者需替换本地资源
   14. type: IconStyleMode.LARGE,
   15. label: 'subIcon', // 无障碍播报内容
   16. isEnabled: true,
   17. action: () => {
   18. }
   19. }
   20. },
   21. menu: {
   22. // 设置菜单内容
   23. value: [{
   24. content: {
   25. // 设置第一个菜单项内容，设置为普通文本按钮
   26. label: '文本',
   27. type: TextStyleMode.NORMAL,
   28. isEnabled: true,
   29. componentId: 'menu_1',
   30. action: () => {
   31. }
   32. }
   33. }, {
   34. content: {
   35. // 设置第二个菜单项内容，设置为单字按钮
   36. label: '单',
   37. type: TextStyleMode.SINGLE_CHARACTER,
   38. isEnabled: true,
   39. componentId: 'menu_2',
   40. action: () => {
   41. }
   42. }
   43. }, {
   44. content: {
   45. // 设置第三个菜单项内容，设置为通用图标按钮
   46. label: 'largeIcon',
   47. icon: $r('sys.symbol.AI_search'),
   48. type: IconStyleMode.NORMAL,
   49. isEnabled: true,
   50. componentId: 'menu_3',
   51. action: () => {
   52. }
   53. }
   54. }],
   55. maxCount: 3 // 最大菜单显示个数配置
   56. },
   57. }
   58. })
   59. .titleMode(HdsNavigationTitleMode.MINI)
   60. .hideBackButton(true)
   61. }
   62. }
   ```
