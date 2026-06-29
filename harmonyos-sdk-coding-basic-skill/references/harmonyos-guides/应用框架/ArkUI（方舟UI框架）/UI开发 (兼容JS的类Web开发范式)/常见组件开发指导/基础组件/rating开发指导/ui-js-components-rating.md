---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-rating
title: rating开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > rating开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T14:33:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a42e1bf6aeff7b889fbdb63fa7e0fc56c4ebcdf28df8312a50c8bee5f69efc40
---
rating是评分组件，用于展示用户对某项内容的评价等级。具体用法请参考[rating](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Full）/基础组件/rating/js-components-basic-rating.md)。

## 创建rating组件

在pages/index目录下的hml文件中创建一个rating组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating></rating>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. display: flex;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .rating {
11. width: 80%;
12. height: 150px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/XLGWbfxIQvuuXJx5Qi76ug/zh-cn_image_0000002622857957.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063338Z&HW-CC-Expire=86400&HW-CC-Sign=9BFCA4DF81E61FCF1C4E9CC35C0F10F6AA62744E1A41C9E945399621CC5C2AAF)

## 设置评分星级

rating组件通过设置numstars和rating属性设置评分条的星级总数和当前评星数。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating numstars="6" rating="5">
4. </rating>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. display: flex;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .rating {
11. width: 80%;
12. height: 150px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/c1RZztwGQPGMSuyI_gR5bQ/zh-cn_image_0000002622698079.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063338Z&HW-CC-Expire=86400&HW-CC-Sign=500D0E34A8D06F87A95AE3EFD1D2251E416BD5A244C783DBDFA17E5EE4577A47)

## 设置评分样式

rating组件通过star-background、star-foreground和star-secondary属性设置单个星级未选择、选中和选中的次级背景图片。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div style="width: 500px;height: 500px;align-items: center;justify-content: center;flex-direction: column;">
4. <rating numstars="5" rating="1" class="myrating" style="width: {{ratewidth}}; height:{{rateheight}};
5. star-background: {{backstar}}; star-secondary: {{secstar}};star-foreground: {{forestar}};rtl-flip: true;">
6. </rating>
7. </div>
8. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
```

```
1. // index.js
2. export default {
3. data: {
4. backstar: 'common/love.png',
5. secstar: 'common/love.png',
6. forestar: 'common/love1.png',
7. ratewidth: '400px',
8. rateheight: '150px'
9. },
10. onInit(){
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/gUynI7jqSHupOidKltEXAw/zh-cn_image_0000002592218518.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063338Z&HW-CC-Expire=86400&HW-CC-Sign=35E117B78D7573E42C578894321168C3DF3EDDA122FB0FAD97CB6D655EB5EE75)

说明

* star-background、star-secondary、star-foreground属性的星级图源必须全部设置，否则默认的星级颜色为灰色，提示图源设置错误。
* star-background、star-secondary、star-foreground属性只支持本地路径图片，图片格式为png和jpg。

## 绑定事件

向rating组件添加change事件，打印当前评分。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating numstars="5" rating="0" onchange="showrating"></rating>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. display: flex;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .rating {
11. width: 80%;
12. height: 150px;
13. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. showrating(e) {
5. promptAction.showToast({
6. message: '当前评分' + e.rating
7. })
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/hirP-ZnjSxu6EfMABvoEOg/zh-cn_image_0000002592378452.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063338Z&HW-CC-Expire=86400&HW-CC-Sign=1C4ED9663A748E7C68A49D3D6E4A90E77E4D595092D2B9CC1DD6066C626E4045)

## 场景示例

开发者可以通过改变开关状态切换星级背景图，通过改变滑动条的值调整星级总数。

```
1. <!-- xxx.hml -->
2. <div style="width: 100%;height:100%;flex-direction: column;align-items: center;background-color: #F1F3F5;">
3. <div style="width: 500px;height: 500px;align-items: center;justify-content: center;flex-direction: column;">
4. <rating numstars="{{stars}}" rating="{{rate}}" stepsize="{{step}}" onchange="showrating" class="myrating"
5. style="width: {{ratewidth}};height:{{rateheight}};star-background: {{backstar}};star-secondary: {{secstar}};
6. star-foreground: {{forestar}};rtl-flip: true;"></rating>
7. </div>
8. <div style="flex-direction: column;width: 80%;align-items: center;">
9. <div style="width: 100%;height: 100px;align-items: center;justify-content: space-around;">
10. <text>替换自定义图片</text>
11. <switch checked="false" showtext="true" onchange="setstar"></switch>
12. </div>
13. <div style="width: 100%;height:120px;margin-top: 50px;margin-bottom: 50px;flex-direction: column;align-items: center;
14. justify-content: space-around;">
15. <text>numstars   {{stars}}</text>
16. <slider id="sli1" min="0" max="10" value="5" step="1" onchange="setnumstars"></slider>
17. </div>
18. <div style="width: 100%;height:120px;flex-direction: column;align-items: center;justify-content: space-around;">
19. <text>rating   {{rate}}</text>
20. <slider id="sli2" min="0" max="10" value="{{rate}}" step="0.5" onchange="setrating"></slider>
21. </div>
22. </div>
23. </div>
```

```
1. /* xxx.css */
2. .myrating:active {
3. width: 500px;
4. height: 100px;
5. }
6. .switch{
7. font-size: 40px;
8. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. backstar: '',
6. secstar: '',
7. forestar: '',
8. stars: 5,
9. ratewidth: '300px',
10. rateheight: '60px',
11. step: 0.5,
12. rate: 0
13. },
14. onInit(){
15. },
16. setstar(e) {
17. if (e.checked == true) {
18. this.backstar = '/common/love.png'
19. this.secstar = 'common/love.png'
20. this.forestar = 'common/love1.png'
21. } else {
22. this.backstar = ''
23. this.secstar = ''
24. this.forestar = ''
25. }
26. },
27. setnumstars(e) {
28. this.stars = e.progress
29. this.ratewidth = 60 * parseInt(this.stars) + 'px'
30. },
31. setstep(e) {
32. this.step = e.progress
33. },
34. setrating(e){
35. this.rate = e.progress
36. },
37. showrating(e) {
38. this.rate = e.rating
39. promptAction.showToast({
40. message: '当前评分' + e.rating
41. })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/QcGzHCAmTCynh3yAn6cJgQ/zh-cn_image_0000002622857959.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063338Z&HW-CC-Expire=86400&HW-CC-Sign=2E6A6E42F4B1398E1EB2665A8C36E724491EB4CD22FE7455015094517F1E0D11)
