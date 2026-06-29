---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-foldsplitcontainer
title: FoldSplitContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FoldSplitContainer
category: harmonyos-references
scraped_at: 2026-06-11T15:50:10+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:96d541d8abbf2eb582b95b306e8744ab9a8965b9d00aae651257b917f91fb634
---
FoldSplitContainer分栏布局，实现折叠屏二分栏、三分栏在展开态、悬停态以及折叠态的区域控制。

说明

* 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 窗口宽度小于等于600vp时默认使用二分栏，窗口宽度大于600vp时在上下分栏的同时可支持扩展区域，窗口宽度大于600vp且在横屏半折状态下可触发悬停态布局。悬停态布局时会增加折痕区的避让并且扩展区域不可以贯穿折痕区，悬停态可设置不展示扩展区域，详情请参考[示例](ohos-arkui-advanced-foldsplitcontainer.md#示例)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FoldSplitContainer } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## FoldSplitContainer

PhonePC/2in1TabletTVWearable

FoldSplitContainer({primary: Callback<void>, secondary: Callback<void>, extra?: Callback<void>, expandedLayoutOptions: ExpandedRegionLayoutOptions, hoverModeLayoutOptions: HoverModeRegionLayoutOptions, foldedLayoutOptions: FoldedRegionLayoutOptions, animationOptions?: AnimateParam | null, onHoverStatusChange?: OnHoverStatusChangeHandler})

实现折叠屏二分栏、三分栏在展开态、悬停态以及折叠态的区域控制的分栏布局。

**装饰器类型：**[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| primary | Callback<void> | 是 | [@BuilderParam](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@BuilderParam装饰器：引用@Builder函数/arkts-builderparam.md>) | 主要区域回调函数。 |
| secondary | Callback<void> | 是 | [@BuilderParam](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@BuilderParam装饰器：引用@Builder函数/arkts-builderparam.md>) | 次要区域回调函数。 |
| extra | Callback<void> | 否 | [@BuilderParam](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/组件扩展/@BuilderParam装饰器：引用@Builder函数/arkts-builderparam.md>) | 扩展区域回调函数，不传入的情况，没有对应区域。 |
| expandedLayoutOptions | [ExpandedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#expandedregionlayoutoptions) | 是 | [@Prop](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md>) | 展开态布局信息。 |
| hoverModeLayoutOptions | [HoverModeRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#hovermoderegionlayoutoptions) | 是 | [@Prop](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md>) | 悬停态布局信息。 |
| foldedLayoutOptions | [FoldedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#foldedregionlayoutoptions) | 是 | [@Prop](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md>) | 折叠态布局信息。 |
| animationOptions | [AnimateParam](<../../动画/显式动画 (animateTo)/ts-explicit-animation.md#animateparam对象说明>) | null | 否 | [@Prop](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md>) | 设置动画效果相关的参数，null表示关闭动效。 |
| onHoverStatusChange | [OnHoverStatusChangeHandler](ohos-arkui-advanced-foldsplitcontainer.md#onhoverstatuschangehandler) | 否 | - | 折叠屏进入或退出悬停模式时触发的回调函数。 |

## ExpandedRegionLayoutOptions

PhonePC/2in1TabletTVWearable

展开态布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isExtraRegionPerpendicular | boolean | 否 | 是 | 设置为true时，扩展区域从上到下贯穿整个组件；设置为false时，扩展区域不贯穿整个组件。此字段仅在extra有效时生效。  默认值：true |
| verticalSplitRatio | number | 否 | 是 | 主要区域与次要区域之间的高度比例。  默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_1V1 |
| horizontalSplitRatio | number | 否 | 是 | 主要区域与扩展区域之间的宽度比例。此字段在extra有效时生效。  默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_3V2 |
| extraRegionPosition | [ExtraRegionPosition](ohos-arkui-advanced-foldsplitcontainer.md#extraregionposition) | 否 | 是 | 扩展区域的位置信息。当isExtraRegionPerpendicular设置为false时，此字段生效。  默认值：ExtraRegionPosition.TOP |

## HoverModeRegionLayoutOptions

PhonePC/2in1TabletTVWearable

悬停态布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showExtraRegion | boolean | 否 | 是 | 可折叠屏幕在半折叠状态下是否显示扩展区域。设置为true时表示显示扩展区域，设置为false时表示不显示扩展区域。  默认值：false |
| horizontalSplitRatio | number | 否 | 是 | 主要区域与扩展区域之间的宽度比例，当且仅当extra有效时此字段才生效。  默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_3V2 |
| extraRegionPosition | [ExtraRegionPosition](ohos-arkui-advanced-foldsplitcontainer.md#extraregionposition) | 否 | 是 | 扩展区域的位置信息，当且仅当showExtraRegion设置为true时此字段才生效。  默认值：ExtraRegionPosition.TOP |

说明

1.在悬停状态下，设备存在避让区域，布局计算时需考虑该区域的影响。

2.在悬停模式下，屏幕上半部分为显示区域，下半部分为操作区域。

## FoldedRegionLayoutOptions

PhonePC/2in1TabletTVWearable

折叠态布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verticalSplitRatio | number | 否 | 是 | 主要区域与次要区域之间的高度比例。默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_1V1 |

## OnHoverStatusChangeHandler

PhonePC/2in1TabletTVWearable

type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void

onHoverStatusChange事件处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | [HoverModeStatus](ohos-arkui-advanced-foldsplitcontainer.md#hovermodestatus) | 是 | 折叠屏进入或退出悬停模式时触发的回调函数。 |

## HoverModeStatus

PhonePC/2in1TabletTVWearable

设备或应用的折叠、旋转、窗口状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foldStatus | [display.FoldStatus](<../../../ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#foldstatus10>) | 否 | 否 | 设备的折叠状态。 |
| isHoverMode | boolean | 否 | 否 | app当前是否处于悬停态。设置为true时表示当前为悬停态，设置为false时表示当前为非悬停态。 |
| appRotation | number | 否 | 否 | 应用旋转角度。 |
| windowStatusType | [window.WindowStatusType](<../../../ArkTS API/窗口管理/@ohos.window (窗口)/Enums/arkts-apis-window-e.md#windowstatustype11>) | 否 | 否 | 窗口模式。 |

## ExtraRegionPosition

PhonePC/2in1TabletTVWearable

扩展区域位置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 1 | 扩展区域在组件上半区域。 |
| BOTTOM | 2 | 扩展区域在组件下半区域。 |

## PresetSplitRatio

PhonePC/2in1TabletTVWearable

区域比例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYOUT\_1V1 | 1 | 1:1比例。 |
| LAYOUT\_3V2 | 1.5 | 3:2比例。 |
| LAYOUT\_2V3 | 0.6666666666666666 | 2:3比例。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置二分栏）

该示例实现了折叠屏二分栏在展开态、悬停态以及折叠态的区域控制。

```
1. import { FoldSplitContainer } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TwoColumns {
6. @Builder
7. privateRegion() {
8. Text("Primary")
9. .backgroundColor('rgba(255, 0, 0, 0.1)')
10. .fontSize(28)
11. .textAlign(TextAlign.Center)
12. .height('100%')
13. .width('100%')
14. }

16. @Builder
17. secondaryRegion() {
18. Text("Secondary")
19. .backgroundColor('rgba(0, 255, 0, 0.1)')
20. .fontSize(28)
21. .textAlign(TextAlign.Center)
22. .height('100%')
23. .width('100%')
24. }

26. build() {
27. RelativeContainer() {
28. FoldSplitContainer({
29. // 主要区域回调函数
30. primary: () => {
31. this.privateRegion()
32. },
33. // 次要区域回调函数
34. secondary: () => {
35. this.secondaryRegion()
36. }
37. })
38. }
39. .height('100%')
40. .width('100%')
41. }
42. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |

### 示例2（设置三分栏）

该示例实现了折叠屏三分栏在展开态、悬停态以及折叠态的区域控制。

```
1. import { FoldSplitContainer } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ThreeColumns {
6. @Builder
7. privateRegion() {
8. Text("Primary")
9. .backgroundColor('rgba(255, 0, 0, 0.1)')
10. .fontSize(28)
11. .textAlign(TextAlign.Center)
12. .height('100%')
13. .width('100%')
14. }

16. @Builder
17. secondaryRegion() {
18. Text("Secondary")
19. .backgroundColor('rgba(0, 255, 0, 0.1)')
20. .fontSize(28)
21. .textAlign(TextAlign.Center)
22. .height('100%')
23. .width('100%')
24. }

26. @Builder
27. extraRegion() {
28. Text("Extra")
29. .backgroundColor('rgba(0, 0, 255, 0.1)')
30. .fontSize(28)
31. .textAlign(TextAlign.Center)
32. .height('100%')
33. .width('100%')
34. }

36. build() {
37. RelativeContainer() {
38. FoldSplitContainer({
39. // 主要区域回调函数
40. primary: () => {
41. this.privateRegion()
42. },
43. // 次要区域回调函数
44. secondary: () => {
45. this.secondaryRegion()
46. },
47. // 扩展区域回调函数
48. extra: () => {
49. this.extraRegion()
50. }
51. })
52. }
53. .height('100%')
54. .width('100%')
55. }
56. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |

### 示例3（展示FoldSplitContainer折叠态、悬停态、展开态下的配置行为）

该示例通过[ExpandedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#expandedregionlayoutoptions)、[HoverModeRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#hovermoderegionlayoutoptions)和[FoldedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#foldedregionlayoutoptions)分别配置折叠屏的展开态、悬停态和折叠态布局信息。示例代码中MajorRegion、MinorRegion和ExtraRegion分别对应组件划分出来的主要区域、次要区域和扩展区域。这些区域使用封装的区域组件Region实现，其中RadioOptions为封装的切换单选框组件，SwitchOption为封装的切换开关组件。

```
1. import { FoldSplitContainer, PresetSplitRatio, ExtraRegionPosition, ExpandedRegionLayoutOptions, HoverModeRegionLayoutOptions, FoldedRegionLayoutOptions } from '@kit.ArkUI';

3. @Component
4. struct Region {
5. @Prop title: string;
6. @BuilderParam content: () => void;
7. @Prop compBackgroundColor: string;

9. build() {
10. Column({ space: 8 }) {
11. Text(this.title)
12. .fontSize("24fp")
13. .fontWeight(600)

15. Scroll() {
16. this.content()
17. }
18. .layoutWeight(1)
19. .width("100%")
20. }
21. .backgroundColor(this.compBackgroundColor)
22. .width("100%")
23. .height("100%")
24. .padding(12)
25. }
26. }

28. const noop = () => {
29. };

31. @Component
32. struct SwitchOption {
33. @Prop label: string = ""
34. @Prop value: boolean = false
35. public onChange: (checked: boolean) => void = noop;

37. build() {
38. Row() {
39. Text(this.label)
40. Blank()
41. Toggle({ type: ToggleType.Switch, isOn: this.value })
42. .onChange((isOn) => {
43. this.onChange(isOn);
44. })
45. }
46. .backgroundColor(Color.White)
47. .borderRadius(8)
48. .padding(8)
49. .width("100%")
50. }
51. }

53. interface RadioOptions {
54. label: string;
55. value: Object | undefined | null;
56. onChecked: () => void;
57. }

59. @Component
60. struct RadioOption {
61. @Prop label: string;
62. @Prop value: Object | undefined | null;
63. @Prop options: Array<RadioOptions>;

65. build() {
66. Row() {
67. Text(this.label)
68. Blank()
69. Column({ space: 4 }) {
70. ForEach(this.options, (option: RadioOptions) => {
71. Row() {
72. Radio({
73. group: this.label,
74. value: JSON.stringify(option.value),
75. })
76. .checked(this.value === option.value)
77. .onChange((checked) => {
78. if (checked) {
79. option.onChecked();
80. }
81. })
82. Text(option.label)
83. }
84. })
85. }
86. .alignItems(HorizontalAlign.Start)
87. }
88. .alignItems(VerticalAlign.Top)
89. .backgroundColor(Color.White)
90. .borderRadius(8)
91. .padding(8)
92. .width("100%")
93. }
94. }

96. @Entry
97. @Component
98. struct Index {
99. // 展开态布局配置
100. @State expandedRegionLayoutOptions: ExpandedRegionLayoutOptions = {
101. horizontalSplitRatio: PresetSplitRatio.LAYOUT_3V2,
102. verticalSplitRatio: PresetSplitRatio.LAYOUT_1V1,
103. isExtraRegionPerpendicular: true,
104. extraRegionPosition: ExtraRegionPosition.TOP
105. };
106. // 悬停态布局配置
107. @State foldingRegionLayoutOptions: HoverModeRegionLayoutOptions = {
108. horizontalSplitRatio: PresetSplitRatio.LAYOUT_3V2,
109. showExtraRegion: false,
110. extraRegionPosition: ExtraRegionPosition.TOP
111. };
112. // 折叠态布局配置
113. @State foldedRegionLayoutOptions: FoldedRegionLayoutOptions = {
114. verticalSplitRatio: PresetSplitRatio.LAYOUT_1V1
115. };

117. @Builder
118. // 主要区域自定义组件
119. MajorRegion() {
120. Region({
121. title: "折叠态配置",
122. compBackgroundColor: "rgba(255, 0, 0, 0.1)",
123. }) {
124. Column({ space: 4 }) {
125. RadioOption({
126. label: "折叠态垂直高度比",
127. value: this.foldedRegionLayoutOptions.verticalSplitRatio,
128. options: [
129. {
130. label: "1:1",
131. value: PresetSplitRatio.LAYOUT_1V1,
132. onChecked: () => {
133. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_1V1
134. }
135. },
136. {
137. label: "2:3",
138. value: PresetSplitRatio.LAYOUT_2V3,
139. onChecked: () => {
140. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_2V3
141. }
142. },
143. {
144. label: "3:2",
145. value: PresetSplitRatio.LAYOUT_3V2,
146. onChecked: () => {
147. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_3V2
148. }
149. },
150. {
151. label: "未定义",
152. value: undefined,
153. onChecked: () => {
154. this.foldedRegionLayoutOptions.verticalSplitRatio = undefined
155. }
156. }
157. ]
158. })
159. }
160. .constraintSize({ minHeight: "100%" })
161. }
162. }

164. @Builder
165. // 次要区域自定义组件
166. MinorRegion() {
167. Region({
168. title: "悬停态配置",
169. compBackgroundColor: "rgba(0, 255, 0, 0.1)"
170. }) {
171. Column({ space: 4 }) {
172. RadioOption({
173. label: "悬停态水平宽度比",
174. value: this.foldingRegionLayoutOptions.horizontalSplitRatio,
175. options: [
176. {
177. label: "1:1",
178. value: PresetSplitRatio.LAYOUT_1V1,
179. onChecked: () => {
180. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_1V1
181. }
182. },
183. {
184. label: "2:3",
185. value: PresetSplitRatio.LAYOUT_2V3,
186. onChecked: () => {
187. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_2V3
188. }
189. },
190. {
191. label: "3:2",
192. value: PresetSplitRatio.LAYOUT_3V2,
193. onChecked: () => {
194. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_3V2
195. }
196. },
197. {
198. label: "未定义",
199. value: undefined,
200. onChecked: () => {
201. this.foldingRegionLayoutOptions.horizontalSplitRatio = undefined
202. }
203. },
204. ]
205. })

207. SwitchOption({
208. label: "悬停态是否显示扩展区",
209. value: this.foldingRegionLayoutOptions.showExtraRegion,
210. onChange: (checked) => {
211. this.foldingRegionLayoutOptions.showExtraRegion = checked;
212. }
213. })

215. if (this.foldingRegionLayoutOptions.showExtraRegion) {
216. RadioOption({
217. label: "悬停态扩展区位置",
218. value: this.foldingRegionLayoutOptions.extraRegionPosition,
219. options: [
220. {
221. label: "顶部",
222. value: ExtraRegionPosition.TOP,
223. onChecked: () => {
224. this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
225. }
226. },
227. {
228. label: "底部",
229. value: ExtraRegionPosition.BOTTOM,
230. onChecked: () => {
231. this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
232. }
233. },
234. {
235. label: "未定义",
236. value: undefined,
237. onChecked: () => {
238. this.foldingRegionLayoutOptions.extraRegionPosition = undefined
239. }
240. },
241. ]
242. })
243. }
244. }
245. .constraintSize({ minHeight: "100%" })
246. }
247. }

249. @Builder
250. // 扩展区域自定义组件
251. ExtraRegion() {
252. Region({
253. title: "展开态配置",
254. compBackgroundColor: "rgba(0, 0, 255, 0.1)"
255. }) {
256. Column({ space: 4 }) {
257. RadioOption({
258. label: "展开态水平宽度比",
259. value: this.expandedRegionLayoutOptions.horizontalSplitRatio,
260. options: [
261. {
262. label: "1:1",
263. value: PresetSplitRatio.LAYOUT_1V1,
264. onChecked: () => {
265. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_1V1
266. }
267. },
268. {
269. label: "2:3",
270. value: PresetSplitRatio.LAYOUT_2V3,
271. onChecked: () => {
272. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_2V3
273. }
274. },
275. {
276. label: "3:2",
277. value: PresetSplitRatio.LAYOUT_3V2,
278. onChecked: () => {
279. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_3V2
280. }
281. },
282. {
283. label: "未定义",
284. value: undefined,
285. onChecked: () => {
286. this.expandedRegionLayoutOptions.horizontalSplitRatio = undefined
287. }
288. },
289. ]
290. })

292. RadioOption({
293. label: "展开态垂直高度比",
294. value: this.expandedRegionLayoutOptions.verticalSplitRatio,
295. options: [
296. {
297. label: "1:1",
298. value: PresetSplitRatio.LAYOUT_1V1,
299. onChecked: () => {
300. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_1V1
301. }
302. },
303. {
304. label: "2:3",
305. value: PresetSplitRatio.LAYOUT_2V3,
306. onChecked: () => {
307. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_2V3
308. }
309. },
310. {
311. label: "3:2",
312. value: PresetSplitRatio.LAYOUT_3V2,
313. onChecked: () => {
314. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_3V2
315. }
316. },
317. {
318. label: "未定义",
319. value: undefined,
320. onChecked: () => {
321. this.expandedRegionLayoutOptions.verticalSplitRatio = undefined
322. }
323. }
324. ]
325. })

327. SwitchOption({
328. label: "展开态扩展区是否上下贯穿",
329. value: this.expandedRegionLayoutOptions.isExtraRegionPerpendicular,
330. onChange: (checked) => {
331. this.expandedRegionLayoutOptions.isExtraRegionPerpendicular = checked;
332. }
333. })

335. if (!this.expandedRegionLayoutOptions.isExtraRegionPerpendicular) {
336. RadioOption({
337. label: "展开态扩展区位置",
338. value: this.expandedRegionLayoutOptions.extraRegionPosition,
339. options: [
340. {
341. label: "顶部",
342. value: ExtraRegionPosition.TOP,
343. onChecked: () => {
344. this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
345. }
346. },
347. {
348. label: "底部",
349. value: ExtraRegionPosition.BOTTOM,
350. onChecked: () => {
351. this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
352. }
353. },
354. {
355. label: "未定义",
356. value: undefined,
357. onChecked: () => {
358. this.expandedRegionLayoutOptions.extraRegionPosition = undefined
359. }
360. },
361. ]
362. })
363. }
364. }
365. .constraintSize({ minHeight: "100%" })
366. }
367. }

369. build() {
370. Column() {
371. FoldSplitContainer({
372. // 主要区域回调函数
373. primary: () => {
374. this.MajorRegion()
375. },
376. // 次要区域回调函数
377. secondary: () => {
378. this.MinorRegion()
379. },
380. // 扩展区域回调函数
381. extra: () => {
382. this.ExtraRegion()
383. },
384. expandedLayoutOptions: this.expandedRegionLayoutOptions,
385. hoverModeLayoutOptions: this.foldingRegionLayoutOptions,
386. foldedLayoutOptions: this.foldedRegionLayoutOptions,
387. })
388. }
389. .width("100%")
390. .height("100%")
391. }
392. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |
| - |  |  |
| - |  |  |
