---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-06-11T15:52:02+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:5a8b089af50f0004088256627c12b927e31ad95d6d019ddbeaaf3e457e0c5ee7
---
说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用CanvasRenderingContext2D在[canvas组件](../canvas组件/js-components-canvas-canvas.md)上进行绘制，绘制对象可以是矩形、文本、图片等。

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="handleClick" onclick="handleClick" />
5. <input type="button" style="width: 180px; height: 60px;" value="antialias" onclick="antialias" />
6. </div>
```

```
1. // xxx.js
2. export default {
3. handleClick() {
4. const el = this.$refs.canvas1;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.arc(100, 75, 50, 0, 6.28);
8. ctx.stroke();
9. },
10. antialias() {
11. const el = this.$refs.canvas1;
12. const ctx = el.getContext('2d', { antialias: true });
13. ctx.beginPath();
14. ctx.arc(100, 75, 50, 0, 6.28);
15. ctx.stroke();
16. }
17. }
```

* 示意图（关闭抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/00Oi9zD_SeOyW696M-8nww/zh-cn_image_0000002622860119.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=BFB9E0FC4E8BA940B006C383F8348D148F183A85FDF2EFA35E7CDBDE01BD2889)
* 示意图（开启抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/b7eUthB0QMeHw0d5VGJR3w/zh-cn_image_0000002622700237.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=4262662486AC2CD307265D80B4C07EC7A5EE3C13E5BCACA49D5FCE6F8815EA10)

## 属性

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| [fillStyle](js-components-canvas-canvasrenderingcontext2d.md#fillstyle) | <color> | [CanvasGradient](../CanvasGradient对象/js-components-canvas-canvasgradient.md) | [CanvasPattern](../../../../ArkTS组件/画布绘制/CanvasPattern/ts-components-canvas-canvaspattern.md) | 指定绘制的填充色。  - 类型为<color>时，表示设置填充区域的颜色。  - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。  - 类型为CanvasPattern时，使用 createPattern()方法创建。  超出取值范围填充为黑色。 |
| [lineWidth](js-components-canvas-canvasrenderingcontext2d.md#linewidth) | number | 设置绘制线条的宽度。 |
| [strokeStyle](js-components-canvas-canvasrenderingcontext2d.md#strokestyle) | <color> | [CanvasGradient](../CanvasGradient对象/js-components-canvas-canvasgradient.md) | [CanvasPattern](../../../../ArkTS组件/画布绘制/CanvasPattern/ts-components-canvas-canvaspattern.md) | 设置描边的颜色。  - 类型为<color>时，表示设置描边使用的颜色。  - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。  - 类型为CanvasPattern时，使用 createPattern()方法创建。 |
| [lineCap](js-components-canvas-canvasrenderingcontext2d.md#linecap) | string | 指定线端点的样式，可选值为：  - butt：线端点以方形结束。  - round：线端点以圆形结束。  - square：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。  默认值：butt |
| [lineJoin](js-components-canvas-canvasrenderingcontext2d.md#linejoin) | string | 指定线段间相交的交点样式，可选值为：  - round：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。  - bevel：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。  - miter：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。  默认值：miter |
| [miterLimit](js-components-canvas-canvasrenderingcontext2d.md#miterlimit) | number | 设置斜接面限制值，该值指定了线条相交处内角和外角的距离。  默认值：10 |
| [font](js-components-canvas-canvasrenderingcontext2d.md#font) | string | 设置文本绘制中的字体样式。  语法：ctx.font="font-style font-weight font-size font-family"5+  - font-style(可选)，用于指定字体样式，支持如下几种样式：normal, italic。  - font-weight(可选)，用于指定字体的粗细，支持如下几种类型：normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900。  - font-size(可选)，指定字号和行高，单位只支持px。  - font-family(可选)，指定字体系列，支持如下几种类型：sans-serif, serif, monospace。  默认值："normal normal 14px sans-serif" |
| [textAlign](js-components-canvas-canvasrenderingcontext2d.md#textalign) | string | 设置文本绘制中的文本对齐方式，可选值为：  - left：文本左对齐。  - right：文本右对齐。  - center：文本居中对齐。  - start：文本对齐界线开始的地方。  - end：文本对齐界线结束的地方。  ltr布局模式下start和left一致，rtl布局模式下start和right一致。  默认值：left |
| [textBaseline](js-components-canvas-canvasrenderingcontext2d.md#textbaseline) | string | 设置文本绘制中的水平对齐方式，可选值为：  - alphabetic：文本基线是标准的字母基线。  - top：文本基线在文本块的顶部。  - hanging：文本基线是悬挂基线。  - middle：文本基线在文本块的中间。  - ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic 基线，那么ideographic基线位置在字符本身的底部。  - bottom：文本基线在文本块的底部。 与 ideographic 基线的区别在于 ideographic 基线不需要考虑下行字母。  默认值： alphabetic |
| [globalAlpha](js-components-canvas-canvasrenderingcontext2d.md#globalalpha) | number | 设置透明度。  范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。 |
| [lineDashOffset](js-components-canvas-canvasrenderingcontext2d.md#linedashoffset) | number | 设置画布的虚线偏移量，精度为float。  默认值：0.0 |
| [globalCompositeOperation](js-components-canvas-canvasrenderingcontext2d.md#globalcompositeoperation) | string | 设置合成操作的方式。类型字段可选值有source-over，source-atop，source-in，source-out，destination-over，destination-atop，destination-in，destination-out，lighter，copy，xor。具体请参考[类型字段说明](js-components-canvas-canvasrenderingcontext2d.md#globalcompositeoperation)。  默认值：source-over |
| [shadowBlur](js-components-canvas-canvasrenderingcontext2d.md#shadowblur) | number | 设置绘制阴影时的模糊级别，值越大越模糊，精度为float。  默认值：0.0 |
| [shadowColor](js-components-canvas-canvasrenderingcontext2d.md#shadowcolor) | <color> | 设置绘制阴影时的阴影颜色。 |
| [shadowOffsetX](js-components-canvas-canvasrenderingcontext2d.md#shadowoffsetx) | number | 设置绘制阴影时和原有对象的水平偏移值。 |
| [shadowOffsetY](js-components-canvas-canvasrenderingcontext2d.md#shadowoffsety) | number | 设置绘制阴影时和原有对象的垂直偏移值。 |
| [imageSmoothingEnabled](js-components-canvas-canvasrenderingcontext2d.md#imagesmoothingenabled) | boolean | 用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。  默认值：true |

### fillStyle

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = '#0000ff';
7. ctx.fillRect(20, 20, 150, 100);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jQUHLtWVSh-jIQQgk4ETPA/zh-cn_image_0000002592220678.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=C5C99CF4FD238F3D8E7BA00DCDE5AB41F8739D74416D4B94E1C2144386DC24C8)

### lineWidth

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth = 5;
7. ctx.strokeRect(25, 25, 85, 105);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/uvrR96lsSDmJn3-dspcv2Q/zh-cn_image_0000002592380610.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=930A7D8A710FD1CDCA7C826FBD54B079A282C1B5A42155D4E48C0FF88F0F4616)

### strokeStyle

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth = 10;
7. ctx.strokeStyle = '#0000ff';
8. ctx.strokeRect(25, 25, 155, 105);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/TalVf9RBQD6UgzcJSv6LAA/zh-cn_image_0000002622860121.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=06F94228F7992A2592D397FBDBEEBF8505C778F9C1D85623C8062509428FA930)

### lineCap

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth = 8;
7. ctx.beginPath();
8. ctx.lineCap = 'round';
9. ctx.moveTo(30, 50);
10. ctx.lineTo(220, 50);
11. ctx.stroke();
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/YjUvjYdZR_-kdGp_Eyq04g/zh-cn_image_0000002622700239.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=B4F16679990F93B05C003B8EDAB26964A4466E3504462E215C37E438D2944C78)

### lineJoin

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.lineWidth = 8;
8. ctx.lineJoin = 'miter';
9. ctx.moveTo(30, 30);
10. ctx.lineTo(120, 60);
11. ctx.lineTo(30, 110);
12. ctx.stroke();
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/PeEUmB5HS_OQy-Sm4-7eEg/zh-cn_image_0000002592220680.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=8BDA1CB2ACA9106F342E146D33ACB11DF355890402FF6660EFB2BB341B6A0C30)

### miterLimit

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth =14;
7. ctx.lineJoin = 'miter';
8. ctx.miterLimit = 3;
9. ctx.moveTo(30, 30);
10. ctx.lineTo(120, 60);
11. ctx.lineTo(30, 70);
12. ctx.stroke();
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/6oO6II0tSX6Jr5yXHd6qYg/zh-cn_image_0000002592380612.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=EBB073C15C3BA4A1B2BBEB52BD342EDFCD8E80277522014182378EA6447FEFA4)

### font

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '30px sans-serif';
7. ctx.fillText("Hello World", 20, 60);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/VbJb_l2sRIyiL7WtVeUPEA/zh-cn_image_0000002622860123.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=CE5FE72ADBE9B37A11EBE81F391882AE3F3BEDE1E95D64D876487C7F91E1154F)

### textAlign

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeStyle = '#0000ff';
7. ctx.moveTo(140, 10);
8. ctx.lineTo(140, 160);
9. ctx.stroke();
10. ctx.font = '18px sans-serif';
11. // Show the different textAlign values
12. ctx.textAlign = 'start';
13. ctx.fillText('textAlign=start', 140, 60);
14. ctx.textAlign = 'end';
15. ctx.fillText('textAlign=end', 140, 80);
16. ctx.textAlign = 'left';
17. ctx.fillText('textAlign=left', 140, 100);
18. ctx.textAlign = 'center';
19. ctx.fillText('textAlign=center',140, 120);
20. ctx.textAlign = 'right';
21. ctx.fillText('textAlign=right',140, 140);
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/D-sAfBGNT8SNT74hKfP3Ww/zh-cn_image_0000002622700241.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=A428681F68B2BAFA3CCE45E65D06D4E102BA9EF84D9DF57E4395A59322355224)

### textBaseline

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeStyle = '#0000ff';
7. ctx.moveTo(0, 120);
8. ctx.lineTo(400, 120);
9. ctx.stroke();
10. ctx.font = '20px sans-serif';
11. ctx.textBaseline = 'top';
12. ctx.fillText('Top', 10, 120);
13. ctx.textBaseline = 'bottom';
14. ctx.fillText('Bottom', 55, 120);
15. ctx.textBaseline = 'middle';
16. ctx.fillText('Middle', 125, 120);
17. ctx.textBaseline = 'alphabetic';
18. ctx.fillText('Alphabetic', 195, 120);
19. ctx.textBaseline = 'hanging';
20. ctx.fillText('Hanging', 295, 120);
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ybu5QjiTTZaDigTWAYVWAQ/zh-cn_image_0000002592220682.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=57082600AA39212FC175A02003BECF27A6EEF0755B04DF7580634F00152F409D)

### globalAlpha

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(255,0,0)';
7. ctx.fillRect(0, 0, 50, 50);
8. ctx.globalAlpha = 0.4;
9. ctx.fillStyle = 'rgb(0,0,255)';
10. ctx.fillRect(50, 50, 50, 50);

12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/9kAg0oIySA6NuyuL3F5npA/zh-cn_image_0000002592380614.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=F25540EB0EFFF7B6F055A30E01CCE9D52CE522BE3CDD7D85C625564C4417A595)

### lineDashOffset

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.arc(100, 75, 50, 0, 6.28);
7. ctx.setLineDash([10,20]);
8. ctx.lineDashOffset = 10.0;
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/zq1_D_kNQ86m7u_7dUWBtA/zh-cn_image_0000002622860125.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=E709D2D73B69BD247635D076E5A1FA4D258881E1A0DCE2E9F405EC195B4E7A5E)

### globalCompositeOperation

PhonePC/2in1TabletTVWearable

类型字段说明。

| 值 | 描述 |
| --- | --- |
| source-over | 在现有绘制内容上显示新绘制内容，属于默认值。 |
| source-atop | 在现有绘制内容顶部显示新绘制内容。 |
| source-in | 在现有绘制内容中显示新绘制内容。 |
| source-out | 在现有绘制内容之外显示新绘制内容。 |
| destination-over | 在新绘制内容上方显示现有绘制内容。 |
| destination-atop | 在新绘制内容顶部显示现有绘制内容。 |
| destination-in | 在新绘制内容中显示现有绘制内容。 |
| destination-out | 在新绘制内容外显示现有绘制内容。 |
| lighter | 显示新绘制内容和现有绘制内容。 |
| copy | 显示新绘制内容而忽略现有绘制内容。 |
| xor | 使用异或操作对新绘制内容与现有绘制内容进行融合。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(255,0,0)';
7. ctx.fillRect(20, 20, 50, 50);
8. ctx.globalCompositeOperation = 'source-over';
9. ctx.fillStyle = 'rgb(0,0,255)';
10. ctx.fillRect(50, 50, 50, 50);
11. // Start drawing second example
12. ctx.fillStyle = 'rgb(255,0,0)';
13. ctx.fillRect(120, 20, 50, 50);
14. ctx.globalCompositeOperation = 'destination-over';
15. ctx.fillStyle = 'rgb(0,0,255)';
16. ctx.fillRect(150, 50, 50, 50);
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/iki357YbTxeVR8I-4XixLQ/zh-cn_image_0000002622700243.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=6FAB6B1F1B5E5B6B5E9FB9BAA99302763F33A00CCD8BFBF348C9ECE7788CEA00)

示例中，新绘制内容是蓝色矩形，现有绘制内容是红色矩形。

### shadowBlur

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 30;
7. ctx.shadowColor = 'rgb(0,0,0)';
8. ctx.fillStyle = 'rgb(255,0,0)';
9. ctx.fillRect(20, 20, 100, 80);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/SChpco9WT_KmbydBFJR7EQ/zh-cn_image_0000002592220684.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=38685D5C736A139FBCA056171B0D39A66B8191EC01213557FDDC59E1A9BA30AC)

### shadowColor

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 30;
7. ctx.shadowColor = 'rgb(0,0,255)';
8. ctx.fillStyle = 'rgb(255,0,0)';
9. ctx.fillRect(30, 30, 100, 100);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pyn57fK5TWKyuRjue959ng/zh-cn_image_0000002592380616.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=E9FFE7A671C20D2A563A43283763CEC5DD858EF9C7F779CD0EABB8274E887631)

### shadowOffsetX

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 10;
7. ctx.shadowOffsetX = 20;
8. ctx.shadowColor = 'rgb(0,0,0)';
9. ctx.fillStyle = 'rgb(255,0,0)';
10. ctx.fillRect(20, 20, 100, 80);
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/I7IxsALKTRKvM0VIIH_LNg/zh-cn_image_0000002622860127.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=B46468A4CE415FA31A58153714E6EBC58706D77FB3E6E22C5E7E0313257CDE2F)

### shadowOffsetY

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 10;
7. ctx.shadowOffsetY = 20;
8. ctx.shadowColor = 'rgb(0,0,0)';
9. ctx.fillStyle = 'rgb(255,0,0)';
10. ctx.fillRect(30, 30, 100, 100);
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/69PoN0WpQWKtokwoE2WfHw/zh-cn_image_0000002622700245.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=3E0C75E25456B4276FC80350DC5ABB9D0B9C8B68E2CE581E7BFBE7445BCAB07A)

### imageSmoothingEnabled

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var img = new Image();
7. // 'common/image/example.jpg'需要替换为开发者所需的图像资源文件
8. img.src = 'common/image/example.jpg';
9. img.onload = function() {
10. ctx.imageSmoothingEnabled = false;
11. ctx.drawImage(img, 0, 0, 400, 200);
12. };
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jOLvtt7eSL2eICmvYDENDw/zh-cn_image_0000002592220686.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=6F5FE4B500F218F5350E8DC3D53B98E3B0968E3802C9EFA93F630F8DDD8F49C1)

## 方法

PhonePC/2in1TabletTVWearable

### fillRect

PhonePC/2in1TabletTVWearable

fillRect(x: number, y: number, width:number, height: number): void

填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形左上角点的x坐标。  单位：vp |
| y | number | 是 | 指定矩形左上角点的y坐标。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillRect(20, 20, 200, 150);
7. }
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/DDG2eN4ETj2qP38btURj0A/zh-cn_image_0000002592380618.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=6167211A2D231398F5CB9E6DDFC67360A29BB74B571A7D187238C8C870474819)

### clearRect

PhonePC/2in1TabletTVWearable

clearRect(x: number, y: number, width:number, height: number): void

删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形上的左上角x坐标。  单位：vp |
| y | number | 是 | 指定矩形上的左上角y坐标。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(0,0,255)';
7. ctx.fillRect(100, 100, 200, 200);
8. ctx.clearRect(110, 110, 80, 50);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/kBa_B4bzQEil2YwDguA5zQ/zh-cn_image_0000002622860129.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=8A93078F69B1A03F7DB85C1E68B85ECD9B1D54E2E4AC9ED4462D63916E7D3B6C)

### strokeRect

PhonePC/2in1TabletTVWearable

strokeRect(x: number, y: number, width:number, height: number): void

绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标。  单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeRect(100, 100, 200, 150);
7. }
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/NdiBSkLXQXCrQEM__Bo8SA/zh-cn_image_0000002622700247.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=86DD986060F78B4C70562339B66E5DFC35A768FD0B3F02B6158646B3808921D3)

### fillText

PhonePC/2in1TabletTVWearable

fillText(text: string, x: number, y: number): void

绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 需要绘制的文本的左下角x坐标。  单位：vp |
| y | number | 是 | 需要绘制的文本的左下角y坐标。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '35px sans-serif';
7. ctx.fillText("Hello World!", 10, 60);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Li-s4hPRQhq8ZIt2HEPb7A/zh-cn_image_0000002592220688.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=4D43190C0A8B6242086C1970D59A13064AD14BA529E63EF71B151C9CECF1612E)

### strokeText

PhonePC/2in1TabletTVWearable

strokeText(text: string, x: number, y: number): void

绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 需要绘制的文本的左下角x坐标。  单位：vp |
| y | number | 是 | 需要绘制的文本的左下角y坐标。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '25px sans-serif';
7. ctx.strokeText("Hello World!", 10, 60);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Bcmui-JNQg6iQmJkbJoViw/zh-cn_image_0000002592380620.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=65A247F05F90576177C9330A1AFEEC382D35AD7B47EB0E314B1CF9181CDBB1C5)

### measureText

PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TextMetrics | 包含指定字体的宽度，该宽度可以通过TextMetrics.width来获取。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '20px sans-serif';
7. var txt = 'Hello World';
8. ctx.fillText("width:" + ctx.measureText(txt).width, 20, 60);
9. ctx.fillText(txt, 20, 110);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/rDR5aoadSee7LAptY3y82Q/zh-cn_image_0000002622860131.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=E9125E9F4A44911C541141D998BA7B7FDB4D99F5C87AA7C96FB5DC3B5EDA84E9)

### stroke

PhonePC/2in1TabletTVWearable

stroke(): void

进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.moveTo(25, 25);
7. ctx.lineTo(25, 250);
8. ctx.lineWidth = '6';
9. ctx.strokeStyle = 'rgb(0,0,255)';
10. ctx.stroke();
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/9RbOHiN_Rh6r0N5l81FqBA/zh-cn_image_0000002622700249.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=44D7C71C98CD8E3C4781E759BAC212D6E3DEDE1B12D34CD68C78972EE07A302D)

### beginPath

PhonePC/2in1TabletTVWearable

beginPath(): void

创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.lineWidth = '6';
8. ctx.strokeStyle = '#0000ff';
9. ctx.moveTo(15, 80);
10. ctx.lineTo(280, 80);
11. ctx.stroke();
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/aZZTQZ0xSICtdyTI4Cc-Iw/zh-cn_image_0000002592220690.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=1B09B7AFEA10F5BDA4C3F90EF53E587AB0C5BBC6D6FE6682A2E8A310D48515EC)

### moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  单位：vp |
| y | number | 是 | 指定位置的y坐标。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(10, 10);
8. ctx.lineTo(280, 160);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ho9qU1FoQxqXNEl0D180Ig/zh-cn_image_0000002592380622.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=259F560F3EBB275CFC0E0A5BFC6DD12BA2A5ECB1A20EF36B80D2F9AFE302853B)

### lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  单位：vp |
| y | number | 是 | 指定位置的y坐标。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(10, 10);
8. ctx.lineTo(280, 160);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/fo8CCGCCSjabCXMNA7pgMA/zh-cn_image_0000002622860133.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=C3F2AC8899824D3F3ABE7719200DB821BBBB90BA0934871F39953B8DC2D359C0)

### closePath

PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(30, 30);
8. ctx.lineTo(110, 30);
9. ctx.lineTo(70, 90);
10. ctx.closePath();
11. ctx.stroke();
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/YGJY3BciRrq7Is9FDOJc3w/zh-cn_image_0000002622700251.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=826CF17E8D964D7FFE560D6D0D1054DA8A49E4B1818E2338F37BB0A46A59E7A1)

### createPattern

PhonePC/2in1TabletTVWearable

createPattern(image: Image, repetition: string): Object

通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | 是 | 图源对象，具体参考[Image对象](../Image对象/js-components-canvas-image.md)。 |
| repetition | string | 是 | 设置图像重复的方式，取值为：'repeat'、'repeat-x'、 'repeat-y'、'no-repeat'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 指定图像填充的Pattern对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 1000px; height: 1000px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var img = new Image();
7. // 'common/images/example.jpg'需要替换为开发者所需的图像资源文件
8. img.src = 'common/images/example.jpg';
9. var pat = ctx.createPattern(img, 'repeat');
10. ctx.fillStyle = pat;
11. ctx.fillRect(0, 0, 500, 500);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/fGmV3nnkQ8-Sk-bU97vMNg/zh-cn_image_0000002592220692.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=398289405A53F019C3B99B0474E7D367E29C6EBF9017C567008FABBD9DD0475B)

### bezierCurveTo

PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。  单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。  单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。  单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。  单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(10, 10);
8. ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/slcvslDCSHWQQAmLBgg2Lg/zh-cn_image_0000002592380624.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=836C4BA92171BF6278DCC98128052D9F28C7677B49B3D018EEBC89B9F5D04E05)

### quadraticCurveTo

PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。  单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。  单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(20, 20);
8. ctx.quadraticCurveTo(100, 100, 200, 20);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/lUBBDAUZQwuIveHmPL0FUw/zh-cn_image_0000002622860135.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=70F4E8EC5CAADD2D47FDA993B838FE68197BD9E51963B6620EA9DFE4DE373C07)

### arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。  单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。  单位：vp |
| radius | number | 是 | 弧线的圆半径。  单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。  单位：vp |
| endAngle | number | 是 | 弧线的终止弧度。  单位：vp |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。  默认值：false |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.arc(100, 75, 50, 0, 6.28);
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/kFbNWZoxQUG1mE7MPTE_Sw/zh-cn_image_0000002622700253.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=31BA62ACBDADC96627A8E75DCFD096324E24A91CA3EB37D83C6C1D64B961D592)

### arcTo

PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 圆弧经过的第一个点的x坐标值。  单位：vp |
| y1 | number | 是 | 圆弧经过的第一个点的y坐标值。  单位：vp |
| x2 | number | 是 | 圆弧经过的第二个点的x坐标值。  单位：vp |
| y2 | number | 是 | 圆弧经过的第二个点的y坐标值。  单位：vp |
| radius | number | 是 | 圆弧的圆半径值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.moveTo(100, 20);
7. ctx.arcTo(150, 20, 150, 70, 50); // Create an arc
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/7HrpW7z8R3iJs9D1u3oVkA/zh-cn_image_0000002592220694.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=6427FB00260F23306F51786BBEEB3893D499C5333A2E5E8817470C792237F79D)

### ellipse

PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。  单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。  单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。  单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。  单位：vp |
| rotation | number | 是 | 椭圆的旋转角度，单位为弧度。  单位：vp |
| startAngle | number | 是 | 椭圆绘制的起始点角度，以弧度表示。  单位：vp |
| endAngle | number | 是 | 椭圆绘制的结束点角度，以弧度表示。  单位：vp |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。  单位：vp  默认值：0 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/iEk-9Dl4TGCKemgHMPuM-w/zh-cn_image_0000002592380626.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=100DE37439C48D86A40F3C0017B3B05D075FF2F00C603DEBCE167EE69A4412EB)

### rect

PhonePC/2in1TabletTVWearable

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
7. ctx.stroke(); // Draw it
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/UHT4XUk7TBWWMlemmDquEQ/zh-cn_image_0000002622860137.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=3E22A4B3569F40DAC07A444B4205E4DD1EE5FA4E5B6C1738E4C7536FF2078B41)

### fill

PhonePC/2in1TabletTVWearable

fill(): void

对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
7. ctx.fill(); // Draw it in default setting
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/48kvVNWQROSZW3QzeY-97A/zh-cn_image_0000002622700255.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=62CADF07404240E59BB1FF5ECBCFC351CB8F65DE21F5408CF62C0F635C790D18)

### clip

PhonePC/2in1TabletTVWearable

clip(): void

设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rect(100, 100, 200, 200);
7. ctx.stroke();
8. ctx.clip();
9. // Draw red rectangle after clip
10. ctx.fillStyle = "rgb(255,0,0)";
11. ctx.fillRect(100, 100, 150, 150);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/YXoZlNKLSSy4L8Jjde84eA/zh-cn_image_0000002592220696.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=E642F8D407942D974629583BBB43B6BAA84D0CDE94E423FE0C54051C100222AC)

### rotate

PhonePC/2in1TabletTVWearable

rotate(rotate: number): void

针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotate | number | 是 | 设置顺时针旋转的弧度值，可以通过Math.PI / 180将角度转换为弧度值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rotate(45 * Math.PI / 180); // Rotate the rectangle 45 degrees
7. ctx.fillRect(70, 20, 50, 50);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/dMqOZJMJQZuVzik38ilHKQ/zh-cn_image_0000002592380628.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=4898AFDA820701142984CA1196842C8A47798D630256F1C2DE024207A1D5F5A8)

### scale

PhonePC/2in1TabletTVWearable

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。  单位：vp |
| y | number | 是 | 设置垂直方向的缩放值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeRect(10, 10, 25, 25);
7. ctx.scale(2, 2);// Scale to 200%
8. ctx.strokeRect(10, 10, 25, 25);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/a7pqgLDRQCirbr35EV7hqA/zh-cn_image_0000002622860139.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=1A3CA0815313C055CB47FD74F1714B70CF2B5EC33B74B07DC13B5848660352FA)

### transform

PhonePC/2in1TabletTVWearable

transform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

说明

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = scaleX \* x + skewY \* y + translateX
* y' = skewX \* x + scaleY \* y + translateY

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。  单位：vp |
| skewX | number | 是 | 指定水平倾斜值。  单位：vp |
| skewY | number | 是 | 指定垂直倾斜值。  单位：vp |
| scaleY | number | 是 | 指定垂直缩放值。  单位：vp |
| translateX | number | 是 | 指定水平移动值。  单位：vp |
| translateY | number | 是 | 指定垂直移动值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(0,0,0)';
7. ctx.fillRect(0, 0, 100, 100);
8. ctx.transform(1, 0.5, -0.5, 1, 10, 10);
9. ctx.fillStyle = 'rgb(255,0,0)';
10. ctx.fillRect(0, 0, 100, 100);
11. ctx.transform(1, 0.5, -0.5, 1, 10, 10);
12. ctx.fillStyle = 'rgb(0,0,255)';
13. ctx.fillRect(0, 0, 100, 100);
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/YjBVP6EzRMm0TgYyiRWFrA/zh-cn_image_0000002622700257.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=3DDC140907FF5FBECA5D45F9F733AAF35B0CBB83E008AF5BB566D8850C5726B5)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。  单位：vp |
| skewX | number | 是 | 指定水平倾斜值。  单位：vp |
| skewY | number | 是 | 指定垂直倾斜值。  单位：vp |
| scaleY | number | 是 | 指定垂直缩放值。  单位：vp |
| translateX | number | 是 | 指定水平移动值。  单位：vp |
| translateY | number | 是 | 指定垂直移动值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(255,0,0)';
7. ctx.fillRect(0, 0, 100, 100);
8. ctx.setTransform(1,0.5, -0.5, 1, 10, 10);
9. ctx.fillStyle = 'rgb(0,0,255)';
10. ctx.fillRect(0, 0, 100, 100);
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/n6JbTeQYSuiURxtwIXc4UA/zh-cn_image_0000002592220698.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=A23FA72CC0042CE621EAA71670756E77AEB9FD00F6E03E1C814ED11A27E8DFAB)

### translate

PhonePC/2in1TabletTVWearable

translate(x: number, y: number): void

移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。  单位：vp |
| y | number | 是 | 设置竖直平移量。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillRect(10, 10, 50, 50);
7. ctx.translate(70, 70);
8. ctx.fillRect(10, 10, 50, 50);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/L4jgE2VoQl-a0Yk1qh_tfQ/zh-cn_image_0000002592380630.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=FD7E3041A8CA0279386B235EA6CB2FB44C061FD68021A095DC6B9333F5038C0D)

### createPath2D6+

PhonePC/2in1TabletTVWearable

createPath2D(path: Path2D, cmds: string): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | Path2D对象。 |
| cmds | string | 是 | SVG的Path描述字符串。 |

**返回值：**

[Path2D对象](../Path2D对象/js-components-canvas-path2d.md)

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path1 = ctx.createPath2D();
7. path1.moveTo(100, 100);
8. path1.lineTo(200, 100);
9. path1.lineTo(100, 200);
10. path1.closePath();
11. ctx.stroke(path1);
12. var path2 = ctx.createPath2D("M150 150 L50 250 L250 250 Z");
13. ctx.stroke(path2);
14. var path3 = ctx.createPath2D(path2);
15. ctx.stroke(path3);
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/uTCFqzfGSTGLTetS1E-ukQ/zh-cn_image_0000002622860141.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=A753925AD2C367758069FAEB1D266D0987A72EA861FF39016EFD9F4BA7FF6002)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: Image | PixelMap, sx: number, sy: number, sWidth: number, sHeight: number, dx: number, dy: number, dWidth: number, dHeight: number):void

进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | PixelMap9+ | 是 | 图片资源，请参考[Image对象](../Image对象/js-components-canvas-image.md) 或[PixelMap](<../../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)对象。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。  单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。  单位：vp |
| sWidth | number | 是 | 裁切源图像时需要裁切的宽度。  单位：vp |
| sHeight | number | 是 | 裁切源图像时需要裁切的高度。  单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  单位：vp |
| dy | number | 是 | 绘制区域左上角在y 轴的位置。  单位：vp |
| dWidth | number | 是 | 绘制区域的宽度。  单位：vp |
| dHeight | number | 是 | 绘制区域的高度。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. var test = this.$refs.canvas;
5. var ctx = test.getContext('2d');
6. var img = new Image();
7. // 'common/image/test.jpg'需要替换为开发者所需的图像资源文件
8. img.src = 'common/image/test.jpg';
9. ctx.drawImage(img, 0, 0, 200, 200, 10, 10, 200, 200);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/4deZhGktRBGhDqaH23o6tA/zh-cn_image_0000002622700259.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=F6D24ADB29C3044DEBB3B7F51E9C2494B5E125F94D1C8AFD653CD66A28823FC6)

### restore

PhonePC/2in1TabletTVWearable

restore(): void

对保存的绘图上下文进行恢复。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.restore();
7. }
8. }
```

