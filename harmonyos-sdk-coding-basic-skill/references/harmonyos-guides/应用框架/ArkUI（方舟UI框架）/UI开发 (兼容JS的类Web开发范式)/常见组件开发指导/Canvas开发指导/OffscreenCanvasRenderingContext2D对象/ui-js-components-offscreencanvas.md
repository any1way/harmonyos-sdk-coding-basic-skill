---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-offscreencanvas
title: OffscreenCanvasRenderingContext2D对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > OffscreenCanvasRenderingContext2D对象
category: harmonyos-guides
scraped_at: 2026-06-11T14:33:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5b7a7dd931b195c5fd6c5b7babf7f35c5200b0155a4e6a97b912b5c3697e58de
---
使用OffscreenCanvas在离屏Canvas画布组件上进行绘制，绘制对象可以是矩形、文本、图片等。 离屏，即GPU在当前缓冲区以外新开辟的一个缓冲区。具体请参考[OffscreenCanvasRenderingContext2D对象](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Full）/画布组件/OffscreenCanvasRenderingContext2D对象/js-offscreencanvasrenderingcontext2d.md)。

以下示例创建了一个OffscreenCanvas画布，再在画布上创建一个getContext2d对象，并设置filter属性改变图片样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1"></canvas>
4. <select @change="change()">
5. <option value="blur(5px)">blur</option>
6. <option value="grayscale(50%)">grayscale</option>
7. <option value="hue-rotate(45deg)">hue-rotate</option>
8. <option value="invert(100%)">invert</option>
9. <option value="drop-shadow(8px 8px 10px green)">drop-shadow</option>
10. <option value="brightness(0.4)">brightness</option>
11. <option value="opacity(0.25)">opacity</option>
12. <option value="saturate(30%)">saturate</option>
13. <option value="sepia(60%)">sepia</option>
14. <option value="contrast(200%)">contrast</option>
15. </select>
16. </div>
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
12. width: 600px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }

18. select {
19. margin-top: 50px;
20. width: 250px;
21. height: 100px;
22. background-color: white;
23. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. el: null,
7. ctx: null,
8. offscreen: null,
9. offCanvas: null,
10. img: null,
11. },
12. onShow() {
13. this.ctx = this.$refs.canvas1.getContext('2d');
14. this.offscreen = new OffscreenCanvas(600, 500);
15. this.offCanvas = this.offscreen.getContext('2d');
16. this.img = new Image();
17. // "common/images/2.png"需要替换为开发者所需的图像资源文件
18. this.img.src = 'common/images/2.png';
19. // 图片成功获取触发方法
20. let _this = this;
21. this.img.onload = function () {
22. _this.offCanvas.drawImage(_this.img, 100, 100, 400, 300);
23. };
24. this.img.onerror = function () {
25. promptAction.showToast({ message: 'error', duration: 2000 })
26. };
27. var bitmap = this.offscreen.transferToImageBitmap();
28. this.ctx.transferFromImageBitmap(bitmap);
29. },
30. change(e) {
31. this.offCanvas.filter = e.newValue;
32. this.offCanvas.drawImage(this.img, 100, 100, 400, 300);
33. var bitmap = this.offscreen.transferToImageBitmap();
34. this.ctx.transferFromImageBitmap(bitmap);
35. },
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ckCCGviHRkuGNL0p9jN0rg/zh-cn_image_0000002622857981.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063353Z&HW-CC-Expire=86400&HW-CC-Sign=0F15922317A362F8A5D13BE869A506753E561C2F71A3E15E891E288885C6B75A)

## 判断位置

使用isPointInPath判断坐标点是否在路径的区域内，使用isPointInStroke判断坐标点是否在路径的边缘线上，并在页面上显示返回结果。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content">
4. <text>坐标：{{X}}, {{Y}}</text>
5. <text>In path:{{textValue}}</text>
6. <text>In stroke:{{textValue1}}</text>
7. </div>
8. <canvas ref="canvas"></canvas>
9. <button onclick="change">Add(50)</button>
10. </div>
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
9. display: flex;
10. }

12. canvas {
13. width: 600px;
14. height: 500px;
15. background-color: #fdfdfd;
16. border: 5px solid red;
17. }

19. .content {
20. flex-direction: column;
21. justify-content: center;
22. align-items: center;
23. }

25. text {
26. font-size: 30px;
27. width: 300px;
28. height: 80px;
29. text-align: center;
30. }

32. button {
33. width: 180px;
34. height: 75px;
35. margin-top: 50px;
36. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. textValue: 0,
5. textValue1: 0,
6. X: 0,
7. Y: 250,
8. },
9. onShow() {
10. let canvas = this.$refs.canvas.getContext('2d');
11. let offscreen = new OffscreenCanvas(500, 500);
12. let offscreenCanvasCtx = offscreen.getContext('2d');
13. let offscreenCanvasCtx1 = offscreen.getContext('2d');
14. offscreenCanvasCtx1.arc(this.X, this.Y, 2, 0, 6.28);
15. offscreenCanvasCtx.lineWidth = 20;
16. offscreenCanvasCtx.rect(200, 150, 200, 200);
17. offscreenCanvasCtx.stroke();
18. this.textValue1 = offscreenCanvasCtx.isPointInStroke(this.X, this.Y) ? 'true' : 'false';
19. this.textValue = offscreenCanvasCtx.isPointInPath(this.X, this.Y) ? 'true' : 'false';
20. let bitmap = offscreen.transferToImageBitmap();
21. canvas.transferFromImageBitmap(bitmap);
22. },
23. change() {
24. if (this.X < 500) {
25. this.X = this.X + 50;
26. } else {
27. this.X = 0;
28. }
29. let canvas = this.$refs.canvas.getContext('2d');
30. let offscreen = new OffscreenCanvas(500, 500);
31. let offscreenCanvasCtx = offscreen.getContext('2d');
32. let offscreenCanvasCtx1 = offscreen.getContext('2d');
33. offscreenCanvasCtx1.arc(this.X, this.Y, 1, 0, 6.28)
34. offscreenCanvasCtx.lineWidth = 20
35. offscreenCanvasCtx.rect(200, 150, 200, 200);
36. offscreenCanvasCtx.stroke();
37. this.textValue1 = offscreenCanvasCtx.isPointInStroke(this.X, this.Y) ? 'true' : 'false';
38. this.textValue = offscreenCanvasCtx.isPointInPath(this.X, this.Y) ? 'true' : 'false';
39. let bitmap = offscreen.transferToImageBitmap();
40. canvas.transferFromImageBitmap(bitmap);
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4XcILdzbQwu2pRW2lTNITA/zh-cn_image_0000002622698103.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063353Z&HW-CC-Expire=86400&HW-CC-Sign=2B6D46CECE330B52B523B8B1CD33E3C0F324480250B4319EC022E35D7A8F8C0F)
