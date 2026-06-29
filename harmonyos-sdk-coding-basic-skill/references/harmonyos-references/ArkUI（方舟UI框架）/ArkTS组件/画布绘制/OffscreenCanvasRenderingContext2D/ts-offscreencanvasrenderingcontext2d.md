---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d
title: OffscreenCanvasRenderingContext2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > OffscreenCanvasRenderingContext2D
category: harmonyos-references
scraped_at: 2026-06-11T15:48:33+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:d0a89b26360310bc5fe4be6b412fb5d0b0a470e273b6f30a7f714a7bcffe10d9
---
使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用，ServiceExtensionAbility中建议使用[绘制模块](<../../../../ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.drawing (绘制模块)/模块描述/arkts-apis-graphics-drawing.md>)进行离屏绘制。

[beginPath](ts-offscreencanvasrenderingcontext2d.md#beginpath)、[moveTo](ts-offscreencanvasrenderingcontext2d.md#moveto)、[lineTo](ts-offscreencanvasrenderingcontext2d.md#lineto)、[closePath](ts-offscreencanvasrenderingcontext2d.md#closepath)、[bezierCurveTo](ts-offscreencanvasrenderingcontext2d.md#beziercurveto)、[quadraticCurveTo](ts-offscreencanvasrenderingcontext2d.md#quadraticcurveto)、[arc](ts-offscreencanvasrenderingcontext2d.md#arc)、[arcTo](ts-offscreencanvasrenderingcontext2d.md#arcto)、[ellipse](ts-offscreencanvasrenderingcontext2d.md#ellipse)、[rect](ts-offscreencanvasrenderingcontext2d.md#rect)和[roundRect](ts-offscreencanvasrenderingcontext2d.md#roundrect20)接口只能对OffscreenCanvasRenderingContext2D中的路径生效，无法对[CanvasRenderingContext2D](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md)和[Path2D](../Path2D/ts-components-canvas-path2d.md)对象中设置的路径生效。

## 构造函数

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, settings?: RenderingContextSettings)

构造离屏Canvas画布对象，支持配置画布宽高和OffscreenCanvasRenderingContext2D对象的参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见RenderingContextSettings接口描述。  异常值undefined按[RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见RenderingContextSettings接口描述。  异常值undefined按[RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |
| unit | [LengthMetricsUnit](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetricsunit12>) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md)。  异常值undefined、NaN和Infinity按默认值处理。  默认值：DEFAULT |

## 属性

PhonePC/2in1TabletTVWearable

说明

fillStyle、shadowColor与 strokeStyle 中string类型格式为 'rgb(255, 255, 255)'，'rgba(255, 255, 255, 1.0)'，'#FFFFFF'。

### fillStyle

PhonePC/2in1TabletTVWearable

指定绘制的填充色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string |number10+ |[CanvasGradient](../CanvasGradient/ts-components-canvas-canvasgradient.md) | [CanvasPattern](../CanvasPattern/ts-components-canvas-canvaspattern.md) | 否 | 否 | - 类型为string时，表示设置填充区域的颜色，颜色格式参考[ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor)中string类型说明。  - 类型为number时，表示设置填充区域的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor)中number类型说明。  - 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](ts-offscreencanvasrenderingcontext2d.md#createlineargradient)方法创建。  - 类型为CanvasPattern时，使用[createPattern](ts-offscreencanvasrenderingcontext2d.md#createpattern)方法创建。  默认值：'#000000'（黑色）  异常值设置无效。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 使用string设置fillStyle属性
18. offContext.fillStyle = '#0000ff'
19. offContext.fillRect(20, 20, 150, 100)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 使用number设置fillStyle属性
18. offContext.fillStyle = 0x0000FF
19. offContext.fillRect(20, 20, 150, 100)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/kTsmxie0S5e6UUbvBfIpnw/zh-cn_image_0000002592380378.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=94A9A01DDBF66020B03BAFF637E58B9E32B4DA9D3F1CC3DE2F4CAA15DBCEEFB6)

### lineWidth

PhonePC/2in1TabletTVWearable

设置绘制线条的宽度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：1（px）  默认单位：vp  lineWidth取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致和lineWidth属性相关的接口无法绘制。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineWidthExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 设置lineWidth属性
18. offContext.lineWidth = 5
19. offContext.strokeRect(25, 25, 85, 105)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/_rcmH3GXSkCsd0viqN7iRQ/zh-cn_image_0000002622859889.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=EA601AEAD7D3B540A93676B1478D7F42161F154194E46279A19243ED8DCD33E0)

### strokeStyle

PhonePC/2in1TabletTVWearable

设置线条的颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string |number10+ |[CanvasGradient](../CanvasGradient/ts-components-canvas-canvasgradient.md) | [CanvasPattern](../CanvasPattern/ts-components-canvas-canvaspattern.md) | 否 | 否 | - 类型为string时，表示设置线条使用的颜色，颜色格式参考[ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor)中string类型说明。  - 类型为number时，表示设置线条使用的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor)中number类型说明。  - 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](ts-offscreencanvasrenderingcontext2d.md#createlineargradient)方法创建。  - 类型为CanvasPattern时，使用[createPattern](ts-offscreencanvasrenderingcontext2d.md#createpattern)方法创建。  默认值：'#000000'（黑色）  异常值设置无效。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 10
18. // 使用string设置strokeStyle属性
19. offContext.strokeStyle = '#0000ff'
20. offContext.strokeRect(25, 25, 155, 105)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 10
18. // 使用number设置strokeStyle属性
19. offContext.strokeStyle = 0x0000ff
20. offContext.strokeRect(25, 25, 155, 105)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/a1hOs7erTkC6IY7sm4b-uA/zh-cn_image_0000002622700007.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=9B400946EFFF337C1342BD6F4C6A34FCD28475F55AE0E7D020C7649FC14CBBFB)

### lineCap

PhonePC/2in1TabletTVWearable

指定线端点的样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasLineCap](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvaslinecap类型说明) | 否 | 否 | 默认值：'butt' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineCapExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 8
18. offContext.beginPath()
19. // 设置lineCap属性
20. offContext.lineCap = 'round'
21. offContext.moveTo(30, 50)
22. offContext.lineTo(220, 50)
23. offContext.stroke()
24. let image = this.offCanvas.transferToImageBitmap()
25. this.context.transferFromImageBitmap(image)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/khRjHzdvTXuHzed99sF6oA/zh-cn_image_0000002592220448.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=F4C8C6B9862859713DBE0D30D318F84B6312D39BA60B7386325D47BE0752B075)

### lineJoin

PhonePC/2in1TabletTVWearable

指定线段间相交的交点样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasLineJoin](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvaslinejoin类型说明) | 否 | 否 | 默认值：'miter' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineJoinExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.lineWidth = 8
19. // 设置lineJoin属性
20. offContext.lineJoin = 'miter'
21. offContext.moveTo(30, 30)
22. offContext.lineTo(120, 60)
23. offContext.lineTo(30, 110)
24. offContext.stroke()
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/mCf2ToszQW2ims6Xjjdgpw/zh-cn_image_0000002592380380.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=3B4A97F9A50F8FA1ABC4BD5E93C0D22A1C86CE4EEBCFB107BC025F7DDCD16167)

### miterLimit

PhonePC/2in1TabletTVWearable

设置斜接面限制值，该值指定了线条相交处内角和外角的距离，仅当设置了lineJoin为miter才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：10px  单位：px  miterLimit取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致和miterLimit属性相关的接口无法绘制。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MiterLimit {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 8
18. offContext.lineJoin = 'miter'
19. // 设置miterLimit属性
20. offContext.miterLimit = 3
21. offContext.moveTo(30, 30)
22. offContext.lineTo(60, 35)
23. offContext.lineTo(30, 37)
24. offContext.stroke()
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/jCvkJj5wRYCRM5XR0tQu5Q/zh-cn_image_0000002622859891.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=26A85578D86BFC22FA41702D7E9806BFBE9FF7D2753FC7603FD4915ABEBF0372)

### font

PhonePC/2in1TabletTVWearable

设置文本绘制中的字体样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

语法：ctx.font = 'font-style font-weight font-size font-family'

- font-style(可选)，用于指定字体样式，支持如下几种样式：'normal','italic'。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：'normal', 'bold', 'bolder', 'lighter', 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位支持px、vp。使用时需要添加单位。

- font-family(可选)，指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。