### save

PhonePC/2in1TabletTVWearable

save(): void

对当前的绘图上下文进行保存。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.save();
7. }
8. }
```

### createLinearGradient6+

PhonePC/2in1TabletTVWearable

createLinearGradient(x0: number, y0: number, x1: number, y1: number): Object

创建一个线性渐变色，返回CanvasGradient对象，请参考[CanvasGradient对象](../CanvasGradient对象/js-components-canvas-canvasgradient.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起点的x轴坐标。  单位：vp |
| y0 | number | 是 | 起点的y轴坐标。  单位：vp |
| x1 | number | 是 | 终点的x轴坐标。  单位：vp |
| y1 | number | 是 | 终点的y轴坐标。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
5. </div>
```

```
1. // xxx.js
2. export default {
3. handleClick() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. // Linear gradient: start(50,0) end(300,100)
7. var gradient = ctx.createLinearGradient(50,0, 300,100);
8. // Add three color stops
9. gradient.addColorStop(0.0, '#ff0000');
10. gradient.addColorStop(0.5, '#ffffff');
11. gradient.addColorStop(1.0, '#00ff00');
12. // Set the fill style and draw a rectangle
13. ctx.fillStyle = gradient;
14. ctx.fillRect(0, 0, 500, 500);
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/-KssPiqqTteLOQdxrDkVIQ/zh-cn_image_0000002592220700.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=B607843D0DB79B6002E01E36BEA9F8B90E5A4C663F93BCE0697484CB3B18824A)

### createRadialGradient6+

PhonePC/2in1TabletTVWearable

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): Object

创建一个径向渐变色，返回CanvasGradient对象，请参考CanvasGradient。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起始圆的x轴坐标。  单位：vp |
| y0 | number | 是 | 起始圆的y轴坐标。  单位：vp |
| r0 | number | 是 | 起始圆的半径。必须是非负且有限的。  单位：vp |
| x1 | number | 是 | 终点圆的x轴坐标。  单位：vp |
| y1 | number | 是 | 终点圆的y轴坐标。  单位：vp |
| r1 | number | 是 | 终点圆的半径。必须为非负且有限的。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
5. </div>
```

