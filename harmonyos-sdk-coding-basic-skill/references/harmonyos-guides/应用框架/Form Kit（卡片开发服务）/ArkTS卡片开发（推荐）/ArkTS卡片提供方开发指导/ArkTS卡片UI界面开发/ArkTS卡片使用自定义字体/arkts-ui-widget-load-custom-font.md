---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-load-custom-font
title: ArkTS卡片使用自定义字体
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片使用自定义字体
category: harmonyos-guides
scraped_at: 2026-06-11T14:37:41+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:b2ce6244d7b3ff2a8fb1f9ea89052da61d3fdb536170202013cb9c29e8d0f318
---
API version 22开始新增了[ohos.graphics.text.FontCollection.getLocalInstance](<../../../../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.text (文本模块)/js-apis-graphics-text.md#getlocalinstance22>)接口获取本地字体集实例，应用可以通过这个本地实例为卡片加载自定义字体。

## 开发步骤

1. 创建动态卡片：按照[创建ArkTS卡片](../../../创建ArkTS卡片/arkts-ui-widget-creation.md)里的描述创建动态卡片。
2. 在项目entry\src\main\resources\rawfile目录下添加自定义字体文件xxx.ttf。
3. 页面布局代码实现entry/src/main/ets/widget/pages/WidgetCard.ets。

   在卡片页面中布局两个按钮，点击按钮load font或按钮unload font，调用本地字体集实例的loadFontSync、unloadFontSync进行字体的加载、卸载。

```
1. // entry/src/main/ets/widget/pages/WidgetCard.ets
2. import { text } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct loadFontSyncCard {
7. // 在这里使用getLocalInstance访问本地字体集实例
8. private fc: text.FontCollection = text.FontCollection.getLocalInstance();
9. @State content: string = '默认字体';

11. build() {
12. Column({ space: 10 }) {
13. Text(this.content)
14. .fontFamily('custom') // 在此处声明组件使用自定义字体
15. Button('load font')
16. .onClick(() => {
17. // 在此处加载自定义字体文件
18. this.fc.loadFontSync('custom', $rawfile('xxx.ttf'));
19. this.content = '自定义字体';
20. })
21. Button('unload font')
22. .onClick(() => {
23. this.fc.unloadFontSync('custom');
24. this.content = '默认字体';
25. })
26. }.width('100%')
27. .height('100%')
28. .justifyContent(FlexAlign.Center)
29. }
30. }
```

[WidgetCard.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Form/CustomFontWidgetCards/entry/src/main/ets/widget/pages/WidgetCard.ets#L16-L47)

说明

* 本地字体集可加载多个自定义字体，所有字体合计最大内存限制加载20MB。
* 同一应用的所有卡片共用一个本地字体集实例。加载或卸载自定义字体后，所有卡片的字体显示会同步更新。

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/rcorqpE-Q2q0obdzS39GzA/zh-cn_image_0000002592218706.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063740Z&HW-CC-Expire=86400&HW-CC-Sign=BC84D8898B8EAB24C4A5CD155309B12F846607C823FA9E373D3E76B63D31F68A)