从API version 20开始，支持通过该接口设置注册过的自定义字体（只能在主线程使用，不支持在worker线程中使用；DevEco Studio的预览器不支持显示自定义字体）。自定义字体注册有以下两种方式。一种是通过ArkUI的异步接口this.uiContext.getFont().[registerFont](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (Font)/arkts-apis-uicontext-font.md#registerfont>)注册，调用后立即绘制可能会导致自定义字体不生效。另一种是直接调用字体引擎的fontCollection.[loadFontSync](<../../../../ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.text (文本模块)/js-apis-graphics-text.md#loadfontsync>)接口来注册自定义字体到字体引擎。在直接调用字体引擎接口注册自定义字体时，fontCollection的实例需要是text.FontCollection.getGlobalInstance()，因为组件默认会从该实例加载字体。如果使用其他实例，可能会导致自定义字体不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 默认值：'normal normal 14px sans-serif' |

```
1. import { text } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct FontDemo {
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('rgb(213,213,213)')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext("2d", this.settings);
18. // 常规字体样式，常规粗细，字体大小为30px，字体系列为sans-serif
19. offContext.font = 'normal normal 30px sans-serif'
20. offContext.fillText("Hello px", 20, 60)
21. // 斜体样式，加粗，字体大小为30vp，字体系列为monospace
22. offContext.font = 'italic bold 30vp monospace'
23. offContext.fillText("Hello vp", 20, 100)
24. // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Thin_Italic.ttf
25. let fontCollection = text.FontCollection.getGlobalInstance();
26. fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
27. // 加粗，字体大小为30vp，字体系列为HarmonyOS_Sans_Thin_Italic
28. offContext.font = "bold 30vp HarmonyOS_Sans_Thin_Italic"
29. offContext.fillText("Hello customFont", 20, 140)
30. let image = this.offCanvas.transferToImageBitmap();
31. this.context.transferFromImageBitmap(image)
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/PybEHxnzRVi_mQ3lXSOMow/zh-cn_image_0000002622700009.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=7FA29AA107AC1EEEC801ECB5C5A97FB7BA344ADB39F0A410D3FBEBBD1B9D1A43)

### textAlign

PhonePC/2in1TabletTVWearable

设置文本绘制中的文本对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasTextAlign](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvastextalign类型说明) | 否 | 否 | ltr布局模式下'start'和'left'一致，rtl布局模式下'start'和'right'一致。  默认值：'left' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.strokeStyle = 'rgb(39,135,217)'
18. offContext.moveTo(140, 10)
19. offContext.lineTo(140, 160)
20. offContext.stroke()

22. offContext.font = '50px sans-serif'

24. // 设置textAlign属性为start
25. offContext.textAlign = 'start'
26. offContext.fillText('textAlign=start', 140, 60)
27. // 设置textAlign属性为end
28. offContext.textAlign = 'end'
29. offContext.fillText('textAlign=end', 140, 80)
30. // 设置textAlign属性为left
31. offContext.textAlign = 'left'
32. offContext.fillText('textAlign=left', 140, 100)
33. // 设置textAlign属性为center
34. offContext.textAlign = 'center'
35. offContext.fillText('textAlign=center', 140, 120)
36. // 设置textAlign属性为right
37. offContext.textAlign = 'right'
38. offContext.fillText('textAlign=right', 140, 140)
39. let image = this.offCanvas.transferToImageBitmap()
40. this.context.transferFromImageBitmap(image)
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/tTVhPkdYT9SfftgkgGHW1g/zh-cn_image_0000002592220450.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=3EE57CBB459615536999E45A71BED005944C65AC22C6182A70C6F3F93F1B9391)

### textBaseline

PhonePC/2in1TabletTVWearable

设置文本绘制中的水平对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasTextBaseline](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明) | 否 | 否 | 默认值：'alphabetic' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextBaseline {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.strokeStyle = '#0000ff'
18. offContext.moveTo(0, 120)
19. offContext.lineTo(400, 120)
20. offContext.stroke()

22. offContext.font = '20px sans-serif'

24. // 设置textBaseline属性为top
25. offContext.textBaseline = 'top'
26. offContext.fillText('Top', 10, 120)
27. // 设置textBaseline属性为bottom
28. offContext.textBaseline = 'bottom'
29. offContext.fillText('Bottom', 55, 120)
30. // 设置textBaseline属性为middle
31. offContext.textBaseline = 'middle'
32. offContext.fillText('Middle', 125, 120)
33. // 设置textBaseline属性为alphabetic
34. offContext.textBaseline = 'alphabetic'
35. offContext.fillText('Alphabetic', 195, 120)
36. // 设置textBaseline属性为hanging
37. offContext.textBaseline = 'hanging'
38. offContext.fillText('Hanging', 295, 120)
39. let image = this.offCanvas.transferToImageBitmap()
40. this.context.transferFromImageBitmap(image)
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/i1l5S3GkQRODW3vJDmsIVg/zh-cn_image_0000002622699963.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=95BDD7A50DE7C478BEAF6EDD3DE66BE5BD161E22C3D3C5D1E88D895A99CCB7AE)

### globalAlpha

PhonePC/2in1TabletTVWearable

设置透明度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制。API version 18及以后，设置NaN或Infinity时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认值：1.0 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GlobalAlpha {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(0,0,255)'
18. offContext.fillRect(0, 0, 50, 50)
19. // 设置globalAlpha属性
20. offContext.globalAlpha = 0.4
21. offContext.fillStyle = 'rgb(0,0,255)'
22. offContext.fillRect(50, 50, 50, 50)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/eajyYvioTFiNo6_gMGT1Tw/zh-cn_image_0000002592380382.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=2F34532AC9A131F98FBCA6405128EA0C197D608C74623F39DB4B279ADF8A7A3A)

### lineDashOffset

PhonePC/2in1TabletTVWearable

设置画布的虚线偏移量，精度为float，仅当设置setLineDash时属性才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0  单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineDashOffset {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.arc(100, 75, 50, 0, 6.28)
18. offContext.setLineDash([10, 20])
19. // 设置lineDashOffset属性
20. offContext.lineDashOffset = 10.0
21. offContext.stroke()
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/MJJxlJxnQOK81Dl57ysJyA/zh-cn_image_0000002622859893.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=29F2EAC3A6B365AE10FF4E00E0E1FCD13B8DE1756D37D7B46F8D8327DCF56563)

### globalCompositeOperation

PhonePC/2in1TabletTVWearable

设置合成操作的方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 类型字段可选值有'source-over'，'source-atop'，'source-in'，'source-out'，'destination-over'，'destination-atop'，'destination-in'，'destination-out'，'lighter'，'copy'，'xor'。  默认值：'source-over' |

| 名称 | 描述 |
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

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GlobalCompositeOperation {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private context3: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private context4: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
10. private context5: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
11. private context6: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

13. build() {
14. Column() {
15. Row() {
16. // 1. source-over：新图形覆盖在原有图形上方（默认行为）
17. Canvas(this.context1)
18. .width('45%')
19. .borderWidth(1)
20. .margin(5)
21. .onReady(() => {
22. let ctx1 = this.context1;
23. let offContext = new OffscreenCanvasRenderingContext2D(ctx1.width, ctx1.height, this.settings);
24. offContext.fillStyle = 'rgb(39,135,217)';
25. offContext.fillRect(25, 25, 75, 75); // 原有图形
26. offContext.globalCompositeOperation = 'source-over'; // 默认值，可省略
27. offContext.fillStyle = 'rgb(23,169,141)';
28. offContext.fillRect(75, 75, 75, 75); // 新图形覆盖
29. let image = offContext.transferToImageBitmap();
30. this.context1.transferFromImageBitmap(image);
31. })
32. // 2. destination-out：新图形擦除原有图形（橡皮擦核心逻辑）
33. Canvas(this.context2)
34. .width('45%')
35. .borderWidth(1)
36. .margin(5)
37. .onReady(() => {
38. let ctx2 = this.context2;
39. let offContext = new OffscreenCanvasRenderingContext2D(ctx2.width, ctx2.height, this.settings);
40. // 先绘制背景
41. offContext.fillStyle = 'rgb(39,135,217)';
42. offContext.fillRect(0, 0, ctx2.width, ctx2.height);
43. // 设置合成模式为擦除
44. offContext.globalCompositeOperation = 'destination-out';
45. // 绘制圆形作为橡皮擦
46. offContext.beginPath();
47. offContext.arc(ctx2.width / 2, ctx2.height / 2, 60, 0, Math.PI * 2);
48. offContext.fill(); // 擦除圆形区域的背景
49. let image = offContext.transferToImageBitmap();
50. this.context2.transferFromImageBitmap(image);
51. })
52. }
53. .height('30%')

55. Row() {
56. // 3. source-in：仅保留新图形与原有图形重叠的部分（裁剪或蒙版）
57. Canvas(this.context3)
58. .width('45%')
59. .borderWidth(1)
60. .margin(5)
61. .onReady(() => {
62. let ctx3 = this.context3;
63. let offContext = new OffscreenCanvasRenderingContext2D(ctx3.width, ctx3.height, this.settings);
64. // 先绘制原有图形（圆形蒙版）
65. offContext.beginPath();
66. offContext.arc(ctx3.width / 2, ctx3.height / 2, 80, 0, Math.PI * 2);
67. offContext.fillStyle = '#fff';
68. offContext.fill();
69. // 设置合成模式
70. offContext.globalCompositeOperation = 'source-in';
71. // 绘制新图形（渐变矩形）
72. const gradient = offContext.createLinearGradient(0, 0, ctx3.width, ctx3.height);
73. gradient.addColorStop(0, 'rgb(23,169,141)');
74. gradient.addColorStop(1, 'rgb(39,135,217)');
75. offContext.fillStyle = gradient;
76. offContext.fillRect(0, 0, 200, 200); // 仅圆形区域显示渐变
77. let image = offContext.transferToImageBitmap();
78. this.context3.transferFromImageBitmap(image);
79. })
80. // 4. lighter：新图形与原有图形叠加（亮度相加，滤色效果）
81. Canvas(this.context4)
82. .width('45%')
83. .borderWidth(1)
84. .margin(5)
85. .onReady(() => {
86. let ctx4 = this.context4;
87. let offContext = new OffscreenCanvasRenderingContext2D(ctx4.width, ctx4.height, this.settings);
88. // 原有图形（半透明红色圆）
89. offContext.beginPath();
90. offContext.arc(70, 100, 50, 0, Math.PI * 2);
91. offContext.fillStyle = 'rgba(234, 67, 53, 0.7)';
92. offContext.fill();
93. // 设置合成模式
94. offContext.globalCompositeOperation = 'lighter';
95. // 新图形（半透明蓝色圆）
96. offContext.beginPath();
97. offContext.arc(110, 100, 50, 0, Math.PI * 2);
98. offContext.fillStyle = 'rgba(66, 133, 244, 0.7)';
99. offContext.fill(); // 重叠区域变成紫色（亮度叠加）
100. let image = offContext.transferToImageBitmap();
101. this.context4.transferFromImageBitmap(image);
102. })
103. }
104. .height('30%')

106. Row() {
107. // 5. destination-atop：保留原有图形与新图形重叠的部分，移除其他区域
108. Canvas(this.context5)
109. .width('45%')
110. .borderWidth(1)
111. .margin(5)
112. .onReady(() => {
113. let ctx5 = this.context5;
114. let offContext = new OffscreenCanvasRenderingContext2D(ctx5.width, ctx5.height, this.settings);
115. // 原有图形（绿色矩形）
116. offContext.fillStyle = 'rgb(23,169,141)';
117. offContext.fillRect(0, 0, ctx5.width, ctx5.height);
118. // 设置合成模式
119. offContext.globalCompositeOperation = 'destination-atop';
120. // 新图形（小圆形）
121. offContext.beginPath();
122. offContext.arc(ctx5.width / 2, ctx5.height / 2, 60, 0, Math.PI * 2);
123. offContext.fillStyle = '#000';
124. offContext.fill(); // 仅矩形与圆形重叠的部分保留
125. let image = offContext.transferToImageBitmap();
126. this.context5.transferFromImageBitmap(image);
127. })
128. // 6. 文字蒙版（“source-in”的高级用法）
129. Canvas(this.context6)
130. .width('45%')
131. .borderWidth(1)
132. .margin(5)
133. .onReady(() => {
134. let ctx6 = this.context6;
135. let offContext = new OffscreenCanvasRenderingContext2D(ctx6.width, ctx6.height, this.settings);
136. // 先绘制文字（作为蒙版）
137. offContext.font = 'bold 40vp';
138. offContext.textAlign = 'center';
139. offContext.textBaseline = 'middle';
140. offContext.fillText('CANVAS', ctx6.width / 2, ctx6.height / 2);
141. // 设置合成模式
142. offContext.globalCompositeOperation = 'source-in';
143. // 绘制渐变背景（仅文字区域显示）
144. let textGradient = offContext.createLinearGradient(50, 0, 300, 100);
145. textGradient.addColorStop(0.0, 'rgb(39,135,217)');
146. textGradient.addColorStop(0.5, 'rgb(255,238,240)');
147. textGradient.addColorStop(1.0, 'rgb(23,169,141)');
148. offContext.fillStyle = textGradient;
149. offContext.fillRect(0, 0, 200, 200); // 渐变仅填充文字区域
150. let image = offContext.transferToImageBitmap();
151. this.context6.transferFromImageBitmap(image);
152. })
153. }
154. .height('30%')
155. }
156. .width('100%')
157. .height('100%')
158. }
159. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/BZ4_sh0ETvSRehuZMEIKGQ/zh-cn_image_0000002622700011.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=79E9B702955A641289D8409B2BD7BEAC7234E7F76B1A3C68C707B46351095FD3)

### shadowBlur

PhonePC/2in1TabletTVWearable

设置绘制阴影时的模糊级别，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 值越大越模糊，精度为float，取值范围≥0。  默认值：0.0  单位：px  shadowBlur取值不支持负数，负数、NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowBlur {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 设置shadowBlur属性
18. offContext.shadowBlur = 30
19. offContext.shadowColor = 'rgb(0,0,0)'
20. offContext.fillStyle = 'rgb(39,135,217)'
21. offContext.fillRect(20, 20, 100, 80)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/CrDdxiQ4RIW-yAmehZQQAg/zh-cn_image_0000002592220452.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=D20764908C70C6BF9F9FA2157A3CBB1644F120C293B7217EA95BF70E2D245FB7)

### shadowColor

PhonePC/2in1TabletTVWearable

设置绘制阴影时的阴影颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 颜色格式参考[ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor)中string类型说明。  默认值：透明黑色 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowColor {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.shadowBlur = 30
18. // 设置shadowColor属性
19. offContext.shadowColor = 'rgb(255,192,0)'
20. offContext.fillStyle = 'rgb(39,135,217)'
21. offContext.fillRect(30, 30, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/hiqiJbD9RpSbvj5jRnJvVQ/zh-cn_image_0000002592380384.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=22C6A341E595019877CB56DEF0E2F28163DBA63617030CB1719C848A9C6E3D6F)

### shadowOffsetX

PhonePC/2in1TabletTVWearable

设置绘制阴影时和原有对象的水平偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0  默认单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowOffsetX {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.shadowBlur = 10
18. // 设置shadowOffsetX属性
19. offContext.shadowOffsetX = 20
20. offContext.shadowColor = 'rgb(0,0,0)'
21. offContext.fillStyle = 'rgb(255,0,0)'
22. offContext.fillRect(20, 20, 100, 80)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/-qXaeimPSLa_021V6oVSaQ/zh-cn_image_0000002622859895.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=CBEB80E094FEACC896FC8409864A05CEC8DE8B8812DFCF8B9A59FC82D71A86F6)

### shadowOffsetY

PhonePC/2in1TabletTVWearable

设置绘制阴影时和原有对象的垂直偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0  默认单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowOffsetY {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.shadowBlur = 10
18. // 设置shadowOffsetY属性
19. offContext.shadowOffsetY = 20
20. offContext.shadowColor = 'rgb(0,0,0)'
21. offContext.fillStyle = 'rgb(255,0,0)'
22. offContext.fillRect(30, 30, 100, 100)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/gz8kpJY_RI6BD-ghI3ikqA/zh-cn_image_0000002622700013.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=9E553B23CDD7951AA2F7FF31B0D19FC5182C75986045E3B1741791BDDB16F10F)

### imageSmoothingEnabled

PhonePC/2in1TabletTVWearable

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| boolean | 否 | 否 | 默认值：true |

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageSmoothingEnabled {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
8. private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. // 设置imageSmoothingEnabled属性
20. offContext.imageSmoothingEnabled = false
21. offContext.drawImage(this.img, 0, 0, 400, 200)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/mnryxJfBQqK6SSBAfQtpzg/zh-cn_image_0000002592220454.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=EF3BF3212762CF1282B607A8B2797DE7C65BE64C22FE9576B7C5C0AACAB7B169)

### imageSmoothingQuality

PhonePC/2in1TabletTVWearable

imageSmoothingEnabled为true时，用于设置图像平滑度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [ImageSmoothingQuality](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#imagesmoothingquality类型说明) | 否 | 否 | 默认值："low" |

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageSmoothingQualityDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.
7. settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
9. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
10. private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");

12. build() {
13. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,
14. justifyContent: FlexAlign.Center }) {
15. Canvas(this.context)
16. .width('100%')
17. .height('100%')
18. .backgroundColor('#ffff00')
19. .onReady(() => {
20. let offContext = this.offCanvas.getContext("2d", this.settings)
21. let offctx = offContext
22. offctx.imageSmoothingEnabled = true
23. // 设置imageSmoothingQuality属性
24. offctx.imageSmoothingQuality = 'high'
25. offctx.drawImage(this.img, 0, 0, 400, 200)

27. let image = this.offCanvas.transferToImageBitmap()
28. this.context.transferFromImageBitmap(image)
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/E0bWXZD-R32H0cI6fzp6pw/zh-cn_image_0000002622699969.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=C59D8D70AD28BCE5A257959895002F8222FAED410431845AF9402831CE3FB509)

### direction

PhonePC/2in1TabletTVWearable

用于设置绘制文字时使用的文字方向，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasDirection](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvasdirection类型说明) | 否 | 否 | 默认值："inherit" |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DirectionDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.
7. settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,
12. justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. let offctx = offContext
20. offctx.font = '48px serif';
21. offctx.textAlign = 'start'
22. offctx.fillText("Hi ltr!", 200, 50);

24. // 设置direction属性
25. offctx.direction = "rtl";
26. offctx.fillText("Hi rtl!", 200, 100);

28. let image = offctx.transferToImageBitmap()
29. this.context.transferFromImageBitmap(image)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qJOs-U_HReiEijIpFOi0xg/zh-cn_image_0000002592220408.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=DDB825A609C255D1F9091163AB33FA402D78CFCC630CE531EBFABCBDB39B909A)

### filter

PhonePC/2in1TabletTVWearable

用于设置图像的滤镜，可以组合任意数量的滤镜，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 支持的滤镜效果如下：  - 'none': 无滤镜效果。  - 'blur(<length>)'：给图像设置高斯模糊，取值范围≥0，支持单位px、vp、rem，默认值：blur(0px)。  - 'brightness([<number>|<percentage>])'：给图片应用一种线性乘法，使其看起来更亮或更暗，支持数字和百分比参数，取值范围≥0，默认值：brightness(1)。  - 'contrast([<number>|<percentage>])'：调整图像的对比度，支持数字和百分比参数，取值范围≥0，默认值：contrast(1)。  - 'grayscale([<number>|<percentage>])'：将图像转换为灰度图像，支持数字和百分比参数，取值范围[0, 1]，默认值：grayscale(0)。  - 'hue-rotate(<angle>)'：给图像应用色相旋转，取值范围0deg-360deg，默认值：hue-rotate(0deg)。  - 'invert([<number>|<percentage>])'：反转输入图像，支持数字和百分比参数，取值范围[0, 1]，默认值：invert(0)。  - 'opacity([<number>|<percentage>])'：调整图像的透明程度，支持数字和百分比参数，取值范围[0, 1]，默认值：opacity(1)。  - 'saturate([<number>|<percentage>])'：转换图像饱和度，支持数字和百分比参数，取值范围≥0，默认值：saturate(1)。  - 'sepia([<number>|<percentage>])'：将图像转换为深褐色，支持数字和百分比参数，取值范围[0, 1]，默认值：sepia(0)。 |

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FilterDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
9. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext("2d", this.settings)
18. let img = this.img

20. offContext.drawImage(img, 0, 0, 100, 100);

22. offContext.filter = 'grayscale(50%)';
23. offContext.drawImage(img, 100, 0, 100, 100);

25. offContext.filter = 'sepia(60%)';
26. offContext.drawImage(img, 200, 0, 100, 100);

28. offContext.filter = 'saturate(30%)';
29. offContext.drawImage(img, 0, 100, 100, 100);

31. offContext.filter = 'hue-rotate(90deg)';
32. offContext.drawImage(img, 100, 100, 100, 100);

34. offContext.filter = 'invert(100%)';
35. offContext.drawImage(img, 200, 100, 100, 100);

37. offContext.filter = 'opacity(25%)';
38. offContext.drawImage(img, 0, 200, 100, 100);

40. offContext.filter = 'brightness(0.4)';
41. offContext.drawImage(img, 100, 200, 100, 100);

43. offContext.filter = 'contrast(200%)';
44. offContext.drawImage(img, 200, 200, 100, 100);

46. offContext.filter = 'blur(5px)';
47. offContext.drawImage(img, 0, 300, 100, 100);

49. // Applying multiple filters
50. offContext.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
51. offContext.drawImage(img, 100, 300, 100, 100);

53. let image = this.offCanvas.transferToImageBitmap()
54. this.context.transferFromImageBitmap(image)
55. })
56. }
57. .width('100%')
58. .height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/vlQTWx6qSDOvt3a6vz7-bw/zh-cn_image_0000002592380342.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=D919E065DC0B950432DFE4665FCC471FC9C59BF16AC9D06C7EC814A66A585B28)

### letterSpacing18+

PhonePC/2in1TabletTVWearable

用于指定绘制文本时字母之间的间距，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | 否 | 当使用LengthMetrics时：  字间距按照指定的单位设置；  不支持FP、PERCENT和LPX（按无效值处理）；  支持负数和小数，设为小数时字间距不四舍五入。  当使用string时：  不支持设置百分比（按无效值处理）；  支持负数和小数，设为小数时字间距不四舍五入；  若letterSpacing的赋值未指定单位（例如：letterSpacing='10'），且未指定LengthMetricsUnit时，默认单位设置为vp；  指定LengthMetricsUnit为px时，默认单位设置为px；  当letterSpacing的赋值指定单位时（例如：letterSpacing='10vp'），字间距按照指定的单位设置。  默认值：0（输入无效值时，字间距设为默认值）  注：推荐使用LengthMetrics，性能更好。 |

```
1. // xxx.ets
2. import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct letterSpacingDemo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('rgb(213,213,213)')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.font = '30vp'
20. // 使用string设置direction属性
21. offContext.letterSpacing = '10vp'
22. offContext.fillText('hello world', 30, 50)
23. // 使用LengthMetrics对象设置direction属性
24. offContext.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
25. offContext.fillText('hello world', 30, 100)
26. let image = this.offCanvas.transferToImageBitmap()
27. this.context.transferFromImageBitmap(image)
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/cJFp1Mh-RqiQubYkQNnrCA/zh-cn_image_0000002622859853.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=B398C614BAF368EA4A1F07C05CF61DFE27BCD29E2162C02B84116A34ECBACE01)

