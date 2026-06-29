---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-stepper
title: stepper开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > stepper开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T14:33:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:acb30412bc72bca2ac4f5b555c4e883edebd17112c11ba034bce875ab3b28037
---
当一个任务需要多个步骤时，可以使用stepper组件展示当前进展。具体用法请参考[stepper API](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Full）/容器组件/stepper/js-components-container-stepper.md)。

## 创建stepper组件

在pages/index目录下的hml文件中创建一个stepper组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper>
4. <stepper-item>
5. <text>Step 1</text>
6. </stepper-item>
7. <stepper-item>
8. <text>Step 2</text>
9. </stepper-item>
10. </stepper>
11. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. text{
11. width: 100%;
12. height: 100%;
13. text-align: center;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/_QWNOklYTdiYmEpd94Ae2A/zh-cn_image_0000002592218496.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063328Z&HW-CC-Expire=86400&HW-CC-Sign=3C100259BDAAE80E088FD3757DE2608525243C2AAF0008FC20859D7C5BC1D8E1)

## 设置index属性

页面默认显示索引值为index的步骤。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper index="2">
4. <stepper-item>
5. <text>stepper-item1</text>
6. </stepper-item>
7. <stepper-item>
8. <text>stepper-item2</text>
9. </stepper-item>
10. <stepper-item>
11. <text>stepper-item3</text>
12. </stepper-item>
13. </stepper>
14. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. }
8. text{
9. width: 100%;
10. height: 100%;
11. text-align: center;
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/0DAIzw9aTtali1rOpkqcgQ/zh-cn_image_0000002592378430.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063328Z&HW-CC-Expire=86400&HW-CC-Sign=F67D5F6E96E30B46CBCC934E9B38A9D116F30FE472075357B4BA6B5C14B337F9)

通过设置label属性，自定义stepper-item的提示按钮。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper index="1">
4. <stepper-item label="{{label_1}}">
5. <text>stepper-item1</text>
6. </stepper-item>
7. <stepper-item label="{{label_2}}">
8. <text>stepper-item2</text>
9. </stepper-item>
10. <stepper-item label="{{label_3}}">
11. <text>stepper-item3</text>
12. </stepper-item>
13. <stepper-item>
14. <text>stepper-item4</text>
15. </stepper-item>
16. </stepper>
17. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. }
8. text{
9. width: 100%;
10. height: 100%;
11. text-align: center;
12. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. label_1:{
5. nextLabel: 'NEXT',
6. status: 'normal'
7. },
8. label_2:{
9. prevLabel: 'BACK',
10. nextLabel: 'NEXT',
11. status: 'normal'
12. },
13. label_3:{
14. prevLabel: 'BACK',
15. nextLabel: 'END',
16. status: 'disabled'
17. },
18. },
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/0rL0JDdvQd2L9UxxhLY1fg/zh-cn_image_0000002622857937.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063328Z&HW-CC-Expire=86400&HW-CC-Sign=86EF7AFC73A799AC4EECB93C244A2B9181B4FFC9F6626DD0F5FCEA60EC9D93FA)

## 设置样式

stepper组件默认填充父容器，通过border和background-color设置边框、背景色。

```
1. <!-- xxx.hml -->
2. <div class="container" >
3. <div class="stepperContent">
4. <stepper class="stepperClass">
5. <stepper-item>
6. <text>stepper-item1</text>
7. </stepper-item>
8. </stepper>
9. </div>
10. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color:#F1F3F5;
9. }
10. .stepperContent{
11. width: 300px;
12. height: 300px;
13. }
14. .stepperClass{
15. border:1px solid silver ;
16. background-color: white;
17. }
18. text{
19. width: 100%;
20. height: 100%;
21. text-align: center;
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/jM6efsBlTsSTeq6Xhq7BJw/zh-cn_image_0000002622698059.png?HW-CC-KV=V1&HW-CC-Date=20260611T063328Z&HW-CC-Expire=86400&HW-CC-Sign=37B24EBBB153CEFF6DE30CF5717263B9FA545B15E4B84C0C8D98F1DB7C9FBF77)

## 添加事件

stepper分别添加finish，change，next，back，skip事件。

* 当change与next或back同时存在时，会先执行next或back事件再去执行change事件。
* 重新设置index属性值时要先清除index的值再重新设置，否则检测不到值的改变。

```
1. <!-- xxx.hml -->
2. <div class="container"  style="background-color:#F1F3F5;">
3. <div >
4. <stepper onfinish="stepperFinish" onchange="stepperChange" onnext="stepperNext" onback="stepperBack" onskip="stepperSkip" id="stepperId" index="{{index}}">
5. <stepper-item>
6. <text>stepper-item1</text>
7. <button value="skip" onclick="skipClick"></button>
8. </stepper-item>
9. <stepper-item>
10. <text>stepper-item2</text>
11. <button value="skip" onclick="skipClick"></button>
12. </stepper-item>
13. <stepper-item>
14. <text>stepper-item3</text>
15. </stepper-item>
16. </stepper>
17. </div>
18. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. }
9. stepper-item{
10. width: 100%;
11. flex-direction: column;
12. align-self: center;
13. justify-content: center;
14. }
15. text{
16. margin-top: 45%;
17. justify-content: center;
18. align-self: center;
19. margin-bottom: 50px;
20. }
21. button{
22. width: 80%;
23. height: 60px;
24. margin-top: 20px;
25. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. index:0,
6. },
7. stepperSkip(){
8. this.index=2;
9. },
10. skipClick(){
11. this.$element('stepperId').setNextButtonStatus({status: 'skip', label: 'SKIP'});
12. },
13. stepperFinish(){
14. promptAction.showToast({
15. message: 'All Finished'
16. })
17. },
18. stepperChange(e){
19. console.info("stepperChange"+e.index)
20. promptAction.showToast({
21. // index表示当前步骤的序号
22. message: 'Previous step: '+e.prevIndex+"-------Current step:"+e.index
23. })
24. },
25. stepperNext(e){
26. console.info("stepperNext"+e.index)
27. promptAction.showToast({
28. // pendingIndex表示将要跳转的序号
29. message: 'Current step:'+e.index+"-------Next step:"+e.pendingIndex
30. })
31. var index = {pendingIndex:e.pendingIndex }
32. return index;
33. },
34. stepperBack(e){
35. console.info("stepperBack"+e.index)
36. var index = {pendingIndex: e.pendingIndex }
37. return index;
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/H68D8XtqQVeSzbPhU_2Jsw/zh-cn_image_0000002592218498.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063328Z&HW-CC-Expire=86400&HW-CC-Sign=825CBF580B3D3655706E43DF9E775CEE1E32421D90CD2A875B87A80B4690ED84)
