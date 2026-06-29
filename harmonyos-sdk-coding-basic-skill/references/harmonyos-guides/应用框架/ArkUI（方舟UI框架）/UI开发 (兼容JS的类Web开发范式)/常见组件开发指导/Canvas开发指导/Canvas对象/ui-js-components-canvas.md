---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas
title: Canvas对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > Canvas对象
category: harmonyos-guides
scraped_at: 2026-06-11T14:33:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ef9380017fb54993609cdfca3870928f2205193223f2445c8508294e122198d8
---
Canvas组件提供画布，用于自定义绘制图形。具体用法请参考[CanvasRenderingContext2D对象](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Full）/画布组件/CanvasRenderingContext2D对象/js-components-canvas-canvasrenderingcontext2d.md)。

## 创建Canvas组件

在pages/index目录下的hml文件中创建一个Canvas组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas></canvas>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }

11. canvas {
12. background-color: #00ff73;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/L9Zs_npLRzai-e6k6GggvA/zh-cn_image_0000002622698097.png?HW-CC-KV=V1&HW-CC-Date=20260611T063349Z&HW-CC-Expire=86400&HW-CC-Sign=BC0F69D612900F17F7D9308F2786C33FDA664B3C24C2D4C6298880D008323D72)

说明

* Canvas组件默认背景色与父组件的背景色一致。
* Canvas默认宽高为width: 300px，height: 150px。

## 添加样式

Canvas组件设置宽（width）、高（height）、背景色（background-color）及边框样式（border）。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas></canvas>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. background-color: #F1F3F5;
7. width: 100%;
8. height: 100%;
9. }

11. canvas {
12. width: 500px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/EsK1pVfhROCbdLUxIzecUw/zh-cn_image_0000002592218536.png?HW-CC-KV=V1&HW-CC-Date=20260611T063349Z&HW-CC-Expire=86400&HW-CC-Sign=4F4A116B0950B949DEFC4AAE5040BF9A630B3D02490D2EA80BD8EF86FFA0B40B)

## 添加事件

Canvas添加长按事件，长按后可获取Canvas组件的dataUrl值（toDataURL方法返回的图片信息），打印在下方文本区域内。

说明

promptAction相关接口参考[弹窗](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.promptAction (弹窗)/js-apis-promptaction.md>)。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1" onlongpress="getUrl"></canvas>
4. <text>dataURL</text>
5. <text class="content">{{ dataURL }}</text>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }

11. canvas {
12. width: 500px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. margin-bottom: 50px;
17. }

19. .content {
20. border: 5px solid blue;
21. padding: 10px;
22. width: 90%;
23. height: 400px;
24. overflow: scroll;
25. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. dataURL: null,
7. },
8. onShow() {
9. let el = this.$refs.canvas1;
10. let ctx = el.getContext("2d");
11. ctx.strokeRect(100, 100, 300, 300);
12. },
13. getUrl() {
14. let el = this.$refs.canvas1
15. let dataUrl = el.toDataURL()
16. this.dataURL = dataUrl;
17. promptAction.showToast({ duration: 2000, message: "long press,get dataURL" })
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/AYkmtvitR3qx1Lc49aGT6w/zh-cn_image_0000002592378470.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063349Z&HW-CC-Expire=86400&HW-CC-Sign=B2DDF51AD35DC369623D3AC038B49AA70D826F24B2A43F0E31BB624BB0C8784A)

说明

画布不支持在onInit和onReady中进行创建。
