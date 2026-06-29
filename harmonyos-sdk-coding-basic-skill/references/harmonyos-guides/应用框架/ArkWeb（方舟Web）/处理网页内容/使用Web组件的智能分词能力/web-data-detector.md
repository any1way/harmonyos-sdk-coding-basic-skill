---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-data-detector
title: 使用Web组件的智能分词能力
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 使用Web组件的智能分词能力
category: harmonyos-guides
scraped_at: 2026-06-11T14:36:06+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:628e0536820189eefb96be880c6f7d2901775af443608bd7f9b57ebd6d565585
---
从API version 20开始，ArkWeb提供了H5页面内的文本分词识别功能，支持文本分词高亮、分词长按预览及文本选择菜单扩展等。这些功能需将[enableDataDetector](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#enabledatadetector20>)设置为true，默认为false。

此功能主要用于单页H5页面内容的实体识别，能够自动识别页面中的电话号码、网址等信息，并提供便捷的交互操作。启用此功能后，用户可以直接在页面中与识别的实体交互，如点击电话号码进行呼叫，点击地址在地图中查看，从而提升用户体验。

可识别的实体类型包括电话、链接、邮箱、地址和时间，详见[TextDataDetectorType](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/文本组件公共接口/ts-text-common.md#textdatadetectortype11枚举说明)。

## 文本分词高亮

Web组件内的H5页面加载完成后，自动识别并高亮标注页面内的特殊实体。页面变化后新出现的实体不会被高亮标注。

特殊实体的高亮过滤规则如下：

* 不处理输入框内、可编辑区域内的文本实体。
* 不处理<a></a>标签内的文本实体。
* 不处理跨域iframe内、两层及以上嵌套iframe内的文本实体。
* 跨节点的实体不会被高亮，如<p>星<span>期六</span></p>。

页面中文本实体高亮后，将转变为超链接形式。触摸点击或鼠标左键点击实体，会根据实体类型弹出操作菜单。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';
7. webController: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Row() {
12. Button('Refresh')
13. .onClick(() => {
14. this.webController.refresh();
15. })
16. }

18. Web({
19. src: $rawfile('index.html'),
20. controller: this.webController
21. })
22. .enableDataDetector(true)
23. .dataDetectorConfig({
24. types: []  // 实体识别类型，为空则识别所有类型
25. })
26. }
27. .height('100%')
28. .width('100%')
29. }
30. }
```

[WebDataDetectorHighlighting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkWeb/ArkWebDataDetector/entry/src/main/ets/pages/WebDataDetectorHighlighting.ets#L15-L46)

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>Test</title>
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. </head>
8. <body>
9. <p>电话：400-123-4567</p>
10. <p>邮箱：test@example.com</p>
11. <p>网址：https://www.example.com/</p>
12. <p>日期：2025.06.01</p>
13. <p>地址：北京市海淀区中关村</p>
14. <p>不会高亮的星<span>期六</span>与会高亮的星期六</p>
15. </body>
16. </html>
```

点击实体文本，弹出对应的操作菜单，如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/jfs038YcTcubkbJq4rEyrA/zh-cn_image_0000002622698207.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063605Z&HW-CC-Expire=86400&HW-CC-Sign=B5B8FEDA3CEC6946DD036D35ABBA262C4996FEBC4159247D4944D03DCD6B3D6B)

鼠标右键点击、鼠标拖拽将触发超链接的默认行为。

接口[dataDetectorConfig](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#datadetectorconfig20>)未被使用，或其参数[TextDataDetectorConfig](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/文本组件公共接口/ts-text-common.md#textdatadetectorconfig11对象说明)的enablePreviewMenu设置为false时，长按、拖拽将触发超链接的默认行为，如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/35742yq_QRyqi8_7-CEW_Q/zh-cn_image_0000002592218646.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063605Z&HW-CC-Expire=86400&HW-CC-Sign=E07248344F0D52B345E96ABD118DBB95C79E5EE61540227EDB971E8E0854825C)

页面文本元素的计算样式存在user-select:none时，实体菜单中“选择文本”的选项无效，但在[copyOptions](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#copyoptions11>)不为CopyOptions.None时，仍可以复制实体文本。

## 分词长按预览

使用分词长按预览功能时，需要额外配置[dataDetectorConfig](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#datadetectorconfig20>)：

```
1. Web({
2. src: $rawfile('index.html'),
3. controller: this.webController
4. })
5. .enableDataDetector(true)
6. .dataDetectorConfig({
7. enablePreviewMenu: true,  // 配置分词长按预览功能
8. types: []
9. })
```

[WebDataDetectorLongPress.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkWeb/ArkWebDataDetector/entry/src/main/ets/pages/WebDataDetectorLongPress.ets#L31-L41)

在[copyOptions](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#copyoptions11>)不为CopyOptions.None时，长按被高亮的实体文本，会弹出预览菜单，如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/cbpwvQHMTDmFCUZV3M2J_w/zh-cn_image_0000002592378580.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063605Z&HW-CC-Expire=86400&HW-CC-Sign=71D47A2A5818A300E82A68751938ADB7534673398EF6AD38B0CC4C7AC71B7894)

通过[bindSelectionMenu](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#bindselectionmenu13>)绑定的[自定义菜单](../使用Web组件菜单处理网页内容/web-menu.md#自定义菜单)与分词长按预览菜单互不影响。长按被高亮的分词超链接不会弹出自定义超链接菜单，长按普通超链接也不会弹出分词预览菜单。

## 文本选择菜单扩展

从API version 22开始，支持通过[enableSelectedDataDetector](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#enableselecteddatadetector22>)单独配置文本选择AI菜单的启用情况。

在非编辑区域中，选中的文本满足以下条件时，文本选择菜单将显示相应的AI菜单项：

* 选中文本经过UTF-8编码转换后，其字节长度不超过255字节。
* 选中文本中仅包含一个匹配识别类型的实体（可通过[dataDetectorConfig](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#datadetectorconfig20>)配置支持的识别类型）。
* 不处于“全选”操作状态下的文本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/5LKHgDcwSteVUf2gjQA9nw/zh-cn_image_0000002622858087.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063605Z&HW-CC-Expire=86400&HW-CC-Sign=E04FA9A337F259486F7EA7BD8D54CC157CFF8C58DEA1A1D264A4FF071214B030)

AI菜单项的出现与是否选中高亮的实体文本无关，只要满足上述条件，AI菜单项就会显示。