### antialias24+

PhonePC/2in1TabletTVWearable

用于设置绘制图形和文本时是否开启抗锯齿。设置此接口会覆盖[RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings)中的抗锯齿效果，未通过该接口设置时，默认值为undefined，与[RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings)中的抗锯齿效果保持一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| boolean | 否 | 否 | 设置绘制图形和文本时是否开启抗锯齿。  true表示开启抗锯齿；false表示不开启抗锯齿。  值为undefined时，与[RenderingContextSettings](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#renderingcontextsettings)中的抗锯齿效果保持一致。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AntialiasDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings);
17. let anti = offContext.antialias;
18. console.info(`current antialias is ${anti}`);
19. // 设置antialias属性为非抗锯齿
20. offContext.antialias = false;
21. offContext.strokeStyle = 'rgb(0,0,0)';
22. offContext.lineWidth = 2;
23. offContext.beginPath();
24. offContext.arc(150, 150, 100, 0, Math.PI);
25. offContext.stroke();
26. offContext.font = 'normal bold 30vp monospace';
27. offContext.fillText("Hello World", 20, 100);
28. anti = offContext.antialias;
29. console.info(`current antialias is ${anti}`);

31. // 设置antialias属性为抗锯齿
32. offContext.antialias = true;
33. offContext.beginPath();
34. offContext.arc(150, 350, 100, 0, Math.PI);
35. offContext.stroke();
36. offContext.font = 'normal bold 30vp monospace';
37. offContext.fillText("Hello World", 20, 300);
38. anti = offContext.antialias;
39. console.info(`current antialias is ${anti}`);
40. let image = this.offCanvas.transferToImageBitmap();
41. this.context.transferFromImageBitmap(image);
42. })
43. }
44. .width('100%')
45. .height('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/XlbIxwNLQ8-gCXr5Im6bfw/zh-cn_image_0000002592380386.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=85D9AF3C1A4E214552E4D812EF7A891048B2532A65D1F26A3D4970B58E90C05C)

## 方法

PhonePC/2in1TabletTVWearable

### fillRect

PhonePC/2in1TabletTVWearable

fillRect(x: number, y: number, w: number, h: number): void

填充一个矩形。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形左上角点的x坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 指定矩形左上角点的y坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillRect(30, 30, 100, 100)
18. let image = this.offCanvas.transferToImageBitmap()
19. this.context.transferFromImageBitmap(image)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/A-J99Up0QLSyGWMOhxhKbg/zh-cn_image_0000002592220410.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=43EF17862D884538F587859F985C0827432CE83F394108914F79669974A0D9B1)

