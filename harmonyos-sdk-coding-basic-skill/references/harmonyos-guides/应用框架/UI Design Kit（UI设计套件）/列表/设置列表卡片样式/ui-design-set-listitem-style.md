---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-set-listitem-style
title: 设置列表卡片样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 列表 > 设置列表卡片样式
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:35+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:9c610a04b54b40b30edb6fa8acbb6f454a7a896c622289e0982290bc4705a4f0
---
## 场景介绍

从6.0.0(20)版本开始，新增支持设置列表卡片样式。

应用使用[HdsListItemCard](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsListItemCard/ui-design-hdslistitemcard.md>)组件实现多设备上的系统列表样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/4cWGxaDjQeWtGe5QZGhP5g/zh-cn_image_0000002622858209.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063934Z&HW-CC-Expire=86400&HW-CC-Sign=D6D17B60D4B9D2853B0DBBFD4ACB2E2EEC43BB0F0367FECAA249B7BDEDA847CE)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsListItemCard, PrefixImage, SuffixSwitch } from '@kit.UIDesignKit';
   ```
2. 创建HdsListItemCard组件，设置左边为Image，中间为Text，右边为Switch的场景。

   ```
   1. @Entry
   2. @Component
   3. struct Test {
   4. private scroller: ListScroller = new ListScroller();

   6. build() {
   7. Column() {
   8. List({ space: 10, scroller: this.scroller }) {
   9. ListItem() {
   10. HdsListItemCard({
   11. // A区图片
   12. prefixItem: new PrefixImage({
   13. image: $r('app.media.background'),
   14. onClick: () => {
   15. console.info('left image');
   16. }
   17. }),
   18. // B区文本
   19. textItem: {
   20. primaryText: {
   21. text: 'Primary Text'
   22. },
   23. secondaryText: {
   24. text: 'Secondary Text'
   25. },
   26. description: {
   27. text: 'Description Text'
   28. }
   29. },
   30. // C区Switch
   31. suffixItem: new SuffixSwitch({
   32. isCheck: false,
   33. onChange: (num: boolean) => {
   34. if (num) {
   35. console.info('switch is true');
   36. } else {
   37. console.info('switch is false');
   38. }
   39. }
   40. }),
   41. onClick: () => {
   42. console.info('hdslistitem');
   43. }
   44. })
   45. }
   46. }
   47. .width('100%')
   48. .height('100%')
   49. .margin(10)
   50. }.backgroundColor(0x1a0a59f7).height('100%')
   51. }
   52. }
   ```
