---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog
title: 日历选择器弹窗 (CalendarPickerDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 日历选择器弹窗 (CalendarPickerDialog)
category: harmonyos-references
scraped_at: 2026-06-11T15:49:14+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:45d7d878162b2501d5d3cce2f7305e8f66a434d2029ebfe429533f04ebf8432a
---
点击日期弹出日历选择器弹窗，可在弹窗内选择日期。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI系统场景化能力/使用UI上下文接口操作界面（UIContext）/arkts-global-interface.md#ui上下文不明确>)的地方使用，参见[UIContext](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)说明。
* 本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。

## CalendarPickerDialog

PhonePC/2in1TabletTVWearable

### show

PhonePC/2in1TabletTVWearable

static show(options?: CalendarDialogOptions): void

定义日历选择器弹窗。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CalendarDialogOptions](ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明) | 否 | 配置日历选择器弹窗参数。 |

## CalendarDialogOptions对象说明

PhonePC/2in1TabletTVWearable

日历选择器弹窗选项。

继承自[CalendarOptions](../../按钮与选择/CalendarPicker/ts-basic-components-calendarpicker.md#calendaroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onAccept | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<Date> | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。  回调函数的参数表示选中的日期值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCancel | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onChange | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<Date> | 否 | 是 | 选择弹窗中日期使当前选中项改变时触发该回调。  回调函数的参数表示选中的日期值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下，获焦时阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦时为ShadowStyle.OUTER\_FLOATING\_SM。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。  - true：响应悬停态。  - false：不响应悬停态。  默认值：false  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](../../通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| markToday19+ | boolean | 否 | 是 | 设置日历选择器弹窗中系统当前日期是否保持高亮显示。  - true：系统当前日期在日历选择器弹窗内保持高亮显示。  - false：系统当前日期在日历选择器弹窗内不保持高亮显示。  默认值：false  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

说明

在应用窗口缩小过程中，弹窗的宽度会被不断压缩，当缩小到一定程度时会导致其内容无法完整显示，保证CalendarPickerDialog内容能够完整显示的最小窗口宽度为386vp。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置弹窗背板）

该示例通过[CalendarDialogOptions](ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)的backgroundColor、backgroundBlurStyle、shadow设置日历选择器弹窗背板。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CalendarPickerDialogExample {
5. private selectedDate: Date = new Date('2024-03-24');

7. build() {
8. Column() {
9. Button('Show CalendarPicker Dialog')
10. .margin(20)
11. .onClick(() => {
12. console.info('CalendarDialog.show');
13. CalendarPickerDialog.show({
14. selected: this.selectedDate,
15. backgroundColor: Color.Gray,
16. backgroundBlurStyle: BlurStyle.NONE,
17. shadow: ShadowStyle.OUTER_FLOATING_SM,
18. onAccept: (value) => {
19. // 点击弹窗中的“确定”按钮时触发该回调，value表示选中的日期值。
20. this.selectedDate = value;
21. console.info('calendar onAccept:' + JSON.stringify(value));
22. },
23. onCancel: () => {
24. // 点击弹窗中的“取消”按钮时触发该回调。
25. console.info('calendar onCancel');
26. },
27. onChange: (value) => {
28. // 选择弹窗中日期使当前选中项改变时触发该回调，value表示选中的日期值。
29. console.info('calendar onChange:' + JSON.stringify(value));
30. },
31. onDidAppear: () => {
32. console.info('calendar onDidAppear');
33. },
34. onDidDisappear: () => {
35. console.info('calendar onDidDisappear');
36. },
37. onWillAppear: () => {
38. console.info('calendar onWillAppear');
39. },
40. onWillDisappear: () => {
41. console.info('calendar onWillDisappear');
42. }
43. });
44. })
45. }.width('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Q6o6CLH9S4exndpzGvPEkA/zh-cn_image_0000002622859961.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=16CE5FBA1B2B233ED947FB90E30B34EFCF15846E7678174F768392C1712067FA)

### 示例2（自定义按钮样式）

从API version 12开始，该示例通过配置[CalendarDialogOptions](ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)的acceptButtonStyle、cancelButtonStyle实现自定义日历选择器弹窗按钮样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CalendarPickerDialogExample {
5. private selectedDate: Date = new Date();

7. build() {
8. Column() {
9. Button('Show CalendarPicker Dialog')
10. .margin(20)
11. .onClick(() => {
12. console.info('CalendarDialog.show');
13. CalendarPickerDialog.show({
14. selected: this.selectedDate,
15. acceptButtonStyle: {
16. type: ButtonType.Normal,
17. style: ButtonStyleMode.NORMAL,
18. role: ButtonRole.NORMAL,
19. fontColor: 'rgb(81, 81, 216)',
20. fontSize: '26fp',
21. fontWeight: FontWeight.Bolder,
22. fontStyle: FontStyle.Normal,
23. fontFamily: 'sans-serif',
24. backgroundColor: '#A6ACAF',
25. borderRadius: 20
26. },
27. cancelButtonStyle: {
28. type: ButtonType.Normal,
29. style: ButtonStyleMode.NORMAL,
30. role: ButtonRole.NORMAL,
31. fontColor: Color.Blue,
32. fontSize: '16fp',
33. fontWeight: FontWeight.Normal,
34. fontStyle: FontStyle.Italic,
35. fontFamily: 'sans-serif',
36. backgroundColor: '#50182431',
37. borderRadius: 10
38. },
39. onAccept: (value) => {
40. this.selectedDate = value;
41. console.info('calendar onAccept:' + JSON.stringify(value));
42. }
43. });
44. })
45. }.width('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/pSf7QqRFRxiK8ORCmNQBnA/zh-cn_image_0000002622700079.png?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=BC5B5634B13F5C4D1DB9AEFDD72BCF3E04ED4E97A7DBA45F7A0AD012B0BA5F5C)

### 示例3（悬停态弹窗）

从API version 14开始，该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. @Entry
2. @Component
3. struct CalendarPickerDialogExample {
4. private selectedDate: Date = new Date('2024-04-23');

6. build() {
7. Column() {
8. Button('Show CalendarPicker Dialog')
9. .margin(20)
10. .onClick(() => {
11. console.info('CalendarDialog.show');
12. CalendarPickerDialog.show({
13. selected: this.selectedDate,
14. onAccept: (value) => {
15. console.info('calendar onAccept:' + JSON.stringify(value));
16. },
17. onCancel: () => {
18. console.info('calendar onCancel');
19. },
20. onChange: (value) => {
21. console.info('calendar onChange:' + JSON.stringify(value));
22. },
23. onDidAppear: () => {
24. console.info('calendar onDidAppear');
25. },
26. onDidDisappear: () => {
27. console.info('calendar onDidDisappear');
28. },
29. onWillAppear: () => {
30. console.info('calendar onWillAppear');
31. },
32. onWillDisappear: () => {
33. console.info('calendar onWillDisappear');
34. },
35. enableHoverMode: true,
36. hoverModeArea: HoverModeAreaType.TOP_SCREEN,
37. });
38. })
39. }.width('100%')
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/b3Ci0l8AQ5mB-03hlRT5SA/zh-cn_image_0000002592220520.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=3F383C8559EFA1B3517DF1C45238B4F746FDE9338853437636B598047151BB21)

### 示例4（设置日期选中态底板样式）

从API version 10开始，该示例通过[CalendarOptions](../../按钮与选择/CalendarPicker/ts-basic-components-calendarpicker.md#calendaroptions对象说明)的hintRadius设置日期选中态底板样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CalendarPickerDialogExample {
5. private selectedDate: Date = new Date('2024-04-23');

7. build() {
8. Column() {
9. Button('Show CalendarPicker Dialog')
10. .margin(20)
11. .onClick(() => {
12. console.info('CalendarDialog.show');
13. CalendarPickerDialog.show({
14. selected: this.selectedDate,
15. hintRadius: 1,
16. onAccept: (value) => {
17. this.selectedDate = value;
18. console.info('calendar onAccept:' + JSON.stringify(value));
19. }
20. });
21. })
22. }.width('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/YmdGFZS0RmaVMRZaC2lh1g/zh-cn_image_0000002592380452.png?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=F6DD5F62C2D64DC61B58C6B5CD0781EEAE7EDDB5D643321149FE00D27F7B0588)

### 示例5（设置开始日期和结束日期）

从API version 18开始，该示例通过[CalendarOptions](../../按钮与选择/CalendarPicker/ts-basic-components-calendarpicker.md#calendaroptions对象说明)的start和end设置日历选择器弹窗的开始日期和结束日期。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CalendarPickerDialogExample {
5. private selectedDate: Date = new Date('2025-01-01');
6. private startDate: Date = new Date('2024-01-10');
7. private endDate: Date = new Date('2025-01-10');

9. build() {
10. Column() {
11. Text('月历日期选择器').fontSize(30)
12. Button('Show CalendarPicker Dialog')
13. .margin(20)
14. .onClick(() => {
15. console.info('CalendarDialog.show');
16. CalendarPickerDialog.show({
17. start: this.startDate,
18. end: this.endDate,
19. selected: this.selectedDate,
20. });
21. })
22. }.width('100%').margin({ top: 350 })
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4ATg7LrBSjKoI2XmsuN4gQ/zh-cn_image_0000002622859963.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=60A2B556425C0747A5525BDC3B631A275BFBCBD087D25CDC2CF26297A7BFB221)

### 示例6（设置系统当前日期在日历选择器弹窗内保持高亮显示，并设置禁用日期区间）

从API version 19开始，该示例通过配置[CalendarDialogOptions](ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)的markToday，使系统当前日期在日历选择器弹窗内保持高亮显示，并通过配置[CalendarOptions](../../按钮与选择/CalendarPicker/ts-basic-components-calendarpicker.md#calendaroptions对象说明)的disabledDateRange设置禁用的日期区间。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CalendarPickerExample {
5. private disabledDateRange: DateRange[] = [
6. { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
7. { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
8. { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
9. { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
10. { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
11. ];

13. build() {
14. Column() {
15. Button("Show CalendarPicker Dialog")
16. .margin(20)
17. .onClick(() => {
18. console.info('CalendarDialog.show');
19. CalendarPickerDialog.show({ markToday: true, disabledDateRange: this.disabledDateRange });
20. })
21. }.width('100%').margin({ top: 350 })
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/5FhIzMioRcKMTWJqzF0paA/zh-cn_image_0000002622700081.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=621002C6539B385C161A62C328466742F23BE175466C8B1E5619BDFA5DA4C653)

### 示例7（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)，实现自定义背景模糊效果。

```
1. @Entry
2. @Component
3. struct CalendarPickerDialogExample {
4. private selectedDate: Date = new Date('2025-08-05');

6. build() {
7. Stack({ alignContent: Alignment.Top }) {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. Column() {
11. Button('Show CalendarPicker Dialog')
12. .margin(20)
13. .onClick(() => {
14. CalendarPickerDialog.show({
15. selected: this.selectedDate,
16. hintRadius: 1,
17. backgroundColor: undefined,
18. backgroundBlurStyle: BlurStyle.Thin,
19. backgroundBlurStyleOptions: {
20. colorMode: ThemeColorMode.LIGHT,
21. adaptiveColor: AdaptiveColor.AVERAGE,
22. scale: 1,
23. blurOptions: { grayscale: [20, 20] },
24. },
25. });
26. })
27. }.width('100%')
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/HbyXszzyRFWyweCvQbsNpA/zh-cn_image_0000002592220522.png?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=BDF0848B40663CEACE15F4EABEC0C71641B7800C265C1857573F75E1CDC9FF30)

### 示例8（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)，实现自定义背景效果。

```
1. @Entry
2. @Component
3. struct CalendarPickerDialogExample {
4. private selectedDate: Date = new Date('2025-08-05');

6. build() {
7. Stack({ alignContent: Alignment.Top }) {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. Column() {
11. Button('Show CalendarPicker Dialog')
12. .margin(20)
13. .onClick(() => {
14. CalendarPickerDialog.show({
15. selected: this.selectedDate,
16. hintRadius: 1,
17. backgroundColor: undefined,
18. backgroundBlurStyle: BlurStyle.Thin,
19. backgroundEffect: {
20. radius: 60,
21. saturation: 0,
22. brightness: 1,
23. color: Color.White,
24. blurOptions: { grayscale: [20, 20] }
25. },
26. });
27. })
28. }.width('100%')
29. }
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/vmrMS4niTeyTyn88gS_gZg/zh-cn_image_0000002592380454.png?HW-CC-KV=V1&HW-CC-Date=20260611T074912Z&HW-CC-Expire=86400&HW-CC-Sign=98D1E659057CCC53A2649D864A0F4EB9EFD0F756691BDEE226D2770DD7A10A35)