### strokeRect

PhonePC/2in1TabletTVWearable

strokeRect(x: number, y: number, w: number, h: number): void

绘制具有边框的矩形，矩形内部不填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| width | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| height | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.strokeRect(30, 30, 200, 150)
18. let image = this.offCanvas.transferToImageBitmap()
19. this.context.transferFromImageBitmap(image)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/iu-82nmKQUaLvBFBKsDVAw/zh-cn_image_0000002592380344.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=C353382E909FBD36ED0DDA01A78AE4F838E2309802F25E0C82748AFEEF8D77E8)

### clearRect

PhonePC/2in1TabletTVWearable

clearRect(x: number, y: number, w: number, h: number): void

删除指定区域内的绘制内容。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形上的左上角x坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 指定矩形上的左上角y坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| width | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| height | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClearRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(0,0,255)'
18. offContext.fillRect(20, 20, 200, 200)
19. offContext.clearRect(30, 30, 150, 100)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/C-9KO70rTSykHYdeEY7WLg/zh-cn_image_0000002622859855.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=031B35D0EDFD66CA8880EC05721471507D7E7EC8B3B3CBF60D6F4EE77281C663)

### fillText

PhonePC/2in1TabletTVWearable

fillText(text: string, x: number, y: number, maxWidth?: number): void

绘制填充类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。  异常值undefined或null按无效值处理，不进行绘制。 |
| x | number | 是 | 文本绘制起点的x轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 文本绘制起点的y轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| maxWidth | number | 否 | 指定文本允许的最大宽度。  异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。  默认单位：vp  默认值：不限制宽度。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '30px sans-serif'
18. offContext.fillText("Hello World!", 20, 100)
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/uj7ogMuEQjyhRA3J4aCqSA/zh-cn_image_0000002622699973.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=2E63F694B79C870776A12477AA6892C9EBA452C0CDE8721A7BFCE14267EAE545)

### strokeText

PhonePC/2in1TabletTVWearable

strokeText(text: string, x: number, y: number, maxWidth?: number): void

绘制描边类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。  异常值undefined或null按无效值处理，不进行绘制。 |
| x | number | 是 | 文本绘制起点的x轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 文本绘制起点的y轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| maxWidth | number | 否 | 需要绘制的文本的最大宽度。  异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。  默认单位：vp  默认值：不限制宽度。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '55px sans-serif'
18. offContext.strokeText("Hello World!", 20, 60)
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/KaNb9xBZQHes0blw5cwloA/zh-cn_image_0000002622859897.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=307C910C5661C7017B82691022E7100E82C47A4D54B753F437F8F325B8E9D29E)

### measureText

PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextMetrics](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#textmetrics) | 文本的尺寸信息。  传入异常值undefined或null时按"undefined"或"null"计算。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MeasureText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '50px sans-serif'
18. offContext.fillText("Hello World!", 20, 100)
19. offContext.fillText("width:" + offContext.measureText("Hello World!").width, 20, 200)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/vS-8_7g5QtW2TMAOMD6MDA/zh-cn_image_0000002622700015.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=F4F4963E8EAB406904109A88ECD66263F77E375CB95793F05D05ADC3ED16D103)

### stroke

PhonePC/2in1TabletTVWearable

stroke(): void

根据当前的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Stroke {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.moveTo(125, 25)
18. offContext.lineTo(125, 105)
19. offContext.lineTo(175, 105)
20. offContext.lineTo(175, 25)
21. offContext.strokeStyle = 'rgb(255,0,0)'
22. offContext.stroke()
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/0rompJRcRia_4mW5jMKPyw/zh-cn_image_0000002592220456.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=AFFB3FCB5B375ADB60424358EC8B4A21687D54F1EF1860921EE3E5881DBC490C)

### stroke

PhonePC/2in1TabletTVWearable

stroke(path: Path2D): void

根据指定的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path2D](../Path2D/ts-components-canvas-path2d.md) | 是 | 需要绘制的Path2D。  异常值undefined或null按无效值处理，不进行绘制。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Stroke {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. private path2Da: Path2D = new Path2D();

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext("2d", this.settings)
18. this.path2Da.moveTo(25, 25)
19. this.path2Da.lineTo(25, 105)
20. this.path2Da.lineTo(75, 105)
21. this.path2Da.lineTo(75, 25)
22. offContext.strokeStyle = 'rgb(0,0,255)'
23. offContext.stroke(this.path2Da)
24. let image = this.offCanvas.transferToImageBitmap()
25. this.context.transferFromImageBitmap(image)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/0vuGrSp8QSOrvrpkpX-Etw/zh-cn_image_0000002592380388.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=875D12E7877E53982E6373A30790EAAE06B26CC85256D1E10BFC8A74575C6F9C)

