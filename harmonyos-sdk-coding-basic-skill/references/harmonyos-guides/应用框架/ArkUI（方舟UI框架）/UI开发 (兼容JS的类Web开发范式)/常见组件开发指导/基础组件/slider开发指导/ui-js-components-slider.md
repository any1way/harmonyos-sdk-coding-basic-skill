---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-slider
title: slider开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > slider开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T14:33:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e1abea27f0c1a828a536c0b67f667aa0ab9c13c6ac12f9c6d2a0992514df6771
---
slider为滑动条组件，用来快速调节音量、亮度等。具体用法请参考[slider](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Full）/基础组件/slider/js-components-basic-slider.md)。

## 创建slider组件

在pages/index目录下的hml文件中创建一个slider组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <slider></slider>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. background-color: #F1F3F5;
6. flex-direction: column;
7. justify-content: center;
8. align-items: center;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ya35-LN4TrOPwmDOexca_w/zh-cn_image_0000002622698081.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063339Z&HW-CC-Expire=86400&HW-CC-Sign=16BA96607067F8DAB87D1B0AD5A1FF165A48CDB43E8C683394F316EC71CB3570)

## 设置样式和属性

slider组件通过color、selected-color、block-color样式分别为滑动条设置背景颜色、已选择颜色和滑块颜色。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <slider class= "sli"></slider>
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
10. .sli{
11. color: #fcfcfc;
12. scrollbar-color: aqua;
13. background-color: #b7e3f3;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/N7xWWcv2SrWIY1xIdsCviw/zh-cn_image_0000002592218520.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063339Z&HW-CC-Expire=86400&HW-CC-Sign=B67964CCE4DB9E30DF083178A891AA4EC0B50BDB358178B4CF2E0A872D71FCD8)

通过添加min、max、value、step、mode属性分别为滑动条设置最小值、最大值、初始值、滑动步长和滑动条样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <slider min="0" max="100" value="1" step="2" mode="inset" showtips="true"></slider>
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
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/GElAZFGeSLe1zWNEwUkZew/zh-cn_image_0000002592378454.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063339Z&HW-CC-Expire=86400&HW-CC-Sign=8A92BB12DBE696E57C6EC61E9FA7D7037379D9EE8677B84F93EF9810BD2E2908)

说明

mode属性为滑动条样式，可选值为：

* outset：滑块在滑杆上。
* inset：滑块在滑杆内。

## 绑定事件

向slider组件添加change事件，添加时需要传入ChangeEvent参数。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text>slider start value is {{startValue}}</text>
4. <text>slider current value is {{currentValue}}</text>
5. <text>slider end value is {{endValue}}</text>
6. <slider min="0" max="100" value="{{value}}" onchange="setValue"></slider>
7. </div>
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
```

```
1. // xxx.js
2. export default {
3. data: {
4. value: 0,
5. startValue: 0,
6. currentValue: 0,
7. endValue: 0,
8. },
9. setValue(e) {
10. if (e.mode === "start") {
11. this.value = e.value;
12. this.startValue = e.value;
13. } else if (e.mode === "move") {
14. this.value = e.value;
15. this.currentValue = e.value;
16. } else if (e.mode === "end") {
17. this.value = e.value;
18. this.endValue = e.value;
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ib7Oi0FQREiZD8rf07jlsw/zh-cn_image_0000002622857961.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063339Z&HW-CC-Expire=86400&HW-CC-Sign=49FB47E1C7051365E94245D4D320EB468EA146418DD3D6C55829B768E5F3B060)

## 场景示例

开发者可以通过调整滑动条的值来改变图片大小，并且动态打印当前图片的宽和高。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <image src="common/landscape3.jpg" style=" width: {{WidthVal}}px;height:{{HeightVal}}px;margin-top: -150px;"></image>
4. <div class="txt">
5. <slider min="0" max="100" value="{{value}}" onchange="setValue"></slider>
6. <text>The width of this picture is {{WidthVal}}</text>
7. <text>The height of this picture is {{HeightVal}}</text>
8. </div>
9. </div>
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
10. .text{
11. flex-direction: column;
12. justify-content: center;
13. align-items: center;
14. position: fixed;
15. top: 65%;
16. }
17. .text{
18. margin-top: 30px;
19. }
```

```
1. // xxx.js
2. export default{
3. data: {
4. value: 0,
5. WidthVal: 200,
6. HeightVal: 200
7. },
8. setValue(e) {
9. this.WidthVal = 200 + e.value;
10. this.HeightVal = 200 + e.value
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/-WPIQnMVRjyBy-OjekCHhg/zh-cn_image_0000002622698083.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063339Z&HW-CC-Expire=86400&HW-CC-Sign=E96BD23C2534CB546DA7CAC60DB309851AB8F470D0061F992476B8DB59B23731)