```
1. // xxx.js
2. export default {
3. handleClick() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. // Radial gradient: inner circle(200,200,r:50) outer circle(200,200,r:200)
7. var gradient = ctx.createRadialGradient(200,200,50, 200,200,200);
8. // Add three color stops
9. gradient.addColorStop(0.0, '#ff0000');
10. gradient.addColorStop(0.5, '#ffffff');
11. gradient.addColorStop(1.0, '#00ff00');
12. // Set the fill style and draw a rectangle
13. ctx.fillStyle = gradient;
14. ctx.fillRect(0, 0, 500, 500);
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/jFyRMzq3SGikIbJoW6cbLw/zh-cn_image_0000002592380632.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=E0642C579A59451737F0E99229FC7A7351678B2592C4456C1E3DAC1284C03320)

### createImageData

PhonePC/2in1TabletTVWearable

createImageData(width: number, height: number): ImageData

创建新的、空白的、指定大小的ImageData对象，请参考[ImageData对象](../ImageData对象/js-components-canvas-imagedata.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | ImageData的宽度。  单位：vp |
| height | number | 是 | ImageData的高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](../ImageData对象/js-components-canvas-imagedata.md) | 返回创建的ImageData对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
7. }
8. }
```

### createImageData

PhonePC/2in1TabletTVWearable

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象，重新创建一个宽、高相同但不会复制图像数据的ImageData对象，请参考[ImageData对象](../ImageData对象/js-components-canvas-imagedata.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](../ImageData对象/js-components-canvas-imagedata.md) | 是 | 复制现有的ImageData对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](../ImageData对象/js-components-canvas-imagedata.md) | 返回创建的ImageData对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
7. var newImageData = ctx.createImageData(imageData);  // Create ImageData using the input imageData
8. }
9. }
```

### getImageData

PhonePC/2in1TabletTVWearable

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData对象](../ImageData对象/js-components-canvas-imagedata.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。  单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。  单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。  单位：vp |
| sh | number | 是 | 需要输出的区域的高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](../ImageData对象/js-components-canvas-imagedata.md) | 返回包含指定区域像素的ImageData对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="getImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('getImageData')
5. const ctx = test.getContext('2d');
6. var imageData = ctx.getImageData(0, 0, 280, 300);
7. }
8. }
```

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void