### beginPath

PhonePC/2in1TabletTVWearable

beginPath(): void

创建一个新的绘制路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BeginPath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.lineWidth = 6
19. offContext.strokeStyle = '#0000ff'
20. offContext.moveTo(15, 80)
21. offContext.lineTo(280, 160)
22. offContext.stroke()
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/k1GRz78ySI2ik46SBHeS2A/zh-cn_image_0000002622859899.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=C551522505ECA5CAD2D6D9B5686DBB0EC0ABE8420B9A8B4AB6CEF66A812E13A9)

### moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定位置的y坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

说明

API version 18之前，若未执行moveTo接口或moveTo接口传入无效参数，路径以(0,0)为起点。

API version 18及以后，若未执行moveTo接口或moveTo接口传入无效参数，路径以初次调用的lineTo、arcTo、bezierCurveTo或quadraticCurveTo接口中的起始点为起点。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MoveTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.moveTo(10, 10)
19. offContext.lineTo(280, 160)
20. offContext.stroke()
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dU9XwSULRaevxwB7iMtZGg/zh-cn_image_0000002622700017.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=505D675CA46598EE2F075F3F3F864AA3013151BDC7CE320886C5CDDC8AD128DF)

### lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定位置的y坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.moveTo(10, 10)
19. offContext.lineTo(280, 160)
20. offContext.stroke()
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/RPPH7-kmSoKf-84mJky5wg/zh-cn_image_0000002592220458.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=1F31C237BEEEC3EE277A6FF0B708F95BD21B9BA42A1487BFFC4989FFF54C97DB)

### closePath

PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径形成一个封闭路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClosePath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.moveTo(30, 30)
19. offContext.lineTo(110, 30)
20. offContext.lineTo(70, 90)
21. offContext.closePath()
22. offContext.stroke()
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/I0C4XhDuSqWcmhvcxuAVNA/zh-cn_image_0000002592380390.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=586BD0F99BE026AD52E05E6D48096EA69B112D0D539EE51A9061A9A68952B645)

### createPattern

PhonePC/2in1TabletTVWearable

createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null

通过指定图像和重复方式创建图片填充的模板。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](../ImageBitmap/ts-components-canvas-imagebitmap.md) | 是 | 图源对象，具体参考ImageBitmap对象。  异常值undefined或null按无效值处理。 |
| repetition | string | null | 是 | 设置图像重复的方式：  'repeat'：沿x轴和y轴重复绘制图像；  'repeat-x'：沿x轴重复绘制图像；  'repeat-y'：沿y轴重复绘制图像；  'no-repeat'：不重复绘制图像；  'clamp'：在原始边界外绘制时，超出部分使用边缘的颜色绘制；  'mirror'：沿x轴和y轴重复翻转绘制图像。  异常值undefined或null按无效值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasPattern](../CanvasPattern/ts-components-canvas-canvaspattern.md) | null | 通过指定图像和重复方式创建图片填充的模板对象。 |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreatePattern {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('rgb(213,213,213)')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. let pattern = offContext.createPattern(this.img, 'repeat')
20. offContext.fillStyle = pattern as CanvasPattern
21. offContext.fillRect(0, 0, 200, 200)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/2EvKE37bSnybWba6UlxNBQ/zh-cn_image_0000002622859901.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=F0A3F382178FACBD5E94A853243920BE9E24E8A7EFD30AC4ADC1C65279C19521)

### bezierCurveTo

PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. import { Point } from '@kit.TestKit';

4. @Entry
5. @Component
6. struct BezierCurveTo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
10. private start: Point = { x: 50, y: 50 };
11. private end: Point = { x: 250, y: 100 };
12. private cp1: Point = { x: 200, y: 30 };
13. private cp2: Point = { x: 130, y: 80 };

15. build() {
16. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
17. Canvas(this.context)
18. .width('100%')
19. .height('100%')
20. .backgroundColor('rgb(213,213,213)')
21. .onReady(() => {
22. let offContext = this.offCanvas.getContext("2d", this.settings)
23. // 三次贝塞尔曲线
24. offContext.beginPath();
25. offContext.moveTo(this.start.x, this.start.y);
26. offContext.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
27. offContext.stroke();

29. // 起点和终点
30. offContext.fillStyle = 'rgb(39,135,217)';
31. offContext.beginPath();
32. offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
33. offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
34. offContext.fill();

36. // 控制点
37. offContext.fillStyle = 'rgb(23,169,141)';
38. offContext.beginPath();
39. offContext.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
40. offContext.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
41. offContext.fill();
42. let image = this.offCanvas.transferToImageBitmap();
43. this.context.transferFromImageBitmap(image);
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/exd5DCU9SZ6ydI6OZhsgbQ/zh-cn_image_0000002622700019.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=E5554FFA7B7BBBCEE110F4629D04C6A7CD733F09F5B4E554BAEECFCA722FB04D)

### quadraticCurveTo

PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. import { Point } from '@kit.TestKit';

4. @Entry
5. @Component
6. struct QuadraticCurveTo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
10. private start: Point = { x: 50, y: 20 };
11. private end: Point = { x: 50, y: 100 };
12. private cp: Point = { x: 230, y: 30 };

14. build() {
15. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
16. Canvas(this.context)
17. .width('100%')
18. .height('100%')
19. .backgroundColor('rgb(213,213,213)')
20. .onReady(() => {
21. let offContext = this.offCanvas.getContext("2d", this.settings);
22. // 二次贝塞尔曲线
23. offContext.beginPath();
24. offContext.moveTo(this.start.x, this.start.y);
25. offContext.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
26. offContext.stroke();

28. // 起始点和结束点
29. offContext.fillStyle = 'rgb(39,135,217)';
30. offContext.beginPath();
31. offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
32. offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
33. offContext.fill();

35. // 控制点
36. offContext.fillStyle = 'rgb(23,169,141)';
37. offContext.beginPath();
38. offContext.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
39. offContext.fill();

41. let image = this.offCanvas.transferToImageBitmap();
42. this.context.transferFromImageBitmap(image);
43. })
44. }
45. .width('100%')
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ex--f6y9Tn2CZhxL5-bv7w/zh-cn_image_0000002592220460.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=F429E7B54F3B05FB3FF62BAD9E4AD15F1E02522A97F020D246D3332CCD00D350)

### arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radius | number | 是 | 弧线的圆半径。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：弧度 |
| endAngle | number | 是 | 弧线的终止弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：弧度 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。  true：逆时针绘制圆弧；false：顺时针绘制圆弧。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Arc {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.arc(100, 75, 50, 0, 6.28)
19. offContext.stroke()
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/f_pPbqwnQuqnOljbxj_tIw/zh-cn_image_0000002592380392.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=F2DC982F3BC68EBE1872B0920CFC5EE386869F80191D5DC5207360971C4D2EAA)

### arcTo

PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据给定的控制点和圆弧半径创建圆弧路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 第一个控制点的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y1 | number | 是 | 第一个控制点的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x2 | number | 是 | 第二个控制点的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y2 | number | 是 | 第二个控制点的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radius | number | 是 | 圆弧的圆半径值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ArcTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)

18. // 切线
19. offContext.beginPath()
20. offContext.strokeStyle = '#808080'
21. offContext.lineWidth = 1.5;
22. offContext.moveTo(360, 20);
23. offContext.lineTo(360, 170);
24. offContext.lineTo(110, 170);
25. offContext.stroke();

27. // 圆弧
28. offContext.beginPath()
29. offContext.strokeStyle = '#000000'
30. offContext.lineWidth = 3;
31. offContext.moveTo(360, 20)
32. offContext.arcTo(360, 170, 110, 170, 150)
33. offContext.stroke()

35. // 起始点
36. offContext.beginPath();
37. offContext.fillStyle = '#00ff00';
38. offContext.arc(360, 20, 4, 0, 2 * Math.PI);
39. offContext.fill();

41. // 控制点
42. offContext.beginPath();
43. offContext.fillStyle = '#ff0000';
44. offContext.arc(360, 170, 4, 0, 2 * Math.PI);
45. offContext.arc(110, 170, 4, 0, 2 * Math.PI);
46. offContext.fill();

48. let image = this.offCanvas.transferToImageBitmap()
49. this.context.transferFromImageBitmap(image)
50. })
51. }
52. .width('100%')
53. .height('100%')
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/16W3_qouSkCiii44z2Dm8g/zh-cn_image_0000002622859903.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=A909896758A6CFC80B7DB646B6BD0544097AEDD0DEA78DAD683E9CE6BD4F6804)

此示例中，arcTo()创建的圆弧为黑色，圆弧的两条切线为灰色。控制点为红色，起始点为绿色。

可以想象两条切线：一条切线从起始点到第一个控制点，另一条切线从第一个控制点到第二个控制点。arcTo()在这两条切线间创建一个圆弧，并使圆弧与这两条切线都相切。

### ellipse

PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

在规定的矩形区域绘制一个椭圆。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| rotation | number | 是 | 椭圆的旋转角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位为弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位为弧度。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位为弧度。 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。  true：逆时针方向绘制椭圆。  false：顺时针方向绘制椭圆。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let offContext = this.offCanvas.getContext("2d", this.settings)
16. offContext.beginPath()
17. offContext.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
18. offContext.stroke()
19. offContext.beginPath()
20. offContext.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
21. offContext.stroke()
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/IWmBrepiRB6fX5rDqofJ-A/zh-cn_image_0000002592380352.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=4F68CF1A80B008BCED38E6E7E455CDFCADDD1641BFD94DA4FC5BA4956B61D9B3)

### rect

PhonePC/2in1TabletTVWearable

rect(x: number, y: number, w: number, h: number): void

