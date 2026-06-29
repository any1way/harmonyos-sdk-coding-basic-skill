---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-xcomponent
title: 使用XComponent实现画中画功能开发（ArkTS）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 在应用程序中使用画中画功能 > 使用XComponent实现画中画功能开发（ArkTS）
category: harmonyos-guides
scraped_at: 2026-06-11T14:34:31+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:a91a74d385462f29c8543636ef9f0328b362aee3b4df92dccd892bf7b7dd75cf
---
本文以视频播放为例，介绍通过XComponent实现画中画功能的基本开发步骤。

## 约束与限制

* HarmonyOS 6.0.0之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从HarmonyOS 6.0.0开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。
* 仅支持以[XComponent](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/渲染绘制/XComponent/ts-basic-components-xcomponent.md)作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。
* UIAbility使用[Navigation](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)管理页面时，需要设置Navigation控件的id属性，并将该id传递给画中画控制器，确保还原时可以正常恢复原页面。
* 如果应用主窗口不在前台，不建议在画中画回调方法中执行UI操作，例如页面push/pop等，这些操作不会立即执行，可能产生预期之外的结果。
* 在关闭画中画时，需要检查自定义组件节点是否释放，避免出现内存泄漏。

## 开发步骤

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 通过create(config: PiPConfiguration)接口创建画中画控制器实例。
   * 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。
   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。
   * 通过画中画控制器实例的on('controlPanelActionEvent')接口注册控制事件回调。
2. 启动画中画。

   创建画中画控制器实例后，通过startPiP接口启动画中画。
3. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。
4. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画。

```
1. // pages/XComponentImplementPage.ets
2. // 该页面用于展示Navigation在画中画场景的使用。如果UIAbility是单页面，则无需使用Navigation
3. import { Page1 } from '../xcomponent/Page1'

5. @Entry
6. @Component
7. struct XComponentImplementPage {
8. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
9. private navId: string = 'navId';

11. @Builder
12. PageMap(name: string) {
13. if (name === 'pageOne') {
14. Page1({ navId: this.navId });
15. }
16. }

18. build() {
19. Navigation(this.pageInfos) {
20. Column() {
21. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
22. .width('80%')
23. .height(40)
24. .margin(20)
25. .onClick(() => {
26. this.pageInfos.pushPath({ name: 'pageOne' }) // 将name指定的NavDestination页面信息入栈
27. })
28. .stateStyles({
29. pressed: {
30. .backgroundColor(Color.Red);
31. },
32. normal: {
33. .backgroundColor(Color.Blue);
34. }
35. })
36. }
37. }
38. .title('NavIndex')
39. .navDestination(this.PageMap)
40. .id(this.navId) // 设置Navigation组件的id属性
41. }
42. }
```

[XComponentImplementPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUIWindowPipSamples/WindowPip/entry/src/main/ets/pages/XComponentImplementPage.ets#L16-L59)

示例中的视频播放需要使用AVPlayer，具体示例可参考[视频播放](<../../../../../媒体/Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer播放视频(ArkTS)/video-playback.md>)。

```
1. // xcomponent/Page1.ets
2. // 该页面用于展示画中画功能的基本使用
3. import { AVPlayer } from '../model/AVPlayer';
4. import { BuilderNode, FrameNode, NodeController, UIContext, PiPWindow } from '@kit.ArkUI';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import { Logger } from '../util/LogUtil';

8. const TAG = 'Page1';

10. class Params {
11. public text: string = '';

13. constructor(text: string) {
14. this.text = text;
15. }
16. }

18. // 开发者可以通过@Builder装饰器实现布局构建
19. @Builder
20. function buildText(params: Params) {
21. Column() {
22. Text(params.text)
23. .fontSize(20)
24. .fontColor(Color.Red)
25. }
26. .width('100%') // 宽度方向充满画中画窗口
27. .height('100%') // 高度方向充满画中画窗口
28. }

30. // 开发者可通过继承NodeController实现自定义UI控制器
31. class TextNodeController extends NodeController {
32. private message: string;
33. private textNode: BuilderNode<[Params]> | null = null;

35. constructor(message: string) {
36. super();
37. this.message = message;
38. }

40. // 通过BuilderNode加载自定义布局
41. makeNode(context: UIContext): FrameNode | null {
42. this.textNode = new BuilderNode(context);
43. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
44. return this.textNode.getFrameNode();
45. }

47. // 开发者可自定义该方法实现布局更新
48. update(message: string) {
49. Logger.info(`update message: ${message}`);
50. if (this.textNode !== null) {
51. this.textNode.update(new Params(message));
52. }
53. }

55. // 开发者需要定义该方法实现布局的注销，避免内存泄漏
56. dispose() {
57. Logger.info('dispose message: execute node dispose');
58. if (this.textNode !== null) {
59. this.textNode.dispose();
60. }
61. }
62. }

64. @Component
65. export struct Page1 {
66. @Consume('pageInfos') pageInfos: NavPathStack;
67. private surfaceId: string = ''; // surfaceId，用于关联XComponent与视频播放器
68. private mXComponentController: XComponentController = new XComponentController();
69. private player?: AVPlayer = undefined;
70. private pipController?: PiPWindow.PiPController = undefined;
71. private nodeController: TextNodeController = new TextNodeController('this is custom UI');
72. navId: string = '';
73. private options: XComponentOptions = {
74. type: XComponentType.SURFACE,
75. controller: this.mXComponentController
76. }

78. build() {
79. NavDestination() {
80. Column() {
81. // XComponent控件，用于播放视频流
82. XComponent(this.options)
83. .onLoad(() => {
84. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
85. // 需要设置AVPlayer的surfaceId为XComponentController的surfaceId
86. this.player = new AVPlayer();
87. this.player.surfaceID = this.surfaceId;
88. this.player.avPlayerFdSrc();
89. })
90. .onDestroy(() => {
91. Logger.info(`[${TAG}] XComponent onDestroy`);
92. })
93. .size({ width: '100%', height: '800px' })
94. Row({ space: 20 }) {
95. Button('startPip') // 启动画中画
96. .onClick(() => {
97. this.startPip();
98. })
99. .stateStyles({
100. pressed: {
101. .backgroundColor(Color.Red);
102. },
103. normal: {
104. .backgroundColor(Color.Blue);
105. }
106. })
107. Button('stopPip') // 停止画中画
108. .onClick(() => {
109. this.stopPip();
110. })
111. .stateStyles({
112. pressed: {
113. .backgroundColor(Color.Red);
114. },
115. normal: {
116. .backgroundColor(Color.Blue);
117. }
118. })
119. Button('updateSize') // 更新视频尺寸
120. .onClick(() => {
121. // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
122. // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
123. this.updateContentSize(900, 1600);
124. })
125. .stateStyles({
126. pressed: {
127. .backgroundColor(Color.Red);
128. },
129. normal: {
130. .backgroundColor(Color.Blue);
131. }
132. })
133. }
134. .size({ width: '100%', height: 60 })
135. .justifyContent(FlexAlign.SpaceAround)
136. }
137. .justifyContent(FlexAlign.Center)
138. .height('100%')
139. .width('100%')
140. }
141. }

143. startPip() {
144. if (!PiPWindow.isPiPEnabled()) {
145. Logger.error(`picture in picture disabled for current OS`);
146. return;
147. }
148. let config: PiPWindow.PiPConfiguration = {
149. context: this.getUIContext().getHostContext() as Context,
150. componentController: this.mXComponentController,
151. // 当前page导航id
152. // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
153. // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
154. // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
155. navigationId: this.navId,
156. // 对于视频通话、视频会议等场景，需要设置相应的模板类型
157. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
158. // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
159. contentWidth: 1920,
160. // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
161. contentHeight: 1080,
162. // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
163. controlGroups: [PiPWindow.VideoPlayControlGroup.VIDEO_PREVIOUS_NEXT],
164. // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
165. customUIController: this.nodeController,
166. };
167. // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
168. PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
169. this.pipController = controller;
170. // 步骤1：初始化画中画控制器
171. this.initPipController();
172. // 步骤2：通过startPiP接口启动画中画
173. this.pipController.startPiP().then(() => {
174. Logger.info(`Succeeded in starting pip.`);
175. }).catch((err: BusinessError) => {
176. Logger.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
177. });
178. }).catch((err: BusinessError) => {
179. Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
180. });
181. }

183. initPipController() {
184. if (!this.pipController) {
185. return;
186. }
187. // 步骤1：通过setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画，注册stateChange和controlPanelActionEvent回调
188. this.pipController.setAutoStartEnabled(false /* or true if necessary */); // 默认为false
189. this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
190. this.onStateChange(state, reason);
191. });
192. this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
193. this.onActionEvent(event, status);
194. });
195. }

197. onStateChange(state: PiPWindow.PiPState, reason: string) {
198. let curState: string = '';
199. switch (state) {
200. case PiPWindow.PiPState.ABOUT_TO_START:
201. curState = 'ABOUT_TO_START';
202. break;
203. case PiPWindow.PiPState.STARTED:
204. curState = 'STARTED';
205. break;
206. case PiPWindow.PiPState.ABOUT_TO_STOP:
207. curState = 'ABOUT_TO_STOP';
208. this.nodeController?.dispose();
209. break;
210. case PiPWindow.PiPState.STOPPED:
211. curState = 'STOPPED';
212. break;
213. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
214. curState = 'ABOUT_TO_RESTORE';
215. break;
216. case PiPWindow.PiPState.ERROR:
217. curState = 'ERROR';
218. break;
219. default:
220. break;
221. }
222. Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
223. }

225. onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
226. switch (event) {
227. case 'playbackStateChanged':
228. // 开始或停止视频
229. if (status === 0) {
230. // 停止视频
231. } else if (status === 1) {
232. // 播放视频
233. }
234. break;
235. case 'nextVideo':
236. // 播放下一个视频
237. break;
238. case 'previousVideo':
239. // 播放上一个视频
240. break;
241. default:
242. break;
243. }
244. }

246. // 步骤3：视频内容变化时，向画中画控制器更新视频尺寸信息，用于调整画中画窗口比例
247. updateContentSize(width: number, height: number) {
248. if (this.pipController) {
249. this.pipController.updateContentSize(width, height);
250. }
251. }

253. // 步骤4：当不再需要显示画中画时，通过stopPiP接口关闭画中画
254. stopPip() {
255. if (this.pipController) {
256. this.pipController.stopPiP()
257. .then(() => {
258. Logger.info(`Succeeded in stopping pip.`);
259. this.pipController?.off('stateChange'); // 如果已注册stateChange回调，停止画中画时取消注册该回调
260. this.pipController?.off('controlPanelActionEvent'); // 如果已注册controlPanelActionEvent回调，停止画中画时取消注册该回调
261. }).catch((err: BusinessError) => {
262. Logger.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
263. });
264. }
265. }
266. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUIWindowPipSamples/WindowPip/entry/src/main/ets/xcomponent/Page1.ets#L16-L283)

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/re4NLLJCSkOdsB8GimXT6A/zh-cn_image_0000002592218584.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063430Z&HW-CC-Expire=86400&HW-CC-Sign=B3FCF327CDA0E89136714797D02C5D36C0F2B08789A448BF52778D24D69226B5)
