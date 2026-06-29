---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input
title: 文本输入 (TextInput/TextArea/Search)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本输入 (TextInput/TextArea/Search)
category: harmonyos-guides
scraped_at: 2026-06-11T14:30:43+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:002aea8edd1be118b164b64fe3eafcd47589c82f942804e89a3a47c9d96bc440
---
TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)和[TextArea](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Search/ts-basic-components-search.md)组件的API文档。

说明

仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md)组件。

## 创建输入框

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

```
1. TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

```
1. TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```
1. Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})
```

* 单行输入框。

  ```
  1. TextInput()
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L26-L28)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/P_-0TkmkSuqBGhoVL4nEFw/zh-cn_image_0000002622697767.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=72FCF6B8C2EAACA72361EC66B45068A43073262A003F33C3BE71B3F9E5FBBC5A)
* 多行输入框。

  ```
  1. TextArea()
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L38-L40)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/JQC-l3g0QNGbYfVY4nfWIA/zh-cn_image_0000002592218206.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=BDB25E4D8C788003432739575F4CEC3424DB6C3FD2A2920FD8AFB62A2E63EAD2)
* 多行输入框文字超出一行时会自动折行。

  ```
  1. /* 请将$r('app.string.CreatTextInput_textContent')替换为实际资源文件，在本示例中该资源文件的value值为
  2. * "我是TextArea我是TextArea我是TextArea我是TextArea"
  3. */
  4. TextArea({ text: $r('app.string.CreatTextInput_textContent') })
  5. .width(300)
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L41-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/i44uHsErQmG6UR3-AMUKcw/zh-cn_image_0000002592378140.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=ED8340B2E0B5067A5BC295DDA3B1FF0FD85B26682BA8B8FF525F222F1A10AD80)
* 搜索框。

  ```
  1. Search()
  2. // 请将$r('app.string.Creat_TextInput_Content')替换为实际资源文件，在本示例中该资源文件的value值为"搜索"
  3. .searchButton($r('app.string.Creat_TextInput_Content'))
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L52-L56)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/hFrhfX3STHmpkzqtGbOI9g/zh-cn_image_0000002622857647.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=0A33697763FC4237C4EF5F77E5E2B61E7255499ED2A7EBC22135675C658580D0)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER\_NAME用户名输入模式、NEW\_PASSWORD新密码输入模式、NUMBER\_PASSWORD纯数字密码输入模式、NUMBER\_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#type)属性进行设置：

### 基本输入模式（默认类型）

```
1. TextInput()
2. .type(InputType.Normal)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L27-L30)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/lUwAPhjURYGLxAcU8HgE8w/zh-cn_image_0000002622697769.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=11EAE19593B7EBCF1124CAA22354FCA88B2BACCC77B08821819D99A80B933B45)

### 密码模式

包括Password密码输入模式、NUMBER\_PASSWORD纯数字密码模式、NEW\_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```
1. TextInput()
2. .type(InputType.Password)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L36-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/EdO6lbJrTU-lACYz7l2DmA/zh-cn_image_0000002592218208.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=292B9BFAF785884C7127F40C193AE6665A66AEDD58CBC8AD9127DD0ED7E65F8D)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```
1. TextInput()
2. .type(InputType.Email)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L45-L48)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/k6viNyENQXCWG9R50bxtTw/zh-cn_image_0000002592378142.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=3775EA8EF80FB4A8A9012155F2EE30F87E6660D79B0DDFE661C845922AEB58CC)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```
1. TextInput()
2. .type(InputType.Number)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L54-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WGnVyuFiQsmyCLqfkeKyhw/zh-cn_image_0000002622857649.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=4A3B70FA3525C81ADD649B1BC2F1D686A376DA0C39188A397815E948CCF8995B)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。