创建矩形路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
18. offContext.stroke()
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/ApRydiG5QFukJOo0owlqqw/zh-cn_image_0000002622700021.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=9BD747742B63C151D33B08152D3FC758ECD6D69C930C588FF639EB13485F6C6B)

### roundRect20+

PhonePC/2in1TabletTVWearable

roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[0, Canvas宽度)。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[0, Canvas高度)。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度，设置负值为向左绘制。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[-x, Canvas宽度 - x]。  默认单位：vp |
| h | number | 是 | 指定矩形的高度，设置负值为向上绘制。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[-y, Canvas高度 - y]。  默认单位：vp |
| radii | number | Array<number> | 否 | 指定用于矩形角的圆弧半径的数字或列表。  参数类型为number时，所有矩形角的圆弧半径按该数字执行。  参数类型为Array<number>时，数目为1-4个按下面执行：  1. [所有矩形角的圆弧半径]  2. [左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径]  3. [左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径]  4. [左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径]  radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。  默认值：0，null和undefined按默认值处理。  圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。  默认单位：vp |

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](../../../错误码/UI界面/Canvas组件错误码/errorcode-canvas.md)。

| 错误码ID | 错误信息 | 可能原因 |
| --- | --- | --- |
| 103701 | Parameter error. | 1. The param radii is a list that has zero or more than four elements; 2. The param radii contains negative value. |

**示例：**

该示例展示了绘制六个圆角矩形：

1. 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
2. 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
3. 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形并描边；
4. 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形并描边；
5. 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边；
6. 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct CanvasExample {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. try {
20. offContext.fillStyle = '#707070'
21. offContext.beginPath()
22. // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
23. offContext.roundRect(10, 10, 100, 100, 10)
24. // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
25. offContext.roundRect(120, 10, 100, 100, [10])
26. offContext.fill()
27. offContext.beginPath()
28. // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
29. offContext.roundRect(10, 120, 100, 100, [10, 20])
30. // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
31. offContext.roundRect(120, 120, 100, 100, [10, 20, 30])
32. // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
33. offContext.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
34. // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
35. offContext.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
36. offContext.stroke()
37. } catch (error) {
38. let e: BusinessError = error as BusinessError;
39. console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
40. }
41. // 在离屏画布最近渲染的图像上创建一个ImageBitmap对象
42. let image = this.offCanvas.transferToImageBitmap()
43. // 将创建的ImageBitmap对象显示在Canvas画布上
44. this.context.transferFromImageBitmap(image)
45. })
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/EM-18Nk5QsWFMJ0yQmJN4Q/zh-cn_image_0000002622699981.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=E533D34FA74E9174FAB040001220E4611E84A6EE3895F2B7D7CAB6BCF808DCF9)

### fill

PhonePC/2in1TabletTVWearable

fill(fillRule?: CanvasFillRule): void

对当前路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要填充对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Fill {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = '#000000'
18. offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
19. offContext.fill()
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/rF0b8nesQwqMjjHW3Z0enQ/zh-cn_image_0000002592220462.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=FEBCB613DBE660151728ECC9BBC612A1E4432BB35BB69E78722D7A3CA9490C36)

### fill

PhonePC/2in1TabletTVWearable

fill(path: Path2D, fillRule?: CanvasFillRule): void

对指定路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path2D](../Path2D/ts-components-canvas-path2d.md) | 是 | Path2D填充路径。  异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要填充对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例:**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Fill {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let region = new Path2D()
18. region.moveTo(30, 90)
19. region.lineTo(110, 20)
20. region.lineTo(240, 130)
21. region.lineTo(60, 130)
22. region.lineTo(190, 20)
23. region.lineTo(270, 90)
24. region.closePath()
25. // Fill path
26. offContext.fillStyle = '#00ff00'
27. offContext.fill(region, "evenodd")
28. let image = this.offCanvas.transferToImageBitmap()
29. this.context.transferFromImageBitmap(image)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/jvK9UZ6xQB22jn5NX7dttg/zh-cn_image_0000002592380394.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=D848B2477A0E5CAF84FA098C46083C04E078C9B36F355BFA5CD81EACF8CC2EAC)

### clip

PhonePC/2in1TabletTVWearable

clip(fillRule?: CanvasFillRule): void

设置当前路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要剪切对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Clip {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.rect(0, 0, 100, 200)
18. offContext.stroke()
19. offContext.clip()
20. offContext.fillStyle = "rgb(255,0,0)"
21. offContext.fillRect(0, 0, 200, 200)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/o2I-64WcSgOTL4JNVAdA6Q/zh-cn_image_0000002622859865.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=4825B3C3168512BDA18863080A887336563192575BF0F5C720A3E15105B1F22A)

### clip

PhonePC/2in1TabletTVWearable

clip(path: Path2D, fillRule?: CanvasFillRule): void

设置指定路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| path | [Path2D](../Path2D/ts-components-canvas-path2d.md) | 是 | Path2D剪切路径。  异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](../CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要剪切对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Clip {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let region = new Path2D()
18. region.moveTo(30, 90)
19. region.lineTo(110, 20)
20. region.lineTo(240, 130)
21. region.lineTo(60, 130)
22. region.lineTo(190, 20)
23. region.lineTo(270, 90)
24. region.closePath()
25. offContext.clip(region,"evenodd")
26. offContext.fillStyle = "rgb(0,255,0)"
27. offContext.fillRect(0, 0, 600, 600)
28. let image = this.offCanvas.transferToImageBitmap()
29. this.context.transferFromImageBitmap(image)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/cdWSpBAgSXyW9CyUEodkgg/zh-cn_image_0000002622699983.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=C3093B95AB02D9028DE42322C4E419EDDCB75E944157F77C16D1C871233EF05A)

### reset12+

PhonePC/2in1TabletTVWearable

reset(): void

将OffscreenCanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Reset {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = '#0000ff'
18. offContext.fillRect(20, 20, 150, 100)
19. offContext.reset()
20. offContext.fillRect(20, 150, 150, 100)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/XKD0lJtFQdSV8QCc62_tqQ/zh-cn_image_0000002592220422.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=6FE067E2FE932D5EEF64463FA535CF0E3980B2CEED8414C9BBBD8C0A924933FE)

### saveLayer12+

PhonePC/2in1TabletTVWearable

saveLayer(): void

创建一个图层。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct saveLayer {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = "#0000ff"
18. offContext.fillRect(50, 100, 300, 100)
19. offContext.fillStyle = "#00ffff"
20. offContext.fillRect(50, 150, 300, 100)
21. offContext.globalCompositeOperation = 'destination-over'
22. offContext.saveLayer()
23. offContext.globalCompositeOperation = 'source-over'
24. offContext.fillStyle = "#ff0000"
25. offContext.fillRect(100, 50, 100, 300)
26. offContext.fillStyle = "#00ff00"
27. offContext.fillRect(150, 50, 100, 300)
28. offContext.restoreLayer()
29. let image = this.offCanvas.transferToImageBitmap()
30. this.context.transferFromImageBitmap(image)
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/eiPdBVpdTsm9dMN5BaKGdA/zh-cn_image_0000002592380356.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=00B6F7EFBD64464A9E8418EA7774C0B79AD6D0D46275361CD2F0AF0DF4F0C789)

### restoreLayer12+

PhonePC/2in1TabletTVWearable

restoreLayer(): void

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。restoreLayer示例同saveLayer。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### resetTransform

PhonePC/2in1TabletTVWearable

resetTransform(): void

使用单位矩阵重新设置当前矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ResetTransform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
18. offContext.fillStyle = 'rgb(0,0,255)'
19. offContext.fillRect(0, 0, 100, 100)
20. offContext.resetTransform()
21. offContext.fillStyle = 'rgb(255,0,0)'
22. offContext.fillRect(0, 0, 100, 100)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/SRhZaHM3T5SYE2msVuaICQ/zh-cn_image_0000002622859867.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=770FE04DDE223DC4F0AA5A8CC7EFB52738712685B1B6EBE899BC3F575190895C)

### rotate

PhonePC/2in1TabletTVWearable

rotate(angle: number): void

针对当前坐标轴进行顺时针旋转。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 设置顺时针旋转的弧度值，可以通过 degree \* Math.PI / 180 将角度转换为弧度值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  单位：弧度 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Rotate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.rotate(45 * Math.PI / 180)
18. offContext.fillRect(70, 20, 50, 50)
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qtRXy5WFRNucOMWnQasg4w/zh-cn_image_0000002622859905.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=2C599FEE7E238CFE2642110CBE4863808FD0223CA7671F6B79C74A26E30323B0)

### scale

PhonePC/2in1TabletTVWearable

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| y | number | 是 | 设置垂直方向的缩放值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Scale {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 3
18. offContext.strokeRect(30, 30, 50, 50)
19. offContext.scale(2, 2) // Scale to 200%
20. offContext.strokeRect(30, 30, 50, 50)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/7lfP-_RlRSyyVhKJk3oWOQ/zh-cn_image_0000002592220424.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=32160CD3397F25DACFD20344C09081BE7D3C782BA91A8107A8690758BE739FFF)

### transform

PhonePC/2in1TabletTVWearable