使用ImageData数据裁剪后填充至新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](../ImageData对象/js-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 填充区域在x轴方向的偏移量。  单位：vp |
| dy | number | 是 | 填充区域在y轴方向的偏移量。  单位：vp |
| dirtyX | number | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。  单位：vp |
| dirtyY | number | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。  单位：vp |
| dirtyWidth | number | 是 | 源图像数据矩形裁切范围的宽度。  单位：vp |
| dirtyHeight | number | 是 | 源图像数据矩形裁切范围的高度。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #D5D5D5;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('putImageData')
5. const ctx = test.getContext('2d');
6. var imgData = ctx.createImageData(100, 100);
7. for (var i = 0; i < imgData.data.length; i += 4) {
8. imgData.data[i + 0] = 39;
9. imgData.data[i + 1] = 135;
10. imgData.data[i + 2] = 217;
11. imgData.data[i + 3] = 255;
12. }
13. ctx.putImageData(imgData, 10, 10, 0, 0, 100, 50);
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/wusLFdZcT-q9iVw9aIhk-A/zh-cn_image_0000002622860143.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=524A92560FD8B54D074C59BD9BED37F5E384363863CECD959C011AD5BA9F7FA1)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number, dy: number): void

使用ImageData数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](../ImageData对象/js-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 填充区域在x轴方向的偏移量。  单位：vp |
| dy | number | 是 | 填充区域在y轴方向的偏移量。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('putImageData')
5. const ctx = test.getContext('2d');
6. var imgData = ctx.createImageData(100, 100);
7. for (var i = 0; i < imgData.data.length; i += 4) {
8. imgData.data[i + 0] = 255;
9. imgData.data[i + 1] = 0;
10. imgData.data[i + 2] = 0;
11. imgData.data[i + 3] = 255;
12. }
13. ctx.putImageData(imgData, 10, 10);
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/d8fuYNkYRY6OjjfdRbpDsQ/zh-cn_image_0000002622700261.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=62F4669513C398F968A7C4466E8056D0C715003B5E0861474F2138B0A0843B70)

