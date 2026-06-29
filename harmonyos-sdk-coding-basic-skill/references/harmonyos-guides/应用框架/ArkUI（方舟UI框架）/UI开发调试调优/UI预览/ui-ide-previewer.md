---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer
title: UI预览
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI预览
category: harmonyos-guides
scraped_at: 2026-06-11T14:34:11+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:30889f762c08523dc9d4308fed5f3c8818d467eefba5ee92e6ffaec22baf368f
---
DevEco Studio为开发者提供了UI预览功能，方便查看UI效果并随时调整页面布局。预览支持页面预览和组件预览。图1中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/CIEYyTYSRYmVR247gvldzA/zh-cn_image_0000002622858001.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=15F5527E97C6BE3FBD85802B5B74BBBF67F2BB45723AD3BAA723B39AD2075247)表示页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/VjdZniO8TeOP0qk-XxN_1A/zh-cn_image_0000002622698123.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=90DD116E555DB3C5489FB9C22EA5A6564DE7B5E386FD6B1172A388737CB37EF6)表示组件预览。

说明

操作系统和真机设备的差异可能导致预览效果与真机效果不同。预览效果仅作参考，实际效果以真机为准。

**图1** 预览图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/vx-4oD9uR6-WhGNuHa_IxA/zh-cn_image_0000002592218562.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=2B3049AF769684429CA68F1322257F3821DF41B83CDB8ABA3283FAE3751F4E4C)

## 页面预览

ArkTS应用/元服务均支持页面预览。页面预览通过在工程的ets文件中，给自定义组件添加[@Entry](<../../UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#entry>)装饰器，即可以查看当前UI页面效果。

* 启动方式：选中需要预览的ets页面，点击右侧侧边栏的Previewer按钮，启动页面预览。
* 热加载：在启动页面预览的前提下，添加、删除或修改UI组件后，通过Ctrl+S保存，预览器会同步刷新预览效果，无需重新启动预览。
* 路由能力：支持通过路由能力进行页面切换查看其它页面预览效果。

在页面预览的基础上，提供了极速预览和Inspector双向预览两种特性。下面将详细说明这两种特性。

### 极速预览

支持在修改组件的属性时，无需使用Ctrl+S进行保存，可以直接观察到修改后的预览效果。极速预览默认开启，若需关闭，点击预览器右上角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/OyiXFCPgQHqP0kd8gC2MqA/zh-cn_image_0000002592378496.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=A487AF118F5608B1E148C8ECF2AF531829DF51F4E6487A3F04102ADE0EF2F6B5)即可。

注意

部分应用场景不支持极速预览：

* 不显示的组件。
* 新增或删除组件。
* 包含private变量或无类型的controller的组件。
* 使用了[@Builder](<../../UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@Builder装饰器：自定义构建函数/arkts-builder.md>)、[@Style](<../../UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@Styles装饰器：定义组件重用样式/arkts-style.md>)、[@Extend](<../../UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@Extend装饰器：定义扩展组件样式/arkts-extend.md>)等装饰器的组件。
* 修改使用import导入外部组件/模块的组件。
* 修改状态变量。

效果如图2所示：

**图2** 极速预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/7WGHlHZzRjWPrY0rVBU3lg/zh-cn_image_0000002622858003.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=50085AD8BA45D841BEB3EFBBEAD044797FA68418ED41DFEC0D81544D065D17F0)

### inspector双向预览

支持ets文件与预览器的双向预览。使用时，点击预览器界面图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/O25hbU93QgqDuW0DK4WT-Q/zh-cn_image_0000002622698125.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=9C533C682810E32258C19478B97CF37933CBF34134AB571D381D8F7D76F65A85)开启双向预览功能。

开启双向预览功能后，支持代码编辑器、UI界面和组件树之间的联动：

1. 选中预览器界面中的组件，组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
2. 选中布局文件中的代码块，预览器界面将高亮显示，组件树上的组件节点将呈现被选中的状态。
3. 选中组件树中的组件，对应的代码块和预览器界面将高亮显示。
4. 在预览界面，通过组件的属性面板修改可修改的属性或样式。预览界面的修改会自动同步到代码编辑器中，并实时刷新预览器界面。代码编辑器中的源码修改也会实时刷新预览器界面，并更新组件树信息及组件属性。

效果如图3所示：

**图3** inspector双向预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/gvF-ENEXRR2iUbENcJcWmw/zh-cn_image_0000002592218564.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=32824903C449C681AF0025FF9B3FCD390ABB4A2628A5B77B2590B9EE9520D690)

## 组件预览

ArkTS应用/元服务支持组件预览功能。组件预览通过在自定义组件前添加[@Preview](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/组件预览/组件预览/ts-universal-component-previewer.md#preview装饰器)装饰器实现。在单个源文件中，最多可以使用10个@Preview装饰自定义组件。启动方式：

* 当组件被@Entry和@Preview装饰时，点击右侧侧边栏的Previewer按钮，启动页面预览，页面加载成功后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/bH92Y9szTK-GvslCjvhyZw/zh-cn_image_0000002622698123.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=43FABBBB01EE2631BE4522CDCEBE6AA659C2616076C5E79C60AD032B6D3C96CE)，切换到组件预览。
* 当组件仅被@Preview装饰时，点击右侧侧边栏的Previewer按钮，则默认为组件预览。

组件预览时，使用@Preview装饰器的默认属性（请参考[PreviewParams](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/组件预览/组件预览/ts-universal-component-previewer.md#previewparams9)）进行效果显示。可以通过设置@Preview的参数，指定预览设备的相关属性，包括设备类型、屏幕形状等。

@Preview的使用参考如下示例：

```
1. @Entry
2. @Preview
3. @Component
4. struct ComponentPreviewOne {
5. build() {
6. Column() {
7. Text('this is component previewer One')
8. .height(80)
9. .fontSize(30)
10. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
11. Image($r('app.media.startIcon'))
12. .height(300)
13. .width(300)
14. }
15. }
16. }

18. @Preview
19. @Component
20. struct ComponentPreviewTwo {
21. build() {
22. Column() {
23. Text('this is component previewer Two')
24. .height(80)
25. .fontSize(30)
26. .fontColor(Color.Pink)
27. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
28. Image($r('app.media.startIcon'))
29. .height(300)
30. .width(300)
31. }
32. }
33. }
```

效果如图4所示：

**图4** 组件预览效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/DQqQ5KtBRjGP0bVdmx-QsA/zh-cn_image_0000002592378498.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=043E5CB89BB25E969C3ED2188BC3A5072FA7334EBD98870DC376F72AFF1BE168)

## 动态修改分辨率

同一个应用/元服务可以运行在多个设备上，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果。预览支持动态修改分辨率，方便开发者随时查看不同设备上的页面显示效果。启动方式：启动页面预览后，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/cqYtC6-sS5OyhYAx9ZAGuA/zh-cn_image_0000002622858005.png?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=BFFFF45FB77360ADAF9B807D512B289C00CFC9F229D4C717099143ABC776511F)，即可拖动页面选中框动态修改当前设备的屏幕大小。

效果如图5所示：

**图5** 动态修改分辨率效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/7sxp3jpCTQeh-tiOfYLM-w/zh-cn_image_0000002622698127.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063410Z&HW-CC-Expire=86400&HW-CC-Sign=7D24826860A6D7E143C91D1DE66D4E89A830E951B1AC2EEB693235500D7EA01E)