transform(a: number, b: number, c: number, d: number, e: number, f: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = a \* x + c \* y + e
* y' = b \* x + d \* y + f

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| a | number | 是 | scaleX：指定水平缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| b | number | 是 | skewY：指定垂直倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| c | number | 是 | skewX：指定水平倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| d | number | 是 | scaleY：指定垂直缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| e | number | 是 | translateX：指定水平移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |
| f | number | 是 | translateY：指定垂直移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Transform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(112,112,112)'
18. offContext.fillRect(0, 0, 100, 100)
19. offContext.transform(1, 0.5, -0.5, 1, 10, 10)
20. offContext.fillStyle = 'rgb(0,74,175)'
21. offContext.fillRect(0, 0, 100, 100)
22. offContext.transform(1, 0.5, -0.5, 1, 10, 10)
23. offContext.fillStyle = 'rgb(39,135,217)'
24. offContext.fillRect(0, 0, 100, 100)
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/LSjsb5eERGWcnp3Tyq8H9A/zh-cn_image_0000002592380358.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=D2B32676B854FBE855BCB015278648C95E5C02EA256510473A9F204115E80FB4)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = a \* x + c \* y + e
* y' = b \* x + d \* y + f

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| a | number | 是 | scaleX：指定水平缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| b | number | 是 | skewY：指定垂直倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| c | number | 是 | skewX：指定水平倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| d | number | 是 | scaleY：指定垂直缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| e | number | 是 | translateX：指定水平移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |
| f | number | 是 | translateY：指定垂直移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SetTransform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(255,0,0)'
18. offContext.fillRect(0, 0, 100, 100)
19. offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
20. offContext.fillStyle = 'rgb(0,0,255)'
21. offContext.fillRect(0, 0, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/IZtcmaz1RYara91Sc-ut7Q/zh-cn_image_0000002622700023.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=3E20C467A738001A7FBB8E2CDB011C40E1CA38B9F6B92312DF40EDC7B9085263)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(transform?: Matrix2D): void

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| transform | [Matrix2D](../Matrix2D/ts-components-canvas-matrix2d.md) | 否 | 变换矩阵。  异常值undefined或null按无效值处理。  默认值：null |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransFormDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offcontext1: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);
8. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offcontext2: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Text('context1');
14. Canvas(this.context1)
15. .width('230vp')
16. .height('160vp')
17. .backgroundColor('#ffff00')
18. .onReady(() => {
19. this.offcontext1.fillRect(100, 20, 50, 50);
20. this.offcontext1.setTransform(1, 0.5, -0.5, 1, 10, 10);
21. this.offcontext1.fillRect(100, 20, 50, 50);
22. let image = this.offcontext1.transferToImageBitmap();
23. this.context1.transferFromImageBitmap(image);
24. })
25. Text('context2');
26. Canvas(this.context2)
27. .width('230vp')
28. .height('160vp')
29. .backgroundColor('#0ffff0')
30. .onReady(() => {
31. this.offcontext2.fillRect(100, 20, 50, 50);
32. let storedTransform = this.offcontext1.getTransform();
33. this.offcontext2.setTransform(storedTransform);
34. this.offcontext2.fillRect(100, 20, 50, 50);
35. let image = this.offcontext2.transferToImageBitmap();
36. this.context2.transferFromImageBitmap(image);
37. })
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/6VQOsvGKQEmK_8Pefyge_w/zh-cn_image_0000002592220464.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=1673FED36D4AA50A3F453EE4AE9E4254015001FD5019900D09271D1B118EA058)

### getTransform

PhonePC/2in1TabletTVWearable

getTransform(): Matrix2D

获取当前被应用到上下文的转换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix2D](../Matrix2D/ts-components-canvas-matrix2d.md) | 当前被应用到上下文的转换矩阵。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransFormDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offcontext1: OffscreenCanvasRenderingContext2D =
8. new OffscreenCanvasRenderingContext2D(600, 100, this.settings);
9. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
10. private offcontext2: OffscreenCanvasRenderingContext2D =
11. new OffscreenCanvasRenderingContext2D(600, 100, this.settings);

13. build() {
14. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
15. Text('context1');
16. Canvas(this.context1)
17. .width('230vp')
18. .height('120vp')
19. .backgroundColor('#ffff00')
20. .onReady(() => {
21. this.offcontext1.fillRect(50, 50, 50, 50);
22. this.offcontext1.setTransform(1.2, Math.PI / 8, Math.PI / 6, 0.5, 30, -25);
23. this.offcontext1.fillRect(50, 50, 50, 50);
24. let image = this.offcontext1.transferToImageBitmap();
25. this.context1.transferFromImageBitmap(image);
26. })
27. Text('context2');
28. Canvas(this.context2)
29. .width('230vp')
30. .height('120vp')
31. .backgroundColor('#0ffff0')
32. .onReady(() => {
33. this.offcontext2.fillRect(50, 50, 50, 50);
34. let storedTransform = this.offcontext1.getTransform();
35. console.info(`Matrix [scaleX = ${storedTransform.scaleX}, scaleY = ${storedTransform.scaleY}, rotateX = ${storedTransform.rotateX}, rotateY = ${storedTransform.rotateY}, translateX = ${storedTransform.translateX}, translateY = ${storedTransform.translateY}]`)
36. this.offcontext2.setTransform(storedTransform);
37. this.offcontext2.fillRect(50, 50, 50, 50);
38. let image = this.offcontext2.transferToImageBitmap();
39. this.context2.transferFromImageBitmap(image);
40. })
41. }
42. .width('100%')
43. .height('100%')
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/JpztSjcEStK3P8CZUswBwQ/zh-cn_image_0000002592220426.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=BDD6E276E7FE96920D931EB5AE3BAECDD00A86D92D721A83728F72C32F73C6E5)

### translate

PhonePC/2in1TabletTVWearable

translate(x: number, y: number): void

移动当前坐标系的原点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |
| y | number | 是 | 设置垂直平移量。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Translate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillRect(10, 10, 50, 50)
18. offContext.translate(70, 70)
19. offContext.fillRect(10, 10, 50, 50)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/PME81gfsRRuIbRbnDs2xXw/zh-cn_image_0000002592380396.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=E1FDCA55ED82FD46B1A3DD7883AEA247DB6F705B46C81383C7EC889246F016FF)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

进行图像绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](../ImageBitmap/ts-components-canvas-imagebitmap.md) | [PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DrawImage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/zvaTnT95Sma6wClmSsOdyg/zh-cn_image_0000002622859907.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=CAD326A63BAF003B2C94D25C880B3C269BCB41B7930715C74FA807EF059F846E)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

将图像拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](../ImageBitmap/ts-components-canvas-imagebitmap.md) | [PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dh | number | 是 | 绘制区域的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DrawImage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0, 300, 300)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/tr7Vz5gdS5emGdtwpHyKUw/zh-cn_image_0000002622700025.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=D57674ECFC0A0506D2D4A78600142D1C845C3BBD58DCED5350A6F707167E71DC)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](../ImageBitmap/ts-components-canvas-imagebitmap.md) | [PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sw | number | 是 | 裁切源图像时需要裁切的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sh | number | 是 | 裁切源图像时需要裁切的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dh | number | 是 | 绘制区域的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DrawImage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Ys6WKMD5Q5eVPYkCGfGPwA/zh-cn_image_0000002592220466.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=5B2347617088C0FF53078AEE4C7853D49ED335282B68B86AE4F843F03B96EE5E)

### createImageData

PhonePC/2in1TabletTVWearable

createImageData(sw: number, sh: number): ImageData

根据当前ImageData对象重新创建一个宽、高相同的ImageData对象，请参考[ImageData](../ImageData/ts-components-canvas-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sw | number | 是 | ImageData的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sh | number | 是 | ImageData的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](../ImageData/ts-components-canvas-imagedata.md) | 新的ImageData对象。 |

### createImageData

createImageData(imageData: ImageData): ImageData

根据已创建的ImageData对象创建新的ImageData对象（不会复制图像数据），请参考[ImageData](../ImageData/ts-components-canvas-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](../ImageData/ts-components-canvas-imagedata.md) | 是 | 被复制的ImageData对象。  异常值undefined和null按width和height为0的ImageData处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](../ImageData/ts-components-canvas-imagedata.md) | 新的ImageData对象。 |

### getPixelMap

PhonePC/2in1TabletTVWearable

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

以当前canvas指定区域内的像素创建[PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sh | number | 是 | 需要输出的区域的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 新的PixelMap对象。 |

**示例：**

说明

* DevEco Studio的预览器不支持显示使用setPixelMap绘制的内容。
* 此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GetPixelMap {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 100, 100, 130, 130)
20. let pixelmap = offContext.getPixelMap(150, 150, 130, 130)
21. offContext.setPixelMap(pixelmap)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/cuarfzKzRwO6W86_kko7Dg/zh-cn_image_0000002592380398.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=F3D1919B2229CBDBA71CCF871DE654ADB82A5C00C8B1B03CDE77559713CEC5E7)

### setPixelMap

PhonePC/2in1TabletTVWearable

setPixelMap(value?: PixelMap): void

将当前传入[PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)对象绘制在画布上。setPixelMap示例同getPixelMap。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PixelMap](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 否 | 包含像素值的PixelMap对象。  异常值undefined和null按无效值处理，不进行绘制。  默认值：null |

### getImageData

PhonePC/2in1TabletTVWearable

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData](../ImageData/ts-components-canvas-imagedata.md)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sh | number | 是 | 需要输出的区域的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](../ImageData/ts-components-canvas-imagedata.md) | 新的ImageData对象。 |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../../../../../harmonyos-guides/构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GetImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. // "/common/images/1234.png"需要替换为开发者所需的图像资源文件
9. private img:ImageBitmap = new ImageBitmap("/common/images/1234.png");

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0, 130, 130)
20. let imageData = offContext.getImageData(50,50,130,130)
21. offContext.putImageData(imageData, 150, 150)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/QeMe6yRhR_SRrDZeFv7AVA/zh-cn_image_0000002622859873.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=544DA9FEA0584A70C288EADD3232F376635577ACF433B19DCA381246639B421D)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

