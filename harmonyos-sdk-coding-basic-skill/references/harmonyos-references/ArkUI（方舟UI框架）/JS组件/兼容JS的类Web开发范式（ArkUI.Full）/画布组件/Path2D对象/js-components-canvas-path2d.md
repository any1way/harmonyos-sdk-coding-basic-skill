---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d
title: Path2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > Path2D对象
category: harmonyos-references
scraped_at: 2026-06-11T15:52:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1421165fd7a39d23589b6886f8f027625b2bc9b2f0db38b64872ea17655b89f7
---
路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的[stroke](../CanvasRenderingContext2D对象/js-components-canvas-canvasrenderingcontext2d.md#stroke)接口进行绘制。

说明

本模块首批接口从API version 4开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## addPath

PhonePC/2in1TabletTVWearable

addPath(path: Object): void

将另一个路径添加到当前的路径对象中。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| path | Object | 需要添加到当前路径的路径对象。 |

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
6. var path1 = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
7. var path2 = ctx.createPath2D();
8. path2.addPath(path1);
9. ctx.stroke(path2);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/SYDz3X0ETo6CvWa6_Sr0lQ/zh-cn_image_0000002592220704.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=7BBEDB1ADA510C86AFEAF83A8D6F9961717284DF7079719D78544C4A7593A87B)

## setTransform

PhonePC/2in1TabletTVWearable

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

设置路径变换矩阵。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| scaleX | number | x轴的缩放比例。 |
| skewX | number | x轴的倾斜角度。 |
| skewY | number | y轴的倾斜角度。 |
| scaleY | number | y轴的缩放比例。 |
| translateX | number | x轴的平移距离。 |
| translateY | number | y轴的平移距离。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
7. path.setTransform(0.8, 0, 0, 0.4, 0, 0);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/v8UPn0rmT6iBwEMSDtg1Lg/zh-cn_image_0000002592380636.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=C35BD33165C913F155986AE776EAC008B1EBCED733E6C717D7824E14E57CBD6E)

## closePath

PhonePC/2in1TabletTVWearable

closePath(): void

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

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
6. var path = ctx.createPath2D();
7. path.moveTo(200, 100);
8. path.lineTo(300, 100);
9. path.lineTo(200, 200);
10. path.closePath();
11. ctx.stroke(path);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/dXUHbjQbQraJTp1u9G5yoQ/zh-cn_image_0000002622860147.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=C1C10AA22C2CD73DA00CE3646C737EBD17057B04293412F4B5B831A990E83997)

## moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(50, 100);
8. path.lineTo(250, 100);
9. path.lineTo(150, 200);
10. path.closePath();
11. ctx.stroke(path);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/tTkZdBf6QJKvMHRiiSrnDg/zh-cn_image_0000002622700265.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=1E908754F3EF517116CD8362CD3A4EE76F7E0A807DCC48AC035FECA36526827D)

## lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点绘制一条直线到目标点。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 400px; height: 450px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(100, 100);
8. path.lineTo(100, 200);
9. path.lineTo(200, 200);
10. path.lineTo(200, 100);
11. path.closePath();
12. ctx.stroke(path);
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/8XfV0s1iSI-5Fe7R6_xjxQ/zh-cn_image_0000002592220706.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=63DF777985BD95A0E99468B6C6AEF8B57F3EC1A13A62954CDC8FBE374D8DF84D)

## bezierCurveTo

PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cp1x | number | 第一个贝塞尔参数的x坐标值。 |
| cp1y | number | 第一个贝塞尔参数的y坐标值。 |
| cp2x | number | 第二个贝塞尔参数的x坐标值。 |
| cp2y | number | 第二个贝塞尔参数的y坐标值。 |
| x | number | 路径结束时的x坐标值。 |
| y | number | 路径结束时的y坐标值。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(10, 10);
8. path.bezierCurveTo(20, 100, 200, 100, 200, 20);
9. ctx.stroke(path);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/rBIUJFyvROSg1EYofU4YZQ/zh-cn_image_0000002592380638.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=75C55B733FF284E8FECF5FE71EBFFD99EF90DE07C4A40882C779F01303145ECD)

## quadraticCurveTo

PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cpx | number | 贝塞尔参数的x坐标值。 |
| cpy | number | 贝塞尔参数的y坐标值。 |
| x | number | 路径结束时的x坐标值。 |
| y | number | 路径结束时的y坐标值。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(10, 10);
8. path.quadraticCurveTo(100, 100, 200, 20);
9. ctx.stroke(path);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/R7u800W7QyaFkqTu1lPMAw/zh-cn_image_0000002622860149.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=196207A8AF9A39AAEEC4FD5322C4897BDB7829228CFCEA8650AD3DC782259A50)

## arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。 |
| y | number | 是 | 弧线圆心的y坐标值。 |
| radius | number | 是 | 弧线的圆半径。 |
| startAngle | number | 是 | 弧线的起始弧度。 |
| endAngle | number | 是 | 弧线的终止弧度。 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。  默认值：false |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.arc(100, 75, 50, 0, 6.28);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/YHlc7WeSTdaTau-so-XChQ/zh-cn_image_0000002622700267.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=ECD706BABBE62BE0D51124199198D7FE99A453FB8D879A9FB07D3E4572238662)

## arcTo

PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x1 | number | 圆弧经过的第一个点的x坐标值。 |
| y1 | number | 圆弧经过的第一个点的y坐标值。 |
| x2 | number | 圆弧经过的第二个点的x坐标值。 |
| y2 | number | 圆弧经过的第二个点的y坐标值。 |
| radius | number | 圆弧的圆半径值。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.arcTo(150, 20, 150, 70, 50);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/pA50j_1RSyavQTPAaMWp4w/zh-cn_image_0000002592220708.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=0DABFEB731C6CEA49521F57C608BEE94CDD42E61BD9B36A1C88B5C91536EE3F9)

## ellipse

PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。 |
| y | number | 是 | 椭圆圆心的y轴坐标。 |
| radiusX | number | 是 | 椭圆x轴的半径长度。 |
| radiusY | number | 是 | 椭圆y轴的半径长度。 |
| rotation | number | 是 | 椭圆的旋转角度，单位为弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度，以弧度表示。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度，以弧度表示。 |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。  默认值：0 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/aoe2lq1YQ8y6jvIvNDgV1g/zh-cn_image_0000002592380640.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=6CC6CE5CA4E966ACF64F4A44BB333C3E4034FD2232969F6A163D0FF5E733747F)

## rect

PhonePC/2in1TabletTVWearable

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标值。 |
| y | number | 指定矩形的左上角y坐标值。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.rect(20, 20, 100, 100);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/5i7L30LfSXuEvHsb3NXxsQ/zh-cn_image_0000002622860151.png?HW-CC-KV=V1&HW-CC-Date=20260611T075203Z&HW-CC-Expire=86400&HW-CC-Sign=DA17B37E6C71731BBE56A47C24B4A42795E08D4628A8618416EE41E96932F032)
