---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-double-edge-streamer
title: 双边边缘流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 双边边缘流光
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:40+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:d94efe66580c9cd206ab302d08725d8abbe1ed423498e07a602eea57f3b2746c
---
## 场景介绍

从6.0.0(20)版本开始，新增支持[双边边缘流光](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS API/hdsEffect/ui-design-hdseffect.md#effecttype>)。

通过双边边缘流光接口可以设置组件的边缘发光效果，并且可以设置两条边的起始、终止位置和边缘颜色效果，常用于胶囊组件、屏幕边缘发光等。

## 开发步骤

1. 导入模块。

   ```
   1. import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 设置双边边缘流光效果。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

   6. build() {
   7. Column() {
   8. Stack() {
   9. }
   10. .visualEffect(new hdsEffect.HdsEffectBuilder()
   11. .shaderEffect({
   12. effectType: hdsEffect.EffectType.DUAL_EDGE_FLOW_LIGHT,
   13. animation: {
   14. duration: 4000,
   15. iterations: -1,
   16. autoPlay: true,
   17. onFinish: () => {
   18. console.info('Succeeded in finishing');
   19. }
   20. },
   21. controller: this.controller,
   22. params: {
   23. firstEdgeFlowLight: {
   24. startPos: 0,
   25. endPos: 1.0,
   26. color: '#1AD0F1',
   27. },
   28. secondEdgeFlowLight: {
   29. startPos: 0.5,
   30. endPos: 1.5,
   31. color: '#FFA4E5',
   32. }
   33. }
   34. })
   35. .buildEffect())
   36. .width(200)
   37. .borderRadius('50%')
   38. .clip(true)
   39. .height(200)
   40. .backgroundColor('#383838')
   41. }
   42. .justifyContent(FlexAlign.Center)
   43. .backgroundColor(Color.Black)
   44. .width('100%')
   45. .height('100%')
   46. }
   47. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/PGzlOKERTOOzUyLGlvld4g/zh-cn_image_0000002592218772.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063752Z&HW-CC-Expire=86400&HW-CC-Sign=315AEBDABC6A43BA59032678D359105C551B7452C62EC92AA3C543033C4481BA)
