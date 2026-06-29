---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-06-11T15:53:17+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:e5ca3b90173cf4627ed0d7b6447e3a5f85b689c13c7ce6aa60ba2ece1558f38a
---

使用CanvasRenderingContext2D在canvas画布组件上进行绘制，绘制对象可以是矩形、文本。

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
5. </div>
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
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/EohG-vgYStC09IHQF7s8KQ/zh-cn_image_0000002592380818.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=6B4566001C675A2B7EEDE3743508D003B50CF563782CB1B2B63EF85AE615B87C)

## fillRect()

PhonePC/2in1TabletTVWearableLite Wearable

填充一个矩形。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形左上角点的x坐标。 |
| y | number | 指定矩形左上角点的y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/MSawPBixROGYaUWksRoqjw/zh-cn_image_0000002622860329.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=C7C9301B892E9B11FA5AACBA98F80E193B7482003ED29773F77EC29900C34400)

```
1. ctx.fillRect(20, 20, 200, 150);
```

## fillStyle

PhonePC/2in1TabletTVWearableLite Wearable

指定绘制的填充色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 设置填充区域的颜色。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/-Fd9aSinR-moU8x9PT6Aqg/zh-cn_image_0000002622700447.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=BE92155D860ADFAC7D5CABD505668C6A0B87EF5C55D97BA95D778C226CA451ED)

```
1. ctx.fillStyle = '#0000ff';
2. ctx.fillRect(20, 20, 150, 100);
```

## strokeRect()

PhonePC/2in1TabletTVWearableLite Wearable

绘制具有边框的矩形，矩形内部不填充。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标。 |
| y | number | 指定矩形的左上角y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/L53m0XNERx2NGG14OSVu2A/zh-cn_image_0000002592220888.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=523323ACADC7B25E09D6670B920E100DE01A521E713610290E472DE5AE28A8E2)

```
1. ctx.strokeRect(30, 30, 200, 150);
```

## fillText()

PhonePC/2in1TabletTVWearableLite Wearable

绘制填充类文本。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| text | string | 需要绘制的文本内容。 |
| x | number | 需要绘制的文本的左下角x坐标。 |
| y | number | 需要绘制的文本的左下角y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/edbP-FeOSyaGxRcaO4VNJg/zh-cn_image_0000002592380820.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=620C2243538BEC7A6701D6268A5FB40362BB030904A200EBE1DEADB8DE9698B8)

```
1. ctx.font = '35px sans-serif';
2. ctx.fillText("Hello World!", 20, 60);
```

## lineWidth

PhonePC/2in1TabletTVWearableLite Wearable

指定绘制线条的宽度值。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| lineWidth | number | 设置绘制线条的宽度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/W7fMFOTVR_elPMBIKjjoUA/zh-cn_image_0000002622860331.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=299CF919BD511418A326A5BEC0B35C9E08EA0ED78972D70D1CF4DBAA49A7355A)

```
1. ctx.lineWidth = 5;
2. ctx.strokeRect(25, 25, 85, 105);
```

## strokeStyle

PhonePC/2in1TabletTVWearableLite Wearable

设置描边的颜色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 指定描边使用的颜色 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/VKTd_F3fQIyqlrgl88S4mA/zh-cn_image_0000002622700449.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=4919C5517F2BFB4F43C3ECE442BF0A4CC77188CA85E6CB9BE04E5B0845B46E5E)