使用[ImageData](../ImageData/ts-components-canvas-imagedata.md)数据填充新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| imageData | [ImageData](../ImageData/ts-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | string10+ | 是 | 填充区域在x轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dy | number | string10+ | 是 | 填充区域在y轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PutImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let imageDataNum = offContext.createImageData(100, 100)
18. let imageData = offContext.createImageData(imageDataNum)
19. for (let i = 0; i < imageData.data.length; i += 4) {
20. imageData.data[i + 0] = 112
21. imageData.data[i + 1] = 112
22. imageData.data[i + 2] = 112
23. imageData.data[i + 3] = 255
24. }
25. offContext.putImageData(imageData, 10, 10)
26. let image = this.offCanvas.transferToImageBitmap()
27. this.context.transferFromImageBitmap(image)
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/eH_FAR1RRTS6nG9mj4aE4w/zh-cn_image_0000002622859909.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=1A1C81B0BCE15EDD4AD3FC915574981CA4ECD85E12801BF8E3B1677A80CD4986)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void

使用[ImageData](../ImageData/ts-components-canvas-imagedata.md)数据裁剪后填充至新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| imageData | [ImageData](../ImageData/ts-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | string10+ | 是 | 填充区域在x轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dy | number | string10+ | 是 | 填充区域在y轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyX | number | string10+ | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyY | number | string10+ | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyWidth | number | string10+ | 是 | 源图像数据矩形裁切范围的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyHeight | number | string10+ | 是 | 源图像数据矩形裁切范围的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PutImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let imageDataNum = offContext.createImageData(100, 100)
18. let imageData = offContext.createImageData(imageDataNum)
19. for (let i = 0; i < imageData.data.length; i += 4) {
20. imageData.data[i + 0] = 112
21. imageData.data[i + 1] = 112
22. imageData.data[i + 2] = 112
23. imageData.data[i + 3] = 255
24. }
25. offContext.putImageData(imageData, 10, 10, 0, 0, 100, 50)
26. let image = this.offCanvas.transferToImageBitmap()
27. this.context.transferFromImageBitmap(image)
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/bURgHlpESQa62_bYc-AA4Q/zh-cn_image_0000002622700027.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=35FA1AF5E58A8CFE9F59412B75A98CFC7D1575CF4AC2DDC2CC86E2A747FCF597)

### setLineDash

setLineDash(segments: number[]): void

设置画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | number[] | 是 | 描述线段如何交替和线段间距长度的数组。  异常值undefined或null按无效值处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SetLineDash {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#D5D5D5')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.arc(100, 75, 50, 0, 6.28)
18. offContext.setLineDash([10, 20])
19. offContext.stroke()
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/mJCW5uHBRU6PZ66IdVmj6Q/zh-cn_image_0000002592220468.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=41171A928DDADAB97CBF8C56DBB3D31D46FE69309C0339F0DF32F5AA78FDF445)

### getLineDash

getLineDash(): number[]

获得当前画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回数组，该数组用来描述线段如何交替和间距长度。  异常值undefined或null按无效值处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasGetLineDash {
5. @State message: string = 'Hello World';
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. Canvas(this.context)
17. .width('100%')
18. .height('100%')
19. .backgroundColor('#D5D5D5')
20. .onReady(() => {
21. let offContext = this.offCanvas.getContext("2d", this.settings)
22. offContext.arc(100, 75, 50, 0, 6.28)
23. offContext.setLineDash([10, 20])
24. offContext.stroke()
25. let res = offContext.getLineDash()
26. this.message = JSON.stringify(res)
27. let image = this.offCanvas.transferToImageBitmap()
28. this.context.transferFromImageBitmap(image)
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/hYypKsuHSymbo8WlCoWS8A/zh-cn_image_0000002622859875.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=A59EBB73490D493404E35DEF7A9ED76C9DF110BCC1997698F58C43484FCBDED1)

### toDataURL

PhonePC/2in1TabletTVWearable

toDataURL(type?: string, quality?: any): string

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 否 | 用于指定图像格式。  可选参数为："image/png"，"image/jpeg"，"image/webp"。  异常值undefined或null按默认值处理。  默认值：image/png |
| quality | any | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。  异常值undefined、null、NaN和Infinity按默认值处理。  默认值：0.92 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ToDataURL {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(100, 100);
8. @State dataURL: string = "";

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width(100)
14. .height(100)
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillRect(0, 0, 100, 100)
18. this.dataURL = offContext.toDataURL()
19. })
20. Text(this.dataURL)
21. }
22. .width('100%')
23. .height('100%')
24. .backgroundColor('#ffff00')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/H0pKCHDSTcys1JH6LXDOYw/zh-cn_image_0000002592380400.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=5371370F1B660B9E948C92E05AEB2F20B7FF999D71A94AB472F057B3D8B7CBFF)

### transferToImageBitmap

PhonePC/2in1TabletTVWearable

transferToImageBitmap(): ImageBitmap

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageBitmap](../ImageBitmap/ts-components-canvas-imagebitmap.md) | 存储离屏画布上渲染的像素数据。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PutImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let imageData = offContext.createImageData(100, 100)
18. for (let i = 0; i < imageData.data.length; i += 4) {
19. imageData.data[i + 0] = 112
20. imageData.data[i + 1] = 112
21. imageData.data[i + 2] = 112
22. imageData.data[i + 3] = 255
23. }
24. offContext.putImageData(imageData, 10, 10)
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/VxWpwcewT9OZioRe16BX5Q/zh-cn_image_0000002622859911.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=A7CBB5C17221CDA51F8F9F875D0A8DA3936032F48629AE60BD4DDEB59EDBEC44)

### restore

PhonePC/2in1TabletTVWearable

restore(): void

对保存的绘图上下文进行恢复。

说明

当restore()次数未超出save()次数时，从栈中弹出存储的绘制状态并恢复CanvasRenderingContext2D对象的属性、剪切路径和变换矩阵的值。

当restore()次数超出save()次数时，此方法不做任何改变。

当没有保存状态时，此方法不做任何改变。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.save() // save the default state
18. offContext.fillStyle = "#00ff00"
19. offContext.fillRect(20, 20, 100, 100)
20. offContext.restore() // restore to the default state
21. offContext.fillRect(150, 75, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/ahZjOG87R0uDQV7feoJPLQ/zh-cn_image_0000002592380366.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=8A98389BD8F62B068366FE093B1D6D7766AF2325D50237633FFCBB9B54CB4BC1)

### save

PhonePC/2in1TabletTVWearable

save(): void

对当前的绘图上下文进行保存。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.save() // save the default state
18. offContext.fillStyle = "#00ff00"
19. offContext.fillRect(20, 20, 100, 100)
20. offContext.restore() // restore to the default state
21. offContext.fillRect(150, 75, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/hc18TD0pTdyKMK05tlKeWQ/zh-cn_image_0000002592380366.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=CF8DE250B44866AD60931900E94814F21337DCC987A7625BEB9A01C93BF26022)

### createLinearGradient

PhonePC/2in1TabletTVWearable

createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient

创建一个线性渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起点的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y0 | number | 是 | 起点的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| x1 | number | 是 | 终点的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y1 | number | 是 | 终点的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasGradient](../CanvasGradient/ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreateLinearGradient {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let grad = offContext.createLinearGradient(50,0, 300,100)
18. grad.addColorStop(0.0, 'rgb(39,135,217)')
19. grad.addColorStop(0.5, 'rgb(255,238,240)')
20. grad.addColorStop(1.0, 'rgb(23,169,141)')
21. offContext.fillStyle = grad
22. offContext.fillRect(0, 0, 400, 400)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/1Z0hpH5FT6uHGRaiipPpLQ/zh-cn_image_0000002622699957.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=C29A1C65B4E386F18B3D110DD384980012C3901B4E73C3567463E6A6A6AA6BE0)

### createRadialGradient

PhonePC/2in1TabletTVWearable

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient

创建一个径向渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起始圆的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y0 | number | 是 | 起始圆的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| r0 | number | 是 | 起始圆的半径。必须是非负且有限的。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| x1 | number | 是 | 终点圆的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y1 | number | 是 | 终点圆的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| r1 | number | 是 | 终点圆的半径。必须为非负且有限的。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasGradient](../CanvasGradient/ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreateRadialGradient {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let grad = offContext.createRadialGradient(200,200,50, 200,200,200)
18. grad.addColorStop(0.0, 'rgb(39,135,217)')
19. grad.addColorStop(0.5, 'rgb(255,238,240)')
20. grad.addColorStop(1.0, 'rgb(112,112,112)')
21. offContext.fillStyle = grad
22. offContext.fillRect(0, 0, 440, 440)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/27CuQcGfQQ6Bj4-VDFzZ9Q/zh-cn_image_0000002622859877.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=215684BB511D5A9BE4A4AFB01D4AC9B83CC725A75BFE56D8D41B6B0D4EB5AA08)

### createConicGradient10+

PhonePC/2in1TabletTVWearable

createConicGradient(startAngle: number, x: number, y: number): CanvasGradient

创建一个圆锥渐变色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startAngle | number | 是 | 开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。  异常值undefined和null按0处理，NaN和Infinity按无效值处理。  单位：弧度 |
| x | number | 是 | 圆锥渐变的中心x轴坐标。  异常值undefined和null按0处理，NaN和Infinity按无效值处理。  默认单位：vp |
| y | number | 是 | 圆锥渐变的中心y轴坐标。  异常值undefined和null按0处理，NaN和Infinity按无效值处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasGradient](../CanvasGradient/ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasConicGradientPage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffffff')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let grad = offContext.createConicGradient(0, 50, 80)
18. grad.addColorStop(0.0, '#ff0000')
19. grad.addColorStop(0.5, '#ffffff')
20. grad.addColorStop(1.0, '#00ff00')
21. offContext.fillStyle = grad
22. offContext.fillRect(0, 30, 100, 100)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/lg5ieNfjTASNRwhwjwB7nw/zh-cn_image_0000002622699995.png?HW-CC-KV=V1&HW-CC-Date=20260611T074827Z&HW-CC-Expire=86400&HW-CC-Sign=9DF61D42DC675E382EFA1C621583EDF217F82B8931B06A324C9F749E41B23ACB)