### getPixelMap9+

PhonePC/2in1TabletTVWearable

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

获取用当前canvas指定区域内的像素创建的PixelMap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 指定区域的左上角x坐标。  单位：vp |
| sy | number | 是 | 指定区域的左上角y坐标。  单位：vp |
| sw | number | 是 | 指定区域的宽度。  单位：vp |
| sh | number | 是 | 指定区域的高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](<../../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 返回包含指定区域像素的PixelMap对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('canvasId')
5. const ctx = test.getContext('2d');
6. var pixelMap = ctx.getPixelMap(0, 0, 280, 300);
7. }
8. }
```

### setLineDash

PhonePC/2in1TabletTVWearable

setLineDash(segments: Array): void

设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | Array | 是 | 作为数组用来描述线段如何交替和间距长度。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.arc(100, 75, 50, 0, 6.28);
7. ctx.setLineDash([10,20]);
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/gUbvHMsYQLyBDeZJFYMRvw/zh-cn_image_0000002592220702.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=9C7D945D6FC55605DBFE57F8553C30B2F866BE55A6D022394CCC7F49E92BCBD5)

### getLineDash

PhonePC/2in1TabletTVWearable

getLineDash(): Array

获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array | 返回数组，该数组用来描述线段如何交替和间距长度。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var info = ctx.getLineDash();
7. }
8. }
```

### transferFromImageBitmap7+

PhonePC/2in1TabletTVWearable

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的[ImageBitmap对象](../ImageBitmap对象/js-components-canvas-imagebitmap.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitmap | [ImageBitmap](../ImageBitmap对象/js-components-canvas-imagebitmap.md) | 是 | 待显示的ImageBitmap对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var canvas = this.$refs.canvas.getContext('2d');
7. var offscreen = new OffscreenCanvas(500,500);
8. var offscreenCanvasCtx = offscreen.getContext("2d");
9. offscreenCanvasCtx.fillRect(0, 0, 200, 200);

11. var bitmap = offscreen.transferToImageBitmap();
12. canvas.transferFromImageBitmap(bitmap);
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/4ZEFv5WyTWitxLo5adjzcA/zh-cn_image_0000002592380634.png?HW-CC-KV=V1&HW-CC-Date=20260611T075159Z&HW-CC-Expire=86400&HW-CC-Sign=A7EACF3330810532930E0F09CCCD6D04FD290775543DC662F3737D3DA13035EE)