```
1. ctx.lineWidth = 10;
2. ctx.strokeStyle = '#0000ff';
3. ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

PhonePC/2in1TabletTVWearableLite Wearable

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/beHOs_M8RQ2b3KV0UYaOzA/zh-cn_image_0000002592220890.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=DEFA7FF827314D7326A21280AF1CF91AE45031C6AEA7C179D5DD68D40E8D8D80)

```
1. ctx.moveTo(25, 25);
2. ctx.lineTo(25, 105);
3. ctx.strokeStyle = 'rgb(0,0,255)';
4. ctx.stroke();
```

### beginPath()5+

PhonePC/2in1TabletTVWearableLite Wearable

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/PGbgX6HdSqOC6hlIrvxS_A/zh-cn_image_0000002592380822.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=202B02D6BE3A13CC565B80129C3C2EB8E2400EABC2948043162591571269255E)

```
1. ctx.beginPath();
2. ctx.lineWidth = 6;
3. ctx.strokeStyle = '#0000ff';
4. ctx.moveTo(15, 80);
5. ctx.lineTo(280, 80);
6. ctx.stroke();
```

### moveTo()5+

PhonePC/2in1TabletTVWearableLite Wearable

路径从当前点移动到指定点。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/II10QQ6WRbS-ly79MLVMrQ/zh-cn_image_0000002622860333.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=7C86144C7C626650BA0E56F8D6D158668A32A543342EBD1CE31EF8F6059339DB)

```
1. ctx.beginPath();
2. ctx.moveTo(10, 10);
3. ctx.lineTo(280, 160);
4. ctx.stroke();
```

### lineTo()5+

PhonePC/2in1TabletTVWearableLite Wearable

从当前点到指定点进行路径连接。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/hao_X-bYRuG0tmFCfhFH1g/zh-cn_image_0000002622700451.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=0F590E01E8AD06ED27AA3D4848B22449024782AD068F7BC87B2D907F66CA2605)

```
1. ctx.beginPath();
2. ctx.moveTo(10, 10);
3. ctx.lineTo(280, 160);
4. ctx.stroke();
```

### closePath()5+

PhonePC/2in1TabletTVWearableLite Wearable

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/9TApYJ7QT5uo8yhK1Mp9mA/zh-cn_image_0000002592220892.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=AB5EE330817C1A0D100A14B293B23F6A0D137CB10B929ACCF957EDCFD85C04E2)

```
1. ctx.beginPath();
2. ctx.moveTo(30, 30);
3. ctx.lineTo(110, 30);
4. ctx.lineTo(70, 90);
5. ctx.closePath();
6. ctx.stroke();
```

## font

PhonePC/2in1TabletTVWearableLite Wearable

设置文本绘制中的字体样式。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| value | string | 字体样式支持：sans-serif, serif, monospace，该属性默认值为30px HYQiHei-65S。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ZQrvfVyWS7eUNZG0h_xcWw/zh-cn_image_0000002592380824.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=DB3B66680E1C41F39E5BBA2F339E28AC8C1019F2AECB2D4BA3133D553C068E87)

```
1. ctx.font = '30px sans-serif';
2. ctx.fillText("Hello World", 20, 60);
```

## textAlign

PhonePC/2in1TabletTVWearableLite Wearable

设置文本绘制中的文本对齐方式。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| align | string | 可选值为：  - left（默认）：文本左对齐；  - right：文本右对齐；  - center：文本居中对齐； |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Icf_iGnlRfalgYPMUIBxlQ/zh-cn_image_0000002622860335.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=264954A784F4E6908D8A4CD544C6C632D863860B963B53C56BB598748B36A407)

```
1. ctx.strokeStyle = '#0000ff';
2. ctx.moveTo(140, 10);
3. ctx.lineTo(140, 160);
4. ctx.stroke();

6. ctx.font = '18px sans-serif';

8. // Show the different textAlign values
9. ctx.textAlign = 'left';
10. ctx.fillText('textAlign=left', 140, 100);
11. ctx.textAlign = 'center';
12. ctx.fillText('textAlign=center',140, 120);
13. ctx.textAlign = 'right';
14. ctx.fillText('textAlign=right',140, 140);
```

## arc()5+

PhonePC/2in1TabletTVWearableLite Wearable

绘制弧线路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值，单位：vp。 |
| y | number | 是 | 弧线圆心的y坐标值，单位：vp。 |
| radius | number | 是 | 弧线的圆半径，单位：vp。 |
| startAngle | number | 是 | 弧线的起始弧度，单位：弧度。 |
| endAngle | number | 是 | 弧线的终止弧度，单位：弧度。 |
| anticlockwise | boolean | 否 | 是否逆时针绘制圆弧。  true：逆时针方向绘制弧线。  false：顺时针方向绘制弧线。  默认值：false。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/--12ViapRTaN9bIsJW1zkg/zh-cn_image_0000002622700453.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=45C5D7CAF4EC745CEE04BE8FAD86E6BF588C627534B0AE7D0253954A7BC79978)

```
1. ctx.beginPath();
2. ctx.arc(100, 75, 50, 0, 6.28);
3. ctx.stroke();
```

### rect()5+

PhonePC/2in1TabletTVWearableLite Wearable

创建矩形路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值，单位：vp。 |
| y | number | 是 | 指定矩形的左上角y坐标值，单位：vp。 |
| width | number | 是 | 指定矩形的宽度，单位：vp。 |
| height | number | 是 | 指定矩形的高度，单位：vp。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/xInLumoMQ8WXtPmfsFG5Vg/zh-cn_image_0000002592220894.png?HW-CC-KV=V1&HW-CC-Date=20260611T075315Z&HW-CC-Expire=86400&HW-CC-Sign=5334A65D8D88CEADB3FE7A61B66888B8C81DD379BC8F1972B445B49CA542DD94)

```
1. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
2. ctx.stroke(); // Draw it
```