```
1. TextInput()
2. .type(InputType.PhoneNumber)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L63-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/miiC0-btRXiACf8MWDvpyA/zh-cn_image_0000002622697771.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=F028278BFF6A8471A49119231266A5942AE1D37F9B1599DDB6495864B96BB46B)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```
1. TextInput()
2. .type(InputType.NUMBER_DECIMAL)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L72-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/GL07g92_R-S54M-6yk5LXA/zh-cn_image_0000002592218210.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=8C143E7CB0D4916573403100C3959A57B7E25406C6BCB0F3B210477229C02590)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```
1. TextInput()
2. .type(InputType.URL)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L81-L84)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/cR5ztAR8TqCtri-KnMrH4A/zh-cn_image_0000002592378144.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=E5FC26257F8663843D9864C588E81AD60E012E1FE5A4B71933EABBDD501E5BCC)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```
1. TextArea()
2. .style(TextContentStyle.DEFAULT)
```

[SetInputMultiTypeStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetInputMultiTypeStyle.ets#L25-L28)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/czJlZtcCSRurZgV1pVwQxw/zh-cn_image_0000002622857651.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=01350001484B8E125C01DC343B470A4CA5DB782F9450C845BC87F6772A23892B)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```
1. TextArea()
2. .style(TextContentStyle.INLINE)
```

[SetInputMultiTypeStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetInputMultiTypeStyle.ets#L32-L35)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/USmhUQkMS4K1o5jIdwySQw/zh-cn_image_0000002622697773.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=4D97E38B0F55658131DF19054E07303BFABA93C241FBC60BB80A745A744D13BE)

## 自定义样式

* 设置无输入时的提示文本。

  ```
  1. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  2. TextInput({ placeholder: $r('app.string.i_am_placeholder') })
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L26-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/lcpP0-S2TGeRGznQ68PRig/zh-cn_image_0000002592218212.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=EBCAD5736271495D430E4E9B183CF20700063A2DE3B48C5E25C7EC6B87039D89)
* 设置输入框当前的文本内容。

  ```
  1. TextInput({
  2. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  3. placeholder: $r('app.string.i_am_placeholder'),
  4. // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
  5. text: $r('app.string.i_am_current_text_content')
  6. })
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L35-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/1kv6LADiTza3rs6i_62TaA/zh-cn_image_0000002592378146.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=F5FE960BD7E35B46897940F20BA7B5AE3CD8C14A331A27E1D694FB89077692EA)
* 添加backgroundColor改变输入框的背景颜色。

  ```
  1. TextInput({
  2. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  3. placeholder: $r('app.string.i_am_placeholder'),
  4. // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
  5. text: $r('app.string.i_am_current_text_content')
  6. })
  7. .backgroundColor(Color.Pink)
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L47-L55)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ygZnRpujSp-BRhcZxm4T3w/zh-cn_image_0000002622857653.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=805DC78E06851B30833C7B7AB03AD306DB4F184EBFBF07514436B118826CB717)

  更丰富的样式可以结合[通用属性](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/ts-component-general-attributes.md)实现。

## 添加事件

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

说明

在密码模式下，设置[showPassword](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#showpassword12)属性时，在[onSecurityStateChange](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。

[onWillInsert](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onwillinsert12)、[onDidInsert](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#ondidinsert12)、[onWillDelete](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onwilldelete12)、[onDidDelete](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#ondiddelete12)回调仅支持系统输入法的场景。

[onWillChange](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onwillchange15)的回调时序晚于[onWillInsert](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onwillinsert12)、[onWillDelete](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onwilldelete12)，早于[onDidInsert](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#ondidinsert12)、[onDidDelete](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#ondiddelete12)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Textcomponent]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'Textcomponent_';

7. @Entry
8. @Component
9. struct TextInputEventAdd {
10. @State text: string = '';
11. @State textStr1: string = '';
12. @State textStr2: string = '';
13. @State textStr3: string = '';
14. @State textStr4: string = '';
15. @State textStr5: string = '';
16. @State textStr6: string = '';
17. @State textStr7: string = '';
18. @State textStr8: string = '';
19. @State textStr9: string = '';
20. @State passwordState: boolean = false;
21. controller: TextInputController = new TextInputController();

23. build() {
24. Row() {
25. Column() {
26. Text(`${this.textStr1}\n${this.textStr2}\n${this.textStr3}
27. \n${this.textStr4}\n${this.textStr5}\n${this.textStr6}
28. \n${this.textStr7}\n${this.textStr8}\n${this.textStr9}`)
29. .fontSize(20)
30. .width('70%')
31. TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
32. .type(InputType.Password)
33. .showPassword(this.passwordState)
34. .onChange((value: string) => {
35. // 文本内容发生变化时触发该回调
36. hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
37. this.textStr1 = `onChange is triggering: ${value}`;
38. })
39. .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
40. // 按下输入法回车键时触发该回调
41. hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
42. this.textStr2 = `onSubmit is triggering: ${enterKey} ${event.text}`;
43. })
44. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
45. // 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调
46. hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
47. this.textStr3 = `onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}`;
48. })
49. .onSecurityStateChange((isShowPassword: boolean) => {
50. // 密码显隐状态切换时，触发该回调
51. hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
52. this.passwordState = isShowPassword;
53. this.textStr4 = `onSecurityStateChange is triggering: ${isShowPassword}`;
54. })
55. .onWillInsert((info: InsertValue) => {
56. // 在将要输入时，触发该回调
57. hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
58. this.textStr5 = `onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
59. return true;
60. })
61. .onDidInsert((info: InsertValue) => {
62. // 在输入完成时，触发该回调
63. hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
64. this.textStr6 = `onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
65. })
66. .onWillDelete((info: DeleteValue) => {
67. // 在将要删除时，触发该回调
68. hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
69. this.textStr7 = `onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
70. return true;
71. })
72. .onDidDelete((info: DeleteValue) => {
73. // 在删除完成时，触发该回调
74. hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
75. this.textStr8 = `onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
76. })
77. .onFocus(() => {
78. // 绑定通用事件，输入框获焦时触发该回调
79. hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
80. this.textStr9 = `onFocus is triggering`;
81. })
82. }.width('100%')
83. }
84. .height('100%')
85. }
86. }
```

[TextInputAddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/TextInputAddEvent.ets#L15-L101)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/NFgq10LwQuSibqpkZSseOg/zh-cn_image_0000002622697775.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=40EBACECC2DFE678C9DEE06632313248A33460F8EAF46CF98897102822798777)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、分享的菜单。

TextInput:

```
1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
2. TextInput({ text: $r('app.string.show_selected_menu') })
```

[SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SelectMenu.ets#L26-L29)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/UJqtEzzgTF-QCJlyFONklQ/zh-cn_image_0000002592218214.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=AD22E2089E2775E810E6A63F99D904E399B3D270AB814740C4AAD3E7E8A828ED)

TextArea:

```
1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
2. TextArea({ text: $r('app.string.show_selected_menu') })
```

[SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SelectMenu.ets#L30-L33)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/ylhFdK3uQf2Z1CDt-m9fYQ/zh-cn_image_0000002592378148.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=6CD0D380209551BD6F069FC74E0901ED2DEBD34B889544763BDD315378E32BE0)

## 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (TextMenuController)/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20>)方法屏蔽文本选择菜单中的所有系统服务菜单项。更多详见[disableSystemServiceMenuItems](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (TextMenuController)/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20>)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md>)的[onCreate](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#oncreate>)和[onDestroy](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#ondestroy>)。

```
1. import { TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct DisableSystemServiceMenuItem {
6. aboutToAppear(): void {
7. // 禁用所有系统服务菜单项
8. TextMenuController.disableSystemServiceMenuItems(true)
9. }

11. aboutToDisappear(): void {
12. // 页面消失时恢复系统服务菜单项
13. TextMenuController.disableSystemServiceMenuItems(false)
14. }

16. build() {
17. Row() {
18. Column() {
19. // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
20. TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
21. .height(60)
22. .fontStyle(FontStyle.Italic)
23. .fontWeight(FontWeight.Bold)
24. .textAlign(TextAlign.Center)
25. .caretStyle({ width: '4vp' })
26. .editMenuOptions({
27. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
28. // menuItems不包含被屏蔽的系统菜单项
29. return menuItems
30. },
31. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
32. return false
33. }
34. })
35. }.width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[DisableSystemServiceMenuItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/disablemenu/DisableSystemServiceMenuItems.ets#L16-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/V1pMe0qdTEa9U-8xkGSq9g/zh-cn_image_0000002622857655.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=4166AEAEFDD1ACC460BF0555039F5047F1215FD628A553CEE1590927DE0FD0C1)

从API version 20开始，支持使用[disableMenuItems](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (TextMenuController)/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20>)方法屏蔽文本选择菜单中指定的系统服务菜单项。更多详见[disableMenuItems](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (TextMenuController)/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20>)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md>)的[onCreate](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#oncreate>)和[onDestroy](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#ondestroy>)。

```
1. import { TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct DisableMenuItem {
6. aboutToAppear(): void {
7. // 禁用搜索，翻译和AI帮写
8. TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI_WRITER])
9. }

11. aboutToDisappear(): void {
12. // 页面消失时恢复系统服务菜单项
13. TextMenuController.disableMenuItems([])
14. }

16. build() {
17. Row() {
18. Column() {
19. // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
20. TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
21. .height(60)
22. .fontStyle(FontStyle.Italic)
23. .fontWeight(FontWeight.Bold)
24. .textAlign(TextAlign.Center)
25. .caretStyle({ width: '4vp' })
26. .editMenuOptions({
27. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
28. // menuItems不包含搜索和翻译
29. return menuItems;
30. },
31. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
32. return false
33. }
34. })
35. }.width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[DisableMenuItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/disablemenu/DisableMenuItems.ets#L16-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/GpAQdE5YSGu2ap6KgnUlBA/zh-cn_image_0000002622697777.png?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=FC97C5F88C3158DC8A46205F4B7F19B55B6488DDEC7D7B9EC2678A7488CCEFF7)

## 自动填充

输入框可以通过[contentType](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#contenttype12)属性设置自动填充类型。

支持的类型请参考[ContentType](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#contenttype12枚举说明)。

```
1. // 请将$r('app.string.Auto_Fill_PlaceHolder')替换为实际资源文件，在本示例中该资源文件的value值为"输入你的邮箱..."
2. TextInput({ placeholder: $r('app.string.Auto_Fill_PlaceHolder') })
3. .width('95%')
4. .height(40)
5. .margin(20)
6. .contentType(ContentType.EMAIL_ADDRESS)
```

[AutoFill.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/AutoFill.ets#L25-L32)

## 设置属性

* 设置省略属性。

  输入框可以通过[ellipsisMode](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#ellipsismode18)属性设置省略位置。

  ellipsisMode属性需要配合[textOverflow](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。

  ```
  1. // 请将$r('app.string.Set_Omission_Property_textContent')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示省略模式"
  2. TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })
  3. .textOverflow(TextOverflow.Ellipsis)
  4. .ellipsisMode(EllipsisMode.END)
  5. .style(TextInputStyle.Inline)
  6. .fontSize(30)
  7. .margin(30)
  ```

  [SetProperty.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetProperty.ets#L26-L34)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/aw9vW8gLRSKnlVNCHW2-ag/zh-cn_image_0000002592218216.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=D06072E6B70B2D40E471706DDB85660D6E5E5A81B270B1DB94EF101212B44AE8)
* 设置文本描边属性。

  从API version 20开始，输入框可以通过[strokeWidth](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#strokewidth20)和[strokeColor](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#strokecolor20)属性设置文本的描边宽度及颜色。

  ```
  1. TextInput({ text: 'Text with stroke' })
  2. .width('100%')
  3. .height(60)
  4. .borderWidth(1)
  5. .fontSize(40)
  6. .strokeWidth(LengthMetrics.px(3.0))
  7. .strokeColor(Color.Red)
  ```

  [SetProperty.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetProperty.ets#L39-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Emu9a9eHRTSEezSeT9yOsQ/zh-cn_image_0000002592378150.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=8F6421418BB3E951F2C2551A099A25C075E23C4834978A1CE0E1F5253BDB329A)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Text/ts-basic-components-text.md#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/文本组件公共接口/ts-text-common.md#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```
1. TextArea({
2. text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
3. })
4. .fontSize(22)
5. .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

[SetTextMargin.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextMargin.ets#L26-L32)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/D0Q__5NwRlqzXKoL95WBmg/zh-cn_image_0000002622857657.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=E899DE42E509DDE468F4D292660B1125819A2BFBA2B4FB168A63D7464329CB7F)

## 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)、[List](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)、[Grid](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)。

```
1. @Entry
2. @Component
3. struct KeyboardAvoid {
4. placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7'];

6. build() {
7. Scroll() {
8. Column() {
9. ForEach(this.placeHolderArr, (placeholder: string) => {
10. TextInput({ placeholder: 'TextInput ' + placeholder })
11. .margin(30)
12. // ···
13. })
14. }
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

[KeyboardAvoidance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/KeyboardAvoidance.ets#L18-L40)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/gDywKX6FTa-AJUvdG1goqQ/zh-cn_image_0000002622697779.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=1836A1F334849FD42360556C1BFD1D4C97FCFE932471EC4637836245D6CA8BFD)

## 光标避让

[keyBoardAvoidMode](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Enums/arkts-apis-uicontext-e.md#keyboardavoidmode11>)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET\_WITH\_CARET和RESIZE\_CARET替换原有的OFFSET和RESIZE模式。

对于滚动容器更推荐使用RESIZE\_WITH\_CARET，非滚动容器应该使用OFFSET\_WITH\_CARET。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { window } from '@kit.ArkUI';
3. import { KeyboardAvoidMode } from '@kit.ArkUI';
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/entryability/EntryAbility.ets#L18-L22)

```
1. // Used in UIAbility
2. onWindowStageCreate(windowStage: window.WindowStage): void {
3. // Main window is created, set main page for this ability
4. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

6. windowStage.loadContent('pages/Index', (err, data) => {
7. let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
8. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET_WITH_CARET);
9. if (err.code) {
10. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
11. return;
12. }
13. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
14. });
15. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/entryability/EntryAbility.ets#L38-L54)

```
1. @Entry
2. @Component
3. struct CursorAvoid {
4. @State caretPosition: number = 600;
5. areaController: TextAreaController = new TextAreaController();
6. text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
7. ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
8. 'anything that makes ourselves unhappy,' +
9. ' totally forgetting that there is something happy in our own life.\
10. So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
11. 'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\
12. If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
13. 'Happiness is just what you think will make you happy.' +
14. 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
15. 'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
16. 'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\
17. ';

19. build() {
20. Scroll() {
21. Column() {
22. Row() {
23. Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
24. this.caretPosition += 1;
25. }).fontSize(10)
26. Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
27. this.caretPosition -= 1;
28. }).fontSize(10)
29. Button('SetCaretPosition: ').onClick(() => {
30. this.areaController.caretPosition(this.caretPosition);
31. }).fontSize(10)
32. }

34. TextArea({ text: this.text, controller: this.areaController })
35. .width('100%')
36. .fontSize('20fp')
37. }
38. }.width('100%').height('100%')
39. }
40. }
```

[CursorAvoidance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CursorAvoidance.ets#L18-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/mqqJmjiJSbu1C8tO7YXx6g/zh-cn_image_0000002592218218.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=4E9A04766D48D0693FB6EE5739F42025DFBE9A3064F658A86F7ED7EDBE2495D5)

## 常见问题

### 如何设置TextArea的文本最少展示行数并自适应高度

**问题现象**

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

**解决措施**

设置[minLines](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#constraintsize)自行计算高度。

```
1. import { MeasureUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TextExample {
6. private textAreaPadding = 12;
7. private setMaxLines = 3;
8. private resourceManager = this.getUIContext().getHostContext()?.resourceManager;
9. // 请在resources\base\element\string.json文件中配置name为'NormalQuestion_change'，value为非空字符串的资源
10. private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion_change') as string;
11. @State fullText: string = this.changeText;
12. @State originText: string = this.changeText;
13. @State uiContext: UIContext = this.getUIContext();
14. @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
15. textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
16. textContent: this.originText,
17. fontSize: 18
18. });

20. build() {
21. Column() {
22. TextArea({ text: 'minLines: ' + this.fullText })
23. .fontSize(18)
24. .width(300)
25. .minLines(3)

27. Blank(50)

29. TextArea({ text: 'constraintSize: ' + this.fullText })
30. .fontSize(18)
31. .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
32. .width(300)
33. .height('auto')
34. .constraintSize({
35. // 结合padding计算，设置至少显示this.setMaxLines行文本
36. // 若涉及适老化字号缩放，需要监听并调整高度
37. minHeight: this.textAreaPadding * 2 +
38. this.setMaxLines * this.getUIContext().px2vp(Number(this.textSize.height))
39. })

41. Blank(50)
42. // 请将$r('app.string.NormalQuestion_AddInput')替换为实际资源文件，在本示例中该资源文件的value值为"增加输入"
43. Button($r('app.string.NormalQuestion_AddInput'))
44. .onClick(() => {
45. this.fullText += this.changeText;
46. })
47. }
48. .justifyContent(FlexAlign.Center)
49. .width('100%')
50. .padding({ top: 30 })
51. }
52. }
```

[NormalQuestion.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/NormalQuestion.ets#L15-L68)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Gl2uOU32QJGd-qnfhS7blQ/zh-cn_image_0000002592378152.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063042Z&HW-CC-Expire=86400&HW-CC-Sign=7D19C1E37AE6FB7FF074F022F6857055F368E4D6F5F50C44B5076953ABFF2287)
